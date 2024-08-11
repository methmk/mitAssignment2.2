import os
import markdown
import pandas as pd
import logging
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from llamaapi import LlamaAPI
import asyncio
from typing import List, Dict, Any
import json
from dotenv import load_dotenv

# Load environment variables (you can keep this if you have other environment variables)
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the SDK with the API key directly
api_key = 'LL-0HPBPQGQjMaZRmsKpoJtTySoccREMLIHWsYTW5gVYU2y3fMl36WauGCYuJt5MAAn'
llama = LlamaAPI(api_key)

# Initialize Sentence-Transformers Model
model = SentenceTransformer('all-MiniLM-L6-v2')

def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        html = markdown.markdown(text)
        return html

def split_content(content, max_length=512):
    words = content.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        if current_length + len(word) > max_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
        else:
            current_chunk.append(word)
            current_length += len(word) + 1  # +1 for the space
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks

# Load .md Data
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Reading the content of js.md, htmlcss.md, js2.md, and js3.md
    js_content = read_md_file(os.path.join(script_dir, "js.md"))
    htmlcss_content = read_md_file(os.path.join(script_dir, "htmlcss.md"))
    js2_content = read_md_file(os.path.join(script_dir, "js2.md"))
    js3_content = read_md_file(os.path.join(script_dir, "js3.md"))

    # Splitting content into chunks
    js_chunks = split_content(js_content)
    htmlcss_chunks = split_content(htmlcss_content)
    js2_chunks = split_content(js2_content)
    js3_chunks = split_content(js3_content)

    # Combining the data
    combined_data = (
            [{"content": chunk, "source": "js.md"} for chunk in js_chunks] +
            [{"content": chunk, "source": "htmlcss.md"} for chunk in htmlcss_chunks] +
            [{"content": chunk, "source": "js2.md"} for chunk in js2_chunks] +
            [{"content": chunk, "source": "js3.md"} for chunk in js3_chunks]
    )

    # Creating the DataFrame
    combined_df = pd.DataFrame(combined_data)

except FileNotFoundError as e:
    logging.error(f"Error loading data: {e}")
    raise

def generate_embeddings(dataframe, column):
    return np.array([model.encode(str(text)) for text in dataframe[column]])

def save_embeddings(file_path, embeddings):
    np.save(file_path, embeddings)

def load_embeddings(file_path):
    return np.load(file_path)

def create_and_save_faiss_index(embeddings, file_path):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, file_path)
    return index

def load_faiss_index(file_path):
    return faiss.read_index(file_path)

# Paths for cached embeddings and indices
embeddings_path = os.path.join(script_dir, "combined_embeddings.npy")
index_path = os.path.join(script_dir, "combined_index.faiss")

# Generate or load embeddings and create/load FAISS index
try:
    if not os.path.exists(index_path) or not os.path.exists(embeddings_path):
        logging.info("Creating and saving combined_index and embeddings")
        combined_embeddings = generate_embeddings(combined_df, 'content')
        save_embeddings(embeddings_path, combined_embeddings)
        combined_index = create_and_save_faiss_index(combined_embeddings, index_path)
    else:
        logging.info("Loading cached combined_index and embeddings")
        combined_embeddings = load_embeddings(embeddings_path)
        combined_index = load_faiss_index(index_path)
except Exception as e:
    logging.error(f"Error in index creation or loading: {e}")
    raise

# Initialize Vector Store
class FaissVectorStore:
    def __init__(self, faiss_index):
        self.index = faiss_index

    def query(self, vector_store_query):
        query_embedding = np.array([vector_store_query.query_embedding]).astype('float32')
        distances, indices = self.index.search(query_embedding, vector_store_query.similarity_top_k)
        return VectorStoreQueryResult(
            nodes=[VectorStoreNode(content=combined_df.iloc[idx]['content'], metadata={"source": combined_df.iloc[idx]['source']}) for idx in indices[0]],
            similarities=distances[0].tolist(),
            ids=indices[0].tolist()
        )

class VectorStoreQuery:
    def __init__(self, query_embedding, similarity_top_k, query_str):
        self.query_embedding = query_embedding
        self.similarity_top_k = similarity_top_k
        self.query_str = query_str

class VectorStoreQueryResult:
    def __init__(self, nodes, similarities, ids):
        self.nodes = nodes
        self.similarities = similarities
        self.ids = ids

class VectorStoreNode:
    def __init__(self, content, metadata):
        self.content = content
        self.metadata = metadata

    def get_content(self):
        return self.content

vector_store = FaissVectorStore(faiss_index=combined_index)

# Updated prompt for query refinement
refine_template = """\
Refine the following query to make it specific and clear for a vector-based search. The refinement should be focused on key terms and concepts relevant to HTML, CSS, and JS, and should consider how the query could be split into parts for code extraction or creation.

Original Query: {query}

Refined Query for Vector Search:
"""


# Updated prompt for interpreting vector search results
interpret_template = """\
Using the provided vector search results, generate a clear and concise answer to the original query. The answer should consider the semantic similarity of the results to the query and should be split into parts to help extract or create relevant HTML, CSS, or JS code and please use only vector-based results to answer.

Original Query: {query}

Vector Search Results: {search_results}

Answer:
"""

