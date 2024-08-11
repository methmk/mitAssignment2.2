# MIT Assignment 2.2 - Speech-to-Text Tool for Speech Prompting

## Table of Contents
- [Project Overview](#project-overview)
- [Assignment Description](#assignment-description)
- [Project Components](#project-components)
  - [Markdown Files](#markdown-files)
  - [Code and Libraries](#code-and-libraries)
  - [Workflow](#workflow)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Logging](#logging)
- [Error Handling](#error-handling)

## Project Overview

This project involves the conversion of four prominent books on web development and JavaScript programming into `.md` (Markdown) format. The books selected for this project are:

1. **HTML & CSS Design and Build Websites** by Jon Duckett
2. **Mastering JavaScript Functional Programming** by Federico Kereki
3. **Eloquent JavaScript** by Marijn Haverbeke
4. **JavaScript for Impatient Programmers** by Dr. Axel Rauschmayer

The primary goal of this project is to convert these books into a format that maintains their structure while making the content more accessible for embedding and analysis, particularly in vector-based search systems.

## Assignment Description

### MIT Assignment: Using a Speech-To-Text Tool for Speech Prompting

**Brief Description**: This assignment is mandatory and will therefore be evaluated as part of your final grade. The assignment must be completed individually.

**Instructions**: Use any tool with speech-to-text functionality to generate HTML, CSS, and JavaScript code for a multiple-choice quiz. Be as clear and direct as you can and provide explicit instructions to the extension to ensure accurate results.

If you are a coder, make sure to save the HTML and load the page in your browser.

## Project Components

### Markdown Files
The contents of the four books have been converted into the following Markdown files:

- `htmlcss.md` - Contains the content of "HTML & CSS Design and Build Websites."
- `js.md` - Contains the content of "Mastering JavaScript Functional Programming."
- `js2.md` - Contains the content of "Eloquent JavaScript."
- `js3.md` - Contains the content of "JavaScript for Impatient Programmers."

### Code and Libraries

The project makes use of the following libraries and technologies:

- **Python**: The programming language used to implement the functionality.
- **Markdown**: Used for processing the .md files.
- **Pandas**: Used for data manipulation and handling the content of the books.
- **NumPy**: Used for numerical operations and handling embeddings.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.
- **Sentence-Transformers**: A Python framework used to generate sentence and text embeddings.
- **LlamaAPI**: Used for querying and refining queries through the Llama model.
- **SpeechRecognition**: Utilized for accepting voice input from the user.

### Workflow

1. **Reading Markdown Files**: The `.md` files for each book are read and converted to HTML format using the `markdown` library. This preserves the structure while making the content ready for further processing.

2. **Content Chunking**: The content of each book is split into manageable chunks of 512 words. This helps in effectively creating embeddings and querying the data.

3. **Creating Embeddings**: The content chunks are converted into vector embeddings using the `SentenceTransformer` model (`all-MiniLM-L6-v2`). These embeddings are used for efficient search and retrieval.

4. **FAISS Index Creation**: The generated embeddings are stored in a FAISS index. This index allows for fast and efficient vector-based querying.

5. **Querying the Content**: The system allows users to query the content either through text input or voice input. Queries are refined using LlamaAPI to ensure they are specific and yield accurate results.

6. **Search and Result Interpretation**: The refined query is searched against the FAISS index, and the results are interpreted using LlamaAPI to provide a concise and relevant answer to the user's query.

## Usage

To use this project, follow these steps:

1. **Install Requirements**: Ensure that all the required libraries and dependencies are installed. You can do this by running the following command in your terminal:

   ```bash
   pip install -r requirements.txt
2. **Run main.py**: file. This can be done by running:
   ```bash
   go run main.go
3. **Select Input Type**: Once the program is running, you will be prompted to choose your input method. You can select either:

-   **Text Input**: Type your query directly into the terminal.
-   **Voice Input**: Use your voice to input the query, utilizing the SpeechRecognition functionality.

Follow the on-screen instructions to interact with the system and obtain the desired results.
## Environment Variables

-   **API Key**: The project uses the LlamaAPI, which requires an API key. This key is loaded from the environment using `dotenv`.

## Logging

The project includes logging to track the progress of operations and to handle errors effectively. Logs are set up to provide information about key events, such as reading files, creating embeddings, and querying the vector store.

## Error Handling

The project has been designed to handle common errors, such as file not found errors and JSON parsing errors, ensuring robustness and reliability during execution.