def parse_llama_response(response):
    try:
        if not response or not response.content:
            logging.error("LlamaAPI response content is empty or None")
            return None
        return response.json()
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse response content as JSON: {e}")
        logging.error(f"Raw response content: {response.content}")
        return None
    except AttributeError as e:
        logging.error(f"Response object missing 'content' attribute: {e}")
        return None

def vector_search(vector_store, query: str, df: pd.DataFrame, top_k: int = 10) -> List[Dict[str, Any]]:
    try:
        query_embedding = model.encode(query)

        if isinstance(query_embedding, np.ndarray):
            query_embedding = query_embedding.tolist()
        elif hasattr(query_embedding, 'cpu'):
            query_embedding = query_embedding.cpu().numpy().tolist()
        else:
            query_embedding = [float(x) for x in query_embedding]

        vector_store_query = VectorStoreQuery(
            query_embedding=query_embedding,
            similarity_top_k=top_k,
            query_str=query
        )

        logging.info(f"Querying vector store with query: {query}")
        results: VectorStoreQueryResult = vector_store.query(vector_store_query)
        logging.info(f"Received results from vector store: {results}")

        if results is None or (results.nodes is None and results.ids is None):
            logging.warning("Vector store returned no usable results")
            return []

        processed_results = []
        if results.nodes is not None:
            for node, score in zip(results.nodes, results.similarities or []):
                if node is None:
                    logging.warning("Encountered None node in results")
                    continue
                try:
                    processed_results.append({
                        "content": node.get_content() if hasattr(node, 'get_content') else str(node),
                        "metadata": node.metadata if hasattr(node, 'metadata') else {},
                        "score": float(score) if score is not None else None
                    })
                except Exception as e:
                    logging.error(f"Error processing node: {e}")
        elif results.ids is not None:
            for id, score in zip(results.ids, results.similarities or []):
                try:
                    node_data = df.loc[df.index == int(id)].iloc[0].to_dict() if int(id) in df.index else None
                    if node_data:
                        processed_results.append({
                            "content": str(node_data),
                            "metadata": node_data,
                            "score": float(score) if score is not None else None
                        })
                except Exception as e:
                    logging.error(f"Error processing ID {id}: {e}")

        return processed_results

    except Exception as e:
        logging.error(f"Error in vector_search: {e}")
        return []

async def handle_query(query: str):
    try:
        refine_request_json = {
            "model": "llama3.1-405b",
            "messages": [
                {
                    "role": "user",
                    "content": refine_template.format(query=query)
                }
            ],
            "max_tokens": 1000,
            "temperature": 0.7
        }

        logging.info(f"Sending request to LlamaAPI for query refinement: {query}")
        refine_response = llama.run(refine_request_json)
        logging.info(f"Received refined query from LlamaAPI: {refine_response}")

        # Log raw response content for debugging
        logging.debug(f"Raw refine_response content: {refine_response.content}")

        parsed_refine_response = parse_llama_response(refine_response)
        if parsed_refine_response is None or 'choices' not in parsed_refine_response:
            logging.warning("Failed to parse refine response, using original query")
            refined_query = query
        else:
            refined_query = parsed_refine_response['choices'][0]['message']['content']

        logging.info(f"Performing vector search with refined query: {refined_query}")
        results = vector_search(vector_store, refined_query, combined_df)

        results.sort(key=lambda x: x['score'] if x['score'] is not None else float('-inf'), reverse=True)
        top_results = results[:10]

        logging.info(f"Top results: {top_results}")

        interpret_request_json = {
            "model": "llama3.1-405b",
            "messages": [
                {
                    "role": "user",
                    "content": interpret_template.format(
                        query=query,
                        search_results=json.dumps(top_results, indent=2)
                    )
                }
            ],
            "max_tokens": 1000,
            "temperature": 0.7
        }

        logging.info(f"Sending request to LlamaAPI for result interpretation: {query}")
        interpret_response = llama.run(interpret_request_json)
        logging.info(f"Received interpretation from LlamaAPI: {interpret_response}")

        # Log raw response content for debugging
        logging.debug(f"Raw interpret_response content: {interpret_response.content}")

        parsed_interpret_response = parse_llama_response(interpret_response)
        if parsed_interpret_response is None or 'choices' not in parsed_interpret_response:
            logging.warning("Failed to interpret results, returning raw search results")
            return json.dumps(top_results, indent=2)
        else:
            interpretation = parsed_interpret_response['choices'][0]['message']['content']
            return interpretation

    except Exception as e:
        logging.error(f"Error handling query: {e}")
        return f"I'm sorry, but I encountered an error while processing your query. Please try again or rephrase your question. Error: {str(e)}"

async def async_input(prompt: str) -> str:
    return await asyncio.to_thread(input, prompt)

async def chat():
    print("Welcome to the Code Assistance Chat!")
    print("You can ask questions about HTML, CSS, and JavaScript code.")
    print("Type 'exit' to end the chat.")

    while True:
        user_query = await async_input("\nYou: ")
        if user_query.lower() == 'exit':
            print("Thank you for using the Code Assistance Chat. Goodbye!")
            break

        print("Processing your query...")
        result = await handle_query(user_query)
        print(f"\nAssistant: {result}")

if __name__ == "__main__":
    asyncio.run(chat())
