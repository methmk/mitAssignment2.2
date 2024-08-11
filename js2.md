
# EloquentJavaScript

### 4thedition

## Marijn Haverbeke


Copyright © 2024 by Marijn Haverbeke

This work is licensed under a Creative Commons attribution-noncommercial
license (http://creativecommons.org/licenses/by-nc/3.0/). All code in
the book may also be considered licensed under an MIT license (https:
//eloquentjavascript.net/code/LICENSE).
The illustrations are contributed by various artists: Cover by Péchane
Sumi-e. Chapter illustrations by Madalina Tantareanu. Pixel art in
Chapters 7 and 16 by Antonio Perdomo Pastor. Regular expression
diagrams in Chapter 9 generated withregexper.comby Jeff Avallone.
Game concept for Chapter 16 byThomas Palef.

You can buy a print version of this book, with an extra bonus chapter in-
cluded, printed by No Starch Press athttp://a-fwd.com/com=marijhaver-
20&asin-com=1593279507.

```
i
```

## Contents













- Introduction
   - On programming
   - Why language matters
   - What is JavaScript?.
   - Code, and what to do with it
   - Overview of this book.
   - Typographic conventions
- 1 Values,Types,andOperators
   - Values.
   - Numbers
   - Strings
   - Unary operators
   - Boolean values
   - Empty values.
   - Automatic type conversion.
   - Summary
- 2 ProgramStructure
   - Expressions and statements
   - Bindings
   - Binding names
   - The environment
   - Functions.
   - The console.log function
   - Return values
   - Control flow
   - Conditional execution.
   - while and do loops.
   - Indenting Code
   - for loops
   - Breaking Out of a Loop
   - Updating bindings succinctly
   - Dispatching on a value with switch
   - Capitalization
   - Comments
   - Summary
   - Exercises
- 3 Functions
   - Defining a function
   - Bindings and scopes.
   - Nested scope
   - Functions as values
   - Declaration notation
   - Arrow functions
   - The call stack
   - Optional Arguments.
   - Closure
   - Recursion.
   - Growing functions.
   - Functions and side effects
   - Summary
   - Exercises
- 4 DataStructures: ObjectsandArrays
   - The weresquirrel.
   - Datasets
   - Properties
   - Methods
   - Objects
   - Mutability
   - The lycanthrope’s log
   - Computing correlation
   - Array loops.
   - The final analysis
   - Further arrayology.
   - Strings and their properties
   - Rest parameters
   - The Math object.
   - Destructuring
   - Optional property access
   - JSON
   - Summary
   - Exercises
- 5 Higher-OrderFunctions
   - Abstraction.
   - Abstracting repetition
   - Higher-order functions
   - Script dataset
   - Filtering arrays
   - Transforming with map.
   - Summarizing with reduce.
   - Composability
   - Strings and character codes
   - Recognizing text.
   - Summary
   - Exercises
- 6 TheSecretLifeofObjects
   - Abstract Data Types
   - Methods
   - Prototypes
   - Classes
   - Private Properties
   - Overriding derived properties
   - Maps
   - Polymorphism
   - Getters, setters, and statics
   - Symbols.
   - The iterator interface
   - Inheritance
   - The instanceof operator.
   - Summary
   - Exercises
- 7 Project: ARobot
   - Meadowfield
   - The task
   - Persistent data.
   - Simulation
   - The mail truck’s route
   - Pathfinding.
   - Exercises
- 8 BugsandErrors
   - Language
   - Strict mode.
   - Types
   - Testing
   - Debugging
   - Error propagation
   - Exceptions
   - Cleaning up after exceptions.
   - Selective catching
   - Assertions
   - Summary
   - Exercises
- 9 RegularExpressions
   - Creating a regular expression
   - Testing for matches
   - Sets of characters
   - International characters.
   - Repeating parts of a pattern.
   - Grouping subexpressions
   - Matches and groups.
   - The Date class
   - Boundaries and look-ahead.
   - Choice patterns
   - The mechanics of matching
   - Backtracking
   - The replace method.
   - Greed
   - Dynamically creating RegExp objects
   - The search method
   - The lastIndex property
   - Parsing an INI file.
   - Code units and characters
   - Summary
   - Exercises
- 10 Modules
   - Modular programs.
   - ES modules.
   - Packages
   - CommonJS modules.
   - Building and bundling
   - Module design
   - Summary
   - Exercises
- 11 AsynchronousProgramming
   - Asynchronicity.
   - Callbacks
   - Promises
   - Failure
   - Carla
   - Breaking In.
   - Async functions
   - Generators
   - A Corvid Art Project
   - The event loop.
   - Asynchronous bugs
   - Summary
   - Exercises
- 12 Project: AProgrammingLanguage
   - Parsing
   - The evaluator
   - Special forms.
   - The environment
   - Functions.
   - Compilation
   - Cheating
   - Exercises
- 13 JavaScriptandtheBrowser
   - Networks and the Internet
   - The Web
   - HTML
   - HTML and JavaScript
   - In the sandbox.
   - Compatibility and the browser wars
- 14 TheDocumentObjectModel
   - Document structure.
   - Trees
   - The standard.
   - Moving through the tree
   - Finding elements
   - Changing the document
   - Creating nodes.
   - Attributes
   - Layout
   - Styling
   - Cascading styles
   - Query selectors.
   - Positioning and animating
   - Summary
   - Exercises
- 15 HandlingEvents
   - Event handlers.
   - Events and DOM nodes
   - Event objects.
   - Propagation
   - Default actions.
   - Key events
   - Pointer events
   - Scroll events
   - Focus events
   - Load event
   - Events and the event loop
   - Timers
   - Debouncing.
   - Summary
   - Exercises
- 16 Project: APlatformGame
   - The game.
   - The technology
   - Levels
   - Reading a level.
   - Actors.
   - Drawing.
   - Motion and collision.
   - Actor updates
   - Tracking keys
   - Running the game.
   - Exercises
- 17 DrawingonCanvas
   - SVG.
   - The canvas element
   - Lines and surfaces
   - Paths
   - Curves
   - Drawing a pie chart
   - Text
   - Images
   - Transformation
   - Storing and clearing transformations
   - Back to the game
   - Choosing a graphics interface
   - Summary
   - Exercises
- 18 HTTPandForms
   - The protocol
   - Browsers and HTTP
   - Fetch
   - HTTP sandboxing.
   - Appreciating HTTP.
   - Security and HTTPS
   - Form fields
   - Focus
   - Disabled fields
   - The form as a whole
   - Text fields
   - Checkboxes and radio buttons.
   - Select fields.
   - File fields
   - Storing data client-side
   - Summary
   - Exercises
- 19 Project: APixelArtEditor
   - Components
   - The state
   - DOM building
   - The canvas
   - The application
   - Drawing tools
   - Saving and loading
   - Undo history.
   - Let’s draw
   - Why is this so hard?
   - Exercises
- 20Node.js
   - Background.
   - The node command
   - Modules.
   - Installing with NPM
   - The filesystem module
   - The HTTP module
   - Streams
   - A file server
   - Summary
   - Exercises
- 21 Project: Skill-SharingWebsite
   - Design.
   - Long polling
   - HTTP interface
   - The server
   - The client.
   - Exercises
- ExerciseHints
   - Program Structure
   - Functions.
   - Data Structures: Objects and Arrays.
- Higher-Order Functions.
- The Secret Life of Objects
- Project: A Robot
- Bugs and Errors
- Regular Expressions.
- Modules.
- Asynchronous Programming
- Project: A Programming Language
- The Document Object Model
- Handling Events.
- Project: A Platform Game.
- Drawing on Canvas
- HTTP and Forms
- Project: A Pixel Art Editor
- Node.js
- Project: Skill-Sharing Website.


```
“We think we are creating the system for our own purposes.
We believe we are making it in our own image... But the
computer is not really like us. It is a projection of a very slim
part of ourselves: that portion devoted to logic, order, rule,
and clarity.”
—Ellen Ullman, Close to the Machine: Technophilia and Its
Discontents
```
## Introduction

This is a book about instructing computers. Computers are about as
common as screwdrivers today, but they are quite a bit more complex,
and making them do what you want them to do isn’t always easy.
If the task you have for your computer is a common, well-understood
one, such as showing you your email or acting like a calculator, you can
open the appropriate application and get to work. But for unique or
open-ended tasks, there often is no appropriate application.
That is where programming may come in. _Programming_ is the act of
constructing a _program_ —a set of precise instructions telling a computer
what to do. Because computers are dumb, pedantic beasts, program-
ming is fundamentally tedious and frustrating.
Fortunately, if you can get over that fact—and maybe even enjoy
the rigor of thinking in terms that dumb machines can deal with—
programming can be rewarding. It allows you to do things in seconds
that would take _forever_ by hand. It is a way to make your computer
tool do things that it couldn’t do before. On top of that, it makes for
a wonderful game of puzzle solving and abstract thinking.
Most programming is done with programming languages. A _program-_


_ming language_ is an artificially constructed language used to instruct
computers. It is interesting that the most effective way we’ve found
to communicate with a computer borrows so heavily from the way we
communicate with each other. Like human languages, computer lan-
guages allow words and phrases to be combined in new ways, making
it possible to express ever new concepts.
At one point, language-based interfaces, such as the BASIC and DOS
prompts of the 1980s and 1990s, were the main method of interacting
with computers. For routine computer use, these have largely been
replaced with visual interfaces, which are easier to learn but offer less
freedom. But if you know where to look, the languages are still there.
One of them, _JavaScript_ , is built into every modern web browser—and
is thus available on almost every device.
This book will try to make you familiar enough with this language
to do useful and amusing things with it.

### On programming

Besides explaining JavaScript, I will introduce the basic principles of
programming. Programming, it turns out, is hard. The fundamental
rules are simple and clear, but programs built on top of these rules tend
to become complex enough to introduce their own rules and complexity.
You’re building your own maze, in a way, and you can easily get lost in
it.
There will be times when reading this book feels terribly frustrating.
If you are new to programming, there will be a lot of new material to


digest. Much of this material will then be _combined_ in ways that require
you to make additional connections.
It is up to you to make the necessary effort. When you are struggling
to follow the book, do not jump to any conclusions about your own
capabilities. You are fine—you just need to keep at it. Take a break,
reread some material, and make sure you read and understand the ex-
ample programs and exercises. Learning is hard work, but everything
you learn is yours and will make further learning easier.

```
When action grows unprofitable, gather information; when
information grows unprofitable, sleep.
—Ursula K. Le Guin, The Left Hand of Darkness
```
A program is many things. It is a piece of text typed by a program-
mer, it is the directing force that makes the computer do what it does,
it is data in the computer’s memory, and, at the same time, it controls
the actions performed on this memory. Analogies that try to compare
programs to familiar objects tend to fall short. A superficially fitting
one is to compare a program to a machine—lots of separate parts tend
to be involved, and to make the whole thing tick, we have to consider
the ways in which these parts interconnect and contribute to the oper-
ation of the whole.
A computer is a physical machine that acts as a host for these imma-
terial machines. Computers themselves can do only stupidly straight-
forward things. The reason they are so useful is that they do these
things at an incredibly high speed. A program can ingeniously combine


an enormous number of these simple actions to do very complicated
things.
A program is a building of thought. It is costless to build, it is
weightless, and it grows easily under our typing hands. But as a pro-
gram grows, so does its complexity. The skill of programming is the
skill of building programs that don’t confuse the programmer. The best
programs are those that manage to do something interesting while still
being easy to understand.
Some programmers believe that this complexity is best managed by
using only a small set of well-understood techniques in their programs.
They have composed strict rules (“best practices”) prescribing the form
programs should have and carefully stay within their safe little zone.
This is not only boring—it is ineffective. New problems often require
new solutions. The field of programming is young and still developing
rapidly, and it is varied enough to have room for wildly different ap-
proaches. There are many terrible mistakes to make in program design,
and you should go ahead and make them at least once so that you un-
derstand them. A sense of what a good program looks like is developed
with practice, not learned from a list of rules.

### Why language matters

In the beginning, at the birth of computing, there were no programming
languages. Programs looked something like this:

```
00110001 00000000 00000000
00110001 00000001 00000001
```

```
00110011 00000001 00000010
01010001 00001011 00000010
00100010 00000010 00001000
01000011 00000001 00000000
01000001 00000001 00000001
00010000 00000010 00000000
01100010 00000000 00000000
```
This is a program to add the numbers from 1 to 10 together and print
the result: 1 + 2 + ... + 10 = 55. It could run on a simple hypotheti-
cal machine. To program early computers, it was necessary to set large
arrays of switches in the right position or punch holes in strips of card-
board and feed them to the computer. You can imagine how tedious
and error prone this procedure was. Even writing simple programs
required much cleverness and discipline. Complex ones were nearly
inconceivable.
Of course, manually entering these arcane patterns of bits (the ones
and zeros) did give the programmer a profound sense of being a mighty
wizard. And that has to be worth something in terms of job satisfaction.
Each line of the previous program contains a single instruction. It
could be written in English like this:

1. Store the number 0 in memory location 0.
2. Store the number 1 in memory location 1.
3. Store the value of memory location 1 in memory location 2.
4. Subtract the number 11 from the value in memory location 2.


5. If the value in memory location 2 is the number 0, continue with
    instruction 9.
6. Add the value of memory location 1 to memory location 0.
7. Add the number 1 to the value of memory location 1.
8. Continue with instruction 3.
9. Output the value of memory location 0.

Although that is already more readable than the soup of bits, it is
still rather obscure. Using names instead of numbers for the instructions
and memory locations helps.

```
Set “total” to 0.
Set “count” to 1.
[loop]
Set “compare” to “count”.
Subtract 11 from “compare”.
If “compare” is 0, continue at [end].
Add “count” to “total”.
Add 1 to “count”.
Continue at [loop].
[end]
Output “total”.
```
Can you see how the program works at this point? The first two lines
give two memory locations their starting values: totalwill be used to
build up the result of the computation, andcountwill keep track of the
number that we are currently looking at. The lines usingcompareare


probably the most confusing ones. The program wants to see whether
count is equal to 11 to decide whether it can stop running. Because
our hypothetical machine is rather primitive, it can test only whether a
number is zero and make a decision based on that. It therefore uses the
memory location labeled compareto compute the value ofcount - 11
and makes a decision based on that value. The next two lines add the
value ofcount to the result and incrementcountby 1 every time the
program decides thatcountis not 11 yet.
Here is the same program in JavaScript:
let total = 0, count = 1;
while (count <= 10) {
total += count;
count += 1;
}
console.log(total);
// → 55

This version gives us a few more improvements. Most importantly,
there is no need to specify the way we want the program to jump
back and forth anymore—the while construct takes care of that. It
continues executing the block (wrapped in braces) below it as long as
the condition it was given holds. That condition iscount <= 10, which
means “the count is less than or equal to 10”. We no longer have to
create a temporary value and compare that to zero, which was just an
uninteresting detail. Part of the power of programming languages is
that they can take care of uninteresting details for us.
At the end of the program, after thewhileconstruct has finished, the


console.logoperation is used to write out the result.
Finally, here is what the program could look like if we happened to
have the convenient operationsrangeandsum available, which respec-
tively create a collection of numbers within a range and compute the
sum of a collection of numbers:

```
console.log(sum(range(1, 10)));
// → 55
```
The moral of this story is that the same program can be expressed in
both long and short, unreadable and readable ways. The first version
of the program was extremely obscure, whereas this last one is almost
English:logthesumof therangeof numbers from 1 to 10. (We will see
inlater chaptershow to define operations likesumandrange.)
A good programming language helps the programmer by allowing
them to talk about the actions that the computer has to perform on a
higher level. It helps omit details, provides convenient building blocks
(such aswhileandconsole.log), allows you to define your own building
blocks (such assumandrange), and makes those blocks easy to compose.

### What is JavaScript?.

JavaScript was introduced in 1995 as a way to add programs to web
pages in the Netscape Navigator browser. The language has since been
adopted by all other major graphical web browsers. It has made modern
web applications possible—that is, applications with which you can in-
teract directly without doing a page reload for every action. JavaScript


is also used in more traditional websites to provide various forms of
interactivity and cleverness.
It is important to note that JavaScript has almost nothing to do
with the programming language named Java. The similar name was
inspired by marketing considerations rather than good judgment. When
JavaScript was being introduced, the Java language was being heavily
marketed and was gaining popularity. Someone thought it was a good
idea to try to ride along on this success. Now we are stuck with the
name.
After its adoption outside of Netscape, a standard document was
written to describe the way the JavaScript language should work so that
the various pieces of software that claimed to support JavaScript could
make sure they actually provided the same language. This is called the
ECMAScript standard, after the Ecma International organization that
conducted the standardization. In practice, the terms ECMAScript
and JavaScript can be used interchangeably—they are two names for
the same language.
There are those who will say _terrible_ things about JavaScript. Many
of these things are true. When I was required to write something in
JavaScript for the first time, I quickly came to despise it. It would
accept almost anything I typed but interpret it in a way that was com-
pletely different from what I meant. This had a lot to do with the fact
that I did not have a clue what I was doing, of course, but there is a real
issue here: JavaScript is ridiculously liberal in what it allows. The idea
behind this design was that it would make programming in JavaScript
easier for beginners. In actuality, it mostly makes finding problems in


your programs harder because the system will not point them out to
you.
This flexibility also has its advantages, though. It leaves room for
techniques that are impossible in more rigid languages and makes for
a pleasant, informal style of programming. After learning the language
properly and working with it for a while, I have come to actually _like_
JavaScript.
There have been several versions of JavaScript. ECMAScript version
3 was the widely supported version during JavaScript’s ascent to dom-
inance, roughly between 2000 and 2010. During this time, work was
underway on an ambitious version 4, which planned a number of rad-
ical improvements and extensions to the language. Changing a living,
widely used language in such a radical way turned out to be politically
diﬀicult, and work on version 4 was abandoned in 2008. A much less
ambitious version 5, which made only some uncontroversial improve-
ments, came out in 2009. In 2015, version 6 came out, a major update
that included some of the ideas planned for version 4. Since then we’ve
had new, small updates every year.
The fact that JavaScript is evolving means that browsers have to
constantly keep up. If you’re using an older browser, it may not sup-
port every feature. The language designers are careful to not make
any changes that could break existing programs, so new browsers can
still run old programs. In this book, I’m using the 2024 version of
JavaScript.
Web browsers are not the only platforms on which JavaScript is used.
Some databases, such as MongoDB and CouchDB, use JavaScript as


their scripting and query language. Several platforms for desktop and
server programming, most notably the Node.js project (the subject of
Chapter 20), provide an environment for programming JavaScript out-
side of the browser.

### Code, and what to do with it

_Code_ is the text that makes up programs. Most chapters in this book
contain quite a lot of code. I believe reading code and writing code
are indispensable parts of learning to program. Try to not just glance
over the examples—read them attentively and understand them. This
may be slow and confusing at first, but I promise that you’ll quickly
get the hang of it. The same goes for the exercises. Don’t assume you
understand them until you’ve actually written a working solution.
I recommend you try your solutions to exercises in an actual JavaScript
interpreter. That way, you’ll get immediate feedback on whether what
you are doing is working, and, I hope, you’ll be tempted to experiment
and go beyond the exercises.
The easiest way to run the example code in the book—and to ex-
periment with it—is to look it up in the online version of the book
at _https://eloquentjavascript.net_. There, you can click any code exam-
ple to edit and run it and to see the output it produces. To work on
the exercises, go to _https://eloquentjavascript.net/code_ , which provides
starting code for each coding exercise and allows you to look at the
solutions.
Running the programs defined in this book outside of the book’s


website requires some care. Many examples stand on their own and
should work in any JavaScript environment. But code in later chapters
is often written for a specific environment (the browser or Node.js) and
can run only there. In addition, many chapters define bigger programs,
and the pieces of code that appear in them depend on each other or on
external files. Thesandboxon the website provides links to ZIP files
containing all the scripts and data files necessary to run the code for a
given chapter.

### Overview of this book.

This book contains roughly three parts. The first 12 chapters discuss the
JavaScript language. The next seven chapters are about web browsers
and the way JavaScript is used to program them. Finally, two chapters
are devoted to Node.js, another environment to program JavaScript in.
There are five _project chapters_ in the book that describe larger example
programs to give you a taste of actual programming.
The language part of the book starts with four chapters that in-
troduce the basic structure of the JavaScript language. They discuss
control structures(such as thewhileword you saw in this introduction),
functions(writing your own building blocks), anddata structures. Af-
ter these, you will be able to write basic programs. Next, Chapters 5
and 6 introduce techniques to use functions and objects to write more
_abstract_ code and keep complexity under control.
After afirst project chapterthat builds a crude delivery robot, the
language part of the book continues with chapters onerror handling


and bug fixing, regular expressions (an important tool for working
with text),modularity(another defense against complexity), andasyn-
chronous programming(dealing with events that take time). Thesec-
ond project chapter, where we implement a programming language,
concludes the first part of the book.
The second part of the book, Chapters 13 to 19 , describes the tools
that browser JavaScript has access to. You’ll learn to display things
on the screen (Chapters 14 and 17 ), respond to user input (Chapter
15 ), and communicate over the network (Chapter 18). There are again
two project chapters in this part: building aplatform gameand apixel
paint program.
Chapter 20describes Node.js, andChapter 21builds a small website
using that tool.

### Typographic conventions

In this book, text written in amonospacedfont will represent elements of
programs. Sometimes these are self-suﬀicient fragments, and sometimes
they just refer to part of a nearby program. Programs (of which you
have already seen a few) are written as follows:

```
function factorial(n) {
if (n == 0) {
return 1;
} else {
return factorial(n - 1) * n;
}
```

```
}
```
Sometimes, to show the output that a program produces, the expected
output is written after it, with two slashes and an arrow in front.

```
console.log(factorial(8));
// → 40320
```
Good luck!


```
“Below the surface of the machine, the program moves.
Without effort, it expands and contracts. In great harmony,
electrons scatter and regroup. The forms on the monitor are
but ripples on the water. The essence stays invisibly below.”
—Master Yuan-Ma, The Book of Programming
```
**Chapter1**

## Values,Types,andOperators

In the computer’s world, there is only data. You can read data, modify
data, create new data—but that which isn’t data cannot be mentioned.
All this data is stored as long sequences of bits and is thus fundamen-
tally alike.
_Bits_ are any kind of two-valued things, usually described as zeros
and ones. Inside the computer, they take forms such as a high or low
electrical charge, a strong or weak signal, or a shiny or dull spot on the
surface of a CD. Any piece of discrete information can be reduced to a
sequence of zeros and ones and thus represented in bits.
For example, we can express the number 13 in bits. This works the
same way as a decimal number, but instead of 10 different digits, we
have only 2, and the weight of each increases by a factor of 2 from right
to left. Here are the bits that make up the number 13, with the weights
of the digits shown below them:

```
0 0 0 0 1 1 0 1
128 64 32 16 8 4 2 1
```
That’s the binary number 00001101. Its nonzero digits stand for 8, 4,


and 1, and add up to 13.

### Values.

Imagine a sea of bits—an ocean of them. A typical modern computer
has more than 100 billion bits in its volatile data storage (working
memory). Nonvolatile storage (the hard disk or equivalent) tends to
have yet a few orders of magnitude more.
To be able to work with such quantities of bits without getting lost,
we separate them into chunks that represent pieces of information. In
a JavaScript environment, those chunks are called _values_. Though all
values are made of bits, they play different roles. Every value has a
type that determines its role. Some values are numbers, some values
are pieces of text, some values are functions, and so on.
To create a value, you must merely invoke its name. This is conve-
nient. You don’t have to gather building material for your values or
pay for them. You just call for one, and _whoosh_ , you have it. Of course,
values are not really created from thin air. Each one has to be stored
somewhere, and if you want to use a gigantic number of them at the
same time, you might run out of computer memory. Fortunately, this
is a problem only if you need them all simultaneously. As soon as you
no longer use a value, it will dissipate, leaving behind its bits to be
recycled as building material for the next generation of values.
The remainder of this chapter introduces the atomic elements of
JavaScript programs, that is, the simple value types and the operators
that can act on such values.


### Numbers

Values of the _number_ type are, unsurprisingly, numeric values. In a
JavaScript program, they are written as follows:

```
13
```
Using that in a program will cause the bit pattern for the number 13
to come into existence inside the computer’s memory.
JavaScript uses a fixed number of bits, 64 of them, to store a sin-
gle number value. There are only so many patterns you can make
with 64 bits, which limits the number of different numbers that can be
represented. With _N_ decimal digits, you can represent 10N numbers.
Similarly, given 64 binary digits, you can represent 2^64 different num-
bers, which is about 18 quintillion (an 18 with 18 zeros after it). That’s
a lot.
Computer memory used to be much smaller, and people tended to
use groups of 8 or 16 bits to represent their numbers. It was easy to
accidentally _overflow_ such small numbers—to end up with a number
that did not fit into the given number of bits. Today, even computers
that fit in your pocket have plenty of memory, so you are free to use
64-bit chunks, and you need to worry about overflow only when dealing
with truly astronomical numbers.
Not all whole numbers less than 18 quintillion fit in a JavaScript
number, though. Those bits also store negative numbers, so one bit in-
dicates the sign of the number. A bigger issue is representing nonwhole
numbers. To do this, some of the bits are used to store the position
of the decimal point. The actual maximum whole number that can be


stored is more in the range of 9 quadrillion (15 zeros)—which is still
pleasantly huge.
Fractional numbers are written using a dot:
9.81

For very big or very small numbers, you may also use scientific notation
by adding an _e_ (for _exponent_ ), followed by the exponent of the number.

```
2.998e8
```
That’s 2.998 × 10^8 = 299,800,000.
Calculations with whole numbers (also called _integers_ ) that are smaller
than the aforementioned 9 quadrillion are guaranteed to always be pre-
cise. Unfortunately, calculations with fractional numbers are generally
not. Just asπ(pi) cannot be precisely expressed by a finite number of
decimal digits, many numbers lose some precision when only 64 bits are
available to store them. This is a shame, but it causes practical prob-
lems only in specific situations. The important thing is to be aware of it
and treat fractional digital numbers as approximations, not as precise
values.

**Arithmetic**

The main thing to do with numbers is arithmetic. Arithmetic oper-
ations such as addition or multiplication take two number values and
produce a new number from them. Here is what they look like in
JavaScript:


```
100 + 4 * 11
```
The+and*symbols are called _operators_. The first stands for addition
and the second stands for multiplication. Putting an operator between
two values will apply it to those values and produce a new value.
Does this example mean “Add 4 and 100, and multiply the result by
11”, or is the multiplication done before the adding? As you might have
guessed, the multiplication happens first. As in mathematics, you can
change this by wrapping the addition in parentheses.

```
(100 + 4) * 11
```
For subtraction, there is the-operator. Division can be done with the
/operator.
When operators appear together without parentheses, the order in
which they are applied is determined by the _precedence_ of the operators.
The example shows that multiplication comes before addition. The /
operator has the same precedence as *. Likewise, + and - have the
same precedence. When multiple operators with the same precedence
appear next to each other, as in1 - 2 + 1, they are applied left to right:
(1 - 2)+ 1.
Don’t worry too much about these precedence rules. When in doubt,
just add parentheses.
There is one more arithmetic operator, which you might not imme-
diately recognize. The % symbol is used to represent the _remainder_
operation. X % Y is the remainder of dividingX by Y. For example,
314 % 100produces 14 , and144 % 12gives 0. The remainder operator’s
precedence is the same as that of multiplication and division. You’ll


also often see this operator referred to as _modulo_.

**Specialnumbers**

There are three special values in JavaScript that are considered numbers
but don’t behave like normal numbers. The first two areInfinityand
-Infinity, which represent the positive and negative infinities.Infinity

- 1is stillInfinity, and so on. Don’t put too much trust in infinity-
based computation, though. It isn’t mathematically sound, and it will
quickly lead to the next special number: NaN.
NaNstands for “not a number”, even though it _is_ a value of the number
type. You’ll get this result when you, for example, try to calculate0 /
0 (zero divided by zero),Infinity - Infinity, or any number of other
numeric operations that don’t yield a meaningful result.

### Strings

The next basic data type is the _string_. Strings are used to represent
text. They are written by enclosing their content in quotes.

```
`Down on the sea`
"Lie on the ocean"
'Float on the ocean'
```
You can use single quotes, double quotes, or backticks to mark strings,
as long as the quotes at the start and the end of the string match.
You can put almost anything between quotes to have JavaScript make
a string value out of it. But a few characters are more diﬀicult. You


can imagine how putting quotes between quotes might be hard, since
they will look like the end of the string. _Newlines_ (the characters you
get when you pressenter) can be included only when the string is
quoted with backticks (\‘).
To make it possible to include such characters in a string, the follow-
ing notation is used: a backslash (\) inside quoted text indicates that
the character after it has a special meaning. This is called _escaping_ the
character. A quote that is preceded by a backslash will not end the
string but be part of it. When anncharacter occurs after a backslash,
it is interpreted as a newline. Similarly, atafter a backslash means a
tab character. Take the following string:

```
"This is the first line\nAnd this is the second"
```
This is the actual text in that string:

```
This is the first line
And this is the second
```
There are, of course, situations where you want a backslash in a string
to be just a backslash, not a special code. If two backslashes follow
each other, they will collapse together, and only one will be left in the
resulting string value. This is how the string “ _A newline character is
written like_ " _\n_ "_._ ” can be expressed:

```
"A newline character is written like \"\\n\"."
```
Strings, too, have to be modeled as a series of bits to be able to ex-
ist inside the computer. The way JavaScript does this is based on the


_Unicode_ standard. This standard assigns a number to virtually every
character you would ever need, including characters from Greek, Ara-
bic, Japanese, Armenian, and so on. If we have a number for every
character, a string can be described by a sequence of numbers. And
that’s what JavaScript does.
There’s a complication though: JavaScript’s representation uses 16
bits per string element, which can describe up to 2^16 different characters.
However, Unicode defines more characters than that—about twice as
many, at this point. So some characters, such as many emoji, take up
two “character positions” in JavaScript strings. We’ll come back to this
inChapter 5.
Strings cannot be divided, multiplied, or subtracted. The+operator
_can_ be used on them, not to add, but to _concatenate_ —to glue two strings
together. The following line will produce the string"concatenate":

```
"con" + "cat" + "e" + "nate"
```
String values have a number of associated functions ( _methods_ ) that can
be used to perform other operations on them. I’ll say more about these
inChapter 4.
Strings written with single or double quotes behave very much the
same—the only difference lies in which type of quote you need to escape
inside of them. Backtick-quoted strings, usually called _template literals_ ,
can do a few more tricks. Apart from being able to span lines, they can
also embed other values.

```
`half of 100 is ${100 / 2}`
```

When you write something inside ${}in a template literal, its result
will be computed, converted to a string, and included at that position.
This example produces the string"half of 100 is 50".

### Unary operators

Not all operators are symbols. Some are written as words. One example
is thetypeofoperator, which produces a string value naming the type
of the value you give it.

```
console.log(typeof 4.5)
// → number
console.log(typeof "x")
// → string
```
We will useconsole.login example code to indicate that we want to
see the result of evaluating something. (More about that in thenext
chapter.)
The other operators shown so far in this chapter all operated on two
values, but typeoftakes only one. Operators that use two values are
called _binary_ operators, while those that take one are called _unary_ op-
erators. The minus operator (-) can be used both as a binary operator
and as a unary operator.

```
console.log(- (10 - 2))
// → -8
```

### Boolean values

It is often useful to have a value that distinguishes between only two
possibilities, like “yes” and “no” or “on” and “off”. For this purpose,
JavaScript has a _Boolean_ type, which has just two values, true and false,
written as those words.

**Comparison**

Here is one way to produce Boolean values:

```
console.log(3 > 2)
// → true
console.log(3 < 2)
// → false
```
The>and<signs are the traditional symbols for “is greater than” and
“is less than”, respectively. They are binary operators. Applying them
results in a Boolean value that indicates whether they hold true in this
case.
Strings can be compared in the same way.
console.log("Aardvark" < "Zoroaster")
// → true

The way strings are ordered is roughly alphabetic but not really what
you’d expect to see in a dictionary: uppercase letters are always “less”
than lowercase ones, so"Z" < "a", and nonalphabetic characters (!, -,
and so on) are also included in the ordering. When comparing strings,


JavaScript goes over the characters from left to right, comparing the
Unicode codes one by one.
Other similar operators are>= (greater than or equal to), <=(less
than or equal to),==(equal to), and!=(not equal to).

```
console.log("Garnet" != "Ruby")
// → true
console.log("Pearl" == "Amethyst")
// → false
```
There is only one value in JavaScript that is not equal to itself, and
that isNaN(“not a number”).

```
console.log(NaN == NaN)
// → false
```
NaNis supposed to denote the result of a nonsensical computation, and as
such, it isn’t equal to the result of any _other_ nonsensical computations.

**Logicaloperators**

There are also some operations that can be applied to Boolean values
themselves. JavaScript supports three logical operators: _and_ , _or_ , and
_not_. These can be used to “reason” about Booleans.
The&&operator represents logical _and_. It is a binary operator, and
its result is true only if both the values given to it are true.

```
console.log(true && false)
// → false
console.log(true && true)
```

```
// → true
```
The ||operator denotes logical _or_. It produces true if either of the
values given to it is true.

```
console.log(false || true)
// → true
console.log(false || false)
// → false
```
_Not_ is written as an exclamation mark (!). It is a unary operator that
flips the value given to it—!trueproducesfalseand!falsegivestrue.
When mixing these Boolean operators with arithmetic and other op-
erators, it is not always obvious when parentheses are needed. In prac-
tice, you can usually get by with knowing that of the operators we have
seen so far,||has the lowest precedence, then comes&&, then the com-
parison operators (>,==, and so on), and then the rest. This order has
been chosen such that, in typical expressions like the following one, as
few parentheses as possible are necessary:

```
1 + 1 == 2 && 10 * 10 > 50
```
The last logical operator we will look at is not unary, not binary, but
_ternary_ , operating on three values. It is written with a question mark
and a colon, like this:

```
console.log(true? 1 : 2);
// → 1
console.log(false? 1 : 2);
// → 2
```

This one is called the _conditional_ operator (or sometimes just _the ternary
operator_ since it is the only such operator in the language). The oper-
ator uses the value to the left of the question mark to decide which of
the two other values to “pick”. If you writea? b : c, the result will be
bwhenais true andcotherwise.

### Empty values.

There are two special values, writtennullandundefined, that are used
to denote the absence of a _meaningful_ value. They are themselves val-
ues, but they carry no information.
Many operations in the language that don’t produce a meaningful
value yieldundefinedsimply because they have to yield _some_ value.
The difference in meaning betweenundefinedandnullis an accident
of JavaScript’s design, and it doesn’t matter most of the time. In
cases where you actually have to concern yourself with these values, I
recommend treating them as mostly interchangeable.

### Automatic type conversion.

In theintroduction, I mentioned that JavaScript goes out of its way
to accept almost any program you give it, even programs that do odd
things. This is nicely demonstrated by the following expressions:

```
console.log(8 * null)
// → 0
console.log("5" - 1)
```

```
// → 4
console.log("5" + 1)
// → 51
console.log("five" * 2)
// → NaN
console.log(false == 0)
// → true
```
When an operator is applied to the “wrong” type of value, JavaScript
will quietly convert that value to the type it needs, using a set of rules
that often aren’t what you want or expect. This is called _type coercion_.
Thenullin the first expression becomes 0 and the"5"in the second
expression becomes 5 (from string to number). Yet in the third expres-
sion, +tries string concatenation before numeric addition, so the 1 is
converted to"1"(from number to string).
When something that doesn’t map to a number in an obvious way
(such as "five" or undefined) is converted to a number, you get the
valueNaN. Further arithmetic operations onNaNkeep producingNaN, so
if you find yourself getting one of those in an unexpected place, look
for accidental type conversions.
When comparing values of the same type using the==operator, the
outcome is easy to predict: you should get true when both values are the
same, except in the case ofNaN. But when the types differ, JavaScript
uses a complicated and confusing set of rules to determine what to do.
In most cases, it just tries to convert one of the values to the other
value’s type. However, whennull or undefined occurs on either side
of the operator, it produces true only if both sides are one ofnullor
undefined.


```
console.log(null == undefined);
// → true
console.log(null == 0);
// → false
```
That behavior is often useful. When you want to test whether a value
has a real value instead ofnullorundefined, you can compare it tonull
with the==or!=operator.
What if you want to test whether something refers to the precise
valuefalse? Expressions like0 == falseand"" == falseare also true
because of automatic type conversion. When you do _not_ want any type
conversions to happen, there are two additional operators:===and!==.
The first tests whether a value is _precisely_ equal to the other, and the
second tests whether it is not precisely equal. Thus "" === false is
false, as expected.
I recommend using the three-character comparison operators defen-
sively to prevent unexpected type conversions from tripping you up.
But when you’re certain the types on both sides will be the same, there
is no problem with using the shorter operators.

**Short-circuitingoflogicaloperators**

The logical operators &&and ||handle values of different types in a
peculiar way. They will convert the value on their left side to Boolean
type in order to decide what to do, but depending on the operator
and the result of that conversion, they will return either the _original_
left-hand value or the right-hand value.
The||operator, for example, will return the value to its left when


that value can be converted to true and will return the value on its right
otherwise. This has the expected effect when the values are Boolean
and does something analogous for values of other types.

```
console.log(null || "user")
// → user
console.log("Agnes" || "user")
// → Agnes
```
We can use this functionality as a way to fall back on a default value.
If you have a value that might be empty, you can put||after it with
a replacement value. If the initial value can be converted to false,
you’ll get the replacement instead. The rules for converting strings and
numbers to Boolean values state that 0 ,NaN, and the empty string ("")
count as false, while all the other values count as true. That means
0 || -1produces-1, and"" || "!?"yields"!?".
The??operator resembles||but returns the value on the right only
if the one on the left isnullorundefined, not if it is some other value
that can be converted tofalse. Often, this is preferable to the behavior
of||.

```
console.log(0 || 100);
// → 100
console.log(0 ?? 100);
// → 0
console.log(null ?? 100);
// → 100
```
The&&operator works similarly but the other way around. When the


value to its left is something that converts to false, it returns that value,
and otherwise it returns the value on its right.
Another important property of these two operators is that the part
to their right is evaluated only when necessary. In the case oftrue
|| X, no matter what Xis—even if it’s a piece of program that does
something _terrible_ —the result will be true, andXis never evaluated.
The same goes forfalse && X, which is false and will ignoreX. This is
called _short-circuit evaluation_.
The conditional operator works in a similar way. Of the second and
third values, only the one that is selected is evaluated.

### Summary

We looked at four types of JavaScript values in this chapter: numbers,
strings, Booleans, and undefined values. Such values are created by
typing in their name (true,null) or value ( 13 ,"abc").
You can combine and transform values with operators. We saw binary
operators for arithmetic (+,-,*,/, and%), string concatenation (+),
comparison (==,!=,===,!==,<,>,<=,>=), and logic (&&,||,??), as well
as several unary operators (-to negate a number,!to negate logically,
andtypeofto find a value’s type) and a ternary operator (?:) to pick
one of two values based on a third value.
This gives you enough information to use JavaScript as a pocket
calculator but not much more. Thenext chapterwill start tying these
expressions together into basic programs.


```
“And my heart glows bright red under my filmy, translucent
skin and they have to administer 10cc of JavaScript to get me
to come back. (I respond well to toxins in the blood.) Man,
that stuff will kick the peaches right out your gills!”
—_why, Why’s (Poignant) Guide to Ruby
```
**Chapter2**

## ProgramStructure

In this chapter, we will start to do things that can actually be called
_programming_. We will expand our command of the JavaScript language
beyond the nouns and sentence fragments we’ve seen so far to the point
where we can express meaningful prose.

### Expressions and statements

InChapter 1, we made values and applied operators to them to get new
values. Creating values like this is the main substance of any JavaScript
program. But that substance has to be framed in a larger structure to
be useful. That’s what we’ll cover in this chapter.
A fragment of code that produces a value is called an _expression_.
Every value that is written literally (such as 22 or"psychoanalysis") is
an expression. An expression between parentheses is also an expression,
as is a binary operator applied to two expressions or a unary operator
applied to one.
This shows part of the beauty of a language-based interface. Expres-


sions can contain other expressions in a way similar to how subsentences
in human languages are nested—a subsentence can contain its own sub-
sentences, and so on. This allows us to build expressions that describe
arbitrarily complex computations.
If an expression corresponds to a sentence fragment, a JavaScript
_statement_ corresponds to a full sentence. A program is a list of state-
ments.
The simplest kind of statement is an expression with a semicolon
after it. This is a program:

```
1;
!false;
```
It is a useless program, though. An expression can be content to just
produce a value, which can then be used by the enclosing code. How-
ever, a statement stands on its own, so if it doesn’t affect the world, it’s
useless. It may display something on the screen, as withconsole.log, or
change the state of the machine in a way that will affect the statements
that come after it. These changes are called _side effects_. The state-
ments in the previous example just produce the values 1 andtrueand
then immediately throw them away. This leaves no impression on the
world at all. When you run this program, nothing observable happens.
In some cases, JavaScript allows you to omit the semicolon at the
end of a statement. In other cases, it has to be there, or the next line
will be treated as part of the same statement. The rules for when it
can be safely omitted are somewhat complex and error prone. So in
this book, every statement that needs a semicolon will always get one.
I recommend you do the same, at least until you’ve learned more about


the subtleties of missing semicolons.

### Bindings

How does a program keep an internal state? How does it remember
things? We have seen how to produce new values from old values,
but this does not change the old values, and the new value must be
used immediately or it will dissipate again. To catch and hold values,
JavaScript provides a thing called a _binding_ , or _variable_.

```
let caught = 5 * 5;
```
That gives us a second kind of statement. The special word ( _keyword_ )
letindicates that this sentence is going to define a binding. It is followed
by the name of the binding and, if we want to immediately give it a
value, by an=operator and an expression.
The example creates a binding calledcaughtand uses it to grab hold
of the number that is produced by multiplying 5 by 5.
After a binding has been defined, its name can be used as an expres-
sion. The value of such an expression is the value the binding currently
holds. Here’s an example:

```
let ten = 10;
console.log(ten * ten);
// → 100
```
When a binding points at a value, that does not mean it is tied to
that value forever. The=operator can be used at any time on existing


bindings to disconnect them from their current value and have them
point to a new one:

```
let mood = "light";
console.log(mood);
// → light
mood = "dark";
console.log(mood);
// → dark
```
You should imagine bindings as tentacles rather than boxes. They do
not _contain_ values; they _grasp_ them—two bindings can refer to the
same value. A program can access only the values to which it still has
a reference. When you need to remember something, you either grow a
tentacle to hold on to it or reattach one of your existing tentacles to it.
Let’s look at another example. To remember the number of dollars
that Luigi still owes you, you create a binding. When he pays back $35,
you give this binding a new value.

```
let luigisDebt = 140;
luigisDebt = luigisDebt - 35;
console.log(luigisDebt);
// → 105
```
When you define a binding without giving it a value, the tentacle has
nothing to grasp, so it ends in thin air. If you ask for the value of an
empty binding, you’ll get the valueundefined.
A singleletstatement may define multiple bindings. The definitions
must be separated by commas:


```
let one = 1, two = 2;
console.log(one + two);
// → 3
```
The wordsvarandconstcan also be used to create bindings, in a similar
fashion tolet.

```
var name = "Ayda";
const greeting = "Hello ";
console.log(greeting + name);
// → Hello Ayda
```
The first of these,var(short for “variable”), is the way bindings were
declared in pre-2015 JavaScript, whenletdidn’t exist yet. I’ll get back
to the precise way it differs from let in thenext chapter. For now,
remember that it mostly does the same thing, but we’ll rarely use it in
this book because it behaves oddly in some situations.
The wordconst stands for _constant_. It defines a constant binding,
which points at the same value for as long as it lives. This is useful for
bindings that just give a name to a value so that you can easily refer
to it later.

### Binding names

Binding names can be any sequence of one or more letters. Digits can
be part of binding names—catch22is a valid name, for example—but
the name must not start with a digit. A binding name may include
dollar signs ($) or underscores (_) but no other punctuation or special


characters.
Words with a special meaning, such aslet, are _keywords_ , and may
not be used as binding names. There are also a number of words that
are “reserved for use” in future versions of JavaScript, which also can’t
be used as binding names. The full list of keywords and reserved words
is rather long:

```
break case catch class const continue debugger default
delete do else enum export extends false finally for
function if implements import interface in instanceof let
new package private protected public return static super
switch this throw true try typeof var void while with yield
```
Don’t worry about memorizing this list. When creating a binding pro-
duces an unexpected syntax error, check whether you’re trying to define
a reserved word.

### The environment

The collection of bindings and their values that exist at a given time is
called the _environment_. When a program starts up, this environment
is not empty. It always contains bindings that are part of the language
standard, and most of the time, it also has bindings that provide ways
to interact with the surrounding system. For example, in a browser,
there are functions to interact with the currently loaded website and to
read mouse and keyboard input.


### Functions.

A lot of the values provided in the default environment have the type
_function_. A function is a piece of program wrapped in a value. Such
values can be _applied_ in order to run the wrapped program. For exam-
ple, in a browser environment, the bindingpromptholds a function that
shows a little dialog asking for user input. It is used like this:

```
prompt("Enter passcode");
```
Executing a function is called _invoking_ , _calling_ , or _applying_ it. You
can call a function by putting parentheses after an expression that pro-
duces a function value. Usually you’ll directly use the name of the
binding that holds the function. The values between the parentheses
are given to the program inside the function. In the example, theprompt
function uses the string that we give it as the text to show in the dialog
box. Values given to functions are called _arguments_. Different functions
might need a different number or different types of arguments.
Thepromptfunction isn’t used much in modern web programming,
mostly because you have no control over the way the resulting dialog


looks, but it can be helpful in toy programs and experiments.

### The console.log function

In the examples, I usedconsole.logto output values. Most JavaScript
systems (including all modern web browsers and Node.js) provide a
console.logfunction that writes out its arguments to _some_ text output
device. In browsers, the output lands in the JavaScript console. This
part of the browser interface is hidden by default, but most browsers
open it when you press F12 or, on a Mac,command-option-I. If that
does not work, search through the menus for an item named Developer
Tools or similar.
Though binding names cannot contain period characters,console.log
does have one. This is becauseconsole.logisn’t a simple binding, but
an expression that retrieves thelogproperty from the value held by the
consolebinding. We’ll find out exactly what this means inChapter 4.

### Return values

Showing a dialog box or writing text to the screen is a _side effect_. Many
functions are useful because of the side effects they produce. Functions
may also produce values, in which case they don’t need to have a side
effect to be useful. For example, the functionMath.maxtakes any amount
of number arguments and gives back the greatest.

```
console.log(Math.max(2, 4));
// → 4
```

When a function produces a value, it is said to _return_ that value. Any-
thing that produces a value is an expression in JavaScript, which means
that function calls can be used within larger expressions. In the follow-
ing code, a call toMath.min, which is the opposite ofMath.max, is used
as part of a plus expression:

```
console.log(Math.min(2, 4) + 100);
// → 102
```
Chapter 3will explain how to write your own functions.

### Control flow

When your program contains more than one statement, the statements
are executed as though they were a story, from top to bottom. For
example, the following program has two statements. The first asks the
user for a number, and the second, which is executed after the first,
shows the square of that number:

```
let theNumber = Number(prompt("Pick a number"));
console.log("Your number is the square root of " +
theNumber * theNumber);
```
The functionNumberconverts a value to a number. We need that con-
version because the result ofpromptis a string value, and we want a
number. There are similar functions called String and Booleanthat
convert values to those types.
Here is the rather trivial schematic representation of straight-line
control flow:


### Conditional execution.

Not all programs are straight roads. We may, for example, want to
create a branching road where the program takes the proper branch
based on the situation at hand. This is called _conditional execution_.

Conditional execution is created with theifkeyword in JavaScript.
In the simple case, we want some code to be executed if, and only if,
a certain condition holds. We might, for example, want to show the
square of the input only if the input is actually a number:

```
let theNumber = Number(prompt("Pick a number"));
if (!Number.isNaN(theNumber)) {
console.log("Your number is the square root of " +
theNumber * theNumber);
}
```
With this modification, if you enter “parrot”, no output is shown.
Theifkeyword executes or skips a statement depending on the value
of a Boolean expression. The deciding expression is written after the
keyword, between parentheses, followed by the statement to execute.
TheNumber.isNaNfunction is a standard JavaScript function that re-
turnstrueonly if the argument it is given isNaN. TheNumberfunction


happens to returnNaNwhen you give it a string that doesn’t represent
a valid number. Thus, the condition translates to “unlesstheNumberis
not-a-number, do this”.
The statement after theifis wrapped in braces ({and }) in this
example. The braces can be used to group any number of statements
into a single statement, called a _block_. You could also have omitted them
in this case, since they hold only a single statement, but to avoid having
to think about whether they are needed, most JavaScript programmers
use them in every wrapped statement like this. We’ll mostly follow that
convention in this book, except for the occasional one-liner.

```
if (1 + 1 == 2) console.log("It's true");
// → It's true
```
You often won’t just have code that executes when a condition holds
true, but also code that handles the other case. This alternate path is
represented by the second arrow in the diagram. You can use theelse
keyword, together withif, to create two separate, alternative execution
paths:

```
let theNumber = Number(prompt("Pick a number"));
if (!Number.isNaN(theNumber)) {
console.log("Your number is the square root of " +
theNumber * theNumber);
} else {
console.log("Hey. Why didn't you give me a number?");
}
```
If you have more than two paths to choose from, you can “chain” mul-


tipleif/elsepairs together. Here’s an example:

```
let num = Number(prompt("Pick a number"));
```
```
if (num < 10) {
console.log("Small");
} else if (num < 100) {
console.log("Medium");
} else {
console.log("Large");
}
```
The program will first check whether num is less than 10. If it is, it
chooses that branch, shows"Small", and is done. If it isn’t, it takes the
elsebranch, which itself contains a secondif. If the second condition
(< 100) holds, that means the number is at least 10 but below 100, and
"Medium" is shown. If it doesn’t, the second and lastelse branch is
chosen.
The schema for this program looks something like this:

### while and do loops.

Consider a program that outputs all even numbers from 0 to 12. One
way to write this is as follows:


```
console.log(0);
console.log(2);
console.log(4);
console.log(6);
console.log(8);
console.log(10);
console.log(12);
```
That works, but the idea of writing a program is to make something
_less_ work, not more. If we needed all even numbers less than 1,000, this
approach would be unworkable. What we need is a way to run a piece
of code multiple times. This form of control flow is called a _loop_.

Looping control flow allows us to go back to some point in the pro-
gram where we were before and repeat it with our current program
state. If we combine this with a binding that counts, we can do some-
thing like this:

```
let number = 0;
while (number <= 12) {
console.log(number);
number = number + 2;
}
// → 0
// → 2
// ... etcetera
```

A statement starting with the keywordwhilecreates a loop. The word
whileis followed by an expression in parentheses and then a statement,
much likeif. The loop keeps entering that statement as long as the
expression produces a value that givestruewhen converted to Boolean.
Thenumber binding demonstrates the way a binding can track the
progress of a program. Every time the loop repeats, number gets a
value that is 2 more than its previous value. At the beginning of every
repetition, it is compared with the number 12 to decide whether the
program’s work is finished.
As an example that actually does something useful, we can now write
a program that calculates and shows the value of 2^10 (2 to the 10th
power). We use two bindings: one to keep track of our result and one
to count how often we have multiplied this result by 2. The loop tests
whether the second binding has reached 10 yet and, if not, updates both
bindings.

```
let result = 1;
let counter = 0;
while (counter < 10) {
result = result * 2;
counter = counter + 1;
}
console.log(result);
// → 1024
```
The counter could also have started at 1 and checked for<= 10, but for
reasons that will become apparent inChapter 4, it is a good idea to get
used to counting from 0.


Note that JavaScript also has an operator for exponentiation (2 **
10 ), which you would use to compute this in real code—but that would
have ruined the example.
Adoloop is a control structure similar to awhileloop. It differs only
on one point: adoloop always executes its body at least once, and it
starts testing whether it should stop only after that first execution. To
reflect this, the test appears after the body of the loop:

```
let yourName;
do {
yourName = prompt("Who are you?");
} while (!yourName);
console.log("Hello " + yourName);
```
This program will force you to enter a name. It will ask again and
again until it gets something that is not an empty string. Applying the
!operator will convert a value to Boolean type before negating it, and
all strings except""convert to true. This means the loop continues
going round until you provide a non-empty name.

### Indenting Code

In the examples, I’ve been adding spaces in front of statements that
are part of some larger statement. These spaces are not required—the
computer will accept the program just fine without them. In fact, even
the line breaks in programs are optional. You could write a program as
a single long line if you felt like it.
The role of this indentation inside blocks is to make the structure of


the code stand out to human readers. In code where new blocks are
opened inside other blocks, it can become hard to see where one block
ends and another begins. With proper indentation, the visual shape of
a program corresponds to the shape of the blocks inside it. I like to
use two spaces for every open block, but tastes differ—some people use
four spaces, and some people use tab characters. The important thing
is that each new block adds the same amount of space.

```
if (false != true) {
console.log("That makes sense.");
if (1 < 2) {
console.log("No surprise there.");
}
}
```
Most code editor programs will help by automatically indenting new
lines the proper amount.

### for loops

Many loops follow the pattern shown in the whileexamples. First a
“counter” binding is created to track the progress of the loop. Then
comes awhileloop, usually with a test expression that checks whether
the counter has reached its end value. At the end of the loop body, the
counter is updated to track progress.
Because this pattern is so common, JavaScript and similar languages
provide a slightly shorter and more comprehensive form, theforloop:


```
for (let number = 0; number <= 12; number = number + 2) {
console.log(number);
}
// → 0
// → 2
// ... etcetera
```
This program is exactly equivalent to theearliereven-number-printing
example. The only change is that all the statements that are related to
the “state” of the loop are grouped together afterfor.
The parentheses after afor keyword must contain two semicolons.
The part before the first semicolon _initializes_ the loop, usually by defin-
ing a binding. The second part is the expression that _checks_ whether
the loop must continue. The final part _updates_ the state of the loop
after every iteration. In most cases, this is shorter and clearer than a
whileconstruct.
This is the code that computes 2^10 usingforinstead ofwhile:
let result = 1;
for (let counter = 0; counter < 10; counter = counter + 1) {
result = result * 2;
}
console.log(result);
// → 1024


### Breaking Out of a Loop

Having the looping condition producefalseis not the only way a loop
can finish. Thebreakstatement has the effect of immediately jumping
out of the enclosing loop. Its use is demonstrated in the following
program, which finds the first number that is both greater than or
equal to 20 and divisible by 7:

```
for (let current = 20; ; current = current + 1) {
if (current % 7 == 0) {
console.log(current);
break;
}
}
// → 21
```
Using the remainder (%) operator is an easy way to test whether a
number is divisible by another number. If it is, the remainder of their
division is zero.
Theforconstruct in the example does not have a part that checks
for the end of the loop. This means that the loop will never stop unless
thebreakstatement inside is executed.
If you were to remove thatbreakstatement or you accidentally write
an end condition that always producestrue, your program would get
stuck in an _infinite loop_. A program stuck in an infinite loop will never
finish running, which is usually a bad thing.
The continuekeyword is similar to breakin that it influences the
progress of a loop. Whencontinueis encountered in a loop body, control


jumps out of the body and continues with the loop’s next iteration.

### Updating bindings succinctly

Especially when looping, a program often needs to “update” a binding
to hold a value based on that binding’s previous value.

```
counter = counter + 1;
```
JavaScript provides a shortcut for this:

```
counter += 1;
```
Similar shortcuts work for many other operators, such asresult *= 2
to doubleresultorcounter -= 1to count downward.
This allows us to further shorten our counting example:
for (let number = 0; number <= 12; number += 2) {
console.log(number);
}

Forcounter += 1andcounter -= 1, there are even shorter equivalents:
counter++andcounter--.

### Dispatching on a value with switch

It is not uncommon for code to look like this:

```
if (x == "value1") action1();
else if (x == "value2") action2();
```

```
else if (x == "value3") action3();
else defaultAction();
```
There is a construct called switchthat is intended to express such a
“dispatch” in a more direct way. Unfortunately, the syntax JavaScript
uses for this (which it inherited from the C/Java line of programming
languages) is somewhat awkward—a chain ofifstatements may look
better. Here is an example:

```
switch (prompt("What is the weather like?")) {
case "rainy":
console.log("Remember to bring an umbrella.");
break;
case "sunny":
console.log("Dress lightly.");
case "cloudy":
console.log("Go outside.");
break;
default:
console.log("Unknown weather type!");
break;
}
```
You may put any number of case labels inside the block opened by
switch. The program will start executing at the label that corresponds
to the value thatswitchwas given, or atdefaultif no matching value
is found. It will continue executing, even across other labels, until it
reaches abreakstatement. In some cases, such as the"sunny"case in
the example, this can be used to share some code between cases (it
recommends going outside for both sunny and cloudy weather). Be


careful, though—it is easy to forget such abreak, which will cause the
program to execute code you do not want executed.

### Capitalization

Binding names may not contain spaces, yet it is often helpful to use
multiple words to clearly describe what the binding represents. These
are pretty much your choices for writing a binding name with several
words in it:

```
fuzzylittleturtle
fuzzy_little_turtle
FuzzyLittleTurtle
fuzzyLittleTurtle
```
The first style can be hard to read. I rather like the look of the un-
derscores, though that style is a little painful to type. The standard
JavaScript functions, and most JavaScript programmers, follow the fi-
nal style—they capitalize every word except the first. It is not hard to
get used to little things like that, and code with mixed naming styles
can be jarring to read, so we follow this convention.
In a few cases, such as theNumberfunction, the first letter of a binding
is also capitalized. This was done to mark this function as a constructor.
It will become clear what a constructor is in Chapter 6. For now,
the important thing is to not be bothered by this apparent lack of
consistency.


### Comments

Often, raw code does not convey all the information you want a program
to convey to human readers, or it conveys it in such a cryptic way that
people might not understand it. At other times, you might just want
to include some related thoughts as part of your program. This is what
_comments_ are for.
A comment is a piece of text that is part of a program but is com-
pletely ignored by the computer. JavaScript has two ways of writing
comments. To write a single-line comment, you can use two slash char-
acters (//) and then the comment text after it:

```
let accountBalance = calculateBalance(account);
// It's a green hollow where a river sings
accountBalance.adjust();
// Madly catching white tatters in the grass.
let report = new Report();
// Where the sun on the proud mountain rings:
addToReport(accountBalance, report);
// It's a little valley, foaming like light in a glass.
```
A//comment goes only to the end of the line. A section of text between
/*and*/will be ignored in its entirety, regardless of whether it contains
line breaks. This is useful for adding blocks of information about a file
or a chunk of program:

```
/*
I first found this number scrawled on the back of an old
notebook. Since then, it has often dropped by, showing up in
```

```
phone numbers and the serial numbers of products that I've
bought. It obviously likes me, so I've decided to keep it.
*/
const myNumber = 11213;
```
### Summary

You now know that a program is built out of statements, which them-
selves sometimes contain more statements. Statements tend to contain
expressions, which themselves can be built out of smaller expressions.
Putting statements after one another gives you a program that is
executed from top to bottom. You can introduce disturbances in the
flow of control by using conditional (if,else, andswitch) and looping
(while,do, andfor) statements.
Bindings can be used to file pieces of data under a name, and they are
useful for tracking state in your program. The environment is the set
of bindings that are defined. JavaScript systems always put a number
of useful standard bindings into your environment.
Functions are special values that encapsulate a piece of program. You
can invoke them by writingfunctionName(argument1, argument2). Such
a function call is an expression and may produce a value.

### Exercises

If you are unsure how to test your solutions to the exercises, refer to
theintroduction.


Each exercise starts with a problem description. Read this descrip-
tion and try to solve the exercise. If you run into problems, consider
reading the hints at theend of the book. You can find full solutions to
the exercises online at _https://eloquentjavascript.net/code_. If you want
to learn something from the exercises, I recommend looking at the so-
lutions only after you’ve solved the exercise, or at least after you’ve
attacked it long and hard enough to have a slight headache.

**Loopingatriangle**

Write a loop that makes seven calls toconsole.logto output the fol-
lowing triangle:

```
#
##
###
####
#####
######
#######
```
It may be useful to know that you can find the length of a string by
writing.lengthafter it.

```
let abc = "abc";
console.log(abc.length);
// → 3
```

**FizzBuzz**

Write a program that usesconsole.logto print all the numbers from 1
to 100, with two exceptions. For numbers divisible by 3, print"Fizz"
instead of the number, and for numbers divisible by 5 (and not 3), print
"Buzz"instead.
When you have that working, modify your program to print"FizzBuzz
"for numbers that are divisible by both 3 and 5 (and still print"Fizz"
or"Buzz"for numbers divisible by only one of those).
(This is actually an interview question that has been claimed to weed
out a significant percentage of programmer candidates. So if you solved
it, your labor market value just went up.)

**Chessboard**

Write a program that creates a string that represents an 8×8 grid, using
newline characters to separate lines. At each position of the grid there
is either a space or a "#" character. The characters should form a
chessboard.
Passing this string toconsole.logshould show something like this:
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #


When you have a program that generates this pattern, define a bind-
ing size = 8and change the program so that it works for any size,
outputting a grid of the given width and height.


```
“People think that computer science is the art of geniuses but
the actual reality is the opposite, just many people doing
things that build on each other, like a wall of mini stones.”
—Donald Knuth
```
**Chapter3**

## Functions

Functions are one of the most central tools in JavaScript programming.
The concept of wrapping a piece of program in a value has many uses.
It gives us a way to structure larger programs, to reduce repetition, to
associate names with subprograms, and to isolate these subprograms
from each other.
The most obvious application of functions is defining new vocabulary.
Creating new words in prose is usually bad style, but in programming,
it is indispensable.
Typical adult English speakers have some 20,000 words in their vo-
cabulary. Few programming languages come with 20,000 commands
built in. And the vocabulary that _is_ available tends to be more precisely
defined, and thus less flexible, than in human language. Therefore, we
_have_ to introduce new words to avoid excessive verbosity.


### Defining a function

A function definition is a regular binding where the value of the binding
is a function. For example, this code definessquareto refer to a function
that produces the square of a given number:

```
const square = function(x) {
return x * x;
};
```
```
console.log(square(12));
// → 144
```
A function is created with an expression that starts with the keyword
function. Functions have a set of _parameters_ (in this case, onlyx) and
a _body_ , which contains the statements that are to be executed when the
function is called. The body of a function created this way must always
be wrapped in braces, even when it consists of only a single statement.
A function can have multiple parameters or no parameters at all. In
the following example, makeNoisedoes not list any parameter names,
whereasroundTo(which roundsnto the nearest multiple ofstep) lists
two:

```
const makeNoise = function() {
console.log("Pling!");
};
```
```
makeNoise();
// → Pling!
```

```
const roundTo = function(n, step) {
let remainder = n % step;
return n - remainder + (remainder < step / 2? 0 : step);
};
```
```
console.log(roundTo(23, 10));
// → 20
```
Some functions, such asroundToandsquare, produce a value, and some
don’t, such asmakeNoise, whose only result is a side effect. Areturn
statement determines the value the function returns. When control
comes across such a statement, it immediately jumps out of the cur-
rent function and gives the returned value to the code that called the
function. Areturnkeyword without an expression after it will cause
the function to returnundefined. Functions that don’t have areturn
statement at all, such asmakeNoise, similarly returnundefined.
Parameters to a function behave like regular bindings, but their ini-
tial values are given by the _caller_ of the function, not the code in the
function itself.

### Bindings and scopes.

Each binding has a _scope_ , which is the part of the program in which the
binding is visible. For bindings defined outside of any function, block,
or module (seeChapter 10), the scope is the whole program—you can
refer to such bindings wherever you want. These are called _global_.
Bindings created for function parameters or declared inside a function


can be referenced only in that function, so they are known as _local_
bindings. Every time the function is called, new instances of these
bindings are created. This provides some isolation between functions—
each function call acts in its own little world (its local environment)
and can often be understood without knowing a lot about what’s going
on in the global environment.
Bindings declared with letand constare in fact local to the _block_
in which they are declared, so if you create one of those inside of a
loop, the code before and after the loop cannot “see” it. In pre-2015
JavaScript, only functions created new scopes, so old-style bindings,
created with thevarkeyword, are visible throughout the whole function
in which they appear—or throughout the global scope, if they are not
in a function.

```
let x = 10; // global
if (true) {
let y = 20; // local to block
var z = 30; // also global
}
```
Each scope can “look out” into the scope around it, soxis visible inside
the block in the example. The exception is when multiple bindings have
the same name—in that case, code can see only the innermost one. For
example, when the code inside thehalvefunction refers ton, it is seeing
its _own_ n, not the globaln.

```
const halve = function(n) {
return n / 2;
};
```

```
let n = 10;
console.log(halve(100));
// → 50
console.log(n);
// → 10
```
### Nested scope

JavaScript distinguishes not just global and local bindings. Blocks and
functions can be created inside other blocks and functions, producing
multiple degrees of locality.
For example, this function—which outputs the ingredients needed to
make a batch of hummus—has another function inside it:

```
const hummus = function(factor) {
const ingredient = function(amount, unit, name) {
let ingredientAmount = amount * factor;
if (ingredientAmount > 1) {
unit += "s";
}
console.log(`${ingredientAmount} ${unit} ${name}`);
};
ingredient(1, "can", "chickpeas");
ingredient(0.25, "cup", "tahini");
ingredient(0.25, "cup", "lemon juice");
ingredient(1, "clove", "garlic");
ingredient(2, "tablespoon", "olive oil");
```

```
ingredient(0.5, "teaspoon", "cumin");
};
```
The code inside theingredientfunction can see thefactorbinding from
the outer function, but its local bindings, such asunitoringredientAmount
, are not visible in the outer function.
The set of bindings visible inside a block is determined by the place
of that block in the program text. Each local scope can also see all the
local scopes that contain it, and all scopes can see the global scope.
This approach to binding visibility is called _lexical scoping_.

### Functions as values

A function binding usually simply acts as a name for a specific piece of
the program. Such a binding is defined once and never changed. This
makes it easy to confuse the function and its name.
But the two are different. A function value can do all the things that
other values can do—you can use it in arbitrary expressions, not just
call it. It is possible to store a function value in a new binding, pass
it as an argument to a function, and so on. Similarly, a binding that
holds a function is still just a regular binding and can, if not constant,
be assigned a new value, like so:

```
let launchMissiles = function() {
missileSystem.launch("now");
};
if (safeMode) {
launchMissiles = function() {/* do nothing */};
```

```
}
```
InChapter 5, we’ll discuss the interesting things that we can do by
passing function values to other functions.

### Declaration notation

There is a slightly shorter way to create a function binding. When the
functionkeyword is used at the start of a statement, it works differently:

```
function square(x) {
return x * x;
}
```
This is a function _declaration_. The statement defines the bindingsquare
and points it at the given function. It is slightly easier to write and
doesn’t require a semicolon after the function.
There is one subtlety with this form of function definition.
console.log("The future says:", future());

```
function future() {
return "You'll never have flying cars";
}
```
The preceding code works, even though the function is defined _below_
the code that uses it. Function declarations are not part of the regular
top-to-bottom flow of control. They are conceptually moved to the top
of their scope and can be used by all the code in that scope. This is


sometimes useful because it offers the freedom to order code in a way
that seems the clearest, without worrying about having to define all
functions before they are used.

### Arrow functions

There’s a third notation for functions, which looks very different from
the others. Instead of thefunctionkeyword, it uses an arrow (=>) made
up of an equal sign and a greater-than character (not to be confused
with the greater-than-or-equal operator, which is written>=):

```
const roundTo = (n, step) => {
let remainder = n % step;
return n - remainder + (remainder < step / 2? 0 : step);
};
```
The arrow comes _after_ the list of parameters and is followed by the func-
tion’s body. It expresses something like “this input (the parameters)
produces this result (the body)”.
When there is only one parameter name, you can omit the paren-
theses around the parameter list. If the body is a single expression
rather than a block in braces, that expression will be returned from the
function. So, these two definitions ofsquaredo the same thing:

```
const square1 = (x) => { return x * x; };
const square2 = x => x * x;
```
When an arrow function has no parameters at all, its parameter list is
just an empty set of parentheses.


```
const horn = () => {
console.log("Toot");
};
```
There’s no deep reason to have both arrow functions andfunctionex-
pressions in the language. Apart from a minor detail, which we’ll discuss
inChapter 6, they do the same thing. Arrow functions were added in
2015, mostly to make it possible to write small function expressions in
a less verbose way. We’ll use them often inChapter 5.

### The call stack

The way control flows through functions is somewhat involved. Let’s
take a closer look at it. Here is a simple program that makes a few
function calls:

```
function greet(who) {
console.log("Hello " + who);
}
greet("Harry");
console.log("Bye");
```
A run through this program goes roughly like this: the call togreet
causes control to jump to the start of that function (line 2). The
function callsconsole.log, which takes control, does its job, and then
returns control to line 2. There, it reaches the end of thegreetfunction,
so it returns to the place that called it—line 4. The line after that calls
console.logagain. After that returns, the program reaches its end.


```
We could show the flow of control schematically like this:
not in function
in greet
in console.log
in greet
not in function
in console.log
not in function
```
Because a function has to jump back to the place that called it when it
returns, the computer must remember the context from which the call
happened. In one case,console.loghas to return to thegreetfunction
when it is done. In the other case, it returns to the end of the program.
The place where the computer stores this context is the _call stack_.
Every time a function is called, the current context is stored on top of
this stack. When a function returns, it removes the top context from
the stack and uses that context to continue execution.
Storing this stack requires space in the computer’s memory. When
the stack grows too big, the computer will fail with a message like “out
of stack space” or “too much recursion”. The following code illustrates
this by asking the computer a really hard question that causes an infinite
back-and-forth between two functions. Or rather, it _would_ be infinite,
if the computer had an infinite stack. As it is, we will run out of space,
or “blow the stack”.

```
function chicken() {
return egg();
}
```

```
function egg() {
return chicken();
}
console.log(chicken() + " came first.");
// → ??
```
### Optional Arguments.

The following code is allowed and executes without any problem:

```
function square(x) { return x * x; }
console.log(square(4, true, "hedgehog"));
// → 16
```
We definedsquarewith only one parameter. Yet when we call it with
three, the language doesn’t complain. It ignores the extra arguments
and computes the square of the first one.
JavaScript is extremely broad-minded about the number of argu-
ments you can pass to a function. If you pass too many, the extra ones
are ignored. If you pass too few, the missing parameters are assigned
the valueundefined.
The downside of this is that it is possible—likely, even—that you’ll
accidentally pass the wrong number of arguments to functions. And no
one will tell you about it. The upside is that you can use this behavior
to allow a function to be called with different numbers of arguments.
For example, thisminusfunction tries to imitate the-operator by acting
on either one or two arguments:


```
function minus(a, b) {
if (b === undefined) return -a;
else return a - b;
}
```
```
console.log(minus(10));
// → -10
console.log(minus(10, 5));
// → 5
```
If you write an=operator after a parameter, followed by an expression,
the value of that expression will replace the argument when it is not
given. For example, this version ofroundTomakes its second argument
optional. If you don’t provide it or pass the value undefined, it will
default to one:

```
function roundTo(n, step = 1) {
let remainder = n % step;
return n - remainder + (remainder < step / 2? 0 : step);
};
```
```
console.log(roundTo(4.5));
// → 5
console.log(roundTo(4.5, 2));
// → 4
```
Thenext chapterwill introduce a way in which a function body can get
at the whole list of arguments it was passed. This is helpful because
it allows a function to accept any number of arguments. For example,
console.logdoes this, outputting all the values it is given:


```
console.log("C", "O", 2);
// → C O 2
```
### Closure

The ability to treat functions as values, combined with the fact that
local bindings are re-created every time a function is called, brings
up an interesting question: What happens to local bindings when the
function call that created them is no longer active?
The following code shows an example of this. It defines a function,
wrapValue, that creates a local binding. It then returns a function that
accesses and returns this local binding.

```
function wrapValue(n) {
let local = n;
return () => local;
}
```
```
let wrap1 = wrapValue(1);
let wrap2 = wrapValue(2);
console.log(wrap1());
// → 1
console.log(wrap2());
// → 2
```
This is allowed and works as you’d hope—both instances of the binding
can still be accessed. This situation is a good demonstration of the fact
that local bindings are created anew for every call, and different calls


don’t affect each other’s local bindings.
This feature—being able to reference a specific instance of a local
binding in an enclosing scope—is called _closure_. A function that ref-
erences bindings from local scopes around it is called _a_ closure. This
behavior not only frees you from having to worry about the lifetimes
of bindings but also makes it possible to use function values in some
creative ways.
With a slight change, we can turn the previous example into a way
to create functions that multiply by an arbitrary amount.

```
function multiplier(factor) {
return number => number * factor;
}
```
```
let twice = multiplier(2);
console.log(twice(5));
// → 10
```
The explicitlocalbinding from thewrapValueexample isn’t really needed
since a parameter is itself a local binding.
Thinking about programs like this takes some practice. A good men-
tal model is to think of function values as containing both the code
in their body and the environment in which they are created. When
called, the function body sees the environment in which it was created,
not the environment in which it is called.
In the previous example,multiplieris called and creates an environ-
ment in which itsfactorparameter is bound to 2. The function value it
returns, which is stored intwice, remembers this environment so that


when that is called, it multiplies its argument by 2.

### Recursion.

It is perfectly okay for a function to call itself, as long as it doesn’t do it
so often that it overflows the stack. A function that calls itself is called
_recursive_. Recursion allows some functions to be written in a different
style. Take, for example, thispowerfunction, which does the same as
the**(exponentiation) operator:

```
function power(base, exponent) {
if (exponent == 0) {
return 1;
} else {
return base * power(base, exponent - 1);
}
}
```
```
console.log(power(2, 3));
// → 8
```
This is rather close to the way mathematicians define exponentiation
and arguably describes the concept more clearly than the loop we used
inChapter 2. The function calls itself multiple times with ever smaller
exponents to achieve the repeated multiplication.
However, this implementation has one problem: in typical JavaScript
implementations, it’s about three times slower than a version using a
for loop. Running through a simple loop is generally cheaper than


calling a function multiple times.
The dilemma of speed versus elegance is an interesting one. You can
see it as a kind of continuum between human-friendliness and machine-
friendliness. Almost any program can be made faster by making it
bigger and more convoluted. The programmer has to find an appropri-
ate balance.
In the case of thepowerfunction, an inelegant (looping) version is still
fairly simple and easy to read. It doesn’t make much sense to replace
it with a recursive function. Often, though, a program deals with such
complex concepts that giving up some eﬀiciency in order to make the
program more straightforward is helpful.
Worrying about eﬀiciency can be a distraction. It’s yet another fac-
tor that complicates program design, and when you’re doing something
that’s already diﬀicult, that extra thing to worry about can be para-
lyzing.
Therefore, you should generally start by writing something that’s
correct and easy to understand. If you’re worried that it’s too slow—
which it usually isn’t since most code simply isn’t executed often enough
to take any significant amount of time—you can measure afterward and
improve it if necessary.
Recursion is not always just an ineﬀicient alternative to looping.
Some problems really are easier to solve with recursion than with loops.
Most often these are problems that require exploring or processing sev-
eral “branches”, each of which might branch out again into even more
branches.
Consider this puzzle: by starting from the number 1 and repeatedly


either adding 5 or multiplying by 3, an infinite set of numbers can be
produced. How would you write a function that, given a number, tries
to find a sequence of such additions and multiplications that produces
that number? For example, the number 13 could be reached by first
multiplying by 3 and then adding 5 twice, whereas the number 15 can-
not be reached at all.
Here is a recursive solution:
function findSolution(target) {
function find(current, history) {
if (current == target) {
return history;
} else if (current > target) {
return null;
} else {
return find(current + 5, `(${history} + 5)`) ??
find(current * 3, `(${history} * 3)`);
}
}
return find(1, "1");
}

```
console.log(findSolution(24));
// → (((1 * 3) + 5) * 3)
```
Note that this program doesn’t necessarily find the _shortest_ sequence
of operations. It is satisfied when it finds any sequence at all.
It’s okay if you don’t see how this code works right away. Let’s work
through it since it makes for a great exercise in recursive thinking.


The inner functionfinddoes the actual recursing. It takes two argu-
ments: the current number and a string that records how we reached
this number. If it finds a solution, it returns a string that shows how to
get to the target. If it can find no solution starting from this number,
it returnsnull.
To do this, the function performs one of three actions. If the current
number is the target number, the current history is a way to reach that
target, so it is returned. If the current number is greater than the target,
there’s no sense in further exploring this branch because both adding
and multiplying will only make the number bigger, so it returnsnull.
Finally, if we’re still below the target number, the function tries both
possible paths that start from the current number by calling itself twice,
once for addition and once for multiplication. If the first call returns
something that is notnull, it is returned. Otherwise, the second call is
returned, regardless of whether it produces a string ornull.
To better understand how this function produces the effect we’re look-
ing for, let’s look at all the calls tofindthat are made when searching
for a solution for the number 13:

```
find(1, "1")
find(6, "(1 + 5)")
find(11, "((1 + 5) + 5)")
find(16, "(((1 + 5) + 5) + 5)")
too big
find(33, "(((1 + 5) + 5) * 3)")
too big
find(18, "((1 + 5) * 3)")
too big
```

```
find(3, "(1 * 3)")
find(8, "((1 * 3) + 5)")
find(13, "(((1 * 3) + 5) + 5)")
found!
```
The indentation indicates the depth of the call stack. The first time
findis called, the function starts by calling itself to explore the solution
that starts with(1 + 5). That call will further recurse to explore _every_
continued solution that yields a number less than or equal to the target
number. Since it doesn’t find one that hits the target, it returnsnull
back to the first call. There the??operator causes the call that explores
(1 * 3)to happen. This search has more luck—its first recursive call,
through yet _another_ recursive call, hits upon the target number. That
innermost call returns a string, and each of the ??operators in the
intermediate calls passes that string along, ultimately returning the
solution.

### Growing functions.

There are two more or less natural ways for functions to be introduced
into programs.
The first occurs when you find yourself writing similar code multiple
times. You’d prefer not to do that, as having more code means more
space for mistakes to hide and more material to read for people trying
to understand the program. So you take the repeated functionality, find
a good name for it, and put it into a function.
The second way is that you find you need some functionality that you


haven’t written yet and that sounds like it deserves its own function.
You start by naming the function, and then write its body. You might
even start writing code that uses the function before you actually define
the function itself.
How diﬀicult it is to find a good name for a function is a good indi-
cation of how clear a concept it is that you’re trying to wrap. Let’s go
through an example.
We want to write a program that prints two numbers: the numbers
of cows and chickens on a farm, with the wordsCowsandChickensafter
them and zeros padded before both numbers so that they are always
three digits long:

```
007 Cows
011 Chickens
```
This asks for a function of two arguments—the number of cows and the
number of chickens. Let’s get coding.

```
function printFarmInventory(cows, chickens) {
let cowString = String(cows);
while (cowString.length < 3) {
cowString = "0" + cowString;
}
console.log(`${cowString} Cows`);
let chickenString = String(chickens);
while (chickenString.length < 3) {
chickenString = "0" + chickenString;
}
console.log(`${chickenString} Chickens`);
```

```
}
printFarmInventory(7, 11);
```
Writing.lengthafter a string expression will give us the length of that
string. Thus, thewhileloops keep adding zeros in front of the number
strings until they are at least three characters long.
Mission accomplished! But just as we are about to send the farmer
the code (along with a hefty invoice), she calls and tells us she’s also
started keeping pigs, and couldn’t we please extend the software to also
print pigs?
We sure can. But just as we’re in the process of copying and pasting
those four lines one more time, we stop and reconsider. There has to
be a better way. Here’s a first attempt:

```
function printZeroPaddedWithLabel(number, label) {
let numberString = String(number);
while (numberString.length < 3) {
numberString = "0" + numberString;
}
console.log(`${numberString} ${label}`);
}
```
```
function printFarmInventory(cows, chickens, pigs) {
printZeroPaddedWithLabel(cows, "Cows");
printZeroPaddedWithLabel(chickens, "Chickens");
printZeroPaddedWithLabel(pigs, "Pigs");
}
```
```
printFarmInventory(7, 11, 3);
```

It works! But that name,printZeroPaddedWithLabel, is a little awkward.
It conflates three things—printing, zero-padding, and adding a label—
into a single function.
Instead of lifting out the repeated part of our program wholesale,
let’s try to pick out a single _concept_ :

```
function zeroPad(number, width) {
let string = String(number);
while (string.length < width) {
string = "0" + string;
}
return string;
}
```
```
function printFarmInventory(cows, chickens, pigs) {
console.log(`${zeroPad(cows, 3)} Cows`);
console.log(`${zeroPad(chickens, 3)} Chickens`);
console.log(`${zeroPad(pigs, 3)} Pigs`);
}
```
```
printFarmInventory(7, 16, 3);
```
A function with a nice, obvious name likezeroPadmakes it easier for
someone who reads the code to figure out what it does. Such a function
is also useful in more situations than just this specific program. For
example, you could use it to help print nicely aligned tables of numbers.
How smart and versatile _should_ our function be? We could write any-
thing, from a terribly simple function that can only pad a number to be
three characters wide to a complicated generalized number-formatting


system that handles fractional numbers, negative numbers, alignment
of decimal dots, padding with different characters, and so on.
A useful principle is to refrain from adding cleverness unless you are
absolutely sure you’re going to need it. It can be tempting to write
general “frameworks” for every bit of functionality you come across.
Resist that urge. You won’t get any real work done—you’ll be too busy
writing code that you never use.

### Functions and side effects

Functions can be roughly divided into those that are called for their
side effects and those that are called for their return value (though it
is also possible to both have side effects and return a value).
The first helper function in the farm example,printZeroPaddedWithLabel
, is called for its side effect: it prints a line. The second version,zeroPad,
is called for its return value. It is no coincidence that the second is use-
ful in more situations than the first. Functions that create values are
easier to combine in new ways than functions that directly perform side
effects.
A _pure_ function is a specific kind of value-producing function that
not only has no side effects but also doesn’t rely on side effects from
other code—for example, it doesn’t read global bindings whose value
might change. A pure function has the pleasant property that, when
called with the same arguments, it always produces the same value (and
doesn’t do anything else). A call to such a function can be substituted
by its return value without changing the meaning of the code. When


you are not sure that a pure function is working correctly, you can
test it by simply calling it and know that if it works in that context,
it will work in any context. Nonpure functions tend to require more
scaffolding to test.
Still, there’s no need to feel bad when writing functions that are not
pure. Side effects are often useful. There’s no way to write a pure
version ofconsole.log, for example, andconsole.logis good to have.
Some operations are also easier to express in an eﬀicient way when we
use side effects.

### Summary

This chapter taught you how to write your own functions. Thefunction
keyword, when used as an expression, can create a function value. When
used as a statement, it can be used to declare a binding and give it a
function as its value. Arrow functions are yet another way to create
functions.

```
// Define f to hold a function value
const f = function(a) {
console.log(a + 2);
};
```
```
// Declare g to be a function
function g(a, b) {
return a * b * 3.5;
}
```

```
// A less verbose function value
let h = a => a % 3;
```
A key part of understanding functions is understanding scopes. Each
block creates a new scope. Parameters and bindings declared in a given
scope are local and not visible from the outside. Bindings declared with
varbehave differently—they end up in the nearest function scope or the
global scope.
Separating the tasks your program performs into different functions
is helpful. You won’t have to repeat yourself as much, and functions can
help organize a program by grouping code into pieces that do specific
things.

### Exercises

**Minimum**

Theprevious chapterintroduced the standard functionMath.minthat re-
turns its smallest argument. We can write a function like that ourselves
now. Define the functionminthat takes two arguments and returns their
minimum.

**Recursion**

We’ve seen that we can use%(the remainder operator) to test whether
a number is even or odd by using% 2 to see whether it’s divisible by
two. Here’s another way to define whether a positive whole number is
even or odd:


- Zero is even.
- One is odd.
- For any other number _N_ , its evenness is the same as _N_ - 2.

Define a recursive functionisEvencorresponding to this description.
The function should accept a single parameter (a positive, whole num-
ber) and return a Boolean.
Test it on 50 and 75. See how it behaves on -1. Why? Can you think
of a way to fix this?

**Beancounting**

You can get the _N_ th character, or letter, from a string by writing[N]
after the string (for example,string[2]). The resulting value will be a
string containing only one character (for example,"b"). The first char-
acter has position 0, which causes the last one to be found at position
string.length - 1. In other words, a two-character string has length 2,
and its characters have positions 0 and 1.
Write a function called countBsthat takes a string as its only ar-
gument and returns a number that indicates how many uppercase B
characters there are in the string.
Next, write a function called countChar that behaves like countBs,
except it takes a second argument that indicates the character that
is to be counted (rather than counting only uppercase B characters).
RewritecountBsto make use of this new function.


```
“On two occasions I have been asked, ‘Pray, Mr. Babbage, if
you put into the machine wrong figures, will the right answers
come out?’ [...] I am not able rightly to apprehend the kind of
confusion of ideas that could provoke such a question.”
—Charles Babbage, Passages from the Life of a Philosopher
(1864)
```
**Chapter4**

## DataStructures: ObjectsandArrays

Numbers, Booleans, and strings are the atoms from which data struc-
tures are built. Many types of information require more than one atom,
though. _Objects_ allow us to group values—including other objects—to
build more complex structures.
The programs we have built so far have been limited by the fact that
they were operating only on simple data types. After learning the basics
of data structures in this chapter, you’ll know enough to start writing
useful programs.
The chapter will work through a more or less realistic programming
example, introducing concepts as they apply to the problem at hand.
The example code will often build on functions and bindings introduced
earlier in the book.
The online coding sandbox for the book ( _https://eloquentjavascript.net/
code_ ) provides a way to run code in the context of a particular chapter.
If you decide to work through the examples in another environment, be
sure to first download the full code for this chapter from the sandbox
page.


### The weresquirrel.

Every now and then, usually between 8 p.m. and 10 p.m., Jacques finds
himself transforming into a small furry rodent with a bushy tail.
On one hand, Jacques is quite glad that he doesn’t have classic lycan-
thropy. Turning into a squirrel does cause fewer problems than turning
into a wolf. Instead of having to worry about accidentally eating the
neighbor ( _that_ would be awkward), he worries about being eaten by the
neighbor’s cat. After two occasions of waking up on a precariously thin
branch in the crown of an oak, naked and disoriented, he has taken to
locking the doors and windows of his room at night and putting a few
walnuts on the floor to keep himself busy.
But Jacques would prefer to get rid of his condition entirely. The
irregular occurrences of the transformation make him suspect that they
might be triggered by something. For a while, he believed that it hap-
pened only on days when he had been near oak trees. However, avoiding
oak trees did not solve the problem.
Switching to a more scientific approach, Jacques has started keeping a
daily log of everything he does on a given day and whether he changed
form. With this data he hopes to narrow down the conditions that
trigger the transformations.
The first thing he needs is a data structure to store this information.


### Datasets

To work with a chunk of digital data, we first have to find a way to
represent it in our machine’s memory. Say, for example, that we want
to represent a collection of the numbers 2, 3, 5, 7, and 11.
We could get creative with strings—after all, strings can have any
length, so we can put a lot of data into them—and use"2 3 5 7 11"
as our representation. But this is awkward. We’d have to somehow
extract the digits and convert them back to numbers to access them.
Fortunately, JavaScript provides a data type specifically for storing
sequences of values. It is called an _array_ and is written as a list of
values between square brackets, separated by commas.

```
let listOfNumbers = [2, 3, 5, 7, 11];
console.log(listOfNumbers[2]);
// → 5
console.log(listOfNumbers[0]);
// → 2
console.log(listOfNumbers[2 - 1]);
// → 3
```
The notation for getting at the elements inside an array also uses square
brackets. A pair of square brackets immediately after an expression,
with another expression inside of them, will look up the element in
the left-hand expression that corresponds to the _index_ given by the
expression in the brackets.
The first index of an array is zero, not one, so the first element is
retrieved withlistOfNumbers[0]. Zero-based counting has a long tradi-


tion in technology and in certain ways makes a lot of sense, but it takes
some getting used to. Think of the index as the number of items to
skip, counting from the start of the array.

### Properties

We’ve seen a few expressions likemyString.length (to get the length
of a string) and Math.max(the maximum function) in past chapters.
These expressions access a _property_ of some value. In the first case, we
access thelengthproperty of the value inmyString. In the second, we
access the property namedmaxin theMathobject (which is a collection
of mathematics-related constants and functions).
Almost all JavaScript values have properties. The exceptions arenull
andundefined. If you try to access a property on one of these nonvalues,
you get an error:

```
null.length;
// → TypeError: null has no properties
```
The two main ways to access properties in JavaScript are with a dot and
with square brackets. Bothvalue.xandvalue[x]access a property on
value—but not necessarily the same property. The difference is in how
xis interpreted. When using a dot, the word after the dot is the literal
name of the property. When using square brackets, the expression
between the brackets is _evaluated_ to get the property name. Whereas
value.x fetches the property ofvalue named “x”, value[x]takes the
value of the variable namedxand uses that, converted to a string, as


the property name.
If you know that the property in which you are interested is called
_color_ , you sayvalue.color. If you want to extract the property named
by the value held in the bindingi, you sayvalue[i]. Property names
are strings. They can be any string, but the dot notation works only
with names that look like valid binding names—starting with a letter
or underscore, and containing only letters, numbers, and underscores.
If you want to access a property named _2_ or _John Doe_ , you must use
square brackets: value[2]orvalue["John Doe"].
The elements in an array are stored as the array’s properties, using
numbers as property names. Because you can’t use the dot notation
with numbers and usually want to use a binding that holds the index
anyway, you have to use the bracket notation to get at them.
Just like strings, arrays have alengthproperty that tells us how many
elements the array has.

### Methods

Both string and array values contain, in addition to thelengthproperty,
a number of properties that hold function values.

```
let doh = "Doh";
console.log(typeof doh.toUpperCase);
// → function
console.log(doh.toUpperCase());
// → DOH
```
Every string has atoUpperCaseproperty. When called, it will return a


copy of the string in which all letters have been converted to uppercase.
There is alsotoLowerCase, going the other way.
Interestingly, even though the call totoUpperCasedoes not pass any
arguments, the function somehow has access to the string"Doh", the
value whose property we called. You’ll find out how this works in
Chapter 6.
Properties that contain functions are generally called _methods_ of the
value they belong to, as in “toUpperCaseis a method of a string”.
This example demonstrates two methods you can use to manipulate
arrays.

```
let sequence = [1, 2, 3];
sequence.push(4);
sequence.push(5);
console.log(sequence);
// → [1, 2, 3, 4, 5]
console.log(sequence.pop());
// → 5
console.log(sequence);
// → [1, 2, 3, 4]
```
Thepushmethod adds values to the end of an array. Thepopmethod
does the opposite, removing the last value in the array and returning
it.
These somewhat silly names are the traditional terms for operations
on a _stack_. A stack, in programming, is a data structure that allows you
to push values into it and pop them out again in the opposite order so
that the thing that was added last is removed first. Stacks are common


in programming—you might remember the function call stack fromthe
previous chapter, which is an instance of the same idea.

### Objects

Back to the weresquirrel. A set of daily log entries can be represented
as an array, but the entries do not consist of just a number or a string—
each entry needs to store a list of activities and a Boolean value that
indicates whether Jacques turned into a squirrel or not. Ideally, we
would like to group these together into a single value and then put
those grouped values into an array of log entries.
Values of the type _object_ are arbitrary collections of properties. One
way to create an object is by using braces as an expression.

```
let day1 = {
squirrel: false,
events: ["work", "touched tree", "pizza", "running"]
};
console.log(day1.squirrel);
// → false
console.log(day1.wolf);
// → undefined
day1.wolf = false;
console.log(day1.wolf);
// → false
```
Inside the braces, you write a list of properties separated by commas.
Each property has a name followed by a colon and a value. When


an object is written over multiple lines, indenting it as shown in this
example helps with readability. Properties whose names aren’t valid
binding names or valid numbers must be quoted:

```
let descriptions = {
work: "Went to work",
"touched tree": "Touched a tree"
};
```
This means that braces have _two_ meanings in JavaScript. At the start
of a statement, they begin a block of statements. In any other posi-
tion, they describe an object. Fortunately, it is rarely useful to start
a statement with an object in braces, so the ambiguity between these
two is not much of a problem. The one case where this does come up is
when you want to return an object from a shorthand arrow function—
you can’t write n => {prop: n}since the braces will be interpreted as
a function body. Instead, you have to put a set of parentheses around
the object to make it clear that it is an expression.
Reading a property that doesn’t exist will give you the valueundefined
.
It is possible to assign a value to a property expression with the =
operator. This will replace the property’s value if it already existed or
create a new property on the object if it didn’t.
To briefly return to our tentacle model of bindings—property bind-
ings are similar. They _grasp_ values, but other bindings and properties
might be holding onto those same values. You can think of objects
as octopuses with any number of tentacles, each of which has a name
written on it.


Thedeleteoperator cuts off a tentacle from such an octopus. It is a
unary operator that, when applied to an object property, will remove
the named property from the object. This is not a common thing to
do, but it is possible.

```
let anObject = {left: 1, right: 2};
console.log(anObject.left);
// → 1
delete anObject.left;
console.log(anObject.left);
// → undefined
console.log("left" in anObject);
// → false
console.log("right" in anObject);
// → true
```
The binaryinoperator, when applied to a string and an object, tells
you whether that object has a property with that name. The difference
between setting a property toundefinedand actually deleting it is that
in the first case, the object still _has_ the property (it just doesn’t have a
very interesting value), whereas in the second case, the property is no
longer present andinwill returnfalse.
To find out what properties an object has, you can use theObject.
keysfunction. Give the function an object and it will return an array
of strings—the object’s property names:

```
console.log(Object.keys({x: 0, y: 0, z: 2}));
// → ["x", "y", "z"]
```
There’s an Object.assignfunction that copies all properties from one


object into another:

```
let objectA = {a: 1, b: 2};
Object.assign(objectA, {b: 3, c: 4});
console.log(objectA);
// → {a: 1, b: 3, c: 4}
```
Arrays, then, are just a kind of object specialized for storing sequences
of things. If you evaluate typeof [], it produces "object". You can
visualize arrays as long, flat octopuses with all their tentacles in a neat
row, labeled with numbers.
Jacques will represent the journal that Jacques keeps as an array of
objects:

```
let journal = [
{events: ["work", "touched tree", "pizza",
"running", "television"],
squirrel: false},
{events: ["work", "ice cream", "cauliflower",
"lasagna", "touched tree", "brushed teeth"],
squirrel: false},
{events: ["weekend", "cycling", "break", "peanuts",
"beer"],
squirrel: true},
/* And so on... */
];
```

### Mutability

We will get to actual programming soon, but first, there’s one more
piece of theory to understand.
We saw that object values can be modified. The types of values
discussed in earlier chapters, such as numbers, strings, and Booleans,
are all _immutable_ —it is impossible to change values of those types. You
can combine them and derive new values from them, but when you take
a specific string value, that value will always remain the same. The text
inside it cannot be changed. If you have a string that contains"cat",
it is not possible for other code to change a character in your string to
make it spell"rat".
Objects work differently. You _can_ change their properties, causing a
single object value to have different content at different times.
When we have two numbers, 120 and 120, we can consider them pre-
cisely the same number, whether or not they refer to the same physical
bits. With objects, there is a difference between having two references
to the same object and having two different objects that contain the
same properties. Consider the following code:

```
let object1 = {value: 10};
let object2 = object1;
let object3 = {value: 10};
```
```
console.log(object1 == object2);
// → true
console.log(object1 == object3);
// → false
```

```
object1.value = 15;
console.log(object2.value);
// → 15
console.log(object3.value);
// → 10
```
Theobject1andobject2bindings grasp the _same_ object, which is why
changingobject1also changes the value ofobject2. They are said to
have the same _identity_. The bindingobject3points to a different ob-
ject, which initially contains the same properties asobject1but lives a
separate life.
Bindings can also be changeable or constant, but this is separate
from the way their values behave. Even though number values don’t
change, you can use aletbinding to keep track of a changing number
by changing the value at which the binding points. Similarly, though a
constbinding to an object can itself not be changed and will continue
to point at the same object, the _contents_ of that object might change.

```
const score = {visitors: 0, home: 0};
// This is okay
score.visitors = 1;
// This isn't allowed
score = {visitors: 1, home: 1};
```
When you compare objects with JavaScript’s==operator, it compares
by identity: it will producetrueonly if both objects are precisely the
same value. Comparing different objects will returnfalse, even if they
have identical properties. There is no “deep” comparison operation


built into JavaScript that compares objects by contents, but it is possi-
ble to write it yourself (which is one of theexercisesat the end of this
chapter).

### Thelycanthrope'slog

Jacques starts up his JavaScript interpreter and sets up the environment
he needs to keep his journal:

```
let journal = [];
```
```
function addEntry(events, squirrel) {
journal.push({events, squirrel});
}
```
Note that the object added to the journal looks a little odd. Instead of
declaring properties likeevents: events, it just gives a property name:
events. This is shorthand that means the same thing—if a property
name in brace notation isn’t followed by a value, its value is taken from
the binding with the same name.
Every evening at 10 p.m.—or sometimes the next morning, after
climbing down from the top shelf of his bookcase—Jacques records the
day:

```
addEntry(["work", "touched tree", "pizza", "running",
"television"], false);
addEntry(["work", "ice cream", "cauliflower", "lasagna",
"touched tree", "brushed teeth"], false);
addEntry(["weekend", "cycling", "break", "peanuts",
```

```
"beer"], true);
```
Once he has enough data points, he intends to use statistics to find out
which of these events may be related to the squirrelifications.
_Correlation_ is a measure of dependence between statistical variables.
A statistical variable is not quite the same as a programming variable.
In statistics you typically have a set of _measurements_ , and each variable
is measured for every measurement. Correlation between variables is
usually expressed as a value that ranges from -1 to 1. Zero correlation
means the variables are not related. A correlation of 1 indicates that
the two are perfectly related—if you know one, you also know the other.
Negative 1 also means that the variables are perfectly related but are
opposites—when one is true, the other is false.
To compute the measure of correlation between two Boolean vari-
ables, we can use the _phi coeﬀicient_ (φ). This is a formula whose input
is a frequency table containing the number of times the different com-
binations of the variables were observed. The output of the formula is
a number between -1 and 1 that describes the correlation.
We could take the event of eating pizza and put that in a frequency
table like this, where each number indicates the number of times that
combination occurred in our measurements.


```
No squirrel, no pizza^76
```
```
Squirrel, no pizza^4
```
```
No squirrel, pizza^9
```
```
Squirrel, pizza^1
```
```
If we call that table n , we can computeφusing the following formula:
```
```
φ=
n 11 n 00 −n 10 n 01
√
n 1 • n 0 • n• 1 n• 0
```
#### (4.1)

(If at this point you’re putting the book down to focus on a terrible
flashback to 10th grade math class—hold on! I do not intend to torture
you with endless pages of cryptic notation—it’s just this one formula
for now. And even with this one, all we do is turn it into JavaScript.)
The notationn 01 indicates the number of measurements where the
first variable (squirrelness) is false (0) and the second variable (pizza)
is true (1). In the pizza table,n 01 is 9.
The valuen 1 • refers to the sum of all measurements where the first
variable is true, which is 5 in the example table. Likewise,n• 0 refers to
the sum of the measurements where the second variable is false.
So for the pizza table, the part above the division line (the dividend)
would be 1×76−4×9 = 40, and the part below it (the divisor) would
be the square root of 5×85×10×80, or

```
√
340 , 000. This comes out toφ
```

≈0.069, which is tiny. Eating pizza does not appear to have influence
on the transformations.

### Computing correlation

We can represent a two-by-two table in JavaScript with a four-element
array ([76, 9, 4, 1]). We could also use other representations, such
as an array containing two two-element arrays ([[76, 9], [4, 1]]) or
an object with property names like"11"and"01", but the flat array is
simple and makes the expressions that access the table pleasantly short.
We’ll interpret the indices to the array as two-bit binary numbers, where
the leftmost (most significant) digit refers to the squirrel variable and
the rightmost (least significant) digit refers to the event variable. For
example, the binary number 10 refers to the case where Jacques did
turn into a squirrel, but the event (say, “pizza”) didn’t occur. This
happened four times. And since binary 10 is 2 in decimal notation, we
will store this number at index 2 of the array.
This is the function that computes theφ coeﬀicient from such an
array:

```
function phi(table) {
return (table[3] * table[0] - table[2] * table[1]) /
Math.sqrt((table[2] + table[3]) *
(table[0] + table[1]) *
(table[1] + table[3]) *
(table[0] + table[2]));
}
```

```
console.log(phi([76, 9, 4, 1]));
// → 0.068599434
```
This is a direct translation of theφformula into JavaScript.Math.sqrt
is the square root function, as provided by theMathobject in a standard
JavaScript environment. We have to add two fields from the table to
get fields liken 1 • because the sums of rows or columns are not stored
directly in our data structure.
Jacques keeps his journal for three months. The resulting dataset is
available in thecoding sandboxfor this chapter ( _https://eloquentjavascript.net/
code#4_ ), where it is stored in theJOURNALbinding, and in a download-
ablefile.
To extract a two-by-two table for a specific event from the journal,
we must loop over all the entries and tally how many times the event
occurs in relation to squirrel transformations:

```
function tableFor(event, journal) {
let table = [0, 0, 0, 0];
for (let i = 0; i < journal.length; i++) {
let entry = journal[i], index = 0;
if (entry.events.includes(event)) index += 1;
if (entry.squirrel) index += 2;
table[index] += 1;
}
return table;
}
```
```
console.log(tableFor("pizza", JOURNAL));
// → [76, 9, 4, 1]
```

Arrays have an includes method that checks whether a given value
exists in the array. The function uses that to determine whether the
event name it is interested in is part of the event list for a given day.
The body of the loop intableForfigures out which box in the table
each journal entry falls into by checking whether the entry contains the
specific event it’s interested in and whether the event happens alongside
a squirrel incident. The loop then adds one to the correct box in the
table.
We now have the tools we need to compute individual correlations.
The only step remaining is to find a correlation for every type of event
that was recorded and see whether anything stands out.

### Array loops.

In thetableForfunction, there’s a loop like this:

```
for (let i = 0; i < JOURNAL.length; i++) {
let entry = JOURNAL[i];
// Do something with entry
}
```
This kind of loop is common in classical JavaScript—going over arrays
one element at a time is something that comes up a lot, and to do
that you’d run a counter over the length of the array and pick out each
element in turn.
There is a simpler way to write such loops in modern JavaScript:
for (let entry of JOURNAL) {


```
console.log(`${entry.events.length} events.`);
}
```
When afor loop uses the wordofafter its variable definition, it will
loop over the elements of the value given afterof. This works not only
for arrays but also for strings and some other data structures. We’ll
discuss _how_ it works inChapter 6.

### The final analysis

We need to compute a correlation for every type of event that occurs
in the dataset. To do that, we first need to _find_ every type of event.

```
function journalEvents(journal) {
let events = [];
for (let entry of journal) {
for (let event of entry.events) {
if (!events.includes(event)) {
events.push(event);
}
}
}
return events;
}
```
```
console.log(journalEvents(JOURNAL));
// → ["carrot", "exercise", "weekend", "bread", ...]
```
By adding any event names that aren’t already in it to theeventsarray,


the function collects every type of event.
Using that function, we can see all the correlations:
for (let event of journalEvents(JOURNAL)) {
console.log(event + ":", phi(tableFor(event, JOURNAL)));
}
// → carrot: 0.0140970969
// → exercise: 0.0685994341
// → weekend: 0.1371988681
// → bread: -0.0757554019
// → pudding: -0.0648203724
// And so on...

Most correlations seem to lie close to zero. Eating carrots, bread, or
pudding apparently does not trigger squirrel-lycanthropy. The trans-
formations _do_ seem to occur somewhat more often on weekends. Let’s
filter the results to show only correlations greater than 0.1 or less than
-0.1:

```
for (let event of journalEvents(JOURNAL)) {
let correlation = phi(tableFor(event, JOURNAL));
if (correlation > 0.1 || correlation < -0.1) {
console.log(event + ":", correlation);
}
}
// → weekend: 0.1371988681
// → brushed teeth: -0.3805211953
// → candy: 0.1296407447
// → work: -0.1371988681
// → spaghetti: 0.2425356250
```

```
// → reading: 0.1106828054
// → peanuts: 0.5902679812
```
Aha! There are two factors with a correlation clearly stronger than
the others. Eating peanuts has a strong positive effect on the chance of
turning into a squirrel, whereas brushing teeth has a significant negative
effect.
Interesting. Let’s try something.
for (let entry of JOURNAL) {
if (entry.events.includes("peanuts") &&
!entry.events.includes("brushed teeth")) {
entry.events.push("peanut teeth");
}
}
console.log(phi(tableFor("peanut teeth", JOURNAL)));
// → 1

That’s a strong result. The phenomenon occurs precisely when Jacques
eats peanuts and fails to brush his teeth. If only he weren’t such a slob
about dental hygiene, he’d never even have noticed his affliction.
Knowing this, Jacques stops eating peanuts altogether and finds that
his transformations stop.
But it takes only a few months for him to notice that something
is missing from this entirely human way of living. Without his feral
adventures, Jacques hardly feels alive at all. He decides he’d rather be
a full-time wild animal. After building a beautiful little tree house in
the forest and equipping it with a peanut butter dispenser and a ten-
year supply of peanut butter, he changes form one last time, and lives


the short and energetic life of a squirrel.

### Further arrayology.

Before finishing the chapter, I want to introduce you to a few more
object-related concepts. I’ll start with some generally useful array meth-
ods.
We sawpushandpop, which add and remove elements at the end of
an array,earlierin this chapter. The corresponding methods for adding
and removing things at the start of an array are calledunshift and
shift.

```
let todoList = [];
function remember(task) {
todoList.push(task);
}
function getTask() {
return todoList.shift();
}
function rememberUrgently(task) {
todoList.unshift(task);
}
```
This program manages a queue of tasks. You add tasks to the end of
the queue by callingremember("groceries"), and when you’re ready to
do something, you callgetTask() to get (and remove) the front item
from the queue. The rememberUrgentlyfunction also adds a task but
adds it to the front instead of the back of the queue.


To search for a specific value, arrays provide an indexOf method.
The method searches through the array from the start to the end and
returns the index at which the requested value was found—or -1 if it
wasn’t found. To search from the end instead of the start, there’s a
similar method calledlastIndexOf:

```
console.log([1, 2, 3, 2, 1].indexOf(2));
// → 1
console.log([1, 2, 3, 2, 1].lastIndexOf(2));
// → 3
```
BothindexOfandlastIndexOftake an optional second argument that
indicates where to start searching.
Another fundamental array method isslice, which takes start and
end indices and returns an array that has only the elements between
them. The start index is inclusive and the end index is exclusive.

```
console.log([0, 1, 2, 3, 4].slice(2, 4));
// → [2, 3]
console.log([0, 1, 2, 3, 4].slice(2));
// → [2, 3, 4]
```
When the end index is not given, slicewill take all of the elements
after the start index. You can also omit the start index to copy the
entire array.
Theconcatmethod can be used to append arrays together to create
a new array, similar to what the+operator does for strings.
The following example shows both concat and slice in action. It
takes an array and an index and returns a new array that is a copy of


the original array with the element at the given index removed:

```
function remove(array, index) {
return array.slice(0, index)
.concat(array.slice(index + 1));
}
console.log(remove(["a", "b", "c", "d", "e"], 2));
// → ["a", "b", "d", "e"]
```
If you passconcatan argument that is not an array, that value will be
added to the new array as if it were a one-element array.

### Strings and their properties

We can read properties likelengthandtoUpperCasefrom string values.
But if we try to add a new property, it doesn’t stick.

```
let kim = "Kim";
kim.age = 88;
console.log(kim.age);
// → undefined
```
Values of type string, number, and Boolean are not objects, and though
the language doesn’t complain if you try to set new properties on them,
it doesn’t actually store those properties. As mentioned earlier, such
values are immutable and cannot be changed.
But these types do have built-in properties. Every string value has
a number of methods. Some very useful ones are sliceand indexOf,
which resemble the array methods of the same name:


```
console.log("coconuts".slice(4, 7));
// → nut
console.log("coconut".indexOf("u"));
// → 5
```
One difference is that a string’sindexOfcan search for a string contain-
ing more than one character, whereas the corresponding array method
looks only for a single element:

```
console.log("one two three".indexOf("ee"));
// → 11
```
Thetrimmethod removes whitespace (spaces, newlines, tabs, and sim-
ilar characters) from the start and end of a string:

```
console.log(" okay \n ".trim());
// → okay
```
ThezeroPadfunction from theprevious chapteralso exists as a method.
It is calledpadStartand takes the desired length and padding character
as arguments:

```
console.log(String(6).padStart(3, "0"));
// → 006
```
You can split a string on every occurrence of another string withsplit
and join it again withjoin:

```
let sentence = "Secretarybirds specialize in stomping";
let words = sentence.split(" ");
console.log(words);
```

```
// → ["Secretarybirds", "specialize", "in", "stomping"]
console.log(words.join(". "));
// → Secretarybirds. specialize. in. stomping
```
A string can be repeated with therepeatmethod, which creates a new
string containing multiple copies of the original string, glued together:

```
console.log("LA".repeat(3));
// → LALALA
```
We have already seen the string type’slengthproperty. Accessing the
individual characters in a string looks like accessing array elements
(with a complication that we’ll discuss inChapter 5).

```
let string = "abc";
console.log(string.length);
// → 3
console.log(string[1]);
// → b
```
### Rest parameters

It can be useful for a function to accept any number of arguments.
For example, Math.maxcomputes the maximum of _all_ the arguments
it is given. To write such a function, you put three dots before the
function’s last parameter, like this:

```
function max(...numbers) {
let result = -Infinity;
```

```
for (let number of numbers) {
if (number > result) result = number;
}
return result;
}
console.log(max(4, 1, 9, -2));
// → 9
```
When such a function is called, the _rest parameter_ is bound to an array
containing all further arguments. If there are other parameters before
it, their values aren’t part of that array. When, as inmax, it is the only
parameter, it will hold all arguments.
You can use a similar three-dot notation to _call_ a function with an
array of arguments.

```
let numbers = [5, 1, 7];
console.log(max(...numbers));
// → 7
```
This “spreads” out the array into the function call, passing its elements
as separate arguments. It is possible to include an array like that along
with other arguments, as inmax(9, ...numbers, 2).
Square bracket array notation similarly allows the triple-dot operator
to spread another array into the new array:

```
let words = ["never", "fully"];
console.log(["will", ...words, "understand"]);
// → ["will", "never", "fully", "understand"]
```
This works even in curly brace objects, where it adds all properties from


another object. If a property is added multiple times, the last value to
be added wins:

```
let coordinates = {x: 10, y: 0};
console.log({...coordinates, y: 5, z: 1});
// → {x: 10, y: 5, z: 1}
```
### The Math object.

As we’ve seen,Mathis a grab bag of number-related utility functions such
as Math.max(maximum), Math.min(minimum), and Math.sqrt (square
root).
TheMathobject is used as a container to group a bunch of related
functionality. There is only oneMathobject, and it is almost never useful
as a value. Rather, it provides a _namespace_ so that all these functions
and values do not have to be global bindings.
Having too many global bindings “pollutes” the namespace. The
more names have been taken, the more likely you are to accidentally
overwrite the value of some existing binding. For example, it’s not
unlikely you’ll want to name something maxin one of your programs.
Since JavaScript’s built-inmaxfunction is tucked safely inside theMath
object, you don’t have to worry about overwriting it.
Many languages will stop you, or at least warn you, when you are
defining a binding with a name that is already taken. JavaScript does
this for bindings you declared withletorconstbut—perversely—not
for standard bindings nor for bindings declared withvarorfunction.


Back to theMathobject. If you need to do trigonometry, Mathcan
help. It containscos(cosine),sin(sine), andtan(tangent), as well as
their inverse functions,acos,asin, andatan, respectively. The number
π(pi)—or at least the closest approximation that fits in a JavaScript
number—is available asMath.PI. There is an old programming tradition
of writing the names of constant values in all caps.

```
function randomPointOnCircle(radius) {
let angle = Math.random() * 2 * Math.PI;
return {x: radius * Math.cos(angle),
y: radius * Math.sin(angle)};
}
console.log(randomPointOnCircle(2));
// → {x: 0.3667, y: 1.966}
```
If you’re not familiar with sines and cosines, don’t worry. I’ll explain
them when they are used inChapter 14.
The previous example usedMath.random. This is a function that re-
turns a new pseudorandom number between 0 (inclusive) and 1 (exclu-
sive) every time you call it:

```
console.log(Math.random());
// → 0.36993729369714856
console.log(Math.random());
// → 0.727367032552138
console.log(Math.random());
// → 0.40180766698904335
```
Though computers are deterministic machines—they always react the
same way if given the same input—it is possible to have them produce


numbers that appear random. To do that, the machine keeps some hid-
den value, and whenever you ask for a new random number, it performs
complicated computations on this hidden value to create a new value.
It stores a new value and returns some number derived from it. That
way, it can produce ever new, hard-to-predict numbers in a way that
_seems_ random.
If we want a whole random number instead of a fractional one, we
can useMath.floor(which rounds down to the nearest whole number)
on the result ofMath.random:

```
console.log(Math.floor(Math.random() * 10));
// → 2
```
Multiplying the random number by 10 gives us a number greater than or
equal to 0 and below 10. SinceMath.floorrounds down, this expression
will produce, with equal chance, any number from 0 through 9.
There are also the functionsMath.ceil(for “ceiling”, which rounds up
to a whole number),Math.round(to the nearest whole number), andMath
.abs, which takes the absolute value of a number, meaning it negates
negative values but leaves positive ones as they are.

### Destructuring

Let’s return to thephifunction for a moment.

```
function phi(table) {
return (table[3] * table[0] - table[2] * table[1]) /
Math.sqrt((table[2] + table[3]) *
```

```
(table[0] + table[1]) *
(table[1] + table[3]) *
(table[0] + table[2]));
}
```
One reason this function is awkward to read is that we have a binding
pointing at our array, but we’d much prefer to have bindings for the _ele-
ments_ of the array—that is,let n00 = table[0]and so on. Fortunately,
there is a succinct way to do this in JavaScript:

```
function phi([n00, n01, n10, n11]) {
return (n11 * n00 - n10 * n01) /
Math.sqrt((n10 + n11) * (n00 + n01) *
(n01 + n11) * (n00 + n10));
}
```
This also works for bindings created with let,var, or const. If you
know that the value you are binding is an array, you can use square
brackets to “look inside” of the value, binding its contents.
A similar trick works for objects, using braces instead of square brack-
ets.

```
let {name} = {name: "Faraji", age: 23};
console.log(name);
// → Faraji
```
Note that if you try to destructurenullorundefined, you get an error,
much as you would if you directly try to access a property of those
values.


### Optional property access

When you aren’t sure whether a given value produces an object, but
still want to read a property from it when it does, you can use a variant
of the dot notation: object?.property.

```
function city(object) {
return object.address?.city;
}
console.log(city({address: {city: "Toronto"}}));
// → Toronto
console.log(city({name: "Vera"}));
// → undefined
```
The expressiona?.bmeans the same asa.bwhenaisn’t null or unde-
fined. When it is, it evaluates toundefined. This can be convenient
when, as in the example, you aren’t sure that a given property exists
or when a variable might hold an undefined value.
A similar notation can be used with square bracket access, and even
with function calls, by putting?.in front of the parentheses or brackets:

```
console.log("string".notAMethod?.());
// → undefined
console.log({}.arrayProp?.[0]);
// → undefined
```

### JSON

Because properties grasp their value rather than contain it, objects and
arrays are stored in the computer’s memory as sequences of bits holding
the _addresses_ —the place in memory—of their contents. An array with
another array inside of it consists of (at least) one memory region for the
inner array and another for the outer array, containing (among other
things) a number that represents the address of the inner array.
If you want to save data in a file for later or send it to another
computer over the network, you have to somehow convert these tangles
of memory addresses to a description that can be stored or sent. You
_could_ send over your entire computer memory along with the address
of the value you’re interested in, I suppose, but that doesn’t seem like
the best approach.
What we can do is _serialize_ the data. That means it is converted
into a flat description. A popular serialization format is called _JSON_
(pronounced “Jason”), which stands for JavaScript Object Notation. It
is widely used as a data storage and communication format on the web,
even with languages other than JavaScript.
JSON looks similar to JavaScript’s way of writing arrays and objects,
with a few restrictions. All property names have to be surrounded
by double quotes, and only simple data expressions are allowed—no
function calls, bindings, or anything that involves actual computation.
Comments are not allowed in JSON.
A journal entry might look like this when represented as JSON data:
{


```
"squirrel": false,
"events": ["work", "touched tree", "pizza", "running"]
}
```
JavaScript gives us the functionsJSON.stringifyandJSON.parseto con-
vert data to and from this format. The first takes a JavaScript value
and returns a JSON-encoded string. The second takes such a string
and converts it to the value it encodes:

```
let string = JSON.stringify({squirrel: false,
events: ["weekend"]});
console.log(string);
// → {"squirrel":false,"events":["weekend"]}
console.log(JSON.parse(string).events);
// → ["weekend"]
```
### Summary

Objects and arrays provide ways to group several values into a single
value. This allows us to put a bunch of related things in a bag and run
around with the bag instead of wrapping our arms around all of the
individual things and trying to hold on to them separately.
Most values in JavaScript have properties, with the exceptions being
nullandundefined. Properties are accessed usingvalue.proporvalue["
prop"]. Objects tend to use names for their properties and store more
or less a fixed set of them. Arrays, on the other hand, usually con-
tain varying amounts of conceptually identical values and use numbers
(starting from 0) as the names of their properties.


There _are_ some named properties in arrays, such as length and a
number of methods. Methods are functions that live in properties and
(usually) act on the value of which they are a property.
You can iterate over arrays using a special kind offorloop: for (let
element of array).

### Exercises

**Thesumofarange**

Theintroductionof this book alluded to the following as a nice way to
compute the sum of a range of numbers:

```
console.log(sum(range(1, 10)));
```
Write a rangefunction that takes two arguments,startand end, and
returns an array containing all the numbers fromstartup to and in-
cludingend.
Next, write asumfunction that takes an array of numbers and returns
the sum of these numbers. Run the example program and see whether
it does indeed return 55.
As a bonus assignment, modify yourrange function to take an op-
tional third argument that indicates the “step” value used when build-
ing the array. If no step is given, the elements should go up by in-
crements of one, corresponding to the old behavior. The function call
range(1, 10, 2) should return[1, 3, 5, 7, 9]. Make sure this also
works with negative step values so thatrange(5, 2, -1)produces[5,
4, 3, 2].


**Reversinganarray**

Arrays have areversemethod that changes the array by inverting the
order in which its elements appear. For this exercise, write two func-
tions, reverseArrayand reverseArrayInPlace. The first, reverseArray,
should take an array as its argument and produce a _new_ array that has
the same elements in the inverse order. The second,reverseArrayInPlace
, should do what thereversemethod does: _modify_ the array given as
its argument by reversing its elements. Neither may use the standard
reversemethod.
Thinking back to the notes about side effects and pure functions in
theprevious chapter, which variant do you expect to be useful in more
situations? Which one runs faster?

**Alist**

As generic blobs of values, objects can be used to build all sorts of data
structures. A common data structure is the _list_ (not to be confused
with arrays). A list is a nested set of objects, with the first object
holding a reference to the second, the second to the third, and so on:

```
let list = {
value: 1,
rest: {
value: 2,
rest: {
value: 3,
rest: null
}
```

```
}
};
```
The resulting objects form a chain, as shown in the following diagram:

```
value: 1
rest: value: 2rest: value: 3
rest: null
```
A nice thing about lists is that they can share parts of their struc-
ture. For example, if I create two new values{value: 0, rest: list}
and{value: -1, rest: list}(withlistreferring to the binding defined
earlier), they are both independent lists, but they share the structure
that makes up their last three elements. The original list is also still a
valid three-element list.
Write a functionarrayToListthat builds up a list structure like the
one shown when given[1, 2, 3]as argument. Also write alistToArray
function that produces an array from a list. Add the helper functions
prepend, which takes an element and a list and creates a new list that
adds the element to the front of the input list, andnth, which takes a
list and a number and returns the element at the given position in the
list (with zero referring to the first element) orundefinedwhen there is
no such element.
If you haven’t already, also write a recursive version ofnth.


**Deepcomparison**

The == operator compares objects by identity, but sometimes you’d
prefer to compare the values of their actual properties.
Write a functiondeepEqual that takes two values and returns true
only if they are the same value or are objects with the same properties,
where the values of the properties are equal when compared with a
recursive call todeepEqual.
To find out whether values should be compared directly (using the
===operator for that) or have their properties compared, you can use
thetypeofoperator. If it produces"object"for both values, you should
do a deep comparison. But you have to take one silly exception into
account: because of a historical accident, typeof null also produces
"object".
TheObject.keysfunction will be useful when you need to go over the
properties of objects to compare them.


```
“
There are two ways of constructing a software design: One
way is to make it so simple that there are obviously no
deficiencies, and the other way is to make it so complicated
that there are no obvious deficiencies.”
—C.A.R. Hoare, 1980 ACM Turing Award Lecture
```
**Chapter5**

## Higher-OrderFunctions

A large program is a costly program, and not just because of the time
it takes to build. Size almost always involves complexity, and complex-
ity confuses programmers. Confused programmers, in turn, introduce
mistakes ( _bugs_ ) into programs. A large program then provides a lot of
space for these bugs to hide, making them hard to find.
Let’s briefly go back to the final two example programs in the intro-
duction. The first is self contained and six lines long.

```
let total = 0, count = 1;
while (count <= 10) {
total += count;
count += 1;
}
console.log(total);
```
The second relies on two external functions and is one line long.

```
console.log(sum(range(1, 10)));
```
Which one is more likely to contain a bug?


If we count the size of the definitions of sumand range, the second
program is also big—even bigger than the first. But still, I’d argue that
it is more likely to be correct.
This is because the solution is expressed in a vocabulary that corre-
sponds to the problem being solved. Summing a range of numbers isn’t
about loops and counters. It is about ranges and sums.
The definitions of this vocabulary (the functionssumandrange) will
still involve loops, counters, and other incidental details. But because
they are expressing simpler concepts than the program as a whole, they
are easier to get right.

### Abstraction.

In the context of programming, these kinds of vocabularies are usually
called _abstractions_. Abstractions give us the ability to talk about prob-
lems at a higher (or more abstract) level, without getting sidetracked
by uninteresting details.
As an analogy, compare these two recipes for pea soup. The first goes
like this:

```
Put 1 cup of dried peas per person into a container. Add
water until the peas are well covered. Leave the peas in
water for at least 12 hours. Take the peas out of the water
and put them in a cooking pan. Add 4 cups of water per
person. Cover the pan and keep the peas simmering for two
hours. Take half an onion per person. Cut it into pieces
with a knife. Add it to the peas. Take a stalk of celery per
```

```
person. Cut it into pieces with a knife. Add it to the peas.
Take a carrot per person. Cut it into pieces. With a knife!
Add it to the peas. Cook for 10 more minutes.
```
```
And this is the second recipe:
```
```
Per person: 1 cup dried split peas, 4 cups of water, half a
chopped onion, a stalk of celery, and a carrot.
Soak peas for 12 hours. Simmer for 2 hours. Chop and add
vegetables. Cook for 10 more minutes.
```
The second is shorter and easier to interpret. But you do need to
understand a few more cooking-related words such as _soak_ , _simmer_ ,
_chop_ , and, I guess, _vegetable_.
When programming, we can’t rely on all the words we need to be
waiting for us in the dictionary. Thus, we might fall into the pattern of
the first recipe—work out the precise steps the computer has to perform,
one by one, blind to the higher-level concepts they express.
It is a useful skill, in programming, to notice when you are working
at too low a level of abstraction.

### Abstracting repetition

Plain functions, as we’ve seen them so far, are a good way to build
abstractions. But sometimes they fall short.
It is common for a program to do something a given number of times.
You can write aforloop for that, like this:


```
for (let i = 0; i < 10; i++) {
console.log(i);
}
```
Can we abstract “doing something _N_ times” as a function? Well, it’s
easy to write a function that callsconsole.log _N_ times.

```
function repeatLog(n) {
for (let i = 0; i < n; i++) {
console.log(i);
}
}
```
But what if we want to do something other than logging the numbers?
Since “doing something” can be represented as a function and functions
are just values, we can pass our action as a function value.

```
function repeat(n, action) {
for (let i = 0; i < n; i++) {
action(i);
}
}
```
```
repeat(3, console.log);
// → 0
// → 1
// → 2
```
We don’t have to pass a predefined function torepeat. Often, it is easier
to create a function value on the spot instead.


```
let labels = [];
repeat(5, i => {
labels.push(`Unit ${i + 1}`);
});
console.log(labels);
// → ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5"]
```
This is structured a little like a for loop—it first describes the kind
of loop and then provides a body. However, the body is now written
as a function value, which is wrapped in the parentheses of the call
torepeat. This is why it has to be closed with the closing brace _and_
closing parenthesis. In cases like this example, where the body is a
single small expression, you could also omit the braces and write the
loop on a single line.

### Higher-order functions

Functions that operate on other functions, either by taking them as ar-
guments or by returning them, are called _higher-order functions_. Since
we have already seen that functions are regular values, there is nothing
particularly remarkable about the fact that such functions exist. The
term comes from mathematics, where the distinction between functions
and other values is taken more seriously.
Higher-order functions allow us to abstract over _actions_ , not just
values. They come in several forms. For example, we can have functions
that create new functions.

```
function greaterThan(n) {
```

```
return m => m > n;
}
let greaterThan10 = greaterThan(10);
console.log(greaterThan10(11));
// → true
```
We can also have functions that change other functions.

```
function noisy(f) {
return (...args) => {
console.log("calling with", args);
let result = f(...args);
console.log("called with", args, ", returned", result);
return result;
};
}
noisy(Math.min)(3, 2, 1);
// → calling with [3, 2, 1]
// → called with [3, 2, 1] , returned 1
```
We can even write functions that provide new types of control flow.

```
function unless(test, then) {
if (!test) then();
}
```
```
repeat(3, n => {
unless(n % 2 == 1, () => {
console.log(n, "is even");
});
});
```

```
// → 0 is even
// → 2 is even
```
There is a built-in array method,forEach, that provides something like
afor/ofloop as a higher-order function.

```
["A", "B"].forEach(l => console.log(l));
// → A
// → B
```
### Script dataset

One area where higher-order functions shine is data processing. To
process data, we’ll need some actual example data. This chapter will
use a dataset about scripts—writing systems such as Latin, Cyrillic, or
Arabic.
Remember Unicode, the system that assigns a number to each char-
acter in written language, fromChapter 1? Most of these characters are
associated with a specific script. The standard contains 140 different
scripts, of which 81 are still in use today and 59 are historic.
Though I can fluently read only Latin characters, I appreciate the
fact that people are writing texts in at least 80 other writing systems,
many of which I wouldn’t even recognize. For example, here’s a sample
of Tamil handwriting:


The example dataset contains some pieces of information about the
140 scripts defined in Unicode. It is available in thecoding sandbox
for this chapter ( _https://eloquentjavascript.net/code#5_ ) as theSCRIPTS
binding. The binding contains an array of objects, each of which
describes a script.

```
{
name: "Coptic",
ranges: [[994, 1008], [11392, 11508], [11513, 11520]],
direction: "ltr",
year: -200,
living: false,
link: "https://en.wikipedia.org/wiki/Coptic_alphabet"
}
```
Such an object tells us the name of the script, the Unicode ranges
assigned to it, the direction in which it is written, the (approximate)
origin time, whether it is still in use, and a link to more information.
The direction may be"ltr"for left to right,"rtl"for right to left (the
way Arabic and Hebrew text are written), or"ttb"for top to bottom
(as with Mongolian writing).
Therangesproperty contains an array of Unicode character ranges,
each of which is a two-element array containing a lower bound and an
upper bound. Any character codes within these ranges are assigned to


the script. The lower bound is inclusive (code 994 is a Coptic character)
and the upper bound is noninclusive (code 1008 isn’t).

### Filtering arrays

If we want to find the scripts in the dataset that are still in use, the
following function might be helpful. It filters out elements in an array
that don’t pass a test.

```
function filter(array, test) {
let passed = [];
for (let element of array) {
if (test(element)) {
passed.push(element);
}
}
return passed;
}
```
```
console.log(filter(SCRIPTS, script => script.living));
// → [{name: "Adlam", ...}, ...]
```
The function uses the argument namedtest, a function value, to fill a
“gap” in the computation—the process of deciding which elements to
collect.
Note how thefilterfunction, rather than deleting elements from the
existing array, builds up a new array with only the elements that pass
the test. This function is _pure_. It does not modify the array it is given.
LikeforEach,filteris a standard array method. The example defined


the function only to show what it does internally. From now on, we’ll
use it like this instead:

```
console.log(SCRIPTS.filter(s => s.direction == "ttb"));
// → [{name: "Mongolian", ...}, ...]
```
### Transforming with map.

Say we have an array of objects representing scripts, produced by fil-
tering theSCRIPTSarray somehow. We want an array of names instead,
which is easier to inspect.
Themapmethod transforms an array by applying a function to all of
its elements and building a new array from the returned values. The
new array will have the same length as the input array, but its content
will have been _mapped_ to a new form by the function.

```
function map(array, transform) {
let mapped = [];
for (let element of array) {
mapped.push(transform(element));
}
return mapped;
}
```
```
let rtlScripts = SCRIPTS.filter(s => s.direction == "rtl");
console.log(map(rtlScripts, s => s.name));
// → ["Adlam", "Arabic", "Imperial Aramaic", ...]
```
LikeforEachandfilter,mapis a standard array method.


### Summarizing with reduce.

Another common thing to do with arrays is to compute a single value
from them. Our recurring example, summing a collection of numbers,
is an instance of this. Another example is finding the script with the
most characters.
The higher-order operation that represents this pattern is called _re-
duce_ (sometimes also called _fold_ ). It builds a value by repeatedly tak-
ing a single element from the array and combining it with the current
value. When summing numbers, you’d start with the number zero and,
for each element, add that to the sum.
The parameters to reduce are, apart from the array, a combining
function and a start value. This function is a little less straightforward
thanfilterandmap, so take a close look at it:

```
function reduce(array, combine, start) {
let current = start;
for (let element of array) {
current = combine(current, element);
}
return current;
}
```
```
console.log(reduce([1, 2, 3, 4], (a, b) => a + b, 0));
// → 10
```
The standard array methodreduce, which of course corresponds to this
function, has an added convenience. If your array contains at least
one element, you are allowed to leave off the start argument. The


method will take the first element of the array as its start value and
start reducing at the second element.

```
console.log([1, 2, 3, 4].reduce((a, b) => a + b));
// → 10
```
To use reduce(twice) to find the script with the most characters, we
can write something like this:

```
function characterCount(script) {
return script.ranges.reduce((count, [from, to]) => {
return count + (to - from);
}, 0);
}
```
```
console.log(SCRIPTS.reduce((a, b) => {
return characterCount(a) < characterCount(b)? b : a;
}));
// → {name: "Han", ...}
```
ThecharacterCountfunction reduces the ranges assigned to a script by
summing their sizes. Note the use of destructuring in the parameter list
of the reducer function. The second call toreducethen uses this to find
the largest script by repeatedly comparing two scripts and returning
the larger one.
The Han script has more than 89,000 characters assigned to it in the
Unicode standard, making it by far the biggest writing system in the
dataset. Han is a script sometimes used for Chinese, Japanese, and
Korean text. Those languages share a lot of characters, though they
tend to write them differently. The (US-based) Unicode Consortium


decided to treat them as a single writing system to save character codes.
This is called _Han unification_ and still makes some people very angry.

### Composability

Consider how we would have written the previous example (finding the
biggest script) without higher-order functions. The code is not that
much worse.

```
let biggest = null;
for (let script of SCRIPTS) {
if (biggest == null ||
characterCount(biggest) < characterCount(script)) {
biggest = script;
}
}
console.log(biggest);
// → {name: "Han", ...}
```
There are a few more bindings, and the program is four lines longer,
but it is still very readable.
The abstractions these functions provide really shine when you need
to _compose_ operations. As an example, let’s write code that finds the
average year of origin for living and dead scripts in the dataset.

```
function average(array) {
return array.reduce((a, b) => a + b) / array.length;
}
```

```
console.log(Math.round(average(
SCRIPTS.filter(s => s.living).map(s => s.year))));
// → 1165
console.log(Math.round(average(
SCRIPTS.filter(s => !s.living).map(s => s.year))));
// → 204
```
As you can see, the dead scripts in Unicode are, on average, older than
the living ones. This is not a terribly meaningful or surprising statistic.
But I hope you’ll agree that the code used to compute it isn’t hard to
read. You can see it as a pipeline: we start with all scripts, filter out
the living (or dead) ones, take the years from those, average them, and
round the result.
You could definitely also write this computation as one big loop.
let total = 0, count = 0;
for (let script of SCRIPTS) {
if (script.living) {
total += script.year;
count += 1;
}
}
console.log(Math.round(total / count));
// → 1165

However, it is harder to see what was being computed and how. And
because intermediate results aren’t represented as coherent values, it’d
be a lot more work to extract something likeaverageinto a separate
function.
In terms of what the computer is actually doing, these two approaches


are also quite different. The first will build up new arrays when running
filterandmap, whereas the second computes only some numbers, doing
less work. You can usually afford the readable approach, but if you’re
processing huge arrays and doing so many times, the less abstract style
might be worth the extra speed.

### Strings and character codes

One interesting use of this dataset would be figuring out what script a
piece of text is using. Let’s go through a program that does this.
Remember that each script has an array of character code ranges
associated with it. Given a character code, we could use a function like
this to find the corresponding script (if any):

```
function characterScript(code) {
for (let script of SCRIPTS) {
if (script.ranges.some(([from, to]) => {
return code >= from && code < to;
})) {
return script;
}
}
return null;
}
```
```
console.log(characterScript(121));
// → {name: "Latin", ...}
```
Thesomemethod is another higher-order function. It takes a test func-


tion and tells you whether that function returns true for any of the
elements in the array.
But how do we get the character codes in a string?
InChapter 1I mentioned that JavaScript strings are encoded as a
sequence of 16-bit numbers. These are called _code units_. A Unicode
character code was initially supposed to fit within such a unit (which
gives you a little over 65,000 characters). When it became clear that
wasn’t going to be enough, many people balked at the need to use
more memory per character. To address these concerns, UTF-16, the
format also used by JavaScript strings, was invented. It describes most
common characters using a single 16-bit code unit but uses a pair of
two such units for others.
UTF-16 is generally considered a bad idea today. It seems almost
intentionally designed to invite mistakes. It’s easy to write programs
that pretend code units and characters are the same thing. And if your
language doesn’t use two-unit characters, that will appear to work just
fine. But as soon as someone tries to use such a program with some less
common Chinese characters, it breaks. Fortunately, with the advent of
emoji, everybody has started using two-unit characters, and the burden
of dealing with such problems is more fairly distributed.
Unfortunately, obvious operations on JavaScript strings, such as get-
ting their length through thelengthproperty and accessing their con-
tent using square brackets, deal only with code units.

```
// Two emoji characters, horse and shoe
let horseShoe = "🐴👟";
console.log(horseShoe.length);
```

```
// → 4
console.log(horseShoe[0]);
// → (Invalid half-character)
console.log(horseShoe.charCodeAt(0));
// → 55357 (Code of the half-character)
console.log(horseShoe.codePointAt(0));
// → 128052 (Actual code for horse emoji)
```
JavaScript’scharCodeAtmethod gives you a code unit, not a full charac-
ter code. ThecodePointAtmethod, added later, does give a full Unicode
character, so we could use that to get characters from a string. But the
argument passed to codePointAtis still an index into the sequence of
code units. To run over all characters in a string, we’d still need to
deal with the question of whether a character takes up one or two code
units.
In theprevious chapter, I mentioned that afor/ofloop can also be
used on strings. LikecodePointAt, this type of loop was introduced at
a time when people were acutely aware of the problems with UTF-16.
When you use it to loop over a string, it gives you real characters, not
code units.

```
let roseDragon = "🌹🐉";
for (let char of roseDragon) {
console.log(char);
}
// → 🌹
// → 🐉
```
If you have a character (which will be a string of one or two code units),


you can usecodePointAt(0)to get its code.

### Recognizing text.

We have acharacterScriptfunction and a way to correctly loop over
characters. The next step is to count the characters that belong to each
script. The following counting abstraction will be useful there:

```
function countBy(items, groupName) {
let counts = [];
for (let item of items) {
let name = groupName(item);
let known = counts.find(c => c.name == name);
if (!known) {
counts.push({name, count: 1});
} else {
known.count++;
}
}
return counts;
}
```
```
console.log(countBy([1, 2, 3, 4, 5], n => n > 2));
// → [{name: false, count: 2}, {name: true, count: 3}]
```
ThecountByfunction expects a collection (anything that we can loop
over with for/of) and a function that computes a group name for a
given element. It returns an array of objects, each of which names a
group and tells you the number of elements that were found in that


group.
It uses another array method,find, which goes over the elements in
the array and returns the first one for which a function returns true. It
returnsundefinedwhen it finds no such element.
UsingcountBy, we can write the function that tells us which scripts
are used in a piece of text.

```
function textScripts(text) {
let scripts = countBy(text, char => {
let script = characterScript(char.codePointAt(0));
return script? script.name : "none";
}).filter(({name}) => name != "none");
```
```
let total = scripts.reduce((n, {count}) => n + count, 0);
if (total == 0) return "No scripts found";
```
```
return scripts.map(({name, count}) => {
return `${Math.round(count * 100 / total)}% ${name}`;
}).join(", ");
}
```
```
console.log(textScripts('英国的狗说"woof", 俄罗斯的狗说"тяв"'))
;
// → 61% Han, 22% Latin, 17% Cyrillic
```
The function first counts the characters by name, usingcharacterScript
to assign them a name and falling back to the string"none"for char-
acters that aren’t part of any script. Thefiltercall drops the entry
for"none"from the resulting array, since we aren’t interested in those


characters.
To be able to compute percentages, we first need the total number of
characters that belong to a script, which we can compute withreduce

. If we find no such characters, the function returns a specific string.
Otherwise, it transforms the counting entries into readable strings with
mapand then combines them withjoin.

### Summary

Being able to pass function values to other functions is a deeply useful
aspect of JavaScript. It allows us to write functions that model com-
putations with “gaps” in them. The code that calls these functions can
fill in the gaps by providing function values.
Arrays provide a number of useful higher-order methods. You can
useforEachto loop over the elements in an array. Thefiltermethod
returns a new array containing only the elements that pass the predicate
function. You can transform an array by putting each element through
a function usingmap. You can usereduceto combine all the elements
in an array into a single value. Thesome method tests whether any
element matches a given predicate function, whilefind finds the first
element that matches a predicate.


### Exercises

**Flattening**

Use thereducemethod in combination with theconcatmethod to “flat-
ten” an array of arrays into a single array that has all the elements of
the original arrays.

**Yourownloop**

Write a higher-order functionloopthat provides something like afor
loop statement. It should take a value, a test function, an update
function, and a body function. Each iteration, it should first run the
test function on the current loop value and stop if that returnsfalse.
It should then call the body function, giving it the current value, and
finally call the update function to create a new value and start over
from the beginning.
When defining the function, you can use a regular loop to do the
actual looping.

**Everything**

Arrays also have aneverymethod analogous to thesomemethod. This
method returns true when the given function returns true for _every_
element in the array. In a way,someis a version of the||operator that
acts on arrays, andeveryis like the&&operator.
Implementeveryas a function that takes an array and a predicate
function as parameters. Write two versions, one using a loop and one


using thesomemethod.

**Dominantwritingdirection**

Write a function that computes the dominant writing direction in a
string of text. Remember that each script object has adirectionprop-
erty that can be"ltr"(left to right),"rtl"(right to left), or"ttb"(top
to bottom).
The dominant direction is the direction of a majority of the char-
acters that have a script associated with them. ThecharacterScript
andcountByfunctions defined earlier in the chapter are probably useful
here.


```
“An abstract data type is realized by writing a special kind of
program [...] which defines the type in terms of the operations
which can be performed on it.”
—Barbara Liskov, Programming with Abstract Data Types
```
**Chapter6**

## TheSecretLifeofObjects

Chapter 4introduced JavaScript’s objects as containers that hold other
data. In programming culture, _object-oriented programming_ is a set of
techniques that use objects as the central principle of program organi-
zation. Though no one really agrees on its precise definition, object-
oriented programming has shaped the design of many programming
languages, including JavaScript. This chapter describes the way these
ideas can be applied in JavaScript.

### Abstract Data Types

The main idea in object-oriented programming is to use objects, or
rather _types_ of objects, as the unit of program organization. Setting
up a program as a number of strictly separated object types provides
a way to think about its structure and thus to enforce some kind of
discipline, preventing everything from becoming entangled.
The way to do this is to think of objects somewhat like you’d think of
an electric mixer or other consumer appliance. The people who design


and assemble a mixer have to do specialized work requiring material
science and understanding of electricity. They cover all that up in a
smooth plastic shell so that the people who only want to mix pancake
batter don’t have to worry about all that—they have to understand
only the few knobs that the mixer can be operated with.
Similarly, an _abstract data type_ , or _object class_ , is a subprogram that
may contain arbitrarily complicated code but exposes a limited set of
methods and properties that people working with it are supposed to
use. This allows large programs to be built up out of a number of
appliance types, limiting the degree to which these different parts are
entangled by requiring them to only interact with each other in specific
ways.
If a problem is found in one such object class, it can often be repaired
or even completely rewritten without impacting the rest of the program.
Even better, it may be possible to use object classes in multiple different
programs, avoiding the need to recreate their functionality from scratch.
You can think of JavaScript’s built-in data structures, such as arrays
and strings, as such reusable abstract data types.
Each abstract data type has an _interface_ , the collection of operations
that external code can perform on it. Any details beyond that interface
are _encapsulated_ , treated as internal to the type and of no concern to
the rest of the program.
Even basic things like numbers can be thought of as an abstract data
type whose interface allows us to add them, multiply them, compare
them, and so on. In fact, the fixation on single _objects_ as the main unit
of organization in classical object-oriented programming is somewhat


unfortunate since useful pieces of functionality often involve a group of
different object classes working closely together.

### Methods

In JavaScript, methods are nothing more than properties that hold
function values. This is a simple method:

```
function speak(line) {
console.log(`The ${this.type} rabbit says '${line}'`);
}
let whiteRabbit = {type: "white", speak};
let hungryRabbit = {type: "hungry", speak};
```
```
whiteRabbit.speak("Oh my fur and whiskers");
// → The white rabbit says 'Oh my fur and whiskers'
hungryRabbit.speak("Got any carrots?");
// → The hungry rabbit says 'Got any carrots?'
```
Typically a method needs to do something with the object on which
it was called. When a function is called as a method—looked up as
a property and immediately called, as inobject.method()—the binding
calledthisin its body automatically points at the object on which it
was called.
You can think ofthis as an extra parameter that is passed to the
function in a different way than regular parameters. If you want to
provide it explicitly, you can use a function’scallmethod, which takes
the this value as its first argument and treats further arguments as


normal parameters.

```
speak.call(whiteRabbit, "Hurry");
// → The white rabbit says 'Hurry'
```
Since each function has its ownthisbinding whose value depends on
the way it is called, you cannot refer to thethisof the wrapping scope
in a regular function defined with thefunctionkeyword.
Arrow functions are different—they do not bind their ownthisbut
can see thethisbinding of the scope around them. Thus, you can do
something like the following code, which referencesthisfrom inside a
local function:

```
let finder = {
find(array) {
return array.some(v => v == this.value);
},
value: 5
};
console.log(finder.find([4, 5]));
// → true
```
A property likefind(array)in an object expression is a shorthand way
of defining a method. It creates a property calledfindand gives it a
function as its value.
If I had written the argument to someusing thefunctionkeyword,
this code wouldn’t work.


### Prototypes

One way to create a rabbit object type with a speak method would
be to create a helper function that has a rabbit type as its parameter
and returns an object holding that as itstypeproperty and our speak
function in itsspeakproperty.
All rabbits share that same method. Especially for types with many
methods, it would be nice if there were a way to keep a type’s methods
in a single place, rather than adding them to each object individually.
In JavaScript, _prototypes_ are the way to do that. Objects can be
linked to other objects, to magically get all the properties that other
object has. Plain old objects created with{}notation are linked to an
object calledObject.prototype.

```
let empty = {};
console.log(empty.toString);
// → function toString()...{}
console.log(empty.toString());
// → [object Object]
```
It looks like we just pulled a property out of an empty object. But
in fact,toStringis a method stored inObject.prototype, meaning it is
available in most objects.
When an object gets a request for a property that it doesn’t have,
its prototype will be searched for the property. If that doesn’t have it,
the _prototype’s_ prototype is searched, and so on until an object without
prototype is reached (Object.prototypeis such an object).

```
console.log(Object.getPrototypeOf({}) == Object.prototype);
```

```
// → true
console.log(Object.getPrototypeOf(Object.prototype));
// → null
```
As you’d guess,Object.getPrototypeOfreturns the prototype of an ob-
ject.
Many objects don’t directly haveObject.prototypeas their prototype
but instead have another object that provides a different set of default
properties. Functions derive fromFunction.prototypeand arrays derive
fromArray.prototype.

```
console.log(Object.getPrototypeOf(Math.max) ==
Function.prototype);
// → true
console.log(Object.getPrototypeOf([]) == Array.prototype);
// → true
```
Such a prototype object will itself have a prototype, often Object.
prototype, so that it still indirectly provides methods liketoString.
You can useObject.createto create an object with a specific proto-
type.

```
let protoRabbit = {
speak(line) {
console.log(`The ${this.type} rabbit says '${line}'`);
}
};
let blackRabbit = Object.create(protoRabbit);
blackRabbit.type = "black";
blackRabbit.speak("I am fear and darkness");
```

```
// → The black rabbit says 'I am fear and darkness'
```
The “proto” rabbit acts as a container for the properties shared by all
rabbits. An individual rabbit object, like the black rabbit, contains
properties that apply only to itself—in this case its type—and derives
shared properties from its prototype.

### Classes

JavaScript’s prototype system can be interpreted as a somewhat free-
form take on abstract data types or classes. A _class_ defines the shape of
a type of object—what methods and properties it has. Such an object
is called an _instance_ of the class.
Prototypes are useful for defining properties for which all instances
of a class share the same value. Properties that differ per instance, such
as our rabbits’typeproperty, need to be stored directly in the objects
themselves.
To create an instance of a given class, you have to make an object
that derives from the proper prototype, but you _also_ have to make sure
it itself has the properties that instances of this class are supposed to
have. This is what a _constructor_ function does.

```
function makeRabbit(type) {
let rabbit = Object.create(protoRabbit);
rabbit.type = type;
return rabbit;
}
```

JavaScript’s class notation makes it easier to define this type of function,
along with a prototype object.

```
class Rabbit {
constructor(type) {
this.type = type;
}
speak(line) {
console.log(`The ${this.type} rabbit says '${line}'`);
}
}
```
Theclasskeyword starts a class declaration, which allows us to define
a constructor and a set of methods together. Any number of methods
may be written inside the declaration’s braces. This code has the effect
of defining a binding calledRabbit, which holds a function that runs the
code inconstructorand has aprototypeproperty that holds thespeak
method.
This function cannot be called like a normal function. Constructors,
in JavaScript, are called by putting the keywordnewin front of them.
Doing so creates a fresh instance object whose prototype is the object
from the function’sprototypeproperty, then runs the function withthis
bound to the new object, and finally returns the object.

```
let killerRabbit = new Rabbit("killer");
```
In fact, class was only introduced in the 2015 edition of JavaScript.
Any function can be used as a constructor, and before 2015, the way to
define a class was to write a regular function and then manipulate its


prototypeproperty.

```
function ArchaicRabbit(type) {
this.type = type;
}
ArchaicRabbit.prototype.speak = function(line) {
console.log(`The ${this.type} rabbit says '${line}'`);
};
let oldSchoolRabbit = new ArchaicRabbit("old school");
```
For this reason, all non-arrow functions start with aprototypeproperty
holding an empty object.
By convention, the names of constructors are capitalized so that they
can easily be distinguished from other functions.
It is important to understand the distinction between the way a pro-
totype is associated with a constructor (through itsprototypeproperty)
and the way objects _have_ a prototype (which can be found withObject
.getPrototypeOf). The actual prototype of a constructor is Function.
prototypesince constructors are functions. The constructor function’s
prototype _property_ holds the prototype used for instances created through
it.

```
console.log(Object.getPrototypeOf(Rabbit) ==
Function.prototype);
// → true
console.log(Object.getPrototypeOf(killerRabbit) ==
Rabbit.prototype);
// → true
```
Constructors will typically add some per-instance properties tothis. It


is also possible to declare properties directly in the class declaration.
Unlike methods, such properties are added to instance objects and not
the prototype.

```
class Particle {
speed = 0;
constructor(position) {
this.position = position;
}
}
```
Likefunction,classcan be used both in statements and in expressions.
When used as an expression, it doesn’t define a binding but just pro-
duces the constructor as a value. You are allowed to omit the class
name in a class expression.

```
let object = new class { getWord() { return "hello"; } };
console.log(object.getWord());
// → hello
```
### Private Properties

It is common for classes to define some properties and methods for
internal use that are not part of their interface. These are called _private_
properties, as opposed to _public_ ones, which are part of the object’s
external interface.
To declare a private method, put a#sign in front of its name. Such
methods can be called only from inside theclassdeclaration that de-


fines them.

```
class SecretiveObject {
#getSecret() {
return "I ate all the plums";
}
interrogate() {
let shallISayIt = this.#getSecret();
return "never";
}
}
```
When a class does not declare a constructor, it will automatically get
an empty one.
If you try to call#getSecretfrom outside the class, you get an error.
Its existence is entirely hidden inside the class declaration.
To use private instance properties, you must declare them. Regu-
lar properties can be created by just assigning to them, but private
properties _must_ be declared in the class declaration to be available at
all.
This class implements an appliance for getting a random whole num-
ber below a given maximum number. It has only one public property:
getNumber.

```
class RandomSource {
#max;
constructor(max) {
this.#max = max;
}
getNumber() {
```

```
return Math.floor(Math.random() * this.#max);
}
}
```
### Overriding derived properties

When you add a property to an object, whether it is present in the
prototype or not, the property is added to the object _itself_. If there was
already a property with the same name in the prototype, this property
will no longer affect the object, as it is now hidden behind the object’s
own property.

```
Rabbit.prototype.teeth = "small";
console.log(killerRabbit.teeth);
// → small
killerRabbit.teeth = "long, sharp, and bloody";
console.log(killerRabbit.teeth);
// → long, sharp, and bloody
console.log((new Rabbit("basic")).teeth);
// → small
console.log(Rabbit.prototype.teeth);
// → small
```
The following diagram sketches the situation after this code has run.
TheRabbitandObjectprototypes lie behindkillerRabbitas a kind of
backdrop, where properties that are not found in the object itself can
be looked up.


```
toString: <function>
...
```
```
teeth: "small"
speak: <function>
```
```
killerRabbit
teeth: "long, sharp, ..."
type: "killer"
```
```
Rabbit
prototype
Object
create: <function>
prototype
...
```
Overriding properties that exist in a prototype can be a useful thing
to do. As the rabbit teeth example shows, overriding can be used to
express exceptional properties in instances of a more generic class of
objects while letting the nonexceptional objects take a standard value
from their prototype.
Overriding is also used to give the standard function and array pro-
totypes a differenttoStringmethod than the basic object prototype.

```
console.log(Array.prototype.toString ==
Object.prototype.toString);
// → false
console.log([1, 2].toString());
// → 1,2
```
CallingtoStringon an array gives a result similar to calling.join(",")
on it—it puts commas between the values in the array. Directly calling
Object.prototype.toString with an array produces a different string.
That function doesn’t know about arrays, so it simply puts the word
_object_ and the name of the type between square brackets.

```
console.log(Object.prototype.toString.call([1, 2]));
```

```
// → [object Array]
```
### Maps

We saw the word _map_ used in theprevious chapterfor an operation
that transforms a data structure by applying a function to its elements.
Confusing as it is, in programming the same word is used for a related
but rather different thing.
A _map_ (noun) is a data structure that associates values (the keys)
with other values. For example, you might want to map names to ages.
It is possible to use objects for this.

```
let ages = {
Boris: 39,
Liang: 22,
Júlia: 62
};
```
```
console.log(`Júlia is ${ages["Júlia"]}`);
// → Júlia is 62
console.log("Is Jack's age known?", "Jack" in ages);
// → Is Jack's age known? false
console.log("Is toString's age known?", "toString" in ages);
// → Is toString's age known? true
```
Here, the object’s property names are the people’s names and the prop-
erty values are their ages. But we certainly didn’t list anybody named
toString in our map. Yet because plain objects derive from Object.


prototype, it looks like the property is there.
For this reason, using plain objects as maps is dangerous. There are
several possible ways to avoid this problem. First, you can create ob-
jects with _no_ prototype. If you passnulltoObject.create, the resulting
object will not derive fromObject.prototypeand can be safely used as
a map.

```
console.log("toString" in Object.create(null));
// → false
```
Object property names must be strings. If you need a map whose keys
can’t easily be converted to strings—such as objects—you cannot use
an object as your map.
Fortunately, JavaScript comes with a class calledMapthat is written
for this exact purpose. It stores a mapping and allows any type of keys.

```
let ages = new Map();
ages.set("Boris", 39);
ages.set("Liang", 22);
ages.set("Júlia", 62);
```
```
console.log(`Júlia is ${ages.get("Júlia")}`);
// → Júlia is 62
console.log("Is Jack's age known?", ages.has("Jack"));
// → Is Jack's age known? false
console.log(ages.has("toString"));
// → false
```
The methodsset,get, andhasare part of the interface of theMapobject.
Writing a data structure that can quickly update and search a large set


of values isn’t easy, but we don’t have to worry about that. Someone
else did it for us, and we can go through this simple interface to use
their work.
If you do have a plain object that you need to treat as a map for some
reason, it is useful to know thatObject.keysreturns only an object’s
_own_ keys, not those in the prototype. As an alternative to the in
operator, you can use the Object.hasOwnfunction, which ignores the
object’s prototype.

```
console.log(Object.hasOwn({x: 1}, "x"));
// → true
console.log(Object.hasOwn({x: 1}, "toString"));
// → false
```
### Polymorphism

When you call theStringfunction (which converts a value to a string)
on an object, it will call the toStringmethod on that object to try
to create a meaningful string from it. I mentioned that some of the
standard prototypes define their own version oftoStringso they can
create a string that contains more useful information than "[object
Object]". You can also do that yourself.

```
Rabbit.prototype.toString = function() {
return `a ${this.type} rabbit`;
};
```
```
console.log(String(killerRabbit));
```

```
// → a killer rabbit
```
This is a simple instance of a powerful idea. When a piece of code is
written to work with objects that have a certain interface—in this case,
a toStringmethod—any kind of object that happens to support this
interface can be plugged into the code and will be able to work with it.
This technique is called _polymorphism_. Polymorphic code can work
with values of different shapes, as long as they support the interface it
expects.
An example of a widely used interface is that of array-like objects that
have alengthproperty holding a number and numbered properties for
each of their elements. Both arrays and strings support this interface, as
do various other objects, some of which we’ll see later in the chapters
about the browser. Our implementation of forEach from Chapter 5
works on anything that provides this interface. In fact, so doesArray.
prototype.forEach.

```
Array.prototype.forEach.call({
length: 2,
0: "A",
1: "B"
}, elt => console.log(elt));
// → A
// → B
```

### Getters, setters, and statics

Interfaces often contain plain properties, not just methods. For exam-
ple,Mapobjects have asizeproperty that tells you how many keys are
stored in them.
It is not necessary for such an object to compute and store such a
property directly in the instance. Even properties that are accessed
directly may hide a method call. Such methods are called _getters_ and
are defined by writing get in front of the method name in an object
expression or class declaration.

```
let varyingSize = {
get size() {
return Math.floor(Math.random() * 100);
}
};
```
```
console.log(varyingSize.size);
// → 73
console.log(varyingSize.size);
// → 49
```
Whenever someone reads from this object’ssizeproperty, the associ-
ated method is called. You can do a similar thing when a property is
written to, using a _setter_.

```
class Temperature {
constructor(celsius) {
this.celsius = celsius;
}
```

```
get fahrenheit() {
return this.celsius * 1.8 + 32;
}
set fahrenheit(value) {
this.celsius = (value - 32) / 1.8;
}
```
```
static fromFahrenheit(value) {
return new Temperature((value - 32) / 1.8);
}
}
```
```
let temp = new Temperature(22);
console.log(temp.fahrenheit);
// → 71.6
temp.fahrenheit = 86;
console.log(temp.celsius);
// → 30
```
The Temperatureclass allows you to read and write the temperature
in either degrees Celsius or degrees Fahrenheit, but internally it stores
only Celsius and automatically converts to and from Celsius in the
fahrenheitgetter and setter.
Sometimes you want to attach some properties directly to your con-
structor function rather than to the prototype. Such methods won’t
have access to a class instance but can, for example, be used to provide
additional ways to create instances.
Inside a class declaration, methods or properties that havestatic
written before their name are stored on the constructor. For example,


the Temperatureclass allows you to write Temperature.fromFahrenheit
(100)to create a temperature using degrees Fahrenheit.

```
let boil = Temperature.fromFahrenheit(212);
console.log(boil.celsius);
// → 100
```
### Symbols.

I mentioned inChapter 4that afor/ofloop can loop over several kinds
of data structures. This is another case of polymorphism—such loops
expect the data structure to expose a specific interface, which arrays
and strings do. And we can also add this interface to our own objects!
But before we can do that, we need to briefly take a look at the symbol
type.
It is possible for multiple interfaces to use the same property name
for different things. For example, on array-like objects, lengthrefers
to the number of elements in the collection. But an object interface
describing a hiking route could uselengthto provide the length of the
route in meters. It would not be possible for an object to conform to
both these interfaces.
An object trying to be a route and array-like (maybe to enumerate its
waypoints) is somewhat far-fetched, and this kind of problem isn’t that
common in practice. For things like the iteration protocol, though, the
language designers needed a type of property that _really_ doesn’t conflict
with any others. So in 2015, _symbols_ were added to the language.


Most properties, including all those we have seen so far, are named
with strings. But it is also possible to use symbols as property names.
Symbols are values created with the Symbolfunction. Unlike strings,
newly created symbols are unique—you cannot create the same symbol
twice.

```
let sym = Symbol("name");
console.log(sym == Symbol("name"));
// → false
Rabbit.prototype[sym] = 55;
console.log(killerRabbit[sym]);
// → 55
```
The string you pass to Symbol is included when you convert it to a
string and can make it easier to recognize a symbol when, for example,
showing it in the console. But it has no meaning beyond that—multiple
symbols may have the same name.
Being both unique and usable as property names makes symbols suit-
able for defining interfaces that can peacefully live alongside other prop-
erties, no matter what their names are.

```
const length = Symbol("length");
Array.prototype[length] = 0;
```
```
console.log([1, 2].length);
// → 2
console.log([1, 2][length]);
// → 0
```
It is possible to include symbol properties in object expressions and


classes by using square brackets around the property name. That causes
the expression between the brackets to be evaluated to produce the
property name, analogous to the square bracket property access nota-
tion.

```
let myTrip = {
length: 2,
0: "Lankwitz",
1: "Babelsberg",
[length]: 21500
};
console.log(myTrip[length], myTrip.length);
// → 21500 2
```
### The iterator interface

The object given to afor/ofloop is expected to be _iterable_. This means
it has a method named with theSymbol.iteratorsymbol (a symbol value
defined by the language, stored as a property of theSymbolfunction).
When called, that method should return an object that provides a
second interface, _iterator_. This is the actual thing that iterates. It has
anextmethod that returns the next result. That result should be an
object with a valueproperty that provides the next value, if there is
one, and adoneproperty, which should be true when there are no more
results and false otherwise.
Note that thenext,value, anddoneproperty names are plain strings,
not symbols. OnlySymbol.iterator, which is likely to be added to a _lot_


of different objects, is an actual symbol.
We can directly use this interface ourselves.
let okIterator = "OK"[Symbol.iterator]();
console.log(okIterator.next());
// → {value: "O", done: false}
console.log(okIterator.next());
// → {value: "K", done: false}
console.log(okIterator.next());
// → {value: undefined, done: true}

Let’s implement an iterable data structure similar to the linked list from
the exercise inChapter 4. We’ll write the list as a class this time.

```
class List {
constructor(value, rest) {
this.value = value;
this.rest = rest;
}
```
```
get length() {
return 1 + (this.rest? this.rest.length : 0);
}
```
```
static fromArray(array) {
let result = null;
for (let i = array.length - 1; i >= 0; i--) {
result = new this(array[i], result);
}
return result;
}
```

```
}
```
Note thatthis, in a static method, points at the constructor of the class,
not an instance—there is no instance around when a static method is
called.
Iterating over a list should return all the list’s elements from start to
end. We’ll write a separate class for the iterator.

```
class ListIterator {
constructor(list) {
this.list = list;
}
```
```
next() {
if (this.list == null) {
return {done: true};
}
let value = this.list.value;
this.list = this.list.rest;
return {value, done: false};
}
}
```
The class tracks the progress of iterating through the list by updating
its listproperty to move to the next list object whenever a value is
returned and reports that it is done when that list is empty (null).
Let’s set up theListclass to be iterable. Throughout this book, I’ll
occasionally use after-the-fact prototype manipulation to add methods
to classes so that the individual pieces of code remain small and self
contained. In a regular program, where there is no need to split the


code into small pieces, you’d declare these methods directly in the class
instead.

```
List.prototype[Symbol.iterator] = function() {
return new ListIterator(this);
};
```
We can now loop over a list withfor/of.

```
let list = List.fromArray([1, 2, 3]);
for (let element of list) {
console.log(element);
}
// → 1
// → 2
// → 3
```
The...syntax in array notation and function calls similarly works with
any iterable object. For example, you can use[...value]to create an
array containing the elements in an arbitrary iterable object.

```
console.log([..."PCI"]);
// → ["P", "C", "I"]
```
### Inheritance

Imagine we need a list type much like theListclass we saw before, but
because we will be asking for its length all the time, we don’t want it
to have to scan through itsrestevery time. Instead, we want to store


the length in every instance for eﬀicient access.
JavaScript’s prototype system makes it possible to create a _new_ class,
much like the old class, but with new definitions for some of its prop-
erties. The prototype for the new class derives from the old prototype
but adds a new definition for, say, thelengthgetter.
In object-oriented programming terms, this is called _inheritance_. The
new class inherits properties and behavior from the old class.

```
class LengthList extends List {
#length;
```
```
constructor(value, rest) {
super(value, rest);
this.#length = super.length;
}
```
```
get length() {
return this.#length;
}
}
```
```
console.log(LengthList.fromArray([1, 2, 3]).length);
// → 3
```
The use of the wordextendsindicates that this class shouldn’t be di-
rectly based on the defaultObjectprototype but on some other class.
This is called the _superclass_. The derived class is the _subclass_.
To initialize aLengthListinstance, the constructor calls the construc-
tor of its superclass through thesuperkeyword. This is necessary be-


cause if this new object is to behave (roughly) like aList, it is going to
need the instance properties that lists have.
The constructor then stores the list’s length in a private property.
If we had writtenthis.lengththere, the class’s own getter would have
been called, which doesn’t work yet since#lengthhasn’t been filled in
yet. We can usesuper.something to call methods and getters on the
superclass’s prototype, which is often useful.
Inheritance allows us to build slightly different data types from ex-
isting data types with relatively little work. It is a fundamental part
of the object-oriented tradition, alongside encapsulation and polymor-
phism. But while the latter two are now generally regarded as wonderful
ideas, inheritance is more controversial.
Whereas encapsulation and polymorphism can be used to _separate_
pieces of code from one another, reducing the tangledness of the over-
all program, inheritance fundamentally ties classes together, creating
_more_ tangle. When inheriting from a class, you usually have to know
more about how it works than when simply using it. Inheritance can
be a useful tool to make some types of programs more succinct, but it
shouldn’t be the first tool you reach for, and you probably shouldn’t ac-
tively go looking for opportunities to construct class hierarchies (family
trees of classes).

### The instanceof operator.

It is occasionally useful to know whether an object was derived from
a specific class. For this, JavaScript provides a binary operator called


instanceof.

```
console.log(
new LengthList(1, null) instanceof LengthList);
// → true
console.log(new LengthList(2, null) instanceof List);
// → true
console.log(new List(3, null) instanceof LengthList);
// → false
console.log([1] instanceof Array);
// → true
```
The operator will see through inherited types, so a LengthList is an
instance ofList. The operator can also be applied to standard con-
structors likeArray. Almost every object is an instance ofObject.

### Summary

Objects do more than just hold their own properties. They have pro-
totypes, which are other objects. They’ll act as if they have properties
they don’t have as long as their prototype has that property. Simple
objects haveObject.prototypeas their prototype.
Constructors, which are functions whose names usually start with a
capital letter, can be used with thenewoperator to create new objects.
The new object’s prototype will be the object found in theprototype
property of the constructor. You can make good use of this by putting
the properties that all values of a given type share into their proto-
type. There’s a classnotation that provides a clear way to define a


constructor and its prototype.
You can define getters and setters to secretly call methods every time
an object’s property is accessed. Static methods are methods stored in
a class’s constructor rather than its prototype.
Theinstanceofoperator can, given an object and a constructor, tell
you whether that object is an instance of that constructor.
One useful thing to do with objects is to specify an interface for them
and tell everybody that they are supposed to talk to your object only
through that interface. The rest of the details that make up your object
are now _encapsulated_ , hidden behind the interface. You can use private
properties to hide a part of your object from the outside world.
More than one type may implement the same interface. Code written
to use an interface automatically knows how to work with any number of
different objects that provide the interface. This is called _polymorphism_.
When implementing multiple classes that differ in only some details,
it can be helpful to write the new classes as _subclasses_ of an existing
class, _inheriting_ part of its behavior.

### Exercises

**Avectortype**

Write a classVecthat represents a vector in two-dimensional space. It
takesxandyparameters (numbers), that it saves to properties of the
same name.
Give theVecprototype two methods,plusandminus, that take an-
other vector as a parameter and return a new vector that has the sum or


difference of the two vectors’ (thisand the parameter) _x_ and _y_ values.
Add a getter property length to the prototype that computes the
length of the vector—that is, the distance of the point ( _x_ , _y_ ) from the
origin (0, 0).

**Groups**

The standard JavaScript environment provides another data structure
calledSet. Like an instance ofMap, a set holds a collection of values.
UnlikeMap, it does not associate other values with those—it just tracks
which values are part of the set. A value can be part of a set only
once—adding it again doesn’t have any effect.
Write a class calledGroup(sinceSetis already taken). LikeSet, it has
add,delete, andhasmethods. Its constructor creates an empty group,
addadds a value to the group (but only if it isn’t already a member),
deleteremoves its argument from the group (if it was a member), and
hasreturns a Boolean value indicating whether its argument is a mem-
ber of the group.
Use the === operator, or something equivalent such as indexOf, to
determine whether two values are the same.
Give the class a staticfrommethod that takes an iterable object as
its argument and creates a group that contains all the values produced
by iterating over it.


**Iterablegroups**

Make theGroupclass from the previous exercise iterable. Refer to the
section about the iterator interface earlier in the chapter if you aren’t
clear on the exact form of the interface anymore.
If you used an array to represent the group’s members, don’t just
return the iterator created by calling theSymbol.iterator method on
the array. That would work, but it defeats the purpose of this exercise.
It is okay if your iterator behaves strangely when the group is modi-
fied during iteration.


```
“The question of whether Machines Can Think [...] is about as
relevant as the question of whether Submarines Can Swim.”
—Edsger Dijkstra, The Threats to Computing Science
```
**Chapter7**

## Project: ARobot

In “project” chapters, I’ll stop pummeling you with new theory for
a brief moment, and instead we’ll work through a program together.
Theory is necessary to learn to program, but reading and understanding
actual programs is just as important.
Our project in this chapter is to build an automaton, a little program
that performs a task in a virtual world. Our automaton will be a mail-
delivery robot picking up and dropping off parcels.

### Meadowfield

The village of Meadowfield isn’t very big. It consists of 11 places with
14 roads between them. It can be described with this array of roads:

```
const roads = [
"Alice's House-Bob's House", "Alice's House-Cabin",
"Alice's House-Post Office", "Bob's House-Town Hall",
"Daria's House-Ernie's House", "Daria's House-Town Hall",
"Ernie's House-Grete's House", "Grete's House-Farm",
```

```
"Grete's House-Shop", "Marketplace-Farm",
"Marketplace-Post Office", "Marketplace-Shop",
"Marketplace-Town Hall", "Shop-Town Hall"
];
```
The network of roads in the village forms a _graph_. A graph is a col-
lection of points (places in the village) with lines between them (roads).
This graph will be the world that our robot moves through.
The array of strings isn’t very easy to work with. What we’re inter-
ested in is the destinations that we can reach from a given place. Let’s
convert the list of roads to a data structure that, for each place, tells
us what can be reached from there.


```
function buildGraph(edges) {
let graph = Object.create(null);
function addEdge(from, to) {
if (from in graph) {
graph[from].push(to);
} else {
graph[from] = [to];
}
}
for (let [from, to] of edges.map(r => r.split("-"))) {
addEdge(from, to);
addEdge(to, from);
}
return graph;
}
```
```
const roadGraph = buildGraph(roads);
```
Given an array of edges,buildGraphcreates a map object that, for each
node, stores an array of connected nodes. It uses thesplitmethod to
go from the road strings—which have the form"Start-End")—to two-
element arrays containing the start and end as separate strings.

### The task

Our robot will be moving around the village. There are parcels in
various places, each addressed to some other place. The robot picks up
parcels when it comes across them and delivers them when it arrives at
their destinations.


The automaton must decide, at each point, where to go next. It has
finished its task when all parcels have been delivered.
To be able to simulate this process, we must define a virtual world
that can describe it. This model tells us where the robot is and where
the parcels are. When the robot has decided to move somewhere, we
need to update the model to reflect the new situation.
If you’re thinking in terms of object-oriented programming, your first
impulse might be to start defining objects for the various elements in
the world: a class for the robot, one for a parcel, maybe one for places.
These could then hold properties that describe their current state, such
as the pile of parcels at a location, which we could change when updat-
ing the world.
This is wrong. At least, it usually is. The fact that something sounds
like an object does not automatically mean that it should be an object
in your program. Reflexively writing classes for every concept in your
application tends to leave you with a collection of interconnected objects
that each have their own internal, changing state. Such programs are
often hard to understand and thus easy to break.
Instead, let’s condense the village’s state down to the minimal set
of values that define it. There’s the robot’s current location and the
collection of undelivered parcels, each of which has a current location
and a destination address. That’s it.
While we’re at it, let’s make it so that we don’t _change_ this state
when the robot moves but rather compute a _new_ state for the situation
after the move.

```
class VillageState {
```

```
constructor(place, parcels) {
this.place = place;
this.parcels = parcels;
}
```
```
move(destination) {
if (!roadGraph[this.place].includes(destination)) {
return this;
} else {
let parcels = this.parcels.map(p => {
if (p.place != this.place) return p;
return {place: destination, address: p.address};
}).filter(p => p.place != p.address);
return new VillageState(destination, parcels);
}
}
}
```
Themovemethod is where the action happens. It first checks whether
there is a road going from the current place to the destination, and if
not, it returns the old state, since this is not a valid move.
Next, the method creates a new state with the destination as the
robot’s new place. It also needs to create a new set of parcels—parcels
that the robot is carrying (that are at the robot’s current place) need
to be moved along to the new place. And parcels that are addressed to
the new place need to be delivered—that is, they need to be removed
from the set of undelivered parcels. The call tomap takes care of the
moving, and the call tofilterdoes the delivering.
Parcel objects aren’t changed when they are moved but re-created.


Themove method gives us a new village state but leaves the old one
entirely intact.

```
let first = new VillageState(
"Post Office",
[{place: "Post Office", address: "Alice's House"}]
);
let next = first.move("Alice's House");
```
```
console.log(next.place);
// → Alice's House
console.log(next.parcels);
// → []
console.log(first.place);
// → Post Office
```
The move causes the parcel to be delivered, which is reflected in the
next state. But the initial state still describes the situation where the
robot is at the post oﬀice and the parcel is undelivered.

### Persistent data.

Data structures that don’t change are called _immutable_ or _persistent_.
They behave a lot like strings and numbers in that they are who they are
and stay that way, rather than containing different things at different
times.
In JavaScript, just about everything _can_ be changed, so working with
values that are supposed to be persistent requires some restraint. There
is a function calledObject.freezethat changes an object so that writing


to its properties is ignored. You could use that to make sure your
objects aren’t changed, if you want to be careful. Freezing does require
the computer to do some extra work, and having updates ignored is
just about as likely to confuse someone as having them do the wrong
thing. I usually prefer to just tell people that a given object shouldn’t
be messed with and hope they remember it.

```
let object = Object.freeze({value: 5});
object.value = 10;
console.log(object.value);
// → 5
```
Why am I going out of my way to not change objects when the language
is obviously expecting me to? Because it helps me understand my
programs. This is about complexity management again. When the
objects in my system are fixed, stable things, I can consider operations
on them in isolation—moving to Alice’s house from a given start state
always produces the same new state. When objects change over time,
that adds a whole new dimension of complexity to this kind of reasoning.
For a small system like the one we are building in this chapter, we
could handle that bit of extra complexity. But the most important limit
on what kind of systems we can build is how much we can understand.
Anything that makes your code easier to understand makes it possible
to build a more ambitious system.
Unfortunately, although understanding a system built on persistent
data structures is easier, _designing_ one, especially when your program-
ming language isn’t helping, can be a little harder. We’ll look for op-
portunities to use persistent data structures in this book, but we’ll also


be using changeable ones.

### Simulation

A delivery robot looks at the world and decides in which direction it
wants to move. So we could say that a robot is a function that takes a
VillageStateobject and returns the name of a nearby place.
Because we want robots to be able to remember things so they can
make and execute plans, we also pass them their memory and allow
them to return a new memory. Thus, the thing a robot returns is an
object containing both the direction it wants to move in and a memory
value that will be given back to it the next time it is called.

```
function runRobot(state, robot, memory) {
for (let turn = 0;; turn++) {
if (state.parcels.length == 0) {
console.log(`Done in ${turn} turns`);
break;
}
let action = robot(state, memory);
state = state.move(action.direction);
memory = action.memory;
console.log(`Moved to ${action.direction}`);
}
}
```
Consider what a robot has to do to “solve” a given state. It must pick
up all parcels by visiting every location that has a parcel and deliver
them by visiting every location to which a parcel is addressed, but only


after picking up the parcel.
What is the dumbest strategy that could possibly work? The robot
could just walk in a random direction every turn. That means, with
great likelihood, it will eventually run into all parcels and then also at
some point reach the place where they should be delivered.
Here’s what that could look like:
function randomPick(array) {
let choice = Math.floor(Math.random() * array.length);
return array[choice];
}

```
function randomRobot(state) {
return {direction: randomPick(roadGraph[state.place])};
}
```
Remember thatMath.random()returns a number between 0 and 1—but
always below 1. Multiplying such a number by the length of an array
and then applying Math.floor to it gives us a random index for the
array.
Since this robot does not need to remember anything, it ignores its
second argument (remember that JavaScript functions can be called
with extra arguments without ill effects) and omits thememoryproperty
in its returned object.
To put this sophisticated robot to work, we’ll first need a way to
create a new state with some parcels. A static method (written here by
directly adding a property to the constructor) is a good place to put
that functionality.


```
VillageState.random = function(parcelCount = 5) {
let parcels = [];
for (let i = 0; i < parcelCount; i++) {
let address = randomPick(Object.keys(roadGraph));
let place;
do {
place = randomPick(Object.keys(roadGraph));
} while (place == address);
parcels.push({place, address});
}
return new VillageState("Post Office", parcels);
};
```
We don’t want any parcels to be sent from the same place that they
are addressed to. For this reason, thedoloop keeps picking new places
when it gets one that’s equal to the address.
Let’s start up a virtual world.
runRobot(VillageState.random(), randomRobot);
// → Moved to Marketplace
// → Moved to Town Hall
// →...
// → Done in 63 turns

It takes the robot a lot of turns to deliver the parcels because it isn’t
planning ahead very well. We’ll address that soon.


### Themailtruck'sroute

We should be able to do a lot better than the random robot. An easy
improvement would be to take a hint from the way real-world mail
delivery works. If we find a route that passes all places in the village,
the robot could run that route twice, at which point it is guaranteed to
be done. Here is one such route (starting from the post oﬀice):

```
const mailRoute = [
"Alice's House", "Cabin", "Alice's House", "Bob's House",
"Town Hall", "Daria's House", "Ernie's House",
"Grete's House", "Shop", "Grete's House", "Farm",
"Marketplace", "Post Office"
];
```
To implement the route-following robot, we’ll need to make use of robot
memory. The robot keeps the rest of its route in its memory and drops
the first element every turn.

```
function routeRobot(state, memory) {
if (memory.length == 0) {
memory = mailRoute;
}
return {direction: memory[0], memory: memory.slice(1)};
}
```
This robot is a lot faster already. It’ll take a maximum of 26 turns
(twice the 13-step route) but usually less.


### Pathfinding.

Still, I wouldn’t really call blindly following a fixed route intelligent be-
havior. The robot could work more eﬀiciently if it adjusted its behavior
to the actual work that needs to be done.
To do that, it has to be able to deliberately move toward a given
parcel or toward the location where a parcel has to be delivered. Doing
that, even when the goal is more than one move away, will require some
kind of route-finding function.
The problem of finding a route through a graph is a typical _search
problem_. We can tell whether a given solution (a route) is valid, but
we can’t directly compute the solution the way we could for 2 + 2.
Instead, we have to keep creating potential solutions until we find one
that works.
The number of possible routes through a graph is infinite. But when
searching for a route from _A_ to _B_ , we are interested only in the ones
that start at _A_. We also don’t care about routes that visit the same
place twice—those are definitely not the most eﬀicient route anywhere.
So that cuts down on the number of routes that the route finder has to
consider.
In fact, since we are mostly interested in the _shortest_ route, we want
to make sure we look at short routes before we look at longer ones.
A good approach would be to “grow” routes from the starting point,
exploring every reachable place that hasn’t been visited yet until a
route reaches the goal. That way, we’ll explore only routes that are
potentially interesting, and we know that the first route we find is the
shortest route (or one of the shortest routes, if there are more than


one).
Here is a function that does this:
function findRoute(graph, from, to) {
let work = [{at: from, route: []}];
for (let i = 0; i < work.length; i++) {
let {at, route} = work[i];
for (let place of graph[at]) {
if (place == to) return route.concat(place);
if (!work.some(w => w.at == place)) {
work.push({at: place, route: route.concat(place)});
}
}
}
}

The exploring has to be done in the right order—the places that were
reached first have to be explored first. We can’t immediately explore a
place as soon as we reach it because that would mean places reached
_from there_ would also be explored immediately, and so on, even though
there may be other, shorter paths that haven’t yet been explored.
Therefore, the function keeps a _work list_. This is an array of places
that should be explored next, along with the route that got us there.
It starts with just the start position and an empty route.
The search then operates by taking the next item in the list and
exploring that, which means it looks at all roads going from that place.
If one of them is the goal, a finished route can be returned. Otherwise,
if we haven’t looked at this place before, a new item is added to the
list. If we have looked at it before, since we are looking at short routes


first, we’ve found either a longer route to that place or one precisely as
long as the existing one, and we don’t need to explore it.
You can visualize this as a web of known routes crawling out from
the start location, growing evenly on all sides (but never tangling back
into itself). As soon as the first thread reaches the goal location, that
thread is traced back to the start, giving us our route.
Our code doesn’t handle the situation where there are no more work
items on the work list because we know that our graph is _connected_ ,
meaning that every location can be reached from all other locations.
We’ll always be able to find a route between two points, and the search
can’t fail.

```
function goalOrientedRobot({place, parcels}, route) {
if (route.length == 0) {
let parcel = parcels[0];
if (parcel.place != place) {
route = findRoute(roadGraph, place, parcel.place);
} else {
route = findRoute(roadGraph, place, parcel.address);
}
}
return {direction: route[0], memory: route.slice(1)};
}
```
This robot uses its memory value as a list of directions to move in, just
like the route-following robot. Whenever that list is empty, it has to
figure out what to do next. It takes the first undelivered parcel in the
set and, if that parcel hasn’t been picked up yet, plots a route toward
it. If the parcel _has_ been picked up, it still needs to be delivered, so the


robot creates a route toward the delivery address instead.
This robot usually finishes the task of delivering 5 parcels in about
16 turns. That’s slightly better thanrouteRobotbut still definitely not
optimal. We’ll continue refining it in the exercises.

### Exercises

**Measuringarobot**

It’s hard to objectively compare robots by just letting them solve a few
scenarios. Maybe one robot just happened to get easier tasks or the
kind of tasks that it is good at, whereas the other didn’t.
Write a functioncompareRobotsthat takes two robots (and their start-
ing memory). It should generate 100 tasks and let both of the robots
solve each of these tasks. When done, it should output the average
number of steps each robot took per task.
For the sake of fairness, make sure you give each task to both robots,
rather than generating different tasks per robot.

**Robotefficiency**

Can you write a robot that finishes the delivery task faster thangoalOrientedRobot
? If you observe that robot’s behavior, what obviously stupid things
does it do? How could those be improved?
If you solved the previous exercise, you might want to use your
compareRobotsfunction to verify whether you improved the robot.


**Persistentgroup**

Most data structures provided in a standard JavaScript environment
aren’t very well suited for persistent use. Arrays havesliceandconcat
methods, which allow us to easily create new arrays without damaging
the old one. ButSet, for example, has no methods for creating a new
set with an item added or removed.
Write a new class PGroup, similar to the Group class fromChapter
6 , which stores a set of values. LikeGroup, it has add, delete, and
has methods. Itsadd method, however, should return a _new_ PGroup
instance with the given member added and leave the old one unchanged.
Similarly,deleteshould create a new instance without a given member.
The class should work for values of any type, not just strings. It does
_not_ have to be eﬀicient when used with large numbers of values.
The constructor shouldn’t be part of the class’s interface (though
you’ll definitely want to use it internally). Instead, there is an empty
instance,PGroup.empty, that can be used as a starting value.
Why do you need only onePGroup.emptyvalue rather than having a
function that creates a new, empty map every time?


```
“Debugging is twice as hard as writing the code in the first
place. Therefore, if you write the code as cleverly as possible,
you are, by definition, not smart enough to debug it.”
—Brian Kernighan and P.J. Plauger, The Elements of
Programming Style
```
**Chapter8**

## BugsandErrors

Flaws in computer programs are usually called _bugs_. It makes program-
mers feel good to imagine them as little things that just happen to crawl
into our work. In reality, of course, we put them there ourselves.
If a program is crystallized thought, we can roughly categorize bugs
into those caused by the thoughts being confused and those caused by
mistakes introduced while converting a thought to code. The former
type is generally harder to diagnose and fix than the latter.

### Language

Many mistakes could be pointed out to us automatically by the com-
puter if it knew enough about what we’re trying to do. But here,
JavaScript’s looseness is a hindrance. Its concept of bindings and prop-
erties is vague enough that it will rarely catch typos before actually
running the program. Even then, it allows you to do some clearly non-
sensical things without complaint, such as computingtrue * "monkey".
There are some things that JavaScript does complain about. Writing


a program that does not follow the language’s grammar will imme-
diately make the computer complain. Other things, such as calling
something that’s not a function or looking up a property on an unde-
fined value, will cause an error to be reported when the program tries
to perform the action.
Often, however, your nonsense computation will merely produceNaN
(not a number) or an undefined value, while the program happily
continues, convinced that it’s doing something meaningful. The mistake
will manifest itself only later, after the bogus value has traveled through
several functions. It might not trigger an error at all, but silently cause
the program’s output to be wrong. Finding the source of such problems
can be diﬀicult.
The process of finding mistakes—bugs—in programs is called _debug-
ging_.

### Strict mode.

JavaScript can be made a _little_ stricter by enabling _strict mode_. This
can done by putting the string "use strict"at the top of a file or a
function body. Here’s an example:

```
function canYouSpotTheProblem() {
"use strict";
for (counter = 0; counter < 10; counter++) {
console.log("Happy happy");
}
}
```

```
canYouSpotTheProblem();
// → ReferenceError: counter is not defined
```
Code inside classes and modules (which we will discuss inChapter 10) is
automatically strict. The old nonstrict behavior still exists only because
some old code might depend on it, and the language designers work hard
to avoid breaking any existing programs.
Normally, when you forget to putletin front of your binding, as with
counterin the example, JavaScript quietly creates a global binding and
uses that. In strict mode, an error is reported instead. This is very
helpful. It should be noted, though, that this doesn’t work when the
binding in question already exists somewhere in scope. In that case,
the loop will still quietly overwrite the value of the binding.
Another change in strict mode is that thethisbinding holds the value
undefinedin functions that are not called as methods. When making
such a call outside of strict mode,thisrefers to the global scope object,
which is an object whose properties are the global bindings. So if you
accidentally call a method or constructor incorrectly in strict mode,
JavaScript will produce an error as soon as it tries to read something
fromthis, rather than happily writing to the global scope.
For example, consider the following code, which calls a constructor
function without thenew keyword so that its thiswill _not_ refer to a
newly constructed object:

```
function Person(name) { this.name = name; }
let ferdinand = Person("Ferdinand"); // oops
console.log(name);
```

```
// → Ferdinand
```
The bogus call toPersonsucceeded, but returned an undefined value and
created the global bindingname. In strict mode, the result is different.

```
"use strict";
function Person(name) { this.name = name; }
let ferdinand = Person("Ferdinand"); // forgot new
// → TypeError: Cannot set property 'name' of undefined
```
We are immediately told that something is wrong. This is helpful.
Fortunately, constructors created with theclassnotation will always
complain if they are called withoutnew, making this less of a problem
even in nonstrict mode.
Strict mode does a few more things. It disallows giving a function
multiple parameters with the same name and removes certain problem-
atic language features entirely (such as thewithstatement, which is so
wrong it is not further discussed in this book).
In short, putting"use strict"at the top of your program rarely hurts
and might help you spot a problem.

### Types

Some languages want to know the types of all your bindings and ex-
pressions before even running a program. They will tell you right away
when a type is used in an inconsistent way. JavaScript considers types
only when actually running the program, and even there often tries to
implicitly convert values to the type it expects, so it’s not much help.


Still, types provide a useful framework for talking about programs.
A lot of mistakes come from being confused about the kind of value
that goes into or comes out of a function. If you have that information
written down, you’re less likely to get confused.
You could add a comment like the following before the findRoute
function from the previous chapter to describe its type:

```
// (graph: Object, from: string, to: string) => string[]
function findRoute(graph, from, to) {
// ...
}
```
There are a number of different conventions for annotating JavaScript
programs with types.
One thing about types is that they need to introduce their own com-
plexity to be able to describe enough code to be useful. What do you
think would be the type of therandomPickfunction that returns a ran-
dom element from an array? You’d need to introduce a _type variable_ ,
_T_ , which can stand in for any type, so that you can giverandomPicka
type like(T[])→T(function from an array of _T_ s to a _T_ ).
When the types of a program are known, it is possible for the com-
puter to _check_ them for you, pointing out mistakes before the program
is run. There are several JavaScript dialects that add types to the lan-
guage and check them. The most popular one is calledTypeScript. If
you are interested in adding more rigor to your programs, I recommend
you give it a try.
In this book, we will continue using raw, dangerous, untyped JavaScript
code.


### Testing

If the language is not going to do much to help us find mistakes, we’ll
have to find them the hard way: by running the program and seeing
whether it does the right thing.
Doing this by hand, again and again, is a really bad idea. Not only
is it annoying but it also tends to be ineffective, since it takes too much
time to exhaustively test everything every time you make a change.
Computers are good at repetitive tasks, and testing is the ideal repet-
itive task. Automated testing is the process of writing a program that
tests another program. Writing tests is a bit more work than testing
manually, but once you’ve done it, you gain a kind of superpower: it
takes you only a few seconds to verify that your program still behaves
properly in all the situations you wrote tests for. When you break some-
thing, you’ll immediately notice rather than randomly running into it
at some later time.
Tests usually take the form of little labeled programs that verify
some aspect of your code. For example, a set of tests for the (standard,
probably already tested by someone else) toUpperCase method might
look like this:

```
function test(label, body) {
if (!body()) console.log(`Failed: ${label}`);
}
```
```
test("convert Latin text to uppercase", () => {
return "hello".toUpperCase() == "HELLO";
});
```

```
test("convert Greek text to uppercase", () => {
return "Χαίρετε".toUpperCase() == "ΧΑΊΡΕΤΕ";
});
test("don't convert case-less characters", () => {
return "مرحبا".toUpperCase() == "مرحبا";
});
```
Writing tests like this tends to produce rather repetitive, awkward code.
Fortunately, there exist pieces of software that help you build and run
collections of tests ( _test suites_ ) by providing a language (in the form
of functions and methods) suited to expressing tests and by outputting
informative information when a test fails. These are usually called _test
runners_.
Some code is easier to test than other code. Generally, the more
external objects that the code interacts with, the harder it is to set up
the context in which to test it. The style of programming shown in
theprevious chapter, which uses self-contained persistent values rather
than changing objects, tends to be easy to test.

### Debugging

Once you notice there is something wrong with your program because
it misbehaves or produces errors, the next step is to figure out _what_ the
problem is.
Sometimes it is obvious. The error message will point at a specific
line of your program, and if you look at the error description and that
line of code, you can often see the problem.


But not always. Sometimes the line that triggered the problem is
simply the first place where a flaky value produced elsewhere gets used
in an invalid way. If you have been solving the exercises in earlier
chapters, you will probably have already experienced such situations.
The following example program tries to convert a whole number to a
string in a given base (decimal, binary, and so on) by repeatedly picking
out the last digit and then dividing the number to get rid of this digit.
But the strange output that it currently produces suggests that it has
a bug.

```
function numberToString(n, base = 10) {
let result = "", sign = "";
if (n < 0) {
sign = "-";
n = -n;
}
do {
result = String(n % base) + result;
n /= base;
} while (n > 0);
return sign + result;
}
console.log(numberToString(13, 10));
// → 1.5e-3231.3e-3221.3e-3211.3e-3201.3e-3191.3e...-3181.3
```
Even if you see the problem already, pretend for a moment that you
don’t. We know that our program is malfunctioning, and we want to
find out why.
This is where you must resist the urge to start making random


changes to the code to see whether that makes it better. Instead, _think_.
Analyze what is happening and come up with a theory of why it might
be happening. Then make additional observations to test this theory—
or, if you don’t yet have a theory, make additional observations to help
you come up with one.
Putting a few strategicconsole.logcalls into the program is a good
way to get additional information about what the program is doing. In
this case, we wantnto take the values 13 , 1 , and then 0. Let’s write
out its value at the start of the loop.

```
13
1.3
0.13
0.013...
```
```
1.5e-323
```
_Right_. Dividing 13 by 10 does not produce a whole number. Instead of
n /= base, what we actually want isn = Math.floor(n / base)so that
the number is properly “shifted” to the right.
An alternative to usingconsole.logto peek into the program’s be-
havior is to use the _debugger_ capabilities of your browser. Browsers
come with the ability to set a _breakpoint_ on a specific line of your code.
When the execution of the program reaches a line with a breakpoint, it
is paused, and you can inspect the values of bindings at that point. I
won’t go into details, as debuggers differ from browser to browser, but
look in your browser’s developer tools or search the web for instructions.
Another way to set a breakpoint is to include adebuggerstatement


(consisting simply of that keyword) in your program. If the developer
tools of your browser are active, the program will pause whenever it
reaches such a statement.

### Error propagation

Not all problems can be prevented by the programmer, unfortunately.
If your program communicates with the outside world in any way, it is
possible to get malformed input, to become overloaded with work, or
to have the network fail.
If you’re programming only for yourself, you can afford to just ignore
such problems until they occur. But if you build something that is going
to be used by anybody else, you usually want the program to do better
than just crash. Sometimes the right thing to do is take the bad input
in stride and continue running. In other cases, it is better to report
to the user what went wrong and then give up. In either situation the
program has to actively do something in response to the problem.
Say you have a functionpromptNumberthat asks the user for a number
and returns it. What should it return if the user inputs “orange”?
One option is to make it return a special value. Common choices for
such values arenull,undefined, or-1.

```
function promptNumber(question) {
let result = Number(prompt(question));
if (Number.isNaN(result)) return null;
else return result;
}
```

```
console.log(promptNumber("How many trees do you see?"));
```
Now any code that calls promptNumbermust check whether an actual
number was read and, failing that, must somehow recover—maybe by
asking again or by filling in a default value. Or it could again return
a special value to _its_ caller to indicate that it failed to do what it was
asked.
In many situations, mostly when errors are common and the caller
should be explicitly taking them into account, returning a special value
is a good way to indicate an error. It does, however, have its downsides.
First, what if the function can already return every possible kind of
value? In such a function, you’ll have to do something like wrap the
result in an object to be able to distinguish success from failure, the
way thenextmethod on the iterator interface does.

```
function lastElement(array) {
if (array.length == 0) {
return {failed: true};
} else {
return {value: array[array.length - 1]};
}
}
```
The second issue with returning special values is that it can lead to
awkward code. If a piece of code callspromptNumber10 times, it has to
check 10 times whethernull was returned. If its response to finding
nullis to simply returnnullitself, callers of the function will in turn
have to check for it, and so on.


### Exceptions

When a function cannot proceed normally, what we would often _like_
to do is just stop what we are doing and immediately jump to a place
that knows how to handle the problem. This is what _exception handling_
does.
Exceptions are a mechanism that makes it possible for code that
runs into a problem to _raise_ (or _throw_ ) an exception. An exception can
be any value. Raising one somewhat resembles a super-charged return
from a function: it jumps out of not just the current function but also
its callers, all the way down to the first call that started the current
execution. This is called _unwinding the stack_. You may remember the
stack of function calls mentioned inChapter 3. An exception zooms
down this stack, throwing away all the call contexts it encounters.
If exceptions always zoomed right down to the bottom of the stack,
they would not be of much use. They’d just provide a novel way to
blow up your program. Their power lies in the fact that you can set
“obstacles” along the stack to _catch_ the exception as it is zooming down.
Once you’ve caught an exception, you can do something with it to
address the problem and then continue to run the program.
Here’s an example:
function promptDirection(question) {
let result = prompt(question);
if (result.toLowerCase() == "left") return "L";
if (result.toLowerCase() == "right") return "R";
throw new Error("Invalid direction: " + result);
}


```
function look() {
if (promptDirection("Which way?") == "L") {
return "a house";
} else {
return "two angry bears";
}
}
```
```
try {
console.log("You see", look());
} catch (error) {
console.log("Something went wrong: " + error);
}
```
Thethrowkeyword is used to raise an exception. Catching one is done
by wrapping a piece of code in atry block, followed by the keyword
catch. When the code in thetryblock causes an exception to be raised,
thecatchblock is evaluated, with the name in parentheses bound to
the exception value. After thecatchblock finishes—or if thetryblock
finishes without problems—the program proceeds beneath the entire
try/catchstatement.
In this case, we used theErrorconstructor to create our exception
value. This is a standard JavaScript constructor that creates an object
with a message property. Instances of Error also gather information
about the call stack that existed when the exception was created, a so-
called _stack trace_. This information is stored in thestackproperty and
can be helpful when trying to debug a problem: it tells us the function
where the problem occurred and which functions made the failing call.


Note that thelookfunction completely ignores the possibility that
promptDirectionmight go wrong. This is the big advantage of excep-
tions: error-handling code is necessary only at the point where the error
occurs and at the point where it is handled. The functions in between
can forget all about it.
Well, almost...

### Cleaning up after exceptions.

The effect of an exception is another kind of control flow. Every action
that might cause an exception, which is pretty much every function call
and property access, might cause control to suddenly leave your code.
This means when code has several side effects, even if its “regular”
control flow looks like they’ll always all happen, an exception might
prevent some of them from taking place.
Here is some really bad banking code:
const accounts = {
a: 100,
b: 0,
c: 20
};

```
function getAccount() {
let accountName = prompt("Enter an account name");
if (!Object.hasOwn(accounts, accountName)) {
throw new Error(`No such account: ${accountName}`);
}
```

```
return accountName;
}
```
```
function transfer(from, amount) {
if (accounts[from] < amount) return;
accounts[from] -= amount;
accounts[getAccount()] += amount;
}
```
Thetransferfunction transfers a sum of money from a given account
to another, asking for the name of the other account in the process. If
given an invalid account name,getAccountthrows an exception.
Buttransfer _first_ removes the money from the account and _then_ calls
getAccountbefore it adds it to another account. If it is broken off by an
exception at that point, it’ll just make the money disappear.
That code could have been written a little more intelligently, for ex-
ample by callinggetAccountbefore it starts moving money around. But
often problems like this occur in more subtle ways. Even functions that
don’t look like they will throw an exception might do so in exceptional
circumstances or when they contain a programmer mistake.
One way to address this is to use fewer side effects. Again, a pro-
gramming style that computes new values instead of changing existing
data helps. If a piece of code stops running in the middle of creating a
new value, no existing data structures were damaged, making it easier
to recover.
Since that isn’t always practical,trystatements have another feature:
they may be followed by afinallyblock either instead of or in addition
to acatchblock. Afinallyblock says “no matter _what_ happens, run


this code after trying to run the code in thetryblock.”

```
function transfer(from, amount) {
if (accounts[from] < amount) return;
let progress = 0;
try {
accounts[from] -= amount;
progress = 1;
accounts[getAccount()] += amount;
progress = 2;
} finally {
if (progress == 1) {
accounts[from] += amount;
}
}
}
```
This version of the function tracks its progress, and if, when leaving, it
notices that it was aborted at a point where it had created an inconsis-
tent program state, it repairs the damage it did.
Note that even though thefinallycode is run when an exception is
thrown in thetryblock, it does not interfere with the exception. After
thefinallyblock runs, the stack continues unwinding.
Writing programs that operate reliably even when exceptions pop up
in unexpected places is hard. Many people simply don’t bother, and
because exceptions are typically reserved for exceptional circumstances,
the problem may occur so rarely that it is never even noticed. Whether
that is a good thing or a really bad thing depends on how much damage
the software will do when it fails.


### Selective catching

When an exception makes it all the way to the bottom of the stack
without being caught, it gets handled by the environment. What
this means differs between environments. In browsers, a description
of the error typically gets written to the JavaScript console (reach-
able through the browser’s Tools or Developer menu). Node.js, the
browserless JavaScript environment we will discuss inChapter 20, is
more careful about data corruption. It aborts the whole process when
an unhandled exception occurs.
For programmer mistakes, just letting the error go through is often
the best you can do. An unhandled exception is a reasonable way to
signal a broken program, and the JavaScript console will, on modern
browsers, provide you with some information about which function calls
were on the stack when the problem occurred.
For problems that are _expected_ to happen during routine use, crashing
with an unhandled exception is a terrible strategy.
Invalid uses of the language, such as referencing a nonexistent bind-
ing, looking up a property onnull, or calling something that’s not a
function, will also result in exceptions being raised. Such exceptions
can also be caught.
When acatchbody is entered, all we know is that _something_ in our
trybody caused an exception. But we don’t know _what_ did or _which_
exception it caused.
JavaScript (in a rather glaring omission) doesn’t provide direct sup-
port for selectively catching exceptions: either you catch them all or
you don’t catch any. This makes it tempting to _assume_ that the ex-


ception you get is the one you were thinking about when you wrote the
catchblock.
But it might not be. Some other assumption might be violated, or
you might have introduced a bug that is causing an exception. Here
is an example that _attempts_ to keep on callingpromptDirectionuntil it
gets a valid answer:

```
for (;;) {
try {
let dir = promtDirection("Where?"); // ← typo!
console.log("You chose ", dir);
break;
} catch (e) {
console.log("Not a valid direction. Try again.");
}
}
```
The for (;;) construct is a way to intentionally create a loop that
doesn’t terminate on its own. We break out of the loop only when a
valid direction is given. Unfortunately, we misspelledpromptDirection,
which will result in an “undefined variable” error. Because thecatch
block completely ignores its exception value (e), assuming it knows
what the problem is, it wrongly treats the binding error as indicating
bad input. Not only does this cause an infinite loop but it also “buries”
the useful error message about the misspelled binding.
As a general rule, don’t blanket-catch exceptions unless it is for the
purpose of “routing” them somewhere—for example, over the network
to tell another system that our program crashed. And even then, think


carefully about how you might be hiding information.
We want to catch a _specific_ kind of exception. We can do this by
checking in thecatchblock whether the exception we got is the one we
are interested in, and if not, rethrow it. But how do we recognize an
exception?
We could compare its message property against the error message
we happen to expect. But that’s a shaky way to write code—we’d be
using information that’s intended for human consumption (the message)
to make a programmatic decision. As soon as someone changes (or
translates) the message, the code will stop working.
Rather, let’s define a new type of error and useinstanceofto identify
it.

```
class InputError extends Error {}
```
```
function promptDirection(question) {
let result = prompt(question);
if (result.toLowerCase() == "left") return "L";
if (result.toLowerCase() == "right") return "R";
throw new InputError("Invalid direction: " + result);
}
```
The new error class extendsError. It doesn’t define its own constructor,
which means that it inherits the Error constructor, which expects a
string message as argument. In fact, it doesn’t define anything at all—
the class is empty.InputErrorobjects behave likeErrorobjects, except
that they have a different class by which we can recognize them.
Now the loop can catch these more carefully.


```
for (;;) {
try {
let dir = promptDirection("Where?");
console.log("You chose ", dir);
break;
} catch (e) {
if (e instanceof InputError) {
console.log("Not a valid direction. Try again.");
} else {
throw e;
}
}
}
```
This will catch only instances ofInputErrorand let unrelated exceptions
through. If you reintroduce the typo, the undefined binding error will
be properly reported.

### Assertions

_Assertions_ are checks inside a program that verify that something is the
way it is supposed to be. They are used not to handle situations that
can come up in normal operation but to find programmer mistakes.
If, for example,firstElementis described as a function that should
never be called on empty arrays, we might write it like this:

```
function firstElement(array) {
if (array.length == 0) {
throw new Error("firstElement called with []");
```

```
}
return array[0];
}
```
Now, instead of silently returning undefined (which you get when read-
ing an array property that does not exist), this will loudly blow up
your program as soon as you misuse it. This makes it less likely for
such mistakes to go unnoticed and easier to find their cause when they
occur.
I do not recommend trying to write assertions for every possible kind
of bad input. That’d be a lot of work and would lead to very noisy
code. You’ll want to reserve them for mistakes that are easy to make
(or that you find yourself making).

### Summary

An important part of programming is finding, diagnosing, and fixing
bugs. Problems can become easier to notice if you have an automated
test suite or add assertions to your programs.
Problems caused by factors outside the program’s control should usu-
ally be actively planned for. Sometimes, when the problem can be
handled locally, special return values are a good way to track them.
Otherwise, exceptions may be preferable.
Throwing an exception causes the call stack to be unwound until the
next enclosing try/catchblock or until the bottom of the stack. The
exception value will be given to thecatchblock that catches it, which
should verify that it is actually the expected kind of exception and then


do something with it. To help address the unpredictable control flow
caused by exceptions,finallyblocks can be used to ensure that a piece
of code _always_ runs when a block finishes.

### Exercises

**Retry**

Say you have a functionprimitiveMultiplythat in 20 percent of cases
multiplies two numbers and in the other 80 percent of cases raises an ex-
ception of typeMultiplicatorUnitFailure. Write a function that wraps
this clunky function and just keeps trying until a call succeeds, after
which it returns the result.
Make sure you handle only the exceptions you are trying to handle.

**Thelockedbox**

Consider the following (rather contrived) object:

```
const box = new class {
locked = true;
#content = [];
```
```
unlock() { this.locked = false; }
lock() { this.locked = true; }
get content() {
if (this.locked) throw new Error("Locked!");
return this.#content;
}
```

```
};
```
It is a box with a lock. There is an array in the box, but you can get
at it only when the box is unlocked.
Write a function calledwithBoxUnlockedthat takes a function value as
argument, unlocks the box, runs the function, and then ensures that the
box is locked again before returning, regardless of whether the argument
function returned normally or threw an exception.
For extra points, make sure that if you callwithBoxUnlockedwhen the
box is already unlocked, the box stays unlocked.


```
“Some people, when confronted with a problem, think ‘I know,
I’ll use regular expressions.’ Now they have two problems.”
—Jamie Zawinski
```
**Chapter9**

## RegularExpressions

Programming tools and techniques survive and spread in a chaotic,
evolutionary way. It’s not always the best or most brilliant ones that
win, but rather the ones that function well enough within the right
niche or that happen to be integrated with another successful piece of
technology.
In this chapter, I will discuss one such tool, _regular expressions_. Reg-
ular expressions are a way to describe patterns in string data. They
form a small, separate language that is part of JavaScript and many
other languages and systems.
Regular expressions are both terribly awkward and extremely useful.
Their syntax is cryptic and the programming interface JavaScript pro-
vides for them is clumsy. But they are a powerful tool for inspecting
and processing strings. Properly understanding regular expressions will
make you a more effective programmer.


### Creating a regular expression

A regular expression is a type of object. It can be either constructed
with theRegExpconstructor or written as a literal value by enclosing a
pattern in forward slash (/) characters.

```
let re1 = new RegExp("abc");
let re2 = /abc/;
```
Both of those regular expression objects represent the same pattern: an
_a_ character followed by a _b_ followed by a _c_.
When using theRegExpconstructor, the pattern is written as a normal
string, so the usual rules apply for backslashes.
The second notation, where the pattern appears between slash char-
acters, treats backslashes somewhat differently. First, since a forward
slash ends the pattern, we need to put a backslash before any forward
slash that we want to be _part_ of the pattern. In addition, backslashes
that aren’t part of special character codes (like\n) will be _preserved_ ,
rather than ignored as they are in strings, and change the meaning of
the pattern. Some characters, such as question marks and plus signs,
have special meanings in regular expressions and must be preceded by
a backslash if they are meant to represent the character itself.

```
let aPlus = /A\+/;
```

### Testing for matches

Regular expression objects have a number of methods. The simplest
one istest. If you pass it a string, it will return a Boolean telling you
whether the string contains a match of the pattern in the expression.

```
console.log(/abc/.test("abcde"));
// → true
console.log(/abc/.test("abxde"));
// → false
```
A regular expression consisting of only nonspecial characters simply
represents that sequence of characters. If _abc_ occurs anywhere in the
string we are testing against (not just at the start), test will return
true.

### Sets of characters

Finding out whether a string contains _abc_ could just as well be done
with a call toindexOf. Regular expressions are useful because they allow
us to describe more complicated patterns.
Say we want to match any number. In a regular expression, putting
a set of characters between square brackets makes that part of the
expression match any of the characters between the brackets.
Both of the following expressions match all strings that contain a
digit:

```
console.log(/[0123456789]/.test("in 1992"));
```

```
// → true
console.log(/[0-9]/.test("in 1992"));
// → true
```
Within square brackets, a hyphen (-) between two characters can be
used to indicate a range of characters, where the ordering is determined
by the character’s Unicode number. Characters 0 to 9 sit right next to
each other in this ordering (codes 48 to 57), so[0-9]covers all of them
and matches any digit.
A number of common character groups have their own built-in short-
cuts. Digits are one of them:\dmeans the same thing as[0-9].
\d Any digit character
\w An alphanumeric character (“word character”)
\s Any whitespace character (space, tab, newline, and similar)
\D A character that is _not_ a digit
\W A nonalphanumeric character
\S A nonwhitespace character

. Any character except for newline
    You could match a date and time format like 01-30-2003 15:20 with
the following expression:

```
let dateTime = /\d\d-\d\d-\d\d\d\d \d\d:\d\d/;
console.log(dateTime.test("01-30-2003 15:20"));
// → true
console.log(dateTime.test("30-jan-2003 15:20"));
// → false
```
That regular expression looks completely awful, doesn’t it? Half of it is
backslashes, producing a background noise that makes it hard to spot


the actual pattern expressed. We’ll see a slightly improved version of
this expressionlater.
These backslash codes can also be used inside square brackets. For
example,[\d.]means any digit or a period character. The period itself,
between square brackets, loses its special meaning. The same goes for
other special characters, such as the plus sign (+).
To _invert_ a set of characters—that is, to express that you want to
match any character _except_ the ones in the set—you can write a caret
(^) character after the opening bracket.

```
let nonBinary = /[^01]/;
console.log(nonBinary.test("1100100010100110"));
// → false
console.log(nonBinary.test("0111010112101001"));
// → true
```
### International characters.

Because of JavaScript’s initial simplistic implementation and the fact
that this simplistic approach was later set in stone as standard behav-
ior, JavaScript’s regular expressions are rather dumb about characters
that do not appear in the English language. For example, as far as
JavaScript’s regular expressions are concerned, a “word character” is
only one of the 26 characters in the Latin alphabet (uppercase or low-
ercase), decimal digits, and, for some reason, the underscore character.
Things like _é_ or _ß_ , which most definitely are word characters, will not
match\w(and _will_ match uppercase\W, the nonword category).


By a strange historical accident,\s(whitespace) does not have this
problem and matches all characters that the Unicode standard con-
siders whitespace, including things like the nonbreaking space and the
Mongolian vowel separator.
It is possible to use\pin a regular expression to match all characters
to which the Unicode standard assigns a given property. This allows
us to match things like letters in a more cosmopolitan way. However,
again due to compatibility with the original language standards, those
are recognized only when you put aucharacter (for Unicode) after the
regular expression.
\p{L} Any letter
\p{N} Any numeric character
\p{P} Any punctuation character
\P{L} Any nonletter (uppercase P inverts)
\p{Script=Hangul} Any character from the given script (seeChapter 5)
Using\wfor text processing that may need to handle non-English text
(or even English text with borrowed words like “cliché”) is a liability,
since it won’t treat characters like “é” as letters. Though they tend to
be a bit more verbose,\pproperty groups are more robust.

```
console.log(/\p{L}/u.test("α"));
// → true
console.log(/\p{L}/u.test("!"));
// → false
console.log(/\p{Script=Greek}/u.test("α"));
// → true
console.log(/\p{Script=Arabic}/u.test("α"));
// → false
```

On the other hand, if you are matching numbers in order to do some-
thing with them, you often do want\dfor digits, since converting ar-
bitrary numeric characters into a JavaScript number is not something
that a function likeNumbercan do for you.

### Repeating parts of a pattern.

We now know how to match a single digit. What if we want to match
a whole number—a sequence of one or more digits?
When you put a plus sign (+) after something in a regular expression,
it indicates that the element may be repeated more than once. Thus,
/\d+/matches one or more digit characters.

```
console.log(/'\d+'/.test("'123'"));
// → true
console.log(/'\d+'/.test("''"));
// → false
console.log(/'\d*'/.test("'123'"));
// → true
console.log(/'\d*'/.test("''"));
// → true
```
The star (*) has a similar meaning but also allows the pattern to match
zero times. Something with a star after it never prevents a pattern from
matching—it’ll just match zero instances if it can’t find any suitable
text to match.
A question mark (?) makes a part of a pattern _optional_ , meaning
it may occur zero times or one time. In the following example, the _u_


character is allowed to occur, but the pattern also matches when it is
missing:

```
let neighbor = /neighbou?r/;
console.log(neighbor.test("neighbour"));
// → true
console.log(neighbor.test("neighbor"));
// → true
```
To indicate that a pattern should occur a precise number of times, use
braces. Putting{4}after an element, for example, requires it to occur
exactly four times. It is also possible to specify a range this way:{2,4}
means the element must occur at least twice and at most four times.
Here is another version of the date and time pattern that allows both
single- and double-digit days, months, and hours. It is also slightly
easier to decipher.

```
let dateTime = /\d{1,2}-\d{1,2}-\d{4} \d{1,2}:\d{2}/;
console.log(dateTime.test("1-30-2003 8:45"));
// → true
```
You can also specify open-ended ranges when using braces by omitting
the number after the comma. For example,{5,} means five or more
times.

### Grouping subexpressions

To use an operator like*or+on more than one element at a time, you
must use parentheses. A part of a regular expression that is enclosed in


parentheses counts as a single element as far as the operators following
it are concerned.

```
let cartoonCrying = /boo+(hoo+)+/i;
console.log(cartoonCrying.test("Boohoooohoohooo"));
// → true
```
The first and second + characters apply only to the secondo inboo
and hoo, respectively. The third +applies to the whole group(hoo+),
matching one or more sequences like that.
Theiat the end of the expression in the example makes this regular
expression case insensitive, allowing it to match the uppercase _B_ in the
input string, even though the pattern is itself all lowercase.

### Matches and groups.

Thetestmethod is the absolute simplest way to match a regular ex-
pression. It tells you only whether it matched and nothing else. Regular
expressions also have anexec(execute) method that will returnnullif
no match was found and return an object with information about the
match otherwise.

```
let match = /\d+/.exec("one two 100");
console.log(match);
// → ["100"]
console.log(match.index);
// → 8
```
An object returned fromexechas anindexproperty that tells us _where_


in the string the successful match begins. Other than that, the object
looks like (and in fact is) an array of strings, whose first element is the
string that was matched. In the previous example, this is the sequence
of digits that we were looking for.
String values have amatchmethod that behaves similarly.
console.log("one two 100".match(/\d+/));
// → ["100"]

When the regular expression contains subexpressions grouped with paren-
theses, the text that matched those groups will also show up in the ar-
ray. The whole match is always the first element. The next element is
the part matched by the first group (the one whose opening parenthesis
comes first in the expression), then the second group, and so on.

```
let quotedText = /'([^']*)'/;
console.log(quotedText.exec("she said 'hello'"));
// → ["'hello'", "hello"]
```
When a group does not end up being matched at all (for example, when
followed by a question mark), its position in the output array will hold
undefined. When a group is matched multiple times (for example, when
followed by a+), only the last match ends up in the array.

```
console.log(/bad(ly)?/.exec("bad"));
// → ["bad", undefined]
console.log(/(\d)+/.exec("123"));
// → ["123", "3"]
```
If you want to use parentheses purely for grouping, without having


them show up in the array of matches, you can put?:after the opening
parenthesis.

```
console.log(/(?:na)+/.exec("banana"));
// → ["nana"]
```
Groups can be useful for extracting parts of a string. If we don’t just
want to verify whether a string contains a date but also extract it and
construct an object that represents it, we can wrap parentheses around
the digit patterns and directly pick the date out of the result ofexec.
But first we’ll take a brief detour to discuss the built-in way to rep-
resent date and time values in JavaScript.

### The Date class

JavaScript has a standardDateclass for representing dates, or rather,
points in time. If you simply create a date object usingnew, you get the
current date and time.

```
console.log(new Date());
// → Fri Feb 02 2024 18:03:06 GMT+0100 (CET)
```
You can also create an object for a specific time.

```
console.log(new Date(2009, 11, 9));
// → Wed Dec 09 2009 00:00:00 GMT+0100 (CET)
console.log(new Date(2009, 11, 9, 12, 59, 59, 999));
// → Wed Dec 09 2009 12:59:59 GMT+0100 (CET)
```
JavaScript uses a convention where month numbers start at zero (so


December is 11), yet day numbers start at one. This is confusing and
silly. Be careful.
The last four arguments (hours, minutes, seconds, and milliseconds)
are optional and taken to be zero when not given.
Timestamps are stored as the number of milliseconds since the start
of 1970, in the UTC time zone. This follows a convention set by “Unix
time”, which was invented around that time. You can use negative
numbers for times before 1970. ThegetTimemethod on a date object
returns this number. It is big, as you can imagine.

```
console.log(new Date(2013, 11, 19).getTime());
// → 1387407600000
console.log(new Date(1387407600000));
// → Thu Dec 19 2013 00:00:00 GMT+0100 (CET)
```
If you give theDate constructor a single argument, that argument is
treated as such a millisecond count. You can get the current millisecond
count by creating a new Date object and callinggetTime on it or by
calling theDate.nowfunction.
Date objects provide methods such asgetFullYear,getMonth,getDate
, getHours, getMinutes, and getSeconds to extract their components.
BesidesgetFullYearthere’s alsogetYear, which gives you the year minus
1900 (such as 98 or 125 ) and is mostly useless.
Putting parentheses around the parts of the expression that we are
interested in, we can now create a date object from a string.

```
function getDate(string) {
let [_, month, day, year] =
/(\d{1,2})-(\d{1,2})-(\d{4})/.exec(string);
```

```
return new Date(year, month - 1, day);
}
console.log(getDate("1-30-2003"));
// → Thu Jan 30 2003 00:00:00 GMT+0100 (CET)
```
The underscore (_) binding is ignored and used only to skip the full
match element in the array returned byexec.

### Boundaries and look-ahead.

Unfortunately,getDatewill also happily extract a date from the string
"100-1-30000". A match may happen anywhere in the string, so in this
case, it’ll just start at the second character and end at the second-to-last
character.
If we want to enforce that the match must span the whole string,
we can add the markers^and$. The caret matches the start of the
input string, whereas the dollar sign matches the end. Thus /^\d+$/
matches a string consisting entirely of one or more digits,/^!/matches
any string that starts with an exclamation mark, and /x^/ does not
match any string (there cannot be anxbefore the start of the string).
There is also a \bmarker that matches _word boundaries_ , positions
that have a word character on one side, and a nonword character on
the other. Unfortunately, these use the same simplistic concept of word
characters as\wand are therefore not very reliable.
Note that these boundary markers don’t match any actual characters.
They just enforce that a given condition holds at the place where it
appears in the pattern.


_Look-ahead_ tests do something similar. They provide a pattern and
will make the match fail if the input doesn’t match that pattern, but
don’t actually move the match position forward. They are written
between(?=and).

```
console.log(/a(?=e)/.exec("braeburn"));
// → ["a"]
console.log(/a(?! )/.exec("a b"));
// → null
```
Theein the first example is necessary to match, but is not part of the
matched string. The (?! ) notation expresses a _negative_ look-ahead.
This matches only if the pattern in the parentheses _doesn’t_ match,
causing the second example to match onlyacharacters that don’t have
a space after them.

### Choice patterns

Say we want to know whether a piece of text contains not only a number
but a number followed by one of the words _pig_ , _cow_ , or _chicken_ , or any
of their plural forms.
We could write three regular expressions and test them in turn, but
there is a nicer way. The pipe character (|) denotes a choice between
the pattern to its left and the pattern to its right. We can use it in
expressions like this:

```
let animalCount = /\d+ (pig|cow|chicken)s?/;
console.log(animalCount.test("15 pigs"));
```

```
// → true
console.log(animalCount.test("15 pugs"));
// → false
```
Parentheses can be used to limit the part of the pattern to which the
pipe operator applies, and you can put multiple such operators next to
each other to express a choice between more than two alternatives.

### The mechanics of matching

Conceptually, when you useexecortest, the regular expression engine
looks for a match in your string by trying to match the expression first
from the start of the string, then from the second character, and so on
until it finds a match or reaches the end of the string. It’ll either return
the first match that can be found or fail to find any match at all.
To do the actual matching, the engine treats a regular expression
something like a flow diagram. This is the diagram for the livestock
expression in the previous example:

```
digit “”
```
```
group #1
```
```
“pig”
```
```
“cow”
```
```
“chicken”
```
```
“s”
```

If we can find a path from the left side of the diagram to the right
side, our expression matches. We keep a current position in the string,
and every time we move through a box, we verify that the part of the
string after our current position matches that box.

### Backtracking

The regular expression/^([01]+b|[\da-f]+h|\d+)$/matches either a bi-
nary number followed by ab, a hexadecimal number (that is, base 16,
with the lettersatofstanding for the digits 10 to 15) followed by an
h, or a regular decimal number with no suﬀix character. This is the
corresponding diagram:

```
Start of line
```
```
group #1
One of:
“ 0 ”
“ 1 ”
```
```
“b”
```
```
One of:
digit
“a” - “f”
```
```
“h”
```
```
digit
```
```
End of line
```

When matching this expression, the top (binary) branch will often
be entered even though the input does not actually contain a binary
number. When matching the string"103", for example, it becomes clear
only at the 3 that we are in the wrong branch. The string _does_ match
the expression, just not the branch we are currently in.
So the matcher _backtracks_. When entering a branch, it remembers
its current position (in this case, at the start of the string, just past
the first boundary box in the diagram) so that it can go back and try
another branch if the current one does not work out. For the string
"103", after encountering the 3 character, the matcher starts trying the
branch for hexadecimal numbers, which fails again because there is no
hafter the number. It then tries the decimal number branch. This one
fits, and a match is reported after all.
The matcher stops as soon as it finds a full match. This means that
if multiple branches could potentially match a string, only the first one
(ordered by where the branches appear in the regular expression) is
used.
Backtracking also happens for repetition operators like + and*. If
you match/^.*x/against"abcxe", the.*part will first try to consume
the whole string. The engine will then realize that it needs an xto
match the pattern. Since there is no x past the end of the string,
the star operator tries to match one character less. But the matcher
doesn’t find anxafterabcxeither, so it backtracks again, matching the
star operator to justabc. _Now_ it finds anxwhere it needs it and reports
a successful match from positions 0 to 4.
It is possible to write regular expressions that will do a _lot_ of back-


tracking. This problem occurs when a pattern can match a piece of
input in many different ways. For example, if we get confused while
writing a binary-number regular expression, we might accidentally write
something like/([01]+)+b/.

```
"b"
```
```
Group #1
```
```
One of:
```
#### "1"

#### "0"

If that tries to match some long series of zeros and ones with no
trailing _b_ character, the matcher first goes through the inner loop until
it runs out of digits. Then it notices there is no _b_ , so it backtracks one
position, goes through the outer loop once, and gives up again, trying
to backtrack out of the inner loop once more. It will continue to try
every possible route through these two loops. This means the amount
of work _doubles_ with each additional character. For even just a few
dozen characters, the resulting match will take practically forever.


### The replace method.

String values have areplacemethod that can be used to replace part
of the string with another string.

```
console.log("papa".replace("p", "m"));
// → mapa
```
The first argument can also be a regular expression, in which case the
first match of the regular expression is replaced. When agoption (for
_global_ ) is added after the regular expression, _all_ matches in the string
will be replaced, not just the first.

```
console.log("Borobudur".replace(/[ou]/, "a"));
// → Barobudur
console.log("Borobudur".replace(/[ou]/g, "a"));
// → Barabadar
```
The real power of using regular expressions withreplacecomes from
the fact that we can refer to matched groups in the replacement string.
For example, say we have a big string containing the names of people,
one name per line, in the formatLastname, Firstname. If we want to
swap these names and remove the comma to get aFirstname Lastname
format, we can use the following code:

```
console.log(
"Liskov, Barbara\nMcCarthy, John\nMilner, Robin"
.replace(/(\p{L}+), (\p{L}+)/gu, "$2 $1"));
// → Barbara Liskov
// John McCarthy
```

```
// Robin Milner
```
The $1 and $2 in the replacement string refer to the parenthesized
groups in the pattern. $1is replaced by the text that matched against
the first group,$2by the second, and so on, up to$9. The whole match
can be referred to with$&.
It is possible to pass a function—rather than a string—as the second
argument toreplace. For each replacement, the function will be called
with the matched groups (as well as the whole match) as arguments,
and its return value will be inserted into the new string.
Here’s an example:
let stock = "1 lemon, 2 cabbages, and 101 eggs";
function minusOne(match, amount, unit) {
amount = Number(amount) - 1;
if (amount == 1) { // only one left, remove the 's'
unit = unit.slice(0, unit.length - 1);
} else if (amount == 0) {
amount = "no";
}
return amount + " " + unit;
}
console.log(stock.replace(/(\d+) (\p{L}+)/gu, minusOne));
// → no lemon, 1 cabbage, and 100 eggs

This code takes a string, finds all occurrences of a number followed by
an alphanumeric word, and returns a string that has one less of every
such quantity.
The(\d+)group ends up as theamountargument to the function, and


the(\p{L}+)group gets bound tounit. The function convertsamount
to a number—which always works, since it matched \d+ earlier—and
makes some adjustments in case there is only one or zero left.

### Greed

We can usereplaceto write a function that removes all comments from
a piece of JavaScript code. Here is a first attempt:

```
function stripComments(code) {
return code.replace(/\/\/.*|\/\*[^]*\*\//g, "");
}
console.log(stripComments("1 + /* 2 */3"));
// → 1 + 3
console.log(stripComments("x = 10;// ten!"));
// → x = 10;
console.log(stripComments("1 /* a */+/* b */ 1"));
// → 1 1
```
The part before the|operator matches two slash characters followed by
any number of non-newline characters. The part for multiline comments
is more involved. We use[^](any character that is not in the empty
set of characters) as a way to match any character. We cannot just use
a period here because block comments can continue on a new line, and
the period character does not match newline characters.
But the output for the last line appears to have gone wrong. Why?
The [^]* part of the expression, as I described in the section on
backtracking, will first match as much as it can. If that causes the next


part of the pattern to fail, the matcher moves back one character and
tries again from there. In the example, the matcher first tries to match
the whole rest of the string and then moves back from there. It will
find an occurrence of*/ after going back four characters and match
that. This is not what we wanted—the intention was to match a single
comment, not to go all the way to the end of the code and find the end
of the last block comment.
Because of this behavior, we say the repetition operators (+,*,?, and
{}) are _greedy_ , meaning they match as much as they can and backtrack
from there. If you put a question mark after them (+?,*?,??,{}?), they
become nongreedy and start by matching as little as possible, matching
more only when the remaining pattern does not fit the smaller match.
And that is exactly what we want in this case. By having the star
match the smallest stretch of characters that brings us to a */, we
consume one block comment and nothing more.

```
function stripComments(code) {
return code.replace(/\/\/.*|\/\*[^]*?\*\//g, "");
}
console.log(stripComments("1 /* a */+/* b */ 1"));
// → 1 + 1
```
A lot of bugs in regular expression programs can be traced to unin-
tentionally using a greedy operator where a nongreedy one would work
better. When using a repetition operator, prefer the nongreedy variant.


### Dynamically creating RegExp objects

In some cases you may not know the exact pattern you need to match
against when you are writing your code. Say you want to test for the
user’s name in a piece of text. You can build up a string and use the
RegExpconstructor on that.

```
let name = "harry";
let regexp = new RegExp("(^|\\s)" + name + "($|\\s)", "gi");
console.log(regexp.test("Harry is a dodgy character."));
// → true
```
When creating the\spart of the string, we have to use two backslashes
because we are writing them in a normal string, not a slash-enclosed
regular expression. The second argument to the RegExp constructor
contains the options for the regular expression—in this case, "gi"for
global and case insensitive.
But what if the name is "dea+hl[]rd" because our user is a nerdy
teenager? That would result in a nonsensical regular expression that
won’t actually match the user’s name.
To work around this, we can add backslashes before any character
that has a special meaning.

```
let name = "dea+hl[]rd";
let escaped = name.replace(/[\\[.+*?(){|^$]/g, "\\$&");
let regexp = new RegExp("(^|\\s)" + escaped + "($|\\s)",
"gi");
let text = "This dea+hl[]rd guy is super annoying.";
console.log(regexp.test(text));
```

```
// → true
```
### The search method

While the indexOfmethod on strings cannot be called with a regular
expression, there is another method, search, that does expect a reg-
ular expression. Like indexOf, it returns the first index on which the
expression was found, or -1 when it wasn’t found.

```
console.log(" word".search(/\S/));
// → 2
console.log(" ".search(/\S/));
// → -1
```
Unfortunately, there is no way to indicate that the match should start
at a given offset (like we can with the second argument toindexOf),
which would often be useful.

### The lastIndex property

Theexecmethod similarly does not provide a convenient way to start
searching from a given position in the string. But it does provide an
_in_ convenient way.
Regular expression objects have properties. One such property is
source, which contains the string that expression was created from.
Another property islastIndex, which controls, in some limited circum-
stances, where the next match will start.


Those circumstances are that the regular expression must have the
global (g) or sticky (y) option enabled, and the match must happen
through theexecmethod. Again, a less confusing solution would have
been to just allow an extra argument to be passed toexec, but confusion
is an essential feature of JavaScript’s regular expression interface.

```
let pattern = /y/g;
pattern.lastIndex = 3;
let match = pattern.exec("xyzzy");
console.log(match.index);
// → 4
console.log(pattern.lastIndex);
// → 5
```
If the match was successful, the call toexecautomatically updates the
lastIndex property to point after the match. If no match was found,
lastIndex is set back to 0, which is also the value it has in a newly
constructed regular expression object.
The difference between the global and the sticky options is that when
sticky is enabled, the match will succeed only if it starts directly at
lastIndex, whereas with global, it will search ahead for a position where
a match can start.

```
let global = /abc/g;
console.log(global.exec("xyz abc"));
// → ["abc"]
let sticky = /abc/y;
console.log(sticky.exec("xyz abc"));
// → null
```

When using a shared regular expression value for multipleexec calls,
these automatic updates to thelastIndexproperty can cause problems.
Your regular expression might be accidentally starting at an index left
over from a previous call.

```
let digit = /\d/g;
console.log(digit.exec("here it is: 1"));
// → ["1"]
console.log(digit.exec("and now: 1"));
// → null
```
Another interesting effect of the global option is that it changes the
way the matchmethod on strings works. When called with a global
expression, instead of returning an array similar to that returned by
exec,matchwill find _all_ matches of the pattern in the string and return
an array containing the matched strings.

```
console.log("Banana".match(/an/g));
// → ["an", "an"]
```
So be cautious with global regular expressions. The cases where they
are necessary—calls toreplaceand places where you want to explicitly
uselastIndex—are typically the situations where you want to use them.
A common thing to do is to find all the matches of a regular expression
in a string. We can do this by using thematchAllmethod.

```
let input = "A string with 3 numbers in it... 42 and 88.";
let matches = input.matchAll(/\d+/g);
for (let match of matches) {
console.log("Found", match[0], "at", match.index);
```

```
}
// → Found 3 at 14
// Found 42 at 33
// Found 88 at 40
```
This method returns an array of match arrays. The regular expression
given tomatchAll _must_ havegenabled.

### Parsing an INI file.

To conclude the chapter, we’ll look at a problem that calls for regular
expressions. Imagine we are writing a program to automatically collect
information about our enemies from the internet. (We will not actually
write that program here, just the part that reads the configuration file.
Sorry.) The configuration file looks like this:

```
searchengine=https://duckduckgo.com/?q=$1
spitefulness=9.7
```
```
; comments are preceded by a semicolon...
; each section concerns an individual enemy
[larry]
fullname=Larry Doe
type=kindergarten bully
website=http://www.geocities.com/CapeCanaveral/11451
```
```
[davaeorn]
fullname=Davaeorn
type=evil wizard
```

```
outputdir=/home/marijn/enemies/davaeorn
```
The exact rules for this format—which is a widely used file format,
usually called an _INI_ file—are as follows:

- Blank lines and lines starting with semicolons are ignored.
- Lines wrapped in[and]start a new section.
- Lines containing an alphanumeric identifier followed by an=char-
    acter add a setting to the current section.
- Anything else is invalid.

Our task is to convert a string like this into an object whose prop-
erties hold strings for settings written before the first section header
and subobjects for sections, with those subobjects holding the section’s
settings.
Since the format has to be processed line by line, splitting up the file
into separate lines is a good start. We saw thesplitmethod inChapter
4. Some operating systems, however, use not just a newline character
to separate lines but a carriage return character followed by a newline
("\r\n"). Given that thesplitmethod also allows a regular expression
as its argument, we can use a regular expression like/\r?\n/to split in
a way that allows both"\n"and"\r\n"between lines.

```
function parseINI(string) {
// Start with an object to hold the top-level fields
let result = {};
```

```
let section = result;
for (let line of string.split(/\r?\n/)) {
let match;
if (match = line.match(/^(\w+)=(.*)$/)) {
section[match[1]] = match[2];
} else if (match = line.match(/^\[(.*)\]$/)) {
section = result[match[1]] = {};
} else if (!/^\s*(;|$)/.test(line)) {
throw new Error("Line '" + line + "' is not valid.");
}
};
return result;
}
```
```
console.log(parseINI(`
name=Vasilis
[address]
city=Tessaloniki`));
// → {name: "Vasilis", address: {city: "Tessaloniki"}}
```
The code goes over the file’s lines and builds up an object. Properties
at the top are stored directly into that object, whereas properties found
in sections are stored in a separate section object. Thesectionbinding
points at the object for the current section.
There are two kinds of significant lines—section headers or property
lines. When a line is a regular property, it is stored in the current
section. When it is a section header, a new section object is created,
andsectionis set to point at it.
Note the recurring use of^and$to make sure the expression matches


the whole line, not just part of it. Leaving these out results in code
that mostly works but behaves strangely for some input, which can be
a diﬀicult bug to track down.
The pattern if (match = string.match(...))makes use of the fact
that the value of an assignment expression (=) is the assigned value.
You often aren’t sure that your call to matchwill succeed, so you can
access the resulting object only inside anif statement that tests for
this. To not break the pleasant chain ofelse ifforms, we assign the
result of the match to a binding and immediately use that assignment
as the test for theifstatement.
If a line is not a section header or a property, the function checks
whether it is a comment or an empty line using the expression/^\s*(;|
$)/ to match lines that either contain only whitespace, or whitespace
followed by a semicolon (making the rest of the line a comment). When
a line doesn’t match any of the expected forms, the function throws an
exception.

### Code units and characters

Another design mistake that’s been standardized in JavaScript regu-
lar expressions is that by default, operators like.or ?work on code
units (as discussed inChapter 5), not actual characters. This means
characters that are composed of two code units behave strangely.

```
console.log(/🍎{3}/.test("🍎🍎🍎"));
// → false
console.log(/<.>/.test("<🌹>"));
```

```
// → false
console.log(/<.>/u.test("<🌹>"));
// → true
```
The problem is that the🍎in the first line is treated as two code units,
and{3}is applied only to the second unit. Similarly, the dot matches
a single code unit, not the two that make up the rose emoji.
You must add theu(Unicode) option to your regular expression to
make it treat such characters properly.

```
console.log(/🍎{3}/u.test("🍎🍎🍎"));
// → true
```
### Summary

Regular expressions are objects that represent patterns in strings. They
use their own language to express these patterns.


/abc/ A sequence of characters
/[abc]/ Any character from a set of characters
/[^abc]/ Any character _not_ in a set of characters
/[0-9]/ Any character in a range of characters
/x+/ One or more occurrences of the patternx
/x+?/ One or more occurrences, nongreedy
/x*/ Zero or more occurrences
/x?/ Zero or one occurrence
/x{2,4}/ Two to four occurrences
/(abc)/ A group
/a|b|c/ Any one of several patterns
/\d/ Any digit character
/\w/ An alphanumeric character (“word character”)
/\s/ Any whitespace character
/./ Any character except newlines
/\p{L}/u Any letter character
/^/ Start of input
/$/ End of input
/(?=a)/ A look-ahead test
A regular expression has a methodtestto test whether a given string
matches it. It also has a method exec that, when a match is found,
returns an array containing all matched groups. Such an array has an
indexproperty that indicates where the match started.
Strings have amatchmethod to match them against a regular expres-
sion and asearchmethod to search for one, returning only the starting
position of the match. Theirreplacemethod can replace matches of a
pattern with a replacement string or function.


Regular expressions can have options, which are written after the
closing slash. The ioption makes the match case insensitive. Theg
option makes the expression _global_ , which, among other things, causes
the replacemethod to replace all instances instead of just the first.
Theyoption makes and expression sticky, which means that it will not
search ahead and skip part of the string when looking for a match. The
uoption turns on Unicode mode, which enables\psyntax and fixes a
number of problems around the handling of characters that take up two
code units.
Regular expressions are a sharp tool with an awkward handle. They
simplify some tasks tremendously but can quickly become unmanage-
able when applied to complex problems. Part of knowing how to use
them is resisting the urge to try to shoehorn things into them that they
cannot cleanly express.

### Exercises

It is almost unavoidable that, in the course of working on these exer-
cises, you will get confused and frustrated by some regular expression’s
inexplicable behavior. Sometimes it helps to enter your expression into
an online tool like _debuggex.com_ to see whether its visualization cor-
responds to what you intended and to experiment with the way it re-
sponds to various input strings.


**Regexpgolf**

_Code golf_ is a term used for the game of trying to express a particular
program in as few characters as possible. Similarly, _regexp golf_ is the
practice of writing as tiny a regular expression as possible to match a
given pattern and _only_ that pattern.
For each of the following items, write a regular expression to test
whether the given pattern occurs in a string. The regular expression
should match only strings containing the pattern. When your expres-
sion works, see whether you can make it any smaller.

1. _car_ and _cat_
2. _pop_ and _prop_
3. _ferret_ , _ferry_ , and _ferrari_
4. Any word ending in _ious_
5. A whitespace character followed by a period, comma, colon, or
    semicolon
6. A word longer than six letters
7. A word without the letter _e_ (or _E_ )

Refer to the table in thechapter summaryfor help. Test each solution
with a few test strings.


**Quotingstyle**

Imagine you have written a story and used single quotation marks
throughout to mark pieces of dialogue. Now you want to replace all
the dialogue quotes with double quotes, while keeping the single quotes
used in contractions like _aren’t_.
Think of a pattern that distinguishes these two kinds of quote usage
and craft a call to thereplacemethod that does the proper replacement.

**Numbersagain**

Write an expression that matches only JavaScript-style numbers. It
must support an optional minus _or_ plus sign in front of the number,
the decimal dot, and exponent notation—5e-3or1E10—again with an
optional sign in front of the exponent. Also note that it is not necessary
for there to be digits in front of or after the dot, but the number cannot
be a dot alone. That is,.5and5.are valid JavaScript numbers, but a
lone dot isn’t.


```
“Write code that is easy to delete, not easy to extend.”
—Tef, programming is terrible
```
**Chapter10**

## Modules

Ideally, a program has a clear, straightforward structure. The way it
works is easy to explain, and each part plays a well-defined role.
In practice, programs grow organically. Pieces of functionality are
added as the programmer identifies new needs. Keeping such a program
well structured requires constant attention and work. This is work that
will pay off only in the future, the _next_ time someone works on the
program, so it’s tempting to neglect it and allow the various parts of
the program to become deeply entangled.
This causes two practical issues. First, understanding an entangled
system is hard. If everything can touch everything else, it is diﬀicult to
look at any given piece in isolation. You are forced to build up a holistic
understanding of the entire thing. Second, if you want to use any of
the functionality from such a program in another situation, rewriting
it may be easier than trying to disentangle it from its context.
The phrase “big ball of mud” is often used for such large, structureless
programs. Everything sticks together, and when you try to pick out a
piece, the whole thing comes apart, and you succeed only in making a


mess.

### Modular programs.

_Modules_ are an attempt to avoid these problems. A module is a piece
of program that specifies which other pieces it relies on and which func-
tionality it provides for other modules to use (its _interface_ ).
Module interfaces have a lot in common with object interfaces, as we
saw them inChapter 6. They make part of the module available to the
outside world and keep the rest private.
But the interface that a module provides for others to use is only
half the story. A good module system also requires modules to specify
which code _they_ use from other modules. These relations are called
_dependencies_. If module A uses functionality from module B, it is said
to _depend_ on that module. When these are clearly specified in the
module itself, they can be used to figure out which other modules need
to be present to be able to use a given module and to automatically
load dependencies.
When the ways in which modules interact with each other are explicit,
a system becomes more like LEGO, where pieces interact through well-
defined connectors, and less like mud, where everything mixes with
everything else.


### ES modules.

The original JavaScript language did not have any concept of a module.
All scripts ran in the same scope, and accessing a function defined in
another script was done by referencing the global bindings created by
that script. This actively encouraged accidental, hard-to-see entangle-
ment of code and invited problems like unrelated scripts trying to use
the same binding name.
Since ECMAScript 2015, JavaScript supports two different types of
programs. _Scripts_ behave in the old way: their bindings are defined
in the global scope, and they have no way to directly reference other
scripts. _Modules_ get their own separate scope and support theimport
andexportkeywords, which aren’t available in scripts, to declare their
dependencies and interface. This module system is usually called _ES
modules_ (where _ES_ stands for ECMAScript).
A modular program is composed of a number of such modules, wired
together via their imports and exports.
The following example module converts between day names and num-
bers (as returned byDate’sgetDaymethod). It defines a constant that
is not part of its interface, and two functions that are. It has no depen-
dencies.

```
const names = ["Sunday", "Monday", "Tuesday", "Wednesday",
"Thursday", "Friday", "Saturday"];
```
```
export function dayName(number) {
return names[number];
}
```

```
export function dayNumber(name) {
return names.indexOf(name);
}
```
Theexportkeyword can be put in front of a function, class, or binding
definition to indicate that that binding is part of the module’s inter-
face. This makes it possible for other modules to use that binding by
importing it.

```
import {dayName} from "./dayname.js";
let now = new Date();
console.log(`Today is ${dayName(now.getDay())}`);
// → Today is Monday
```
The import keyword, followed by a list of binding names in braces,
makes bindings from another module available in the current module.
Modules are identified by quoted strings.
How such a module name is resolved to an actual program differs by
platform. The browser treats them as web addresses, whereas Node.js
resolves them to files. When you run a module, all the other modules
it depends on—and the modules _those_ depend on—are loaded, and the
exported bindings are made available to the modules that import them.
Import and export declarations cannot appear inside of functions,
loops, or other blocks. They are immediately resolved when the module
is loaded, regardless of how the code in the module executes. To reflect
this, they must appear only in the outer module body.
A module’s interface thus consists of a collection of named bindings,
which other modules that depend on the module can access. Imported
bindings can be renamed to give them a new local name usingasafter


their name.

```
import {dayName as nomDeJour} from "./dayname.js";
console.log(nomDeJour(3));
// → Wednesday
```
A module may also have a special export nameddefault, which is often
used for modules that only export a single binding. To define a de-
fault export, you writeexport defaultbefore an expression, a function
declaration, or a class declaration.

```
export default ["Winter", "Spring", "Summer", "Autumn"];
```
Such a binding is imported by omitting the braces around the name of
the import.

```
import seasonNames from "./seasonname.js";
```
To import all bindings from a module at the same time, you can use
import *. You provide a name, and that name will be bound to an
object holding all the module’s exports. This can be useful when you
are using a lot of different exports.

```
import * as dayName from "./dayname.js";
console.log(dayName.dayName(3));
// → Wednesday
```

### Packages

One of the advantages of building a program out of separate pieces and
being able to run some of those pieces on their own is that you might
be able to use the same piece in different programs.
But how do you set this up? Say I want to use theparseINIfunction
fromChapter 9 in another program. If it is clear what the function
depends on (in this case, nothing), I can just copy that module into my
new project and use it. But then, if I find a mistake in the code, I’ll
probably fix it in whichever program I’m working with at the time and
forget to also fix it in the other program.
Once you start duplicating code, you’ll quickly find yourself wasting
time and energy moving copies around and keeping them up to date.
That’s where _packages_ come in. A package is a chunk of code that
can be distributed (copied and installed). It may contain one or more
modules and has information about which other packages it depends
on. A package also usually comes with documentation explaining what
it does so that people who didn’t write it might still be able to use it.
When a problem is found in a package or a new feature is added, the
package is updated. Now the programs that depend on it (which may
also be packages) can copy the new version to get the improvements
that were made to the code.
Working in this way requires infrastructure. We need a place to
store and find packages and a convenient way to install and upgrade
them. In the JavaScript world, this infrastructure is provided by NPM
( _https://npmjs.com_ ).
NPM is two things: an online service where you can download (and


upload) packages, and a program (bundled with Node.js) that helps
you install and manage them.
At the time of writing, there are more than three million different
packages available on NPM. A large portion of those are rubbish, to
be fair. But almost every useful, publicly available JavaScript package
can be found on NPM. For example, an INI file parser, similar to the
one we built inChapter 9, is available under the package nameini.
Chapter 20will show how to install such packages locally using the
npmcommand line program.
Having quality packages available for download is extremely valuable.
It means that we can often avoid reinventing a program that 100 people
have written before and get a solid, well-tested implementation at the
press of a few keys.
Software is cheap to copy, so once someone has written it, distributing
it to other people is an eﬀicient process. Writing it in the first place _is_
work, though, and responding to people who have found problems in
the code or who want to propose new features is even more work.
By default, you own the copyright to the code you write, and other
people may use it only with your permission. But because some people
are just nice and because publishing good software can help make you
a little bit famous among programmers, many packages are published
under a license that explicitly allows other people to use it.
Most code on NPM is licensed this way. Some licenses require you
to also publish code that you build on top of the package under the
same license. Others are less demanding, requiring only that you keep
the license with the code as you distribute it. The JavaScript commu-


nity mostly uses the latter type of license. When using other people’s
packages, make sure you are aware of their licenses.
Now, instead of writing our own INI file parser, we can use one from
NPM.

```
import {parse} from "ini";
```
```
console.log(parse("x = 10\ny = 20"));
// → {x: "10", y: "20"}
```
### CommonJS modules.

Before 2015, when the JavaScript language had no built-in module sys-
tem, people were already building large systems in JavaScript. To make
that workable, they _needed_ modules.
The community designed its own improvised module systems on top
of the language. These use functions to create a local scope for the
modules and regular objects to represent module interfaces.
Initially, people just manually wrapped their entire module in an
“immediately invoked function expression” to create the module’s scope
and assigned their interface objects to a single global variable.

```
const weekDay = function() {
const names = ["Sunday", "Monday", "Tuesday", "Wednesday",
"Thursday", "Friday", "Saturday"];
return {
name(number) { return names[number]; },
number(name) { return names.indexOf(name); }
```

```
};
}();
```
```
console.log(weekDay.name(weekDay.number("Sunday")));
// → Sunday
```
This style of modules provides isolation, to a certain degree, but it does
not declare dependencies. Instead, it just puts its interface into the
global scope and expects its dependencies, if any, to do the same. This
is not ideal.
If we implement our own module loader, we can do better. The
most widely used approach to bolted-on JavaScript modules is called
_CommonJS modules_. Node.js used this module system from the start
(though it now also knows how to load ES modules), and it is the
module system used by many packages on NPM.
A CommonJS module looks like a regular script, but it has access to
two bindings that it uses to interact with other modules. The first is
a function calledrequire. When you call this with the module name
of your dependency, it makes sure the module is loaded and returns its
interface. The second is an object namedexports, which is the interface
object for the module. It starts out empty and you add properties to it
to define exported values.
This CommonJS example module provides a date-formatting func-
tion. It uses two packages from NPM—ordinalto convert numbers to
strings like"1st"and"2nd", anddate-namesto get the English names for
weekdays and months. It exports a single function,formatDate, which
takes aDateobject and a template string.


The template string may contain codes that direct the format, such
asYYYYfor the full year andDofor the ordinal day of the month. You
could give it a string like"MMMM Do YYYY"to get output likeNovember 22
nd 2017.

```
const ordinal = require("ordinal");
const {days, months} = require("date-names");
```
```
exports.formatDate = function(date, format) {
return format.replace(/YYYY|M(MMM)?|Do?|dddd/g, tag => {
if (tag == "YYYY") return date.getFullYear();
if (tag == "M") return date.getMonth();
if (tag == "MMMM") return months[date.getMonth()];
if (tag == "D") return date.getDate();
if (tag == "Do") return ordinal(date.getDate());
if (tag == "dddd") return days[date.getDay()];
});
};
```
The interface ofordinalis a single function, whereasdate-namesexports
an object containing multiple things—days and months are arrays of
names. Destructuring is very convenient when creating bindings for
imported interfaces.
The module adds its interface function toexportsso that modules
that depend on it get access to it. We could use the module like this:

```
const {formatDate} = require("./format-date.js");
```
```
console.log(formatDate(new Date(2017, 9, 13),
"dddd the Do"));
```

```
// → Friday the 13th
```
CommonJS is implemented with a module loader that, when loading a
module, wraps its code in a function (giving it its own local scope) and
passes therequireandexportsbindings to that function as arguments.
If we assume we have access to areadFilefunction that reads a file
by name and gives us its content, we can define a simplified form of
requirelike this:

```
function require(name) {
if (!(name in require.cache)) {
let code = readFile(name);
let exports = require.cache[name] = {};
let wrapper = Function("require, exports", code);
wrapper(require, exports);
}
return require.cache[name];
}
require.cache = Object.create(null);
```
Functionis a built-in JavaScript function that takes a list of arguments
(as a comma-separated string) and a string containing the function body
and returns a function value with those arguments and that body. This
is an interesting concept—it allows a program to create new pieces of
program from string data—but also a dangerous one, since if someone
can trick your program into putting a string they provide intoFunction,
they can make the program do anything they want.
Standard JavaScript provides no such function asreadFile, but dif-
ferent JavaScript environments, such as the browser and Node.js, pro-


vide their own ways of accessing files. The example just pretends that
readFileexists.
To avoid loading the same module multiple times, requirekeeps a
store (cache) of already loaded modules. When called, it first checks
whether the requested module has been loaded and, if not, loads it.
This involves reading the module’s code, wrapping it in a function, and
calling it.
By defining require and exports as parameters for the generated
wrapper function (and passing the appropriate values when calling it),
the loader makes sure that these bindings are available in the module’s
scope.
An important difference between this system and ES modules is that
ES module imports happen before a module’s script starts running,
whereasrequireis a normal function, invoked when the module is al-
ready running. Unlike import declarations, require calls _can_ appear
inside functions, and the name of the dependency can be any expres-
sion that evaluates to a string, whereasimportallows only plain quoted
strings.
The transition of the JavaScript community from CommonJS style to
ES modules has been a slow and somewhat rough one. Fortunately we
are now at a point where most of the popular packages on NPM provide
their code as ES modules, and Node.js allows ES modules to import
from CommonJS modules. While CommonJS code is still something
you will run across, there is no real reason to write new programs in
this style anymore.


### Building and bundling

Many JavaScript packages aren’t technically written in JavaScript. Lan-
guage extensions such as TypeScript, the type checking dialect men-
tioned in Chapter 8, are widely used. People also often start using
planned new language features long before they have been added to the
platforms that actually run JavaScript. To make this possible, they
_compile_ their code, translating it from their chosen JavaScript dialect
to plain old JavaScript—or even to a past version of JavaScript—so
that browsers can run it.
Including a modular program that consists of 200 different files in
a web page produces its own problems. If fetching a single file over
the network takes 50 milliseconds, loading the whole program takes 10
seconds, or maybe half that if you can load several files simultaneously.
That’s a lot of wasted time. Because fetching a single big file tends to
be faster than fetching a lot of tiny ones, web programmers have started
using tools that combine their programs (which they painstakingly split
into modules) into a single big file before they publish it to the web.
Such tools are called _bundlers_.
And we can go further. Apart from the number of files, the _size_ of the
files also determines how fast they can be transferred over the network.
Thus, the JavaScript community has invented _minifiers_. These are tools
that take a JavaScript program and make it smaller by automatically
removing comments and whitespace, renaming bindings, and replacing
pieces of code with equivalent code that take up less space.
It is not uncommon for the code that you find in an NPM pack-
age or that runs on a web page to have gone through _multiple_ stages of


transformation—converting from modern JavaScript to historic JavaScript,
combining the modules into a single file, and minifying the code. We
won’t go into the details of these tools in this book, since there are
many of them, and which one is popular changes regularly. Just be
aware that such things exist, and look them up when you need them.

### Module design

Structuring programs is one of the subtler aspects of programming. Any
nontrivial piece of functionality can be organized in various ways.
Good program design is subjective—there are trade-offs involved, and
matters of taste. The best way to learn the value of well-structured
design is to read or work on a lot of programs and notice what works
and what doesn’t. Don’t assume that a painful mess is “just the way
it is”. You can improve the structure of almost everything by putting
more thought into it.
One aspect of module design is ease of use. If you are designing
something that is intended to be used by multiple people—or even by
yourself, in three months when you no longer remember the specifics of
what you did—it is helpful if your interface is simple and predictable.
That may mean following existing conventions. A good example is
the ini package. This module imitates the standardJSON object by
providingparseandstringify(to write an INI file) functions, and, like
JSON, converts between strings and plain objects. The interface is small
and familiar, and after you’ve worked with it once, you’re likely to
remember how to use it.


Even if there’s no standard function or widely used package to imi-
tate, you can keep your modules predictable by using simple data struc-
tures and doing a single, focused thing. Many of the INI-file parsing
modules on NPM provide a function that directly reads such a file from
the hard disk and parses it, for example. This makes it impossible to
use such modules in the browser, where we don’t have direct filesystem
access, and adds complexity that would have been better addressed by
_composing_ the module with some file-reading function.
This points to another helpful aspect of module design—the ease with
which something can be composed with other code. Focused modules
that compute values are applicable in a wider range of programs than
bigger modules that perform complicated actions with side effects. An
INI file reader that insists on reading the file from disk is useless in a
scenario where the file’s content comes from some other source.
Relatedly, stateful objects are sometimes useful or even necessary, but
if something can be done with a function, use a function. Several of the
INI file readers on NPM provide an interface style that requires you to
first create an object, then load the file into your object, and finally use
specialized methods to get at the results. This type of thing is common
in the object-oriented tradition, and it’s terrible. Instead of making a
single function call and moving on, you have to perform the ritual of
moving your object through its various states. And because the data is
now wrapped in a specialized object type, all code that interacts with it
has to know about that type, creating unnecessary interdependencies.
Often, defining new data structures can’t be avoided—only a few
basic ones are provided by the language standard, and many types of


data have to be more complex than an array or a map. But when an
array suﬀices, use an array.
An example of a slightly more complex data structure is the graph
fromChapter 7. There is no single obvious way to represent a graph in
JavaScript. In that chapter, we used an object whose properties hold
arrays of strings—the other nodes reachable from that node.
There are several different pathfinding packages on NPM, but none
of them uses this graph format. They usually allow the graph’s edges
to have a weight, which is the cost or distance associated with it. That
isn’t possible in our representation.
For example, there’s thedijkstrajspackage. A well-known approach
to pathfinding, quite similar to ourfindRoutefunction, is called _Dijk-
stra’s algorithm_ , after Edsger Dijkstra, who first wrote it down. The
jssuﬀix is often added to package names to indicate the fact that they
are written in JavaScript. Thisdijkstrajspackage uses a graph format
similar to ours, but instead of arrays, it uses objects whose property
values are numbers—the weights of the edges.
If we wanted to use that package, we’d have to make sure that our
graph was stored in the format it expects. All edges get the same
weight, since our simplified model treats each road as having the same
cost (one turn).

```
const {find_path} = require("dijkstrajs");
```
```
let graph = {};
for (let node of Object.keys(roadGraph)) {
let edges = graph[node] = {};
for (let dest of roadGraph[node]) {
```

```
edges[dest] = 1;
}
}
```
```
console.log(find_path(graph, "Post Office", "Cabin"));
// → ["Post Office", "Alice's House", "Cabin"]
```
This can be a barrier to composition—when various packages are using
different data structures to describe similar things, combining them is
diﬀicult. Therefore, if you want to design for composability, find out
what data structures other people are using and, when possible, follow
their example.
Designing a fitting module structure for a program can be diﬀicult.
In the phase where you are still exploring the problem, trying different
things to see what works, you might want to not worry about it too
much, since keeping everything organized can be a big distraction. Once
you have something that feels solid, that’s a good time to take a step
back and organize it.

### Summary

Modules provide structure to bigger programs by separating the code
into pieces with clear interfaces and dependencies. The interface is the
part of the module that’s visible to other modules, and the dependencies
are the other modules it makes use of.
Because JavaScript historically did not provide a module system, the
CommonJS system was built on top of it. Then at some point it _did_


get a built-in system, which now coexists uneasily with the CommonJS
system.
A package is a chunk of code that can be distributed on its own.
NPM is a repository of JavaScript packages. You can download all
kinds of useful (and useless) packages from it.

### Exercises

**Amodularrobot**

These are the bindings that the project fromChapter 7creates:

```
roads
buildGraph
roadGraph
VillageState
runRobot
randomPick
randomRobot
mailRoute
routeRobot
findRoute
goalOrientedRobot
```
If you were to write that project as a modular program, what modules
would you create? Which module would depend on which other module,
and what would their interfaces look like?
Which pieces are likely to be available prewritten on NPM? Would
you prefer to use an NPM package or write them yourself?


**Roadsmodule**

Write an ES module based on the example fromChapter 7that contains
the array of roads and exports the graph data structure representing
them asroadGraph. It depends on a module./graph.jsthat exports a
functionbuildGraph, used to build the graph. This function expects an
array of two-element arrays (the start and end points of the roads).

**Circulardependencies**

A circular dependency is a situation where module A depends on B,
and B also, directly or indirectly, depends on A. Many module systems
simply forbid this because whichever order you choose for loading such
modules, you cannot make sure that each module’s dependencies have
been loaded before it runs.
CommonJS modules allow a limited form of cyclic dependencies. As
long as the modules don’t access each other’s interface until after they
finish loading, cyclic dependencies are okay.
Therequirefunction givenearlier in this chaptersupports this type
of dependency cycle. Can you see how it handles cycles?


```
“Who can wait quietly while the mud settles?
Who can remain still until the moment of action?”
—Laozi, Tao Te Ching
```
**Chapter11**

## AsynchronousProgramming

The central part of a computer, the part that carries out the individual
steps that make up our programs, is called the _processor_. The programs
we have seen so far will keep the processor busy until they have finished
their work. The speed at which something like a loop that manipulates
numbers can be executed depends pretty much entirely on the speed of
the computer’s processor and memory.
But many programs interact with things outside of the processor. For
example, they may communicate over a computer network or request
data from the hard disk—which is a lot slower than getting it from
memory.
When such a thing is happening, it would be a shame to let the
processor sit idle—there might be some other work it could do in the
meantime. In part, this is handled by your operating system, which
will switch the processor between multiple running programs. But that
doesn’t help when we want a _single_ program to be able to make progress
while it is waiting for a network request.


### Asynchronicity.

In a _synchronous_ programming model, things happen one at a time.
When you call a function that performs a long-running action, it returns
only when the action has finished and it can return the result. This
stops your program for the time the action takes.
An _asynchronous_ model allows multiple things to happen at the same
time. When you start an action, your program continues to run. When
the action finishes, the program is informed and gets access to the result
(for example, the data read from disk).
We can compare synchronous and asynchronous programming using
a small example: a program that makes two requests over the network
and then combines the results.
In a synchronous environment, where the request function returns
only after it has done its work, the easiest way to perform this task is
to make the requests one after the other. This has the drawback that
the second request will be started only when the first has finished. The
total time taken will be at least the sum of the two response times.
The solution to this problem, in a synchronous system, is to start
additional threads of control. A _thread_ is another running program
whose execution may be interleaved with other programs by the operat-
ing system—since most modern computers contain multiple processors,
multiple threads may even run at the same time, on different processors.
A second thread could start the second request, and then both threads
wait for their results to come back, after which they resynchronize to
combine their results.
In the following diagram, the thick lines represent time the program


spends running normally, and the thin lines represent time spent waiting
for the network. In the synchronous model, the time taken by the
network is _part_ of the timeline for a given thread of control. In the
asynchronous model, starting a network action allows the program to
continue running while the network communication happens alongside
it, notifying the program when it is finished.

```
synchronous, single thread of control
```
```
synchronous, two threads of control
```
```
asynchronous
```
Another way to describe the difference is that waiting for actions to
finish is _implicit_ in the synchronous model, while it is _explicit_ —under
our control—in the asynchronous one.
Asynchronicity cuts both ways. It makes expressing programs that
do not fit the straight-line model of control easier, but it can also make
expressing programs that do follow a straight line more awkward. We’ll
see some ways to reduce this awkwardness later in the chapter.
Both prominent JavaScript programming platforms—browsers and
Node.js—make operations that might take a while asynchronous, rather
than relying on threads. Since programming with threads is notoriously
hard (understanding what a program does is much more diﬀicult when
it’s doing multiple things at once), this is generally considered a good


thing.

### Callbacks

One approach to asynchronous programming is to make functions that
need to wait for something take an extra argument, a _callback function_.
The asynchronous function starts a process, sets things up so that the
callback function is called when the process finishes, and then returns.
As an example, thesetTimeout function, available both in Node.js
and in browsers, waits a given number of milliseconds and then calls a
function.

```
setTimeout(() => console.log("Tick"), 500);
```
Waiting is not generally important work, but it can be very useful when
you need to arrange for something to happen at a certain time or check
whether some action is taking longer than expected.
Another example of a common asynchronous operation is reading a
file from a device’s storage. Imagine you have a functionreadTextFile
that reads a file’s content as a string and passes it to a callback function.

```
readTextFile("shopping_list.txt", content => {
console.log(`Shopping List:\n${content}`);
});
// → Shopping List:
// → Peanut butter
// → Bananas
```

ThereadTextFilefunction is not part of standard JavaScript. We will
see how to read files in the browser and in Node.js in later chapters.
Performing multiple asynchronous actions in a row using callbacks
means that you have to keep passing new functions to handle the con-
tinuation of the computation after the actions. An asynchronous func-
tion that compares two files and produces a boolean indicating whether
their content is the same might look like this:

```
function compareFiles(fileA, fileB, callback) {
readTextFile(fileA, contentA => {
readTextFile(fileB, contentB => {
callback(contentA == contentB);
});
});
}
```
This style of programming is workable, but the indentation level in-
creases with each asynchronous action because you end up in another
function. Doing more complicated things, such as wrapping asyn-
chronous actions in a loop, can get awkward.
In a way, asynchronicity is _contagious_. Any function that calls a
function that works asynchronously must itself be asynchronous, using
a callback or similar mechanism to deliver its result. Calling a callback
is somewhat more involved and error prone than simply returning a
value, so needing to structure large parts of your program that way is
not great.


### Promises

A slightly different way to build an asynchronous program is to have
asynchronous functions return an object that represents its (future)
result instead of passing around callback functions. This way, such
functions actually return something meaningful, and the shape of the
program more closely resembles that of synchronous programs.
This is what the standard classPromiseis for. A _promise_ is a receipt
representing a value that may not be available yet. It provides athen
method that allows you to register a function that should be called
when the action for which it is waiting finishes. When the promise
is _resolved_ , meaning its value becomes available, such functions (there
can be multiple) are called with the result value. It is possible to call
thenon a promise that has already resolved—your function will still be
called.
The easiest way to create a promise is by calling Promise.resolve.
This function ensures that the value you give it is wrapped in a promise.
If it’s already a promise, it is simply returned. Otherwise, you get a
new promise that immediately resolves with your value as its result.

```
let fifteen = Promise.resolve(15);
fifteen.then(value => console.log(`Got ${value}`));
// → Got 15
```
To create a promise that does not immediately resolve, you can use
Promiseas a constructor. It has a somewhat odd interface: the con-
structor expects a function as its argument, which it immediately calls,
passing it a function that it can use to resolve the promise.


For example, this is how you could create a promise-based interface
for thereadTextFilefunction:

```
function textFile(filename) {
return new Promise(resolve => {
readTextFile(filename, text => resolve(text));
});
}
```
```
textFile("plans.txt").then(console.log);
```
Note how, in contrast to callback-style functions, this asynchronous
function returns a meaningful value—a promise to give you the contents
of the file at some point in the future.
A useful thing about thethenmethod is that it itself returns another
promise. This one resolves to the value returned by the callback func-
tion or, if that returned value is a promise, to the value that promise
resolves to. Thus, you can “chain” multiple calls tothentogether to set
up a sequence of asynchronous actions.
This function, which reads a file full of filenames and returns the
content of a random file in that list, shows this kind of asynchronous
promise pipeline:

```
function randomFile(listFile) {
return textFile(listFile)
.then(content => content.trim().split("\n"))
.then(ls => ls[Math.floor(Math.random() * ls.length)])
.then(filename => textFile(filename));
}
```

The function returns the result of this chain ofthencalls. The initial
promise fetches the list of files as a string. The firstthencall transforms
that string into an array of lines, producing a new promise. The second
thencall picks a random line from that, producing a third promise that
yields a single filename. The finalthencall reads this file, so the result
of the function as a whole is a promise that returns the content of a
random file.
In this code, the functions used in the first twothencalls return a
regular value that will immediately be passed into the promise returned
bythenwhen the function returns. The lastthencall returns a promise
(textFile(filename)), making it an actual asynchronous step.
It would also have been possible to perform all these steps inside a
singlethencallback, since only the last step is actually asynchronous.
But the kind of then wrappers that only do some synchronous data
transformation are often useful, such as when you want to return a
promise that produces a processed version of some asynchronous result.

```
function jsonFile(filename) {
return textFile(filename).then(JSON.parse);
}
```
```
jsonFile("package.json").then(console.log);
```
Generally, it is useful to think of a promise as a device that lets code
ignore the question of when a value is going to arrive. A normal value
has to actually exist before we can reference it. A promised value is
a value that _might_ already be there or might appear at some point in
the future. Computations defined in terms of promises, by wiring them


together withthen calls, are executed asynchronously as their inputs
become available.

### Failure

Regular JavaScript computations can fail by throwing an exception.
Asynchronous computations often need something like that. A network
request may fail, a file may not exist, or some code that is part of the
asynchronous computation may throw an exception.
One of the most pressing problems with the callback style of asyn-
chronous programming is that it makes it extremely diﬀicult to ensure
failures are properly reported to the callbacks.
A common convention is to use the first argument to the callback
to indicate that the action failed, and the second to pass the value
produced by the action when it was successful.

```
someAsyncFunction((error, value) => {
if (error) handleError(error);
else processValue(value);
});
```
Such callback functions must always check whether they received an
exception and make sure that any problems they cause, including ex-
ceptions thrown by functions they call, are caught and given to the
right function.
Promises make this easier. They can be either resolved (the action
finished successfully) or rejected (it failed). Resolve handlers (as reg-
istered with then) are called only when the action is successful, and


rejections are propagated to the new promise returned bythen. When
a handler throws an exception, this automatically causes the promise
produced by itsthencall to be rejected. If any element in a chain of
asynchronous actions fails, the outcome of the whole chain is marked
as rejected, and no success handlers are called beyond the point where
it failed.
Much like resolving a promise provides a value, rejecting one also
provides a value, usually called the _reason_ of the rejection. When an
exception in a handler function causes the rejection, the exception value
is used as the reason. Similarly, when a handler returns a promise that
is rejected, that rejection flows into the next promise. There’s aPromise
.rejectfunction that creates a new, immediately rejected promise.
To explicitly handle such rejections, promises have acatchmethod
that registers a handler to be called when the promise is rejected, similar
to howthenhandlers handle normal resolution. It’s also very much like
then in that it returns a new promise, which resolves to the original
promise’s value when that resolves normally and to the result of the
catchhandler otherwise. If a catchhandler throws an error, the new
promise is also rejected.
As a shorthand, then also accepts a rejection handler as a second
argument, so you can install both types of handlers in a single method
call:.then(acceptHandler, rejectHandler).
A function passed to thePromiseconstructor receives a second argu-
ment, alongside the resolve function, which it can use to reject the new
promise.
When ourreadTextFilefunction encounters a problem, it passes the


error to its callback function as a second argument. OurtextFilewrap-
per should actually check that argument so that a failure causes the
promise it returns to be rejected.

```
function textFile(filename) {
return new Promise((resolve, reject) => {
readTextFile(filename, (text, error) => {
if (error) reject(error);
else resolve(text);
});
});
}
```
The chains of promise values created by calls tothen andcatch thus
form a pipeline through which asynchronous values or failures move.
Since such chains are created by registering handlers, each link has
a success handler or a rejection handler (or both) associated with it.
Handlers that don’t match the type of outcome (success or failure)
are ignored. Handlers that do match are called, and their outcome
determines what kind of value comes next—success when they return
a non-promise value, rejection when they throw an exception, and the
outcome of the promise when they return a promise.

```
new Promise((_, reject) => reject(new Error("Fail")))
.then(value => console.log("Handler 1:", value))
.catch(reason => {
console.log("Caught failure " + reason);
return "nothing";
})
.then(value => console.log("Handler 2:", value));
```

```
// → Caught failure Error: Fail
// → Handler 2: nothing
```
The firstthenhandler function isn’t called because at that point of the
pipeline the promise holds a rejection. Thecatchhandler handles that
rejection and returns a value, which is given to the secondthenhandler
function.
Much like an uncaught exception is handled by the environment,
JavaScript environments can detect when a promise rejection isn’t han-
dled and will report this as an error.

### Carla

It’s a sunny day in Berlin. The runway of the old, decommissioned
airport is teeming with cyclists and inline skaters. In the grass near a
garbage container, a flock of crows noisily mills about, trying to con-
vince a group of tourists to part with their sandwiches.
One of the crows stands out—a large scruffy female with a few white
feathers in her right wing. She is baiting people with a skill and con-
fidence that suggest she’s been doing this for a long time. When an
elderly man is distracted by the antics of another crow, she casually
swoops in, snatches his half-eaten bun from his hand, and sails away.
Contrary to the rest of the group, who look like they are happy
to spend the day goofing around here, the large crow looks purpose-
ful. Carrying her loot, she flies straight toward the roof of the hangar
building, disappearing into an air vent.
Inside the building, you can hear an odd tapping sound—soft, but


persistent. It comes from a narrow space under the roof of an unfinished
stairwell. The crow is sitting there, surrounded by her stolen snacks,
half a dozen smartphones (several of which are turned on), and a mess
of cables. She rapidly taps the screen of one of the phones with her
beak. Words are appearing on it. If you didn’t know better, you’d
think she was typing.
This crow is known to her peers as “cāāw-krö”. But since those sounds
are poorly suited for human vocal chords, we’ll refer to her as Carla.
Carla is a somewhat peculiar crow. In her youth, she was fascinated
by human language, eavesdropping on people until she had a good grasp
of what they were saying. Later in life, her interest shifted to human
technology, and she started stealing phones to study them. Her current
project is learning to program. The text she is typing in her hidden lab
is, in fact, a piece of asynchronous JavaScript code.

### Breaking In.

Carla loves the internet. Annoyingly, the phone she is working on is
about to run out of prepaid data. The building has a wireless network,
but it requires a code to access.
Fortunately, the wireless routers in the building are 20 years old and
poorly secured. Doing some research, Carla finds out that the network
authentication mechanism has a flaw she can use. When joining the
network, a device must send along the correct six-digit passcode. The
access point will reply with a success or failure message depending on
whether the right code is provided. However, when sending a partial


code (say, only three digits), the response is different based on whether
those digits are the correct start of the code or not. Sending incorrect
numbers immediately returns a failure message. When sending the
correct ones, the access point waits for more digits.
This makes it possible to greatly speed up the guessing of the number.
Carla can find the first digit by trying each number in turn, until she
finds one that doesn’t immediately return failure. Having one digit, she
can find the second digit in the same way, and so on, until she knows
the entire passcode.
Assume Carla has ajoinWififunction. Given the network name and
the passcode (as a string), the function tries to join the network, return-
ing a promise that resolves if successful and rejects if the authentication
failed. The first thing she needs is a way to wrap a promise so that it
automatically rejects after it takes too much time, to allow the program
to quickly move on if the access point doesn’t respond.

```
function withTimeout(promise, time) {
return new Promise((resolve, reject) => {
promise.then(resolve, reject);
setTimeout(() => reject("Timed out"), time);
});
}
```
This makes use of the fact that a promise can be resolved or rejected
only once. If the promise given as its argument resolves or rejects first,
that result will be the result of the promise returned bywithTimeout.
If, on the other hand, thesetTimeoutfires first, rejecting the promise,
any further resolve or reject calls are ignored.


To find the whole passcode, the program needs to repeatedly look for
the next digit by trying each digit. If authentication succeeds, we know
we have found what we are looking for. If it immediately fails, we know
that digit was wrong and must try the next digit. If the request times
out, we have found another correct digit and must continue by adding
another digit.
Because you cannot wait for a promise inside aforloop, Carla uses a
recursive function to drive this process. On each call, this function gets
the code as we know it so far, as well as the next digit to try. Depending
on what happens, it may return a finished code or call through to itself,
to either start cracking the next position in the code or to try again
with another digit.

```
function crackPasscode(networkID) {
function nextDigit(code, digit) {
let newCode = code + digit;
return withTimeout(joinWifi(networkID, newCode), 50)
.then(() => newCode)
.catch(failure => {
if (failure == "Timed out") {
return nextDigit(newCode, 0);
} else if (digit < 9) {
return nextDigit(code, digit + 1);
} else {
throw failure;
}
});
}
return nextDigit("", 0);
```

```
}
```
The access point tends to respond to bad authentication requests in
about 20 milliseconds, so to be safe, this function waits for 50 millisec-
onds before timing out a request.

```
crackPasscode("HANGAR 2").then(console.log);
// → 555555
```
Carla tilts her head and sighs. This would have been more satisfying if
the code had been a bit harder to guess.

### Async functions

Even with promises, this kind of asynchronous code is annoying to write.
Promises often need to be tied together in verbose, arbitrary-looking
ways. To create an asynchronous loop, Carla was forced to introduce a
recursive function.
The thing the cracking function actually does is completely linear—
it always waits for the previous action to complete before starting the
next one. In a synchronous programming model, it’d be more straight-
forward to express.
The good news is that JavaScript allows you to write pseudosyn-
chronous code to describe asynchronous computation. Anasyncfunc-
tion implicitly returns a promise and can, in its body, await other
promises in a way that _looks_ synchronous.
We can rewritecrackPasscodelike this:


```
async function crackPasscode(networkID) {
for (let code = "";;) {
for (let digit = 0;; digit++) {
let newCode = code + digit;
try {
await withTimeout(joinWifi(networkID, newCode), 50);
return newCode;
} catch (failure) {
if (failure == "Timed out") {
code = newCode;
break;
} else if (digit == 9) {
throw failure;
}
}
}
}
}
```
This version more clearly shows the double loop structure of the func-
tion (the inner loop tries digit 0 to 9 and the outer loop adds digits to
the passcode).
Anasyncfunction is marked by the wordasyncbefore thefunction
keyword. Methods can also be madeasyncby writingasyncbefore their
name. When such a function or method is called, it returns a promise.
As soon as the function returns something, that promise is resolved. If
the body throws an exception, the promise is rejected.
Inside an asyncfunction, the word awaitcan be put in front of an
expression to wait for a promise to resolve and only then continue the


execution of the function. If the promise rejects, an exception is raised
at the point of theawait.
Such a function no longer runs from start to completion in one go like
a regular JavaScript function. Instead, it can be _frozen_ at any point
that has anawaitand can be resumed at a later time.
For most asynchronous code, this notation is more convenient than
directly using promises. You do still need an understanding of promises,
since in many cases you’ll still interact with them directly. But when
wiring them together, asyncfunctions are generally more pleasant to
write than chains ofthencalls.

### Generators

This ability of functions to be paused and then resumed again is not ex-
clusive toasyncfunctions. JavaScript also has a feature called _generator_
functions. These are similar, but without the promises.
When you define a function withfunction*(placing an asterisk after
the wordfunction), it becomes a generator. When you call a generator,
it returns an iterator, which we already saw inChapter 6.

```
function* powers(n) {
for (let current = n;; current *= n) {
yield current;
}
}
```
```
for (let power of powers(3)) {
if (power > 50) break;
```

```
console.log(power);
}
// → 3
// → 9
// → 27
```
Initially, when you callpowers, the function is frozen at its start. Every
time you callnexton the iterator, the function runs until it hits ayield
expression, which pauses it and causes the yielded value to become the
next value produced by the iterator. When the function returns (the
one in the example never does), the iterator is done.
Writing iterators is often much easier when you use generator func-
tions. The iterator for theGroupclass (from the exercise inChapter 6)
can be written with this generator:

```
Group.prototype[Symbol.iterator] = function*() {
for (let i = 0; i < this.members.length; i++) {
yield this.members[i];
}
};
```
There’s no longer a need to create an object to hold the iteration state—
generators automatically save their local state every time they yield.
Suchyieldexpressions may occur only directly in the generator func-
tion itself and not in an inner function you define inside of it. The state
a generator saves, when yielding, is only its _local_ environment and the
position where it yielded.
Anasyncfunction is a special type of generator. It produces a promise
when called, which is resolved when it returns (finishes) and rejected


when it throws an exception. Whenever it yields (awaits) a promise,
the result of that promise (value or thrown exception) is the result of
theawaitexpression.

### A Corvid Art Project

One morning, Carla wakes up to unfamiliar noise from the tarmac out-
side of her hangar. Hopping onto the edge of the roof, she sees the
humans are setting up for something. There’s a lot of electric cabling,
a stage, and some kind of big black wall being built up.
Being a curious crow, Carla takes a closer look at the wall. It appears
to consist of a number of large glass-fronted devices wired up to cables.
On the back, the devices say “LedTec SIG-5030”.
A quick internet search turns up a user manual for these devices.
They appear to be traﬀic signs, with a programmable matrix of amber
LED lights. The intent of the humans is probably to display some kind
of information on them during their event. Interestingly, the screens can
be programmed over a wireless network. Could it be they are connected
to the building’s local network?
Each device on a network gets an _IP address_ , which other devices can
use to send it messages. We talk more about that inChapter 13. Carla
notices that her own phones all get addresses like10.0.0.20or10.0.0.33

. It might be worth trying to send messages to all such addresses and
see if any one of them responds to the interface described in the manual
for the signs.
    Chapter 18 shows how to make real requests on real networks. In


this chapter, we’ll use a simplified dummy function called requestfor
network communication. This function takes two arguments—a net-
work address and a message, which may be anything that can be sent
as JSON—and returns a promise that either resolves to a response from
the machine at the given address, or rejects if there was a problem.
According to the manual, you can change what is displayed on a
SIG-5030 sign by sending it a message with content like {"command":
"display", "data": [0, 0, 3, ...]}, wheredata holds one number per
LED dot, providing its brightness—0 means off, 3 means maximum
brightness. Each sign is 50 lights wide and 30 lights high, so an update
command should send 1,500 numbers.
This code sends a display update message to all addresses on the
local network, to see what sticks. Each of the numbers in an IP address
can go from 0 to 255. In the data it sends, it activates a number of
lights corresponding to the network address’s last number.

```
for (let addr = 1; addr < 256; addr++) {
let data = [];
for (let n = 0; n < 1500; n++) {
data.push(n < addr? 3 : 0);
}
let ip = `10.0.0.${addr}`;
request(ip, {command: "display", data})
.then(() => console.log(`Request to ${ip} accepted`))
.catch(() => {});
}
```
Since most of these addresses won’t exist or will not accept such mes-
sages, thecatchcall makes sure network errors don’t crash the program.


The requests are all sent out immediately, without waiting for other re-
quests to finish, in order to not waste time when some of the machines
don’t answer.
Having fired off her network scan, Carla heads back outside to see
the result. To her delight, all of the screens are now showing a stripe
of light in their upper-left corners. They _are_ on the local network, and
they _do_ accept commands. She quickly notes the numbers shown on
each screen. There are nine screens, arranged three high and three wide.
They have the following network addresses:

```
const screenAddresses = [
"10.0.0.44", "10.0.0.45", "10.0.0.41",
"10.0.0.31", "10.0.0.40", "10.0.0.42",
"10.0.0.48", "10.0.0.47", "10.0.0.46"
];
```
Now this opens up possibilities for all kinds of shenanigans. She could
show “crows rule, humans drool” on the wall in giant letters. But that
feels a bit crude. Instead, she plans to show a video of a flying crow
covering all of the screens at night.
Carla finds a fitting video clip, in which a second and a half of footage
can be repeated to create a looping video showing a crow’s wingbeat.
To fit the nine screens (each of which can show 50×30 pixels), Carla
cuts and resizes the videos to get a series of 150×90 images, 10 per
second. Those are then each cut into nine rectangles, and processed
so that the dark spots on the video (where the crow is) show a bright
light, and the light spots (no crow) are left dark, which should create
the effect of an amber crow flying against a black background.


She has set up theclipImages variable to hold an array of frames,
where each frame is represented with an array of nine sets of pixels—
one for each screen—in the format that the signs expect.
To display a single frame of the video, Carla needs to send a request
to all the screens at once. But she also needs to wait for the result of
these requests, both in order to not start sending the next frame before
the current one has been properly sent and in order to notice when
requests are failing.
Promisehas a static methodallthat can be used to convert an array
of promises into a single promise that resolves to an array of results.
This provides a convenient way to have some asynchronous actions
happen alongside each other, wait for them all to finish, and then do
something with their results (or at least wait for them to make sure
they don’t fail).

```
function displayFrame(frame) {
return Promise.all(frame.map((data, i) => {
return request(screenAddresses[i], {
command: "display",
data
});
}));
}
```
This maps over the images inframe(which is an array of display data
arrays) to create an array of request promises. It then returns a promise
that combines all of those.
In order to be able to stop a playing video, the process is wrapped


in a class. This class has an asynchronousplaymethod that returns a
promise that resolves only when the playback is stopped again via the
stopmethod.

```
function wait(time) {
return new Promise(accept => setTimeout(accept, time));
}
```
```
class VideoPlayer {
constructor(frames, frameTime) {
this.frames = frames;
this.frameTime = frameTime;
this.stopped = true;
}
```
```
async play() {
this.stopped = false;
for (let i = 0; !this.stopped; i++) {
let nextFrame = wait(this.frameTime);
await displayFrame(this.frames[i % this.frames.length]);
await nextFrame;
}
}
```
```
stop() {
this.stopped = true;
}
}
```
Thewaitfunction wrapssetTimeoutin a promise that resolves after the


given number of milliseconds. This is useful for controlling the speed
of the playback.

```
let video = new VideoPlayer(clipImages, 100);
video.play().catch(e => {
console.log("Playback failed: " + e);
});
setTimeout(() => video.stop(), 15000);
```
For the entire week that the screen wall stands, every evening, when it
is dark, a huge glowing orange bird mysteriously appears on it.

### The event loop.

An asynchronous program starts by running its main script, which will
often set up callbacks to be called later. That main script, as well as the
callbacks, run to completion in one piece, uninterrupted. But between
them, the program may sit idle, waiting for something to happen.
So callbacks are not directly called by the code that scheduled them.
If I callsetTimeoutfrom within a function, that function will have re-
turned by the time the callback function is called. And when the call-
back returns, control does not go back to the function that scheduled
it.
Asynchronous behavior happens on its own empty function call stack.
This is one of the reasons that, without promises, managing exceptions
across asynchronous code is so hard. Since each callback starts with a
mostly empty stack, your catchhandlers won’t be on the stack when
they throw an exception.


```
try {
setTimeout(() => {
throw new Error("Woosh");
}, 20);
} catch (e) {
// This will not run
console.log("Caught", e);
}
```
No matter how closely together events—such as timeouts or incoming
requests—happen, a JavaScript environment will run only one program
at a time. You can think of this as it running a big loop _around_ your
program, called the _event loop_. When there’s nothing to be done, that
loop is paused. But as events come in, they are added to a queue, and
their code is executed one after the other. Because no two things run
at the same time, slow-running code can delay the handling of other
events.
This example sets a timeout but then dallies until after the timeout’s
intended point of time, causing the timeout to be late.

```
let start = Date.now();
setTimeout(() => {
console.log("Timeout ran at", Date.now() - start);
}, 20);
while (Date.now() < start + 50) {}
console.log("Wasted time until", Date.now() - start);
// → Wasted time until 50
// → Timeout ran at 55
```
Promises always resolve or reject as a new event. Even if a promise is


already resolved, waiting for it will cause your callback to run after the
current script finishes, rather than right away.

```
Promise.resolve("Done").then(console.log);
console.log("Me first!");
// → Me first!
// → Done
```
In later chapters we’ll see various other types of events that run on the
event loop.

### Asynchronous bugs

When your program runs synchronously, in a single go, there are no
state changes happening except those that the program itself makes.
For asynchronous programs this is different—they may have _gaps_ in
their execution during which other code can run.
Let’s look at an example. This is a function that tries to report the
size of each file in an array of files, making sure to read them all at the
same time rather than in sequence.

```
async function fileSizes(files) {
let list = "";
await Promise.all(files.map(async fileName => {
list += fileName + ": " +
(await textFile(fileName)).length + "\n";
}));
return list;
}
```

Theasync fileName =>part shows how arrow functions can also be made
asyncby putting the wordasyncin front of them.
The code doesn’t immediately look suspicious... it maps theasync
arrow function over the array of names, creating an array of promises,
and then usesPromise.allto wait for all of these before returning the
list they build up.
But this program is entirely broken. It’ll always return only a single
line of output, listing the file that took the longest to read.
Can you work out why?
The problem lies in the +=operator, which takes the _current_ value
oflistat the time the statement starts executing and then, when the
await finishes, sets thelist binding to be that value plus the added
string.
But between the time the statement starts executing and the time it
finishes, there’s an asynchronous gap. Themapexpression runs before
anything has been added to the list, so each of the+=operators starts
from an empty string and ends up, when its storage retrieval finishes,
settinglistto the result of adding its line to the empty string.
This could have easily been avoided by returning the lines from the
mapped promises and callingjoinon the result ofPromise.all, instead
of building up the list by changing a binding. As usual, computing new
values is less error prone than changing existing values.

```
async function fileSizes(files) {
let lines = files.map(async fileName => {
return fileName + ": " +
(await textFile(fileName)).length;
```

```
});
return (await Promise.all(lines)).join("\n");
}
```
Mistakes like this are easy to make, especially when usingawait, and
you should be aware of where the gaps in your code occur. An advan-
tage of JavaScript’s _explicit_ asynchronicity (whether through callbacks,
promises, orawait) is that spotting these gaps is relatively easy.

### Summary

Asynchronous programming makes it possible to express waiting for
long-running actions without freezing the whole program. JavaScript
environments typically implement this style of programming using call-
backs, functions that are called when the actions complete. An event
loop schedules such callbacks to be called when appropriate, one after
the other, so that their execution does not overlap.
Programming asynchronously is made easier by promises, objects
that represent actions that might complete in the future, and async
functions, which allow you to write an asynchronous program as if it
were synchronous.


### Exercises

**QuietTimes**

There’s a security camera near Carla’s lab that’s activated by a motion
sensor. It is connected to the network and starts sending out a video
stream when it is active. Because she’d rather not be discovered, Carla
has set up a system that notices this kind of wireless network traﬀic
and turns on a light in her lair whenever there is activity outside, so
she knows when to keep quiet.
She’s also been logging the times at which the camera is tripped for
a while and wants to use this information to visualize which times, in
an average week, tend to be quiet and which tend to be busy. The
log is stored in files holding one time stamp number (as returned by
Date.now()) per line.

```
1695709940692
1695701068331
1695701189163
```
The"camera_logs.txt"file holds a list of logfiles. Write an asynchronous
functionactivityTable(day)that for a given day of the week returns an
array of 24 numbers, one for each hour of the day, that hold the number
of camera network traﬀic observations seen in that hour of the day. Days
are identified by number using the system used byDate.getDay, where
Sunday is 0 and Saturday is 6.
The activityGraphfunction, provided by the sandbox, summarizes
such a table into a string.


To read the files, use thetextFilefunction defined earlier—given a
filename, it returns a promise that resolves to the file’s content. Re-
member thatnew Date(timestamp)creates a Dateobject for that time,
which hasgetDayandgetHoursmethods returning the day of the week
and the hour of the day.
Both types of files—the list of logfiles and the logfiles themselves—
have each piece of data on its own line, separated by newline ("\n")
characters.

**RealPromises**

Rewrite the function from the previous exercise withoutasync/await,
using plainPromisemethods.
In this style, usingPromise.allwill be more convenient than trying
to model a loop over the logfiles. In theasyncfunction, just usingawait
in a loop is simpler. If reading a file takes some time, which of these
two approaches will take the least time to run?
If one of the files listed in the file list has a typo, and reading it fails,
how does that failure end up in thePromiseobject that your function
returns?

**BuildingPromise.all**

As we saw, given an array of promises,Promise.allreturns a promise
that waits for all of the promises in the array to finish. It then succeeds,
yielding an array of result values. If a promise in the array fails, the
promise returned by all fails too, passing on the failure reason from


the failing promise.
Implement something like this yourself as a regular function called
Promise_all.
Remember that after a promise has succeeded or failed, it can’t suc-
ceed or fail again, and further calls to the functions that resolve it
are ignored. This can simplify the way you handle a failure of your
promise.


```
“The evaluator, which determines the meaning of expressions
in a programming language, is just another program.”
—Hal Abelson and Gerald Sussman, Structure and
Interpretation of Computer Programs
```
**Chapter12**

## Project: AProgrammingLanguage

Building your own programming language is surprisingly easy (as long
as you do not aim too high) and very enlightening.
The main thing I want to show in this chapter is that there’s no
magic involved in building a programming language. I’ve often felt
that some human inventions were so immensely clever and complicated
that I’d never be able to understand them. But with a little reading
and experimenting, they often turn out to be quite mundane.
We will build a programming language called Egg. It will be a tiny,
simple language—but one that is powerful enough to express any com-
putation you can think of. It will allow simple abstraction based on
functions.

### Parsing

The most immediately visible part of a programming language is its
_syntax_ , or notation. A _parser_ is a program that reads a piece of text
and produces a data structure that reflects the structure of the program


contained in that text. If the text does not form a valid program, the
parser should point out the error.
Our language will have a simple and uniform syntax. Everything in
Egg is an expression. An expression can be the name of a binding, a
number, a string, or an _application_. Applications are used for function
calls but also for constructs such asiforwhile.
To keep the parser simple, strings in Egg do not support anything
like backslash escapes. A string is simply a sequence of characters
that are not double quotes, wrapped in double quotes. A number is a
sequence of digits. Binding names can consist of any character that is
not whitespace and that does not have a special meaning in the syntax.
Applications are written the way they are in JavaScript, by putting
parentheses after an expression and having any number of arguments
between those parentheses, separated by commas.

```
do(define(x, 10),
if(>(x, 5),
print("large"),
print("small")))
```
The uniformity of the Egg language means that things that are oper-
ators in JavaScript (such as>) are normal bindings in this language,
applied just like other functions. Since the syntax has no concept of
a block, we need adoconstruct to represent doing multiple things in
sequence.
The data structure that the parser will use to describe a program
consists of expression objects, each of which has atypeproperty indi-
cating the kind of expression it is and other properties to describe its


content.
Expressions of type"value"represent literal strings or numbers. Their
valueproperty contains the string or number value that they represent.
Expressions of type"word"are used for identifiers (names). Such objects
have anameproperty that holds the identifier’s name as a string. Finally,
"apply"expressions represent applications. They have anoperatorprop-
erty that refers to the expression that is being applied, as well as an
argsproperty that holds an array of argument expressions.
The>(x, 5)part of the previous program would be represented like
this:

```
{
type: "apply",
operator: {type: "word", name: ">"},
args: [
{type: "word", name: "x"},
{type: "value", value: 5}
]
}
```
Such a data structure is called a _syntax tree_. If you imagine the objects
as dots and the links between them as lines between those dots, as
shown in the following diagram, the structure has a treelike shape. The
fact that expressions contain other expressions, which in turn might
contain more expressions, is similar to the way tree branches split and
split again.


```
do
define
x
10
if
>
x
5
print
"large"
print
"small"
```
Contrast this to the parser we wrote for the configuration file format
inChapter 9, which had a simple structure: it split the input into lines
and handled those lines one at a time. There were only a few simple
forms that a line was allowed to have.
Here we must find a different approach. Expressions are not separated
into lines, and they have a recursive structure. Application expressions
_contain_ other expressions.
Fortunately, this problem can be solved very well by writing a parser
function that is recursive in a way that reflects the recursive nature of
the language.
We define a function parseExpression that takes a string as input.
It returns an object containing the data structure for the expression
at the start of the string, along with the part of the string left after


parsing this expression. When parsing subexpressions (the argument to
an application, for example), this function can be called again, yielding
the argument expression as well as the text that remains. This text
may in turn contain more arguments or may be the closing parenthesis
that ends the list of arguments.
This is the first part of the parser:
function parseExpression(program) {
program = skipSpace(program);
let match, expr;
if (match = /^"([^"]*)"/.exec(program)) {
expr = {type: "value", value: match[1]};
} else if (match = /^\d+\b/.exec(program)) {
expr = {type: "value", value: Number(match[0])};
} else if (match = /^[^\s(),#"]+/.exec(program)) {
expr = {type: "word", name: match[0]};
} else {
throw new SyntaxError("Unexpected syntax: " + program);
}

```
return parseApply(expr, program.slice(match[0].length));
}
```
```
function skipSpace(string) {
let first = string.search(/\S/);
if (first == -1) return "";
return string.slice(first);
}
```
Because Egg, like JavaScript, allows any amount of whitespace between


its elements, we have to repeatedly cut the whitespace off the start of
the program string. TheskipSpacefunction helps with this.
After skipping any leading space, parseExpressionuses three regu-
lar expressions to spot the three atomic elements that Egg supports:
strings, numbers, and words. The parser constructs a different kind of
data structure depending on which expression matches. If the input
does not match one of these three forms, it is not a valid expression,
and the parser throws an error. We use the SyntaxError constructor
here. This is an exception class defined by the standard, likeError, but
more specific.
We then cut off the part that was matched from the program string
and pass that, along with the object for the expression, toparseApply,
which checks whether the expression is an application. If so, it parses
a parenthesized list of arguments.

```
function parseApply(expr, program) {
program = skipSpace(program);
if (program[0] != "(") {
return {expr: expr, rest: program};
}
```
```
program = skipSpace(program.slice(1));
expr = {type: "apply", operator: expr, args: []};
while (program[0] != ")") {
let arg = parseExpression(program);
expr.args.push(arg.expr);
program = skipSpace(arg.rest);
if (program[0] == ",") {
program = skipSpace(program.slice(1));
```

```
} else if (program[0] != ")") {
throw new SyntaxError("Expected ',' or ')'");
}
}
return parseApply(expr, program.slice(1));
}
```
If the next character in the program is not an opening parenthesis,
this is not an application, and parseApply returns the expression it
was given. Otherwise, it skips the opening parenthesis and creates the
syntax tree object for this application expression. It then recursively
calls parseExpression to parse each argument until a closing paren-
thesis is found. The recursion is indirect, through parseApply and
parseExpressioncalling each other.
Because an application expression can itself be applied (such as in
multiplier(2)(1)),parseApplymust, after it has parsed an application,
call itself again to check whether another pair of parentheses follows.
This is all we need to parse Egg. We wrap it in a convenientparse
function that verifies that it has reached the end of the input string
after parsing the expression (an Egg program is a single expression),
and that gives us the program’s data structure.

```
function parse(program) {
let {expr, rest} = parseExpression(program);
if (skipSpace(rest).length > 0) {
throw new SyntaxError("Unexpected text after program");
}
return expr;
}
```

```
console.log(parse("+(a, 10)"));
// → {type: "apply",
// operator: {type: "word", name: "+"},
// args: [{type: "word", name: "a"},
// {type: "value", value: 10}]}
```
It works! It doesn’t give us very helpful information when it fails and
doesn’t store the line and column on which each expression starts, which
might be helpful when reporting errors later, but it’s good enough for
our purposes.

### The evaluator

What can we do with the syntax tree for a program? Run it, of course!
And that is what the evaluator does. You give it a syntax tree and
a scope object that associates names with values, and it will evaluate
the expression that the tree represents and return the value that this
produces.

```
const specialForms = Object.create(null);
```
```
function evaluate(expr, scope) {
if (expr.type == "value") {
return expr.value;
} else if (expr.type == "word") {
if (expr.name in scope) {
return scope[expr.name];
} else {
```

```
throw new ReferenceError(
`Undefined binding: ${expr.name}`);
}
} else if (expr.type == "apply") {
let {operator, args} = expr;
if (operator.type == "word" &&
operator.name in specialForms) {
return specialForms[operator.name](expr.args, scope);
} else {
let op = evaluate(operator, scope);
if (typeof op == "function") {
return op(...args.map(arg => evaluate(arg, scope)));
} else {
throw new TypeError("Applying a non-function.");
}
}
}
}
```
The evaluator has code for each of the expression types. A literal value
expression produces its value. (For example, the expression 100 evalu-
ates to the number 100.) For a binding, we must check whether it is
actually defined in the scope and, if it is, fetch the binding’s value.
Applications are more involved. If they are a special form, likeif, we
do not evaluate anything—we just and pass the argument expressions,
along with the scope, to the function that handles this form. If it is a
normal call, we evaluate the operator, verify that it is a function, and
call it with the evaluated arguments.
We use plain JavaScript function values to represent Egg’s function


values. We will come back to thislater, when the special formfun is
defined.
The recursive structure of evaluate resembles the structure of the
parser, and both mirror the structure of the language itself. It would
also be possible to combine the parser and the evaluator into one func-
tion and evaluate during parsing, but splitting them up this way makes
the program clearer and more flexible.
This is really all that’s needed to interpret Egg. It’s that simple. But
without defining a few special forms and adding some useful values to
the environment, you can’t do much with this language yet.

### Special forms.

The specialForms object is used to define special syntax in Egg. It
associates words with functions that evaluate such forms. It is currently
empty. Let’s addif.

```
specialForms.if = (args, scope) => {
if (args.length != 3) {
throw new SyntaxError("Wrong number of args to if");
} else if (evaluate(args[0], scope) !== false) {
return evaluate(args[1], scope);
} else {
return evaluate(args[2], scope);
}
};
```
Egg’s ifconstruct expects exactly three arguments. It will evaluate


the first, and if the result isn’t the value false, it will evaluate the
second. Otherwise, the third gets evaluated. This if form is more
similar to JavaScript’s ternary?:operator than to JavaScript’sif. It
is an expression, not a statement, and it produces a value—namely, the
result of the second or third argument.
Egg also differs from JavaScript in how it handles the condition value
toif. It will treat only the valuefalseas false, not things like zero or
the empty string.
The reason we need to representifas a special form rather than a
regular function is that all arguments to functions are evaluated before
the function is called, whereasifshould evaluate only _either_ its second
or its third argument, depending on the value of the first.
Thewhileform is similar.
specialForms.while = (args, scope) => {
if (args.length != 2) {
throw new SyntaxError("Wrong number of args to while");
}
while (evaluate(args[0], scope) !== false) {
evaluate(args[1], scope);
}

```
// Since undefined does not exist in Egg, we return false,
// for lack of a meaningful result
return false;
};
```
Another basic building block isdo, which executes all its arguments from
top to bottom. Its value is the value produced by the last argument.


```
specialForms.do = (args, scope) => {
let value = false;
for (let arg of args) {
value = evaluate(arg, scope);
}
return value;
};
```
To be able to create bindings and give them new values, we also create
a form called define. It expects a word as its first argument and an
expression producing the value to assign to that word as its second
argument. Sincedefine, like everything, is an expression, it must return
a value. We’ll make it return the value that was assigned (just like
JavaScript’s=operator).

```
specialForms.define = (args, scope) => {
if (args.length != 2 || args[0].type != "word") {
throw new SyntaxError("Incorrect use of define");
}
let value = evaluate(args[1], scope);
scope[args[0].name] = value;
return value;
};
```
### The environment

The scope accepted by evaluate is an object with properties whose
names correspond to binding names and whose values correspond to the


values those bindings are bound to. Let’s define an object to represent
the global scope.
To be able to use the ifconstruct we just defined, we must have
access to Boolean values. Since there are only two Boolean values, we
do not need special syntax for them. We simply bind two names to the
valuestrueandfalseand use them.

```
const topScope = Object.create(null);
```
```
topScope.true = true;
topScope.false = false;
```
We can now evaluate a simple expression that negates a Boolean value.

```
let prog = parse(`if(true, false, true)`);
console.log(evaluate(prog, topScope));
// → false
```
To supply basic arithmetic and comparison operators, we will also add
some function values to the scope. In the interest of keeping the code
short, we’ll useFunctionto synthesize a bunch of operator functions in
a loop instead of defining them individually.

```
for (let op of ["+", "-", "*", "/", "==", "<", ">"]) {
topScope[op] = Function("a, b", `return a ${op} b;`);
}
```
It is also useful to have a way to output values, so we’ll wrapconsole.log
in a function and call itprint.

```
topScope.print = value => {
```

```
console.log(value);
return value;
};
```
That gives us enough elementary tools to write simple programs. The
following function provides a convenient way to parse a program and
run it in a fresh scope:

```
function run(program) {
return evaluate(parse(program), Object.create(topScope));
}
```
We’ll use object prototype chains to represent nested scopes so that
the program can add bindings to its local scope without changing the
top-level scope.

```
run(`
do(define(total, 0),
define(count, 1),
while(<(count, 11),
do(define(total, +(total, count)),
define(count, +(count, 1)))),
print(total))
`);
// → 55
```
This is the program we’ve seen several times before that computes the
sum of the numbers 1 to 10, expressed in Egg. It is clearly uglier
than the equivalent JavaScript program—but not bad for a language
implemented in fewer than 150 lines of code.


### Functions.

A programming language without functions is a poor programming lan-
guage indeed. Fortunately, it isn’t hard to add afunconstruct, which
treats its last argument as the function’s body and uses all arguments
before that as the names of the function’s parameters.

```
specialForms.fun = (args, scope) => {
if (!args.length) {
throw new SyntaxError("Functions need a body");
}
let body = args[args.length - 1];
let params = args.slice(0, args.length - 1).map(expr => {
if (expr.type != "word") {
throw new SyntaxError("Parameter names must be words");
}
return expr.name;
});
```
```
return function(...args) {
if (args.length != params.length) {
throw new TypeError("Wrong number of arguments");
}
let localScope = Object.create(scope);
for (let i = 0; i < args.length; i++) {
localScope[params[i]] = args[i];
}
return evaluate(body, localScope);
};
};
```

Functions in Egg get their own local scope. The function produced by
thefunform creates this local scope and adds the argument bindings
to it. It then evaluates the function body in this scope and returns the
result.

```
run(`
do(define(plusOne, fun(a, +(a, 1))),
print(plusOne(10)))
`);
// → 11
```
```
run(`
do(define(pow, fun(base, exp,
if(==(exp, 0),
1,
*(base, pow(base, -(exp, 1)))))),
print(pow(2, 10)))
`);
// → 1024
```
### Compilation

What we have built is an interpreter. During evaluation, it acts directly
on the representation of the program produced by the parser.
_Compilation_ is the process of adding another step between the pars-
ing and the running of a program, which transforms the program into
something that can be evaluated more eﬀiciently by doing as much
work as possible in advance. For example, in well-designed languages it


is obvious, for each use of a binding, which binding is being referred to,
without actually running the program. This can be used to avoid look-
ing up the binding by name every time it is accessed, instead directly
fetching it from some predetermined memory location.
Traditionally, compilation involves converting the program to ma-
chine code, the raw format that a computer’s processor can execute.
But any process that converts a program to a different representation
can be thought of as compilation.
It would be possible to write an alternative evaluation strategy for
Egg, one that first converts the program to a JavaScript program, uses
Functionto invoke the JavaScript compiler on it, and runs the result.
When done right, this would make Egg run very fast while still being
quite simple to implement.
If you are interested in this topic and willing to spend some time on
it, I encourage you to try to implement such a compiler as an exercise.

### Cheating

When we defined ifandwhile, you probably noticed that they were
more or less trivial wrappers around JavaScript’s own if and while

. Similarly, the values in Egg are just regular old JavaScript values.
Bridging the gap to a more primitive system, such as the machine code
the processor understands, takes more effort—but the way it works
resembles what we are doing here.
    Though the toy language in this chapter doesn’t do anything that
couldn’t be done better in JavaScript, there _are_ situations where writing


small languages helps get real work done.
Such a language does not have to resemble a typical programming
language. If JavaScript didn’t come equipped with regular expressions,
for example, you could write your own parser and evaluator for regular
expressions.
Or imagine you are building a program that makes it possible to
quickly create parsers by providing a logical description of the language
they need to parse. You could define a specific notation for that, and a
compiler that compiles it to a parser program.

```
expr = number | string | name | application
```
```
number = digit+
```
```
name = letter+
```
```
string = '"' (! '"')* '"'
```
```
application = expr '(' (expr (',' expr)*)? ')'
```
This is what is usually called a _domain-specific language_ , a language
tailored to express a narrow domain of knowledge. Such a language
can be more expressive than a general-purpose language because it is
designed to describe exactly the things that need to be described in its
domain and nothing else.


### Exercises

**Arrays**

Add support for arrays to Egg by adding the following three functions
to the top scope: array(...values)to construct an array containing the
argument values,length(array)to get an array’s length, andelement(
array, n)to fetch the _n_ th element from an array.

**Closure**

The way we have definedfun allows functions in Egg to reference the
surrounding scope, allowing the function’s body to use local values that
were visible at the time the function was defined, just like JavaScript
functions do.
The following program illustrates this: functionfreturns a function
that adds its argument tof’s argument, meaning that it needs access
to the local scope insidefto be able to use bindinga.

```
run(`
do(define(f, fun(a, fun(b, +(a, b)))),
print(f(4)(5)))
`);
// → 9
```
Go back to the definition of thefunform and explain which mechanism
causes this to work.


**Comments**

It would be nice if we could write comments in Egg. For example,
whenever we find a hash sign (#), we could treat the rest of the line as
a comment and ignore it, similar to//in JavaScript.
We do not have to make any big changes to the parser to support
this. We can simply changeskipSpaceto skip comments as if they are
whitespace so that all the points whereskipSpaceis called will now also
skip comments. Make this change.

**Fixingscope**

Currently, the only way to assign a binding a value is define. This
construct acts as a way both to define new bindings and to give existing
ones a new value.
This ambiguity causes a problem. When you try to give a nonlocal
binding a new value, you will end up defining a local one with the same
name instead. Some languages work like this by design, but I’ve always
found it an awkward way to handle scope.
Add a special form set, similar to define, which gives a binding a
new value, updating the binding in an outer scope if it doesn’t already
exist in the inner scope. If the binding is not defined at all, throw a
ReferenceError(another standard error type).
The technique of representing scopes as simple objects, which has
made things convenient so far, will get in your way a little at this
point. You might want to use theObject.getPrototypeOffunction, which
returns the prototype of an object. Also remember that you can use


Object.hasOwnto find out if a given object has a property.


```
“The dream behind the web is of a common information space
in which we communicate by sharing information. Its
universality is essential: the fact that a hypertext link can
point to anything, be it personal, local or global, be it draft or
highly polished.”
—Tim Berners-Lee, The World Wide Web: A Very Short
Personal Pistory
```
**Chapter13**

## JavaScriptandtheBrowser

The next chapters of this book will discuss web browsers. Without
browsers, there would be no JavaScript—or if there were, no one would
ever have paid any attention to it.
Web technology has been decentralized from the start, not just tech-
nically but also in terms of the way it evolved. Various browser vendors
have added new functionality in ad hoc and sometimes poorly thought-
out ways, which were then—sometimes—adopted by others, and finally
set down in standards.
This is both a blessing and a curse. On the one hand, it is empower-
ing to not have a central party control a system but have it be improved
by various parties working in loose collaboration (or occasionally, open
hostility). On the other hand, the haphazard way in which the web was
developed means that the resulting system is not exactly a shining ex-
ample of internal consistency. Some parts of it are downright confusing
and badly designed.


### Networks and the Internet

Computer networks have been around since the 1950s. If you put cables
between two or more computers and allow them to send data back and
forth through these cables, you can do all kinds of wonderful things.
If connecting two machines in the same building allows us to do won-
derful things, connecting machines all over the planet should be even
better. The technology to start implementing this vision was developed
in the 1980s, and the resulting network is called the _internet_. It has
lived up to its promise.
A computer can use this network to shoot bits at another computer.
For any effective communication to arise out of this bit-shooting, the
computers on both ends must know what the bits are supposed to rep-
resent. The meaning of any given sequence of bits depends entirely
on the kind of thing that it is trying to express and on the encoding
mechanism used.
A _network protocol_ describes a style of communication over a network.
There are protocols for sending email, for fetching email, for sharing
files, and even for controlling computers that happen to be infected by
malicious software.
The _HyperText Transfer Protocol_ (HTTP) is a protocol for retrieving
named resources (chunks of information, such as web pages or pictures).
It specifies that the side making the request should start with a line like
this, naming the resource and the version of the protocol that it is trying
to use:

```
GET /index.html HTTP/1.1
```

There are many more rules about the way the requester can include
more information in the request and the way the other side, which
returns the resource, packages up its content. We’ll look at HTTP in a
little more detail inChapter 18.
Most protocols are built on top of other protocols. HTTP treats the
network as a streamlike device into which you can put bits and have
them arrive at the correct destination in the correct order. Providing
those guarantees on top of the primitive data-sending that the network
gives you is already a rather tricky problem.
The _Transmission Control Protocol_ (TCP) is a protocol that ad-
dresses this problem. All internet-connected devices “speak” it, and
most communication on the internet is built on top of it.
A TCP connection works as follows: one computer must be waiting,
or _listening_ , for other computers to start talking to it. To be able to
listen for different kinds of communication at the same time on a single
machine, each listener has a number (called a _port_ ) associated with
it. Most protocols specify which port should be used by default. For
example, when we want to send an email using the SMTP protocol, the
machine through which we send it is expected to be listening on port
25.
Another computer can then establish a connection by connecting to
the target machine using the correct port number. If the target ma-
chine can be reached and is listening on that port, the connection is
successfully created. The listening computer is called the _server_ , and
the connecting computer is called the _client_.
Such a connection acts as a two-way pipe through which bits can


flow—the machines on both ends can put data into it. Once the bits
are successfully transmitted, they can be read out again by the machine
on the other side. This is a convenient model. You could say that TCP
provides an abstraction of the network.

### The Web

The _World Wide Web_ (not to be confused with the internet as a whole)
is a set of protocols and formats that allow us to visit web pages in a
browser. The word _Web_ refers to the fact that such pages can easily
link to each other, thus connecting into a huge mesh that users can
move through.
To become part of the web, all you need to do is connect a machine
to the internet and have it listen on port 80 with the HTTP protocol
so that other computers can ask it for documents.
Each document on the web is named by a _uniform resource locator_
(URL), which looks something like this:

```
http://eloquentjavascript.net/13_browser.html
| | | |
protocol server path
```
The first part tells us that this URL uses the HTTP protocol (as op-
posed to, for example, encrypted HTTP, which would be _https://_ ).
Then comes the part that identifies which server we are requesting the
document from. Last is a path string that identifies the document (or
_resource_ ) we are interested in.


Machines connected to the internet get an _IP address_ , a number that
can be used to send messages to that machine, and looks something
like 149.210.142.219 or 2001:4860:4860::8888. Since lists of more or
less random numbers are hard to remember and awkward to type, you
can instead register a _domain name_ for an address or set of addresses. I
registered _eloquentjavascript.net_ to point at the IP address of a machine
I control and can thus use that domain name to serve web pages.
If you type this URL into your browser’s address bar, the browser
will try to retrieve and display the document at that URL. First, your
browser has to find out what address _eloquentjavascript.net_ refers to.
Then, using the HTTP protocol, it will make a connection to the server
at that address and ask for the resource _/13_browser.html_. If all goes
well, the server sends back a document, which your browser then dis-
plays on your screen.

### HTML

_HTML_ , which stands for HyperText Markup Language, is the document
format used for web pages. An HTML document contains text, as well
as _tags_ that give structure to the text, describing things such as links,
paragraphs, and headings.
A short HTML document might look like this:
<!doctype html>
<html>
<head>
<meta charset="utf-8">


```
<title>My home page</title>
</head>
<body>
<h1>My home page</h1>
<p>Hello, I am Marijn and this is my home page.</p>
<p>I also wrote a book! Read it
<a href="http://eloquentjavascript.net">here</a>.</p>
</body>
</html>
```
This is what such a document would look like in the browser:

The tags, wrapped in angle brackets (<and>, the symbols for _less
than_ and _greater than_ ), provide information about the structure of the
document. The other text is just plain text.
The document starts with<!doctype html>, which tells the browser
to interpret the page as _modern_ HTML, as opposed to obsolete styles
used in the past.
HTML documents have a head and a body. The head contains in-
formation _about_ the document, and the body contains the document
itself. In this case, the head declares that the title of this document
is “My home page” and that it uses the UTF-8 encoding, which is a
way to encode Unicode text as binary data. The document’s body


contains a heading (<h1>, meaning “heading 1”—<h2>to<h6>produce
subheadings) and two paragraphs (<p>).
Tags come in several forms. An element, such as the body, a para-
graph, or a link, is started by an _opening tag_ like<p> and ended by
a _closing tag_ like </p>. Some opening tags, such as the one for the
link (<a>), contain extra information in the form ofname="value"pairs.
These are called _attributes_. In this case, the destination of the link is in-
dicated withhref="http://eloquentjavascript.net", wherehrefstands
for “hypertext reference”.
Some kinds of tags do not enclose anything and thus do not need to
be closed. The metadata tag<meta charset="utf-8">is an example of
this.
To be able to include angle brackets in the text of a document even
though they have a special meaning in HTML, yet another form of
special notation has to be introduced. A plain opening angle bracket is
written as&lt; (“less than”), and a closing bracket is written as&gt;
(“greater than”). In HTML, an ampersand (&) character followed by a
name or character code and a semicolon (;) is called an _entity_ and will
be replaced by the character it encodes.
This is analogous to the way backslashes are used in JavaScript
strings. Since this mechanism gives ampersand characters a special
meaning too, they need to be escaped as&amp;. Inside attribute values,
which are wrapped in double quotes, &quot; can be used to insert a
literal quote character.
HTML is parsed in a remarkably error-tolerant way. When tags that
should be there are missing, the browser automatically adds them. The


way this is done has been standardized, and you can rely on all modern
browsers to do it in the same way.
The following document will be treated just like the one shown pre-
viously:

```
<!doctype html>
```
```
<meta charset=utf-8>
<title>My home page</title>
```
```
<h1>My home page</h1>
<p>Hello, I am Marijn and this is my home page.
<p>I also wrote a book! Read it
<a href=http://eloquentjavascript.net>here</a>.
```
The<html>,<head>, and<body>tags are completely gone. The browser
knows that<meta>and<title>belong in the head and that<h1>means
the body has started. Furthermore, I am no longer explicitly closing
the paragraphs, since opening a new paragraph or ending the document
will close them implicitly. The quotes around the attribute values are
also gone.
This book will usually omit the<html>,<head>, and<body>tags from
examples to keep them short and free of clutter. I _will_ close tags and
include quotes around attributes, though.
I will also usually omit the doctype andcharsetdeclaration. Don’t
take this as encouragement to drop these from HTML documents.
Browsers will often do ridiculous things when you forget them. Con-
sider the doctype and thecharsetmetadata to be implicitly present in


examples, even when they are not actually shown in the text.

### HTML and JavaScript

In the context of this book, the most important HTML tag is<script>,
which allows us to include a piece of JavaScript in a document.

```
<h1>Testing alert</h1>
<script>alert("hello!");</script>
```
Such a script will run as soon as its<script>tag is encountered while
the browser reads the HTML. This page will pop up a dialog when
opened—thealertfunction resemblesprompt, in that it pops up a little
window, but only shows a message without asking for input.
Including large programs directly in HTML documents is often im-
practical. The <script>tag can be given an srcattribute to fetch a
script file (a text file containing a JavaScript program) from a URL.

```
<h1>Testing alert</h1>
<script src="code/hello.js"></script>
```
The _code/hello.js_ file included here contains the same program—alert
("hello!"). When an HTML page references other URLs as part of
itself, such as an image file or a script, web browsers will retrieve them
immediately and include them in the page.
A script tag must always be closed with</script>, even if it refers
to a script file and doesn’t contain any code. If you forget this, the rest
of the page will be interpreted as part of the script.


You can load ES modules (seeChapter 10) in the browser by giving
your script tag atype="module"attribute. Such modules can depend on
other modules by using URLs relative to themselves as module names
inimportdeclarations.
Some attributes can also contain a JavaScript program. The<button>
tag (which shows up as a button) supports anonclickattribute. The
attribute’s value will be run whenever the button is clicked.

```
<button onclick="alert('Boom!');">DO NOT PRESS</button>
```
Note that I had to use single quotes for the string in theonclickat-
tribute because double quotes are already used to quote the whole at-
tribute. I could also have used&quot;to escape the inner quotes.

### In the sandbox.

Running programs downloaded from the internet is potentially danger-
ous. You don’t know much about the people behind most sites you
visit, and they do not necessarily mean well. Running programs by
malicious actors is how you get your computer infected by viruses, your
data stolen, and your accounts hacked.
Yet the attraction of the web is that you can browse it without nec-
essarily trusting all the pages you visit. This is why browsers severely
limit the things a JavaScript program may do: it can’t look at the files
on your computer or modify anything not related to the web page it
was embedded in.
Isolating a programming environment in this way is called _sandboxing_ ,


the idea being that the program is harmlessly playing in a sandbox. But
you should imagine this particular kind of sandbox as having a cage of
thick steel bars over it so that the programs playing in it can’t actually
get out.
The hard part of sandboxing is allowing programs enough room to
be useful while restricting them from doing anything dangerous. Lots
of useful functionality, such as communicating with other servers or
reading the content of the copy-paste clipboard, can also be used for
problematic, privacy-invading purposes.
Every now and then, someone comes up with a new way to circumvent
the limitations of a browser and do something harmful, ranging from
leaking minor private information to taking over the whole machine on
which the browser is running. The browser developers respond by fixing
the hole, and all is well again—until the next problem is discovered, and
hopefully publicized rather than secretly exploited by some government
agency or criminal organization.

### Compatibility and the browser wars

In the early stages of the web, a browser called Mosaic dominated the
market. After a few years, the balance shifted to Netscape, which was,
in turn, largely supplanted by Microsoft’s Internet Explorer. At any
point where a single browser was dominant, that browser’s vendor would
feel entitled to unilaterally invent new features for the web. Since most
users used the most popular browser, websites would simply start using
those features—never mind the other browsers.


This was the dark age of compatibility, often called the _browser wars_.
Web developers were left with not one unified web but two or three
incompatible platforms. To make things worse, the browsers in use
around 2003 were all full of bugs, and of course the bugs were different
for each browser. Life was hard for people writing web pages.
Mozilla Firefox, a not-for-profit offshoot of Netscape, challenged In-
ternet Explorer’s position in the late 2000s. Because Microsoft was
not particularly interested in staying competitive at the time, Firefox
took a lot of market share away from it. Around the same time, Google
introduced its Chrome browser and Apple’s Safari browser gained popu-
larity, leading to a situation where there were four major players, rather
than one.
The new players had a more serious attitude toward standards and
better engineering practices, giving us less incompatibility and fewer
bugs. Microsoft, seeing its market share crumble, came around and
adopted these attitudes in its Edge browser, which replaced Internet
Explorer. If you are starting to learn web development today, consider
yourself lucky. The latest versions of the major browsers behave quite
uniformly and have relatively few bugs.
Unfortunately, with Firefox’s market share getting ever smaller, and
Edge becoming just a wrapper around Chrome’s core in 2018, this uni-
formity might once again take the form of a single vendor—Google, this
time—having enough control over the browser market to push its idea
of what the web should look like onto the rest of the world.
For what it is worth, this long chain of historical events and acci-
dents has produced the web platform that we have today. In the next


chapters, we are going to write programs for it.


```
“Too bad! Same old story! Once you’ve finished building your
house you notice you’ve accidentally learned something that
you really should have known—before you started.”
—Friedrich Nietzsche, Beyond Good and Evil
```
**Chapter14**

## TheDocumentObjectModel

When you open a web page, your browser retrieves the page’s HTML
text and parses it, much like our parser fromChapter 12parsed pro-
grams. The browser builds up a model of the document’s structure and
uses this model to draw the page on the screen.
This representation of the document is one of the toys that a JavaScript
program has available in its sandbox. It is a data structure that you
can read or modify. It acts as a _live_ data structure: when it’s modified,
the page on the screen is updated to reflect the changes.

### Document structure.

You can imagine an HTML document as a nested set of boxes. Tags
such as<body> and</body>enclose other tags, which in turn contain
other tags or text. Here’s the example document from the previous
chapter:

```
<!doctype html>
<html>
```

```
<head>
<title>My home page</title>
</head>
<body>
<h1>My home page</h1>
<p>Hello, I am Marijn and this is my home page.</p>
<p>I also wrote a book! Read it
<a href="http://eloquentjavascript.net">here</a>.</p>
</body>
</html>
```
This page has the following structure:

```
here
```
```
a
I also wrote a book! Read it.
```
```
p
```
```
Hello, I am Marijn and this is...
```
```
p
```
```
My home page
```
```
h1
```
```
body
```
```
My home page
```
```
title
```
```
head
```
```
html
```

The data structure the browser uses to represent the document fol-
lows this shape. For each box, there is an object, which we can interact
with to find out things such as what HTML tag it represents and which
boxes and text it contains. This representation is called the _Document
Object Model_ , or _DOM_ for short.
The global binding document gives us access to these objects. Its
documentElement property refers to the object representing the<html>
tag. Since every HTML document has a head and a body, it also has
headandbodyproperties pointing at those elements.

### Trees

Think back to the syntax trees fromChapter 12for a moment. Their
structures are strikingly similar to the structure of a browser’s docu-
ment. Each _node_ may refer to other nodes, _children_ , which in turn
may have their own children. This shape is typical of nested structures,
where elements can contain subelements that are similar to themselves.
We call a data structure a _tree_ when it has a branching structure, no
cycles (a node may not contain itself, directly or indirectly), and a sin-
gle, well-defined _root_. In the case of the DOM,document.documentElement
serves as the root.
Trees come up a lot in computer science. In addition to representing
recursive structures such as HTML documents or programs, they are
often used to maintain sorted sets of data because elements can usually
be found or inserted more eﬀiciently in a tree than in a flat array.
A typical tree has different kinds of nodes. The syntax tree forthe


Egg languagehad identifiers, values, and application nodes. Applica-
tion nodes may have children, whereas identifiers and values are _leaves_ ,
or nodes without children.
The same goes for the DOM. Nodes for _elements_ , which represent
HTML tags, determine the structure of the document. These can have
child nodes. An example of such a node isdocument.body. Some of these
children can be leaf nodes, such as pieces of text or comment nodes.
Each DOM node object has a nodeTypeproperty, which contains a
code (number) that identifies the type of node. Elements have code
1, which is also defined as the constant property Node.ELEMENT_NODE.
Text nodes, representing a section of text in the document, get code 3
(Node.TEXT_NODE). Comments have code 8 (Node.COMMENT_NODE).
Another way to visualize our document tree is as follows:

```
html head title My home page
body h1 My home page
p Hello! I am...
p I also wrote...
a here
.
```
The leaves are text nodes, and the arrows indicate parent-child rela-
tionships between nodes.


### The standard.

Using cryptic numeric codes to represent node types is not a very
JavaScript-like thing to do. Later in this chapter, we’ll see that other
parts of the DOM interface also feel cumbersome and alien. This is be-
cause the DOM interface wasn’t designed for JavaScript alone. Rather,
it tries to be a language-neutral interface that can be used in other sys-
tems as well—not just for HTML but also for XML, which is a generic
data format with an HTML-like syntax.
This is unfortunate. Standards are often useful. But in this case,
the advantage (cross-language consistency) isn’t all that compelling.
Having an interface that is properly integrated with the language you’re
using will save you more time than having a familiar interface across
languages.
As an example of this poor integration, consider thechildNodesprop-
erty that element nodes in the DOM have. This property holds an
array-like object with alengthproperty and properties labeled by num-
bers to access the child nodes. But it is an instance of the NodeList
type, not a real array, so it does not have methods such assliceand
map.
Then there are issues that are simply caused by poor design. For
example, there is no way to create a new node and immediately add
children or attributes to it. Instead, you have to first create it and then
add the children and attributes one by one, using side effects. Code
that interacts heavily with the DOM tends to get long, repetitive, and
ugly.
But these flaws aren’t fatal. Since JavaScript allows us to create


our own abstractions, it is possible to design improved ways to express
the operations we are performing. Many libraries intended for browser
programming come with such tools.

### Moving through the tree

DOM nodes contain a wealth of links to other nearby nodes. The
following diagram illustrates these:

```
I also wrote a book! ...
```
```
p
```
```
Hello, I am Marijn...
```
```
p
```
```
My home page
```
```
h1
```
```
body
0
```
```
1
```
```
2
```
```
childNodes firstChild
```
```
lastChild
```
```
previousSibling
```
```
nextSibling
```
```
parentNode
```
Although the diagram shows only one link of each type, every node
has aparentNodeproperty that points to the node it is part of, if any.
Likewise, every element node (node type 1) has achildNodesproperty
that points to an array-like object holding its children.
In theory, you could move anywhere in the tree using just these par-
ent and child links. But JavaScript also gives you access to a number
of additional convenience links. The firstChild and lastChild prop-


erties point to the first and last child elements or have the valuenull
for nodes without children. Similarly,previousSiblingandnextSibling
point to adjacent nodes, which are nodes with the same parent that
appear immediately before or after the node itself. For a first child,
previousSibling will be null, and for a last child,nextSiblingwill be
null.
There’s also thechildrenproperty, which is likechildNodesbut con-
tains only element (type 1) children, not other types of child nodes.
This can be useful when you aren’t interested in text nodes.
When dealing with a nested data structure like this one, recursive
functions are often useful. The following function scans a document for
text nodes containing a given string and returnstruewhen it has found
one:

```
function talksAbout(node, string) {
if (node.nodeType == Node.ELEMENT_NODE) {
for (let child of node.childNodes) {
if (talksAbout(child, string)) {
return true;
}
}
return false;
} else if (node.nodeType == Node.TEXT_NODE) {
return node.nodeValue.indexOf(string) > -1;
}
}
```
```
console.log(talksAbout(document.body, "book"));
// → true
```

ThenodeValueproperty of a text node holds the string of text that it
represents.

### Finding elements

Navigating these links among parents, children, and siblings is often
useful. But if we want to find a specific node in the document, reaching
it by starting atdocument.bodyand following a fixed path of properties
is a bad idea. Doing so bakes assumptions into our program about
the precise structure of the document—a structure you might want to
change later. Another complicating factor is that text nodes are created
even for the whitespace between nodes. The example document’s<body
>tag has not just three children (<h1>and two<p>elements), but seven:
those three, plus the spaces before, after, and between them.
If we want to get the href attribute of the link in that document,
we don’t want to say something like “Get the second child of the sixth
child of the document body”. It’d be better if we could say “Get the
first link in the document”. And we can.

```
let link = document.body.getElementsByTagName("a")[0];
console.log(link.href);
```
All element nodes have agetElementsByTagNamemethod, which collects
all elements with the given tag name that are descendants (direct or
indirect children) of that node and returns them as an array-like object.
To find a specific _single_ node, you can give it anidattribute and use
document.getElementByIdinstead.


```
<p>My ostrich Gertrude:</p>
<p><img id="gertrude" src="img/ostrich.png"></p>
```
```
<script>
let ostrich = document.getElementById("gertrude");
console.log(ostrich.src);
</script>
```
A third, similar method isgetElementsByClassName, which, likegetElementsByTagName
, searches through the contents of an element node and retrieves all
elements that have the given string in theirclassattribute.

### Changing the document

Almost everything about the DOM data structure can be changed. The
shape of the document tree can be modified by changing parent-child
relationships. Nodes have aremovemethod to remove them from their
current parent node. To add a child node to an element node, we can
use appendChild, which puts it at the end of the list of children, or
insertBefore, which inserts the node given as the first argument before
the node given as the second argument.

```
<p>One</p>
<p>Two</p>
<p>Three</p>
```
```
<script>
let paragraphs = document.body.getElementsByTagName("p");
document.body.insertBefore(paragraphs[2], paragraphs[0]);
```

```
</script>
```
A node can exist in the document in only one place. Thus, inserting
paragraph _Three_ in front of paragraph _One_ will first remove it from
the end of the document and then insert it at the front, resulting in
_Three_ / _One_ / _Two_. All operations that insert a node somewhere will, as
a side effect, cause it to be removed from its current position (if it has
one).
ThereplaceChildmethod is used to replace a child node with another
one. It takes as arguments two nodes: a new node and the node to be
replaced. The replaced node must be a child of the element the method
is called on. Note that bothreplaceChildandinsertBeforeexpect the
_new_ node as their first argument.

### Creating nodes.

Say we want to write a script that replaces all images (<img>tags) in
the document with the text held in theiraltattributes, which specifies
an alternative textual representation of the image. This involves not
only removing the images but also adding a new text node to replace
them.

```
<p>The <img src="img/cat.png" alt="Cat"> in the
<img src="img/hat.png" alt="Hat">.</p>
```
```
<p><button onclick="replaceImages()">Replace</button></p>
```
```
<script>
```

```
function replaceImages() {
let images = document.body.getElementsByTagName("img");
for (let i = images.length - 1; i >= 0; i--) {
let image = images[i];
if (image.alt) {
let text = document.createTextNode(image.alt);
image.parentNode.replaceChild(text, image);
}
}
}
</script>
```
Given a string,createTextNodegives us a text node that we can insert
into the document to make it show up on the screen.
The loop that goes over the images starts at the end of the list.
This is necessary because the node list returned by a method like
getElementsByTagName (or a property like childNodes) is _live_. That is,
it is updated as the document changes. If we started from the front,
removing the first image would cause the list to lose its first element
so that the second time the loop repeats, whereiis 1, it would stop
because the length of the collection is now also 1.
If you want a _solid_ collection of nodes, as opposed to a live one, you
can convert the collection to a real array by callingArray.from.

```
let arrayish = {0: "one", 1: "two", length: 2};
let array = Array.from(arrayish);
console.log(array.map(s => s.toUpperCase()));
// → ["ONE", "TWO"]
```
To create element nodes, you can use thedocument.createElementmethod.


This method takes a tag name and returns a new empty node of the
given type.
The following example defines a utilityelt, which creates an element
node and treats the rest of its arguments as children to that node. This
function is then used to add an attribution to a quote.

```
<blockquote id="quote">
No book can ever be finished. While working on it we learn
just enough to find it immature the moment we turn away
from it.
</blockquote>
```
```
<script>
function elt(type, ...children) {
let node = document.createElement(type);
for (let child of children) {
if (typeof child != "string") node.appendChild(child);
else node.appendChild(document.createTextNode(child));
}
return node;
}
```
```
document.getElementById("quote").appendChild(
elt("footer", "—",
elt("strong", "Karl Popper"),
", preface to the second edition of ",
elt("em", "The Open Society and Its Enemies"),
", 1950"));
</script>
```

This is what the resulting document looks like:

### Attributes

Some element attributes, such ashreffor links, can be accessed through
a property of the same name on the element’s DOM object. This is the
case for most commonly used standard attributes.
HTML allows you to set any attribute you want on nodes. This can
be useful because it allows you to store extra information in a document.
To read or change custom attributes, which aren’t available as regular
object properties, you have to use thegetAttributeand setAttribute
methods.

```
<p data-classified="secret">The launch code is 00000000.</p>
<p data-classified="unclassified">I have two feet.</p>
```
```
<script>
let paras = document.body.getElementsByTagName("p");
for (let para of Array.from(paras)) {
if (para.getAttribute("data-classified") == "secret") {
para.remove();
}
}
```

```
</script>
```
It is recommended to prefix the names of such made-up attributes with
data-to ensure they do not conflict with any other attributes.
There is a commonly used attribute,class, which is a keyword in the
JavaScript language. For historical reasons—some old JavaScript im-
plementations could not handle property names that matched keywords—
the property used to access this attribute is calledclassName. You can
also access it under its real name,"class", with thegetAttributeand
setAttributemethods.

### Layout

You may have noticed that different types of elements are laid out
differently. Some, such as paragraphs (<p>) or headings (<h1>), take up
the whole width of the document and are rendered on separate lines.
These are called _block_ elements. Others, such as links (<a>) or the <
strong>element, are rendered on the same line with their surrounding
text. Such elements are called _inline_ elements.
For any given document, browsers are able to compute a layout, which
gives each element a size and position based on its type and content.
This layout is then used to actually draw the document.
The size and position of an element can be accessed from JavaScript.
The offsetWidth and offsetHeight properties give you the space the
element takes up in _pixels_. A pixel is the basic unit of measurement in
the browser. It traditionally corresponds to the smallest dot that the
screen can draw, but on modern displays, which can draw _very_ small


dots, that may no longer be the case, and a browser pixel may span
multiple display dots.
Similarly,clientWidthandclientHeightgive you the size of the space
_inside_ the element, ignoring border width.

```
<p style="border: 3px solid red">
I'm boxed in
</p>
```
```
<script>
let para = document.body.getElementsByTagName("p")[0];
console.log("clientHeight:", para.clientHeight);
// → 19
console.log("offsetHeight:", para.offsetHeight);
// → 25
</script>
```
Giving a paragraph a border causes a rectangle to be drawn around it.

The most effective way to find the precise position of an element on
the screen is thegetBoundingClientRect method. It returns an object
withtop,bottom,left, andrightproperties, indicating the pixel posi-
tions of the sides of the element relative to the upper left of the screen.
If you want pixel positions relative to the whole document, you must
add the current scroll position, which you can find in thepageXOffset
andpageYOffsetbindings.
Laying out a document can be quite a lot of work. In the interest


of speed, browser engines do not immediately re-layout a document
every time you change it but wait as long as they can before doing
so. When a JavaScript program that changed the document finishes
running, the browser will have to compute a new layout to draw the
changed document to the screen. When a program _asks_ for the posi-
tion or size of something by reading properties such asoffsetHeightor
callinggetBoundingClientRect, providing that information also requires
computing a layout.
A program that repeatedly alternates between reading DOM layout
information and changing the DOM forces a lot of layout computations
to happen and will consequently run very slowly. The following code is
an example of this. It contains two different programs that build up a
line of _X_ characters 2,000 pixels wide and measures the time each one
takes.

```
<p><span id="one"></span></p>
<p><span id="two"></span></p>
```
```
<script>
function time(name, action) {
let start = Date.now(); // Current time in milliseconds
action();
console.log(name, "took", Date.now() - start, "ms");
}
```
```
time("naive", () => {
let target = document.getElementById("one");
while (target.offsetWidth < 2000) {
target.appendChild(document.createTextNode("X"));
```

```
}
});
// → naive took 32 ms
```
```
time("clever", function() {
let target = document.getElementById("two");
target.appendChild(document.createTextNode("XXXXX"));
let total = Math.ceil(2000 / (target.offsetWidth / 5));
target.firstChild.nodeValue = "X".repeat(total);
});
// → clever took 1 ms
</script>
```
### Styling

We have seen that different HTML elements are drawn differently.
Some are displayed as blocks, others inline. Some add styling—<strong>
makes its content bold, and<a>makes it blue and underlines it.
The way an<img>tag shows an image or an<a>tag causes a link to
be followed when it is clicked is strongly tied to the element type. But
we can change the styling associated with an element, such as the text
color or underline. Here is an example that uses thestyleproperty:

```
<p><a href=".">Normal link</a></p>
<p><a href="." style="color: green">Green link</a></p>
```
The second link will be green instead of the default link color:


A style attribute may contain one or more _declarations_ , which are a
property (such ascolor) followed by a colon and a value (such asgreen).
When there is more than one declaration, they must be separated by
semicolons, as in"color: red; border: none".
A lot of aspects of the document can be influenced by styling. For
example, thedisplayproperty controls whether an element is displayed
as a block or an inline element.

```
This text is displayed <strong>inline</strong>,
<strong style="display: block">as a block</strong>, and
<strong style="display: none">not at all</strong>.
```
The block tag will end up on its own line, since block elements are
not displayed inline with the text around them. The last tag is not
displayed at all—display: noneprevents an element from showing up
on the screen. This is a way to hide elements. It is often preferable to
removing them from the document entirely because it makes it easy to
reveal them again later.

JavaScript code can directly manipulate the style of an element through
the element’sstyleproperty. This property holds an object that has
properties for all possible style properties. The values of these proper-


ties are strings, which we can write to in order to change a particular
aspect of the element’s style.

```
<p id="para" style="color: purple">
Nice text
</p>
```
```
<script>
let para = document.getElementById("para");
console.log(para.style.color);
para.style.color = "magenta";
</script>
```
Some style property names contain hyphens, such asfont-family. Be-
cause such property names are awkward to work with in JavaScript
(you’d have to say style["font-family"]), the property names in the
style object for such properties have their hyphens removed and the
letters after them capitalized (style.fontFamily).

### Cascading styles

The styling system for HTML is called _CSS_ , for _Cascading Style Sheets_.
A _style sheet_ is a set of rules for how to style elements in a document.
It can be given inside a<style>tag.

```
<style>
strong {
font-style: italic;
color: gray;
```

```
}
</style>
<p>Now <strong>strong text</strong> is italic and gray.</p>
```
The _cascading_ in the name refers to the fact that multiple such rules are
combined to produce the final style for an element. In the example, the
default styling for<strong>tags, which gives themfont-weight: bold,
is overlaid by the rule in the<style>tag, which addsfont-styleand
color.
When multiple rules define a value for the same property, the most
recently read rule gets a higher precedence and wins. For example, if the
rule in the<style>tag includedfont-weight: normal, contradicting the
defaultfont-weightrule, the text would be normal, _not_ bold. Styles in a
styleattribute applied directly to the node have the highest precedence
and always win.
It is possible to target things other than tag names in CSS rules. A
rule for.abcapplies to all elements with"abc"in theirclassattribute.
A rule for #xyz applies to the element with an idattribute of "xyz"
(which should be unique within the document).

```
.subtle {
color: gray;
font-size: 80%;
}
#header {
background: blue;
color: white;
}
/* p elements with id main and with classes a and b */
```

```
p#main.a.b {
margin-bottom: 20px;
}
```
The precedence rule favoring the most recently defined rule applies only
when the rules have the same _specificity_. A rule’s specificity is a mea-
sure of how precisely it describes matching elements, determined by the
number and kind (tag, class, or ID) of element aspects it requires. For
example, a rule that targetsp.ais more specific than rules that target
por just.aand would thus take precedence over them.
The notationp > a ...{} applies the given styles to all<a> tags that
are direct children of<p>tags. Similarly,p a ...{}applies to all<a>tags
inside<p>tags, whether they are direct or indirect children.

### Query selectors.

We won’t be using style sheets very much in this book. Understand-
ing them is helpful when programming in the browser, but they are
complicated enough to warrant a separate book. The main reason I
introduced _selector_ syntax—the notation used in style sheets to deter-
mine which elements a set of styles apply to—is that we can use this
same mini-language as an effective way to find DOM elements.
ThequerySelectorAllmethod, which is defined both on thedocument
object and on element nodes, takes a selector string and returns a
NodeListcontaining all the elements that it matches.

```
<p>And if you go chasing
<span class="animal">rabbits</span></p>
```

```
<p>And you know you're going to fall</p>
<p>Tell 'em a <span class="character">hookah smoking
<span class="animal">caterpillar</span></span></p>
<p>Has given you the call</p>
```
```
<script>
function count(selector) {
return document.querySelectorAll(selector).length;
}
console.log(count("p")); // All <p> elements
// → 4
console.log(count(".animal")); // Class animal
// → 2
console.log(count("p .animal")); // Animal inside of <p>
// → 2
console.log(count("p > .animal")); // Direct child of <p>
// → 1
</script>
```
Unlike methods such asgetElementsByTagName, the object returned by
querySelectorAll is _not_ live. It won’t change when you change the
document. It is still not a real array, though, so you need to callArray
.fromif you want to treat it like one.
ThequerySelectormethod (without theAll part) works in a simi-
lar way. This one is useful if you want a specific single element. It
will return only the first matching element, or nullwhen no element
matches.


### Positioning and animating

Thepositionstyle property influences layout in a powerful way. It has
a default value ofstatic, meaning the element sits in its normal place
in the document. When it is set torelative, the element still takes up
space in the document, but now thetopandleftstyle properties can be
used to move it relative to that normal place. Whenpositionis set to
absolute, the element is removed from the normal document flow—that
is, it no longer takes up space and may overlap with other elements. Its
topandleftproperties can be used to absolutely position it relative to
the upper-left corner of the nearest enclosing element whoseposition
property isn’tstatic, or relative to the document if no such enclosing
element exists.
We can use this to create an animation. The following document
displays a picture of a cat that moves around in an ellipse:

```
<p style="text-align: center">
<img src="img/cat.png" style="position: relative">
</p>
<script>
let cat = document.querySelector("img");
let angle = Math.PI / 2;
function animate(time, lastTime) {
if (lastTime != null) {
angle += (time - lastTime) * 0.001;
}
cat.style.top = (Math.sin(angle) * 20) + "px";
cat.style.left = (Math.cos(angle) * 200) + "px";
requestAnimationFrame(newTime => animate(newTime, time));
```

```
}
requestAnimationFrame(animate);
</script>
```
The gray arrow shows the path along which the image moves.

Our picture is centered on the page and given apositionofrelative.
We’ll repeatedly update that picture’stopandleftstyles to move it.
The script usesrequestAnimationFrameto schedule theanimatefunc-
tion to run whenever the browser is ready to repaint the screen. The
animatefunction itself again callsrequestAnimationFrameto schedule the
next update. When the browser window (or tab) is active, this will
cause updates to happen at a rate of about 60 per second, which tends
to produce a good-looking animation.
If we just updated the DOM in a loop, the page would freeze, and
nothing would show up on the screen. Browsers do not update their
display while a JavaScript program is running, nor do they allow any
interaction with the page. This is why we needrequestAnimationFrame
—it lets the browser know that we are done for now, and it can go
ahead and do the things that browsers do, such as updating the screen
and responding to user actions.
The animation function is passed the current time as an argument.


To ensure that the motion of the cat per millisecond is stable, it bases
the speed at which the angle changes on the difference between the
current time and the last time the function ran. If it just moved the
angle by a fixed amount per step, the motion would stutter when, for
example, another heavy task running on the same computer prevented
the function from running for a fraction of a second.
Moving in circles is done using the trigonometry functionsMath.cos
and Math.sin. For those who aren’t familiar with these, I’ll briefly
introduce them, since we will occasionally use them in this book.
Math.cosandMath.sinare useful for finding points that lie on a circle
around point (0, 0) with a radius of 1. Both functions interpret their
argument as the position on this circle, with 0 denoting the point on the
far right of the circle, going clockwise until 2π(about 6.28) has taken
us around the whole circle. Math.costells you the x-coordinate of the
point that corresponds to the given position, andMath.sinyields the
y-coordinate. Positions (or angles) greater than 2πor less than 0 are
valid—the rotation repeats so that _a_ +2πrefers to the same angle as _a_.
This unit for measuring angles is called radians—a full circle is 2π
radians, similar to how it is 360 degrees when measuring in degrees.
The constantπis available asMath.PIin JavaScript.


```
cos(¼π)
```
```
sin(¼π)
```
```
cos(-⅔π)
```
```
sin(-⅔⅔ππ)sin(- )
```
The cat animation code keeps a counter,angle, for the current angle
of the animation and increments it every time theanimatefunction is
called. It can then use this angle to compute the current position of the
image element. Thetopstyle is computed withMath.sinand multiplied
by 20, which is the vertical radius of our ellipse. Theleftstyle is based
onMath.cosand multiplied by 200 so that the ellipse is much wider than
it is high.
Note that styles usually need _units_. In this case, we have to append
"px"to the number to tell the browser that we are counting in pixels (as
opposed to centimeters, “ems”, or other units). This is easy to forget.
Using numbers without units will result in your style being ignored—
unless the number is 0, which always means the same thing, regardless
of its unit.

### Summary

JavaScript programs may inspect and interfere with the document that
the browser is displaying through a data structure called the DOM. This


data structure represents the browser’s model of the document, and a
JavaScript program can modify it to change the visible document.
The DOM is organized like a tree, where elements are arranged hier-
archically according to the structure of the document. The objects rep-
resenting elements have properties such asparentNodeandchildNodes,
which can be used to navigate through this tree.
The way a document is displayed can be influenced by _styling_ , both
by attaching styles to nodes directly and by defining rules that match
certain nodes. There are many different style properties, such ascolor
ordisplay. JavaScript code can manipulate an element’s style directly
through itsstyleproperty.

### Exercises

**Buildatable**

An HTML table is built with the following tag structure:

```
<table>
<tr>
<th>name</th>
<th>height</th>
<th>place</th>
</tr>
<tr>
<td>Kilimanjaro</td>
<td>5895</td>
<td>Tanzania</td>
```

```
</tr>
</table>
```
For each _row_ , the<table>tag contains a<tr>tag. Inside of these<tr>
tags, we can put cell elements: either heading cells (<th>) or regular
cells (<td>).
Given a dataset of mountains, an array of objects withname,height
, and placeproperties, generate the DOM structure for a table that
enumerates the objects. It has one column per key and one row per
object, plus a header row with <th> elements at the top, listing the
column names.
Write this so that the columns are automatically derived from the
objects, by taking the property names of the first object in the data.
Show the resulting table in the document by appending it to the
element that has anidattribute of"mountains".
Once you have this working, right-align cells that contain number
values by setting theirstyle.textAlignproperty to"right".

**Elementsbytagname**

Thedocument.getElementsByTagNamemethod returns all child elements
with a given tag name. Implement your own version of this as a function
that takes a node and a string (the tag name) as arguments and returns
an array containing all descendant element nodes with the given tag
name. Your function should go through the document itself. It may
not use a method likequerySelectorAllto do the work.
To find the tag name of an element, use itsnodeNameproperty. But


note that this will return the tag name in all uppercase. Use the
toLowerCaseortoUpperCasestring methods to compensate for this.

**Thecat'shat**

Extend the cat animation definedearlierso that both the cat and his
hat (<img src="img/hat.png">) orbit at opposite sides of the ellipse.
Or make the hat circle around the cat. Or alter the animation in
some other interesting way.
To make positioning multiple objects easier, you’ll probably want
to switch to absolute positioning. This means thattop and leftare
counted relative to the upper left of the document. To avoid using
negative coordinates, which would cause the image to move outside of
the visible page, you can add a fixed number of pixels to the position
values.


```
“You have power over your mind—not outside events. Realize
this, and you will find strength.”
—Marcus Aurelius, Meditations
```
**Chapter15**

## HandlingEvents

Some programs work with direct user input, such as mouse and key-
board actions. That kind of input isn’t available ahead of time, as a
well-organized data structure—it comes in piece by piece, in real time,
and the program must respond to it as it happens.

### Event handlers.

Imagine an interface where the only way to find out whether a key on
the keyboard is being pressed is to read the current state of that key.
To be able to react to keypresses, you would have to constantly read the
key’s state to catch it before it is released again. It would be dangerous
to perform other time-intensive computations, since you might miss a
keypress.
Some primitive machines handle input like this. A step up from this
is for the hardware or operating system to notice the keypress and put
it in a queue. A program can then periodically check the queue for new
events and react to what it finds there.


Of course, the program has to remember to look at the queue, and
to do it often because any time between the key being pressed and the
program noticing the event will cause the software to feel unresponsive.
This approach is called _polling_. Most programmers prefer to avoid it.
A better mechanism is for the system to actively notify the code when
an event occurs. Browsers do this by allowing us to register functions
as _handlers_ for specific events.

```
<p>Click this document to activate the handler.</p>
<script>
window.addEventListener("click", () => {
console.log("You knocked?");
});
</script>
```
Thewindowbinding refers to a built-in object provided by the browser.
It represents the browser window that contains the document. Calling
itsaddEventListenermethod registers the second argument to be called
whenever the event described by its first argument occurs.

### Events and DOM nodes

Each browser event handler is registered in a context. In the previous
example, we calledaddEventListeneron thewindowobject to register a
handler for the whole window. Such a method can also be found on
DOM elements and some other types of objects. Event listeners are
called only when the event happens in the context of the object on
which they are registered.


```
<button>Click me</button>
<p>No handler here.</p>
<script>
let button = document.querySelector("button");
button.addEventListener("click", () => {
console.log("Button clicked.");
});
</script>
```
That example attaches a handler to the button node. Clicks on the
button cause that handler to run, but clicks on the rest of the document
do not.
Giving a node anonclickattribute has a similar effect. This works for
most types of events—you can attach a handler through the attribute
whose name is the event name withonin front of it.
But a node can have only oneonclickattribute, so you can register
only one handler per node that way. The addEventListener method
allows you to add any number of handlers meaning it’s safe to add
handlers even if there is already another handler on the element.
TheremoveEventListenermethod, called with arguments similar to
addEventListener, removes a handler.

```
<button>Act-once button</button>
<script>
let button = document.querySelector("button");
function once() {
console.log("Done.");
button.removeEventListener("click", once);
}
```

```
button.addEventListener("click", once);
</script>
```
The function given to removeEventListenerhas to be the same func-
tion value given toaddEventListener. When you need to unregister a
handler, you’ll want to give the handler function a name (once, in the
example) to be able to pass the same function value to both methods.

### Event objects.

Though we have ignored it so far, event handler functions are passed an
argument: the _event object_. This object holds additional information
about the event. For example, if we want to know _which_ mouse button
was pressed, we can look at the event object’sbuttonproperty.

```
<button>Click me any way you want</button>
<script>
let button = document.querySelector("button");
button.addEventListener("mousedown", event => {
if (event.button == 0) {
console.log("Left button");
} else if (event.button == 1) {
console.log("Middle button");
} else if (event.button == 2) {
console.log("Right button");
}
});
</script>
```

The information stored in an event object differs per type of event.
(We’ll discuss different types later in the chapter.) The object’stype
property always holds a string identifying the event (such as"click"or
"mousedown").

### Propagation

For most event types, handlers registered on nodes with children will
also receive events that happen in the children. If a button inside a
paragraph is clicked, event handlers on the paragraph will also see the
click event.
But if both the paragraph and the button have a handler, the more
specific handler—the one on the button—gets to go first. The event
is said to _propagate_ outward from the node where it happened to that
node’s parent node and on to the root of the document. Finally, after
all handlers registered on a specific node have had their turn, handlers
registered on the whole window get a chance to respond to the event.
At any point, an event handler can call thestopPropagationmethod
on the event object to prevent handlers further up from receiving the
event. This can be useful when, for example, you have a button inside
another clickable element and you don’t want clicks on the button to
activate the outer element’s click behavior.
The following example registers"mousedown"handlers on both a but-
ton and the paragraph around it. When clicked with the right mouse
button, the handler for the button calls stopPropagation, which will
prevent the handler on the paragraph from running. When the button


is clicked with another mouse button, both handlers will run.

```
<p>A paragraph with a <button>button</button>.</p>
<script>
let para = document.querySelector("p");
let button = document.querySelector("button");
para.addEventListener("mousedown", () => {
console.log("Handler for paragraph.");
});
button.addEventListener("mousedown", event => {
console.log("Handler for button.");
if (event.button == 2) event.stopPropagation();
});
</script>
```
Most event objects have atargetproperty that refers to the node where
they originated. You can use this property to ensure that you’re not
accidentally handling something that propagated up from a node you
do not want to handle.
It is also possible to use thetargetproperty to cast a wide net for
a specific type of event. For example, if you have a node containing a
long list of buttons, it may be more convenient to register a single click
handler on the outer node and have it use thetargetproperty to figure
out whether a button was clicked, rather than registering individual
handlers on all of the buttons.

```
<button>A</button>
<button>B</button>
<button>C</button>
<script>
```

```
document.body.addEventListener("click", event => {
if (event.target.nodeName == "BUTTON") {
console.log("Clicked", event.target.textContent);
}
});
</script>
```
### Default actions.

Many events have a default action. If you click a link, you will be taken
to the link’s target. If you press the down arrow, the browser will scroll
the page down. If you right-click, you’ll get a context menu. And so
on.
For most types of events, the JavaScript event handlers are called
_before_ the default behavior takes place. If the handler doesn’t want
this normal behavior to happen, typically because it has already taken
care of handling the event, it can call thepreventDefaultmethod on the
event object.
This can be used to implement your own keyboard shortcuts or con-
text menu. It can also be used to obnoxiously interfere with the be-
havior that users expect. For example, here is a link that cannot be
followed:

```
<a href="https://developer.mozilla.org/">MDN</a>
<script>
let link = document.querySelector("a");
link.addEventListener("click", event => {
```

```
console.log("Nope.");
event.preventDefault();
});
</script>
```
Try not to do such things without a really good reason. It’ll be unpleas-
ant for people who use your page when expected behavior is broken.
Depending on the browser, some events can’t be intercepted at all.
On Chrome, for example, the keyboard shortcut to close the current
tab (ctrl-W orcommand-W) cannot be handled by JavaScript.

### Key events

When a key on the keyboard is pressed, your browser fires a"keydown"
event. When it is released, you get a"keyup"event.

```
<p>This page turns violet when you hold the V key.</p>
<script>
window.addEventListener("keydown", event => {
if (event.key == "v") {
document.body.style.background = "violet";
}
});
window.addEventListener("keyup", event => {
if (event.key == "v") {
document.body.style.background = "";
}
});
</script>
```

Despite its name, "keydown"fires not only when the key is physically
pushed down. When a key is pressed and held, the event fires again
every time the key _repeats_. Sometimes you have to be careful about this.
For example, if you add a button to the DOM when a key is pressed
and remove it again when the key is released, you might accidentally
add hundreds of buttons when the key is held down longer.
The previous example looks at thekeyproperty of the event object
to see which key the event is about. This property holds a string that,
for most keys, corresponds to the thing that pressing that key would
type. For special keys such as enter, it holds a string that names
the key ("Enter", in this case). If you holdshiftwhile pressing a key,
that might also influence the name of the key—"v"becomes"V", and
"1"may become"!", if that is what pressingshift-1 produces on your
keyboard.
Modifier keys such asshift,ctrl,alt, andmeta(commandon
Mac) generate key events just like normal keys. When looking for key
combinations, you can also find out whether these keys are held down
by looking at theshiftKey,ctrlKey,altKey, andmetaKeyproperties of
keyboard and mouse events.

```
<p>Press Control-Space to continue.</p>
<script>
window.addEventListener("keydown", event => {
if (event.key == " " && event.ctrlKey) {
console.log("Continuing!");
}
});
</script>
```

The DOM node where a key event originates depends on the element
that has focus when the key is pressed. Most nodes cannot have focus
unless you give them atabindexattribute, but things like links, buttons,
and form fields can. We’ll come back to form fields inChapter 18. When
nothing in particular has focus,document.bodyacts as the target node
of key events.
When the user is typing text, using key events to figure out what is
being typed is problematic. Some platforms, most notably the virtual
keyboard on Android phones, don’t fire key events. But even when you
have an old-fashioned keyboard, some types of text input don’t match
keypresses in a straightforward way, such as _input method editor_ ( _IME_ )
software used by people whose scripts don’t fit on a keyboard, where
multiple keystrokes are combined to create characters.
To notice when something was typed, elements that you can type into,
such as the<input>and <textarea>tags, fire"input"events whenever
the user changes their content. To get the actual content that was
typed, it is best to directly read it from the focused field, which we
discuss inChapter 18.

### Pointer events

There are currently two widely used ways to point at things on a screen:
mice (including devices that act like mice, such as touchpads and track-
balls) and touchscreens. These produce different kinds of events.


**Mouseclicks**

Pressing a mouse button causes a number of events to fire. The "
mousedown" and"mouseup"events are similar to"keydown"and"keyup"
and fire when the button is pressed and released. These happen on the
DOM nodes that are immediately below the mouse pointer when the
event occurs.
After the "mouseup"event, a "click" event fires on the most spe-
cific node that contained both the press and the release of the button.
For example, if I press down the mouse button on one paragraph and
then move the pointer to another paragraph and release the button,
the"click"event will happen on the element that contains both those
paragraphs.
If two clicks happen close together, a"dblclick"(double-click) event
also fires, after the second click event.
To get precise information about the place where a mouse event hap-
pened, you can look at itsclientXandclientYproperties, which contain
the event’s coordinates (in pixels) relative to the upper-left corner of the
window, orpageXandpageY, which are relative to the upper-left corner
of the whole document (which may be different when the window has
been scrolled).
The following program implements a primitive drawing application.
Every time you click the document, it adds a dot under your mouse
pointer.

```
<style>
body {
height: 200px;
```

```
background: beige;
}
.dot {
height: 8px; width: 8px;
border-radius: 4px; /* rounds corners */
background: teal;
position: absolute;
}
</style>
<script>
window.addEventListener("click", event => {
let dot = document.createElement("div");
dot.className = "dot";
dot.style.left = (event.pageX - 4) + "px";
dot.style.top = (event.pageY - 4) + "px";
document.body.appendChild(dot);
});
</script>
```
We’ll create a less primitive drawing application inChapter 19.

**Mousemotion**

Every time the mouse pointer moves, a"mousemove" event fires. This
event can be used to track the position of the mouse. A common situa-
tion in which this is useful is when implementing some form of mouse-
dragging functionality.
As an example, the following program displays a bar and sets up
event handlers so that dragging to the left or right on this bar makes it


narrower or wider:

```
<p>Drag the bar to change its width:</p>
<div style="background: orange; width: 60px; height: 20px">
</div>
<script>
let lastX; // Tracks the last observed mouse X position
let bar = document.querySelector("div");
bar.addEventListener("mousedown", event => {
if (event.button == 0) {
lastX = event.clientX;
window.addEventListener("mousemove", moved);
event.preventDefault(); // Prevent selection
}
});
```
```
function moved(event) {
if (event.buttons == 0) {
window.removeEventListener("mousemove", moved);
} else {
let dist = event.clientX - lastX;
let newWidth = Math.max(10, bar.offsetWidth + dist);
bar.style.width = newWidth + "px";
lastX = event.clientX;
}
}
</script>
```
The resulting page looks like this:


Note that the"mousemove"handler is registered on the whole window.
Even if the mouse goes outside of the bar during resizing, as long as
the button is held, we still want to update its size.
We must stop resizing the bar when the mouse button is released.
For that, we can use thebuttonsproperty (note the plural), which tells
us about the buttons that are currently held down. When it is 0, no
buttons are down. When buttons are held, the value of the buttons
property is the sum of the codes for those buttons—the left button has
code 1, the right button 2, and the middle one 4. With the left and
right buttons held, for example, the value ofbuttonswill be 3.
Note that the order of these codes is different from the one used by
button, where the middle button came before the right one. As men-
tioned, consistency isn’t a strong point of the browser’s programming
interface.

**Touchevents**

The style of graphical browser that we use was designed with mouse
interfaces in mind, at a time where touchscreens were rare. To make
the web “work” on early touchscreen phones, browsers for those devices
pretended, to a certain extent, that touch events were mouse events.
If you tap your screen, you’ll get"mousedown","mouseup", and"click"
events.


But this illusion isn’t very robust. A touchscreen doesn’t work like a
mouse: it doesn’t have multiple buttons, you can’t track the finger when
it isn’t on the screen (to simulate"mousemove"), and it allows multiple
fingers to be on the screen at the same time.
Mouse events cover touch interaction only in straightforward cases—
if you add a"click"handler to a button, touch users will still be able
to use it. But something like the resizeable bar in the previous example
does not work on a touchscreen.
There are specific event types fired by touch interaction. When a
finger starts touching the screen, you get a"touchstart"event. When
it is moved while touching, "touchmove" events fire. Finally, when it
stops touching the screen, you’ll see a"touchend"event.
Because many touchscreens can detect multiple fingers at the same
time, these events don’t have a single set of coordinates associated with
them. Rather, their event objects have atouchesproperty, which holds
an array-like object of points, each of which has its ownclientX,clientY,
pageX, andpageYproperties.
You could do something like this to show red circles around every
touching finger:

```
<style>
dot { position: absolute; display: block;
border: 2px solid red; border-radius: 50px;
height: 100px; width: 100px; }
</style>
<p>Touch this page</p>
<script>
function update(event) {
```

```
for (let dot; dot = document.querySelector("dot");) {
dot.remove();
}
for (let i = 0; i < event.touches.length; i++) {
let {pageX, pageY} = event.touches[i];
let dot = document.createElement("dot");
dot.style.left = (pageX - 50) + "px";
dot.style.top = (pageY - 50) + "px";
document.body.appendChild(dot);
}
}
window.addEventListener("touchstart", update);
window.addEventListener("touchmove", update);
window.addEventListener("touchend", update);
</script>
```
You’ll often want to callpreventDefaultin touch event handlers to over-
ride the browser’s default behavior (which may include scrolling the
page on swiping) and to prevent the mouse events from being fired, for
which you may _also_ have a handler.

### Scroll events

Whenever an element is scrolled, a"scroll"event is fired on it. This
has various uses, such as knowing what the user is currently looking at
(for disabling off-screen animations or sending spy reports to your evil
headquarters) or showing some indication of progress (by highlighting
part of a table of contents or showing a page number).
The following example draws a progress bar above the document and


updates it to fill up as you scroll down:

```
<style>
#progress {
border-bottom: 2px solid blue;
width: 0;
position: fixed;
top: 0; left: 0;
}
</style>
<div id="progress"></div>
<script>
// Create some content
document.body.appendChild(document.createTextNode(
"supercalifragilisticexpialidocious ".repeat(1000)));
```
```
let bar = document.querySelector("#progress");
window.addEventListener("scroll", () => {
let max = document.body.scrollHeight - innerHeight;
bar.style.width = `${(pageYOffset / max) * 100}%`;
});
</script>
```
Giving an element apositionoffixedacts much like anabsolutepo-
sition but also prevents it from scrolling along with the rest of the
document. The effect is to make our progress bar stay at the top. Its
width is changed to indicate the current progress. We use %, rather
thanpx, as a unit when setting the width so that the element is sized
relative to the page width.
The global innerHeightbinding gives us the height of the window,


which we must subtract from the total scrollable height—you can’t keep
scrolling when you hit the bottom of the document. There’s also an
innerWidthfor the window width. By dividingpageYOffset, the current
scroll position, by the maximum scroll position and multiplying by 100,
we get the percentage for the progress bar.
CallingpreventDefaulton a scroll event does not prevent the scrolling
from happening. In fact, the event handler is called only _after_ the
scrolling takes place.

### Focus events

When an element gains focus, the browser fires a"focus"event on it.
When it loses focus, the element gets a"blur"event.
Unlike the events discussed earlier, these two events do not propagate.
A handler on a parent element is not notified when a child element gains
or loses focus.
The following example displays help text for the text field that cur-
rently has focus:

```
<p>Name: <input type="text" data-help="Your full name"></p>
<p>Age: <input type="text" data-help="Your age in years"></p>
<p id="help"></p>
```
```
<script>
let help = document.querySelector("#help");
let fields = document.querySelectorAll("input");
for (let field of Array.from(fields)) {
field.addEventListener("focus", event => {
```

```
let text = event.target.getAttribute("data-help");
help.textContent = text;
});
field.addEventListener("blur", event => {
help.textContent = "";
});
}
</script>
```
This screenshot shows the help text for the age field:

The window object will receive"focus"and"blur"events when the
user moves from or to the browser tab or window in which the document
is shown.

### Load event

When a page finishes loading, the"load"event fires on the window and
the document body objects. This is often used to schedule initialization
actions that require the whole document to have been built. Remember
that the content of <script>tags is run immediately when the tag is
encountered. This may be too soon, for example when the script needs
to do something with parts of the document that appear after the <


script>tag.
Elements such as images and script tags that load an external file also
have a"load"event that indicates the files they reference were loaded.
Like the focus-related events, loading events do not propagate.
When you close page or navigate away from it (for example, by fol-
lowing a link), a"beforeunload"event fires. The main use of this event
is to prevent the user from accidentally losing work by closing a doc-
ument. If you prevent the default behavior on this event _and_ set the
returnValueproperty on the event object to a string, the browser will
show the user a dialog asking if they really want to leave the page. That
dialog might include your string, but because some malicious sites try
to use these dialogs to confuse people into staying on their page to look
at dodgy weight-loss ads, most browsers no longer display them.

### Events and the event loop

In the context of the event loop, as discussed inChapter 11, browser
event handlers behave like other asynchronous notifications. They are
scheduled when the event occurs but must wait for other scripts that
are running to finish before they get a chance to run.
The fact that events can be processed only when nothing else is run-
ning means that if the event loop is tied up with other work, any inter-
action with the page (which happens through events) will be delayed
until there’s time to process it. So if you schedule too much work, either
with long-running event handlers or with lots of short-running ones, the
page will become slow and cumbersome to use.


For cases where you _really_ do want to do some time-consuming thing
in the background without freezing the page, browsers provide some-
thing called _web workers_. A worker is a JavaScript process that runs
alongside the main script, on its own timeline.
Imagine that squaring a number is a heavy, long-running computation
that we want to perform in a separate thread. We could write a file
calledcode/squareworker.jsthat responds to messages by computing a
square and sending a message back.

```
addEventListener("message", event => {
postMessage(event.data * event.data);
});
```
To avoid the problems of having multiple threads touching the same
data, workers do not share their global scope or any other data with
the main script’s environment. Instead, you have to communicate with
them by sending messages back and forth.
This code spawns a worker running that script, sends it a few mes-
sages, and outputs the responses.

```
let squareWorker = new Worker("code/squareworker.js");
squareWorker.addEventListener("message", event => {
console.log("The worker responded:", event.data);
});
squareWorker.postMessage(10);
squareWorker.postMessage(24);
```
ThepostMessagefunction sends a message, which will cause a"message"
event to fire in the receiver. The script that created the worker sends


and receives messages through the Workerobject, whereas the worker
talks to the script that created it by sending and listening directly on its
global scope. Only values that can be represented as JSON can be sent
as messages—the other side will receive a _copy_ of them, rather than the
value itself.

### Timers

ThesetTimeoutfunction we saw inChapter 11schedules another func-
tion to be called later, after a given number of milliseconds. Sometimes
you need to cancel a function you have scheduled. You can do this by
storing the value returned bysetTimeoutand callingclearTimeouton it.

```
let bombTimer = setTimeout(() => {
console.log("BOOM!");
}, 500);
```
```
if (Math.random() < 0.5) { // 50% chance
console.log("Defused.");
clearTimeout(bombTimer);
}
```
ThecancelAnimationFramefunction works in the same way asclearTimeout

. Calling it on a value returned byrequestAnimationFrame will cancel
that frame (assuming it hasn’t already been called).
    A similar set of functions, setIntervalandclearInterval, are used
to set timers that should repeat every _X_ milliseconds.

```
let ticks = 0;
```

```
let clock = setInterval(() => {
console.log("tick", ticks++);
if (ticks == 10) {
clearInterval(clock);
console.log("stop.");
}
}, 200);
```
### Debouncing.

Some types of events have the potential to fire rapidly many times in a
row, such as the"mousemove"and"scroll"events. When handling such
events, you must be careful not to do anything too time-consuming
or your handler will take up so much time that interaction with the
document starts to feel slow.
If you do need to do something nontrivial in such a handler, you can
usesetTimeout to make sure you are not doing it too often. This is
usually called _debouncing_ the event. There are several slightly different
approaches to this.
For example, suppose we want to react when the user has typed
something, but we don’t want to do it immediately for every input
event. When they are typing quickly, we just want to wait until a
pause occurs. Instead of immediately performing an action in the event
handler, we set a timeout. We also clear the previous timeout (if any) so
that when events occur close together (closer than our timeout delay),
the timeout from the previous event will be canceled.


```
<textarea>Type something here...</textarea>
<script>
let textarea = document.querySelector("textarea");
let timeout;
textarea.addEventListener("input", () => {
clearTimeout(timeout);
timeout = setTimeout(() => console.log("Typed!"), 500);
});
</script>
```
Giving an undefined value to clearTimeoutor calling it on a timeout
that has already fired has no effect. Thus, we don’t have to be careful
about when to call it, and we simply do so for every event.
We can use a slightly different pattern if we want to space responses
so that they’re separated by at least a certain length of time but want
to fire them _during_ a series of events, not just afterward. For example,
we might want to respond to"mousemove"events by showing the current
coordinates of the mouse, but only every 250 milliseconds.

```
<script>
let scheduled = null;
window.addEventListener("mousemove", event => {
if (!scheduled) {
setTimeout(() => {
document.body.textContent =
`Mouse at ${scheduled.pageX}, ${scheduled.pageY}`;
scheduled = null;
}, 250);
}
scheduled = event;
```

```
});
</script>
```
### Summary

Event handlers make it possible to detect and react to events happening
in our web page. TheaddEventListenermethod is used to register such
a handler.
Each event has a type ("keydown","focus", and so on) that identifies
it. Most events are called on a specific DOM element and then prop-
agate to that element’s ancestors, allowing handlers associated with
those elements to handle them.
When an event handler is called, it’s passed an event object with
additional information about the event. This object also has methods
that allow us to stop further propagation (stopPropagation) and prevent
the browser’s default handling of the event (preventDefault).
Pressing a key fires"keydown"and"keyup"events. Pressing a mouse
button fires"mousedown","mouseup", and"click" events. Moving the
mouse fires"mousemove" events. Touchscreen interaction will result in
"touchstart","touchmove", and"touchend"events.
Scrolling can be detected with the"scroll"event, and focus changes
can be detected with the"focus"and"blur"events. When the docu-
ment finishes loading, a"load"event fires on the window.


### Exercises

**Balloon**

Write a page that displays a balloon (using the balloon emoji,🎈). When
you press the up arrow, it should inflate (grow) 10 percent. When you
press the down arrow, it should deflate (shrink) 10 percent.
You can control the size of text (emoji are text) by setting thefont-
sizeCSS property (style.fontSize) on its parent element. Remember
to include a unit in the value—for example, pixels (10px).
The key names of the arrow keys are "ArrowUp" and "ArrowDown".
Make sure the keys change only the balloon, without scrolling the page.
Once you have that working, add a feature where if you blow up the
balloon past a certain size, it “explodes”. In this case, exploding means
that it is replaced with an💥emoji, and the event handler is removed
(so that you can’t inflate or deflate the explosion).

**Mousetrail**

In JavaScript’s early days, which was the high time of gaudy home
pages with lots of animated images, people came up with some truly
inspiring ways to use the language. One of these was the _mouse trail_ —a
series of elements that would follow the mouse pointer as you moved it
across the page.
In this exercise, I want you to implement a mouse trail. Use abso-
lutely positioned<div>elements with a fixed size and background color
(refer to thecodein the “Mouse Clicks” section for an example). Create


a bunch of these elements and, when the mouse moves, display them in
the wake of the mouse pointer.
There are various possible approaches here. You can make your trail
as simple or as complex as you want. A simple solution to start with is
to keep a fixed number of trail elements and cycle through them, moving
the next one to the mouse’s current position every time a"mousemove"
event occurs.

**Tabs**

Tabbed panels are common in user interfaces. They allow you to select
an interface panel by choosing from a number of tabs “sticking out”
above an element.
Implement a simple tabbed interface. Write a function,asTabs, that
takes a DOM node and creates a tabbed interface showing the child
elements of that node. It should insert a list of <button>elements at
the top of the node, one for each child element, containing text retrieved
from thedata-tabnameattribute of the child. All but one of the original
children should be hidden (given adisplaystyle ofnone). The currently
visible node can be selected by clicking the buttons.
When that works, extend it to style the button for the currently
selected tab differently so that it is obvious which tab is selected.


```
“All reality is a game.”
—Iain Banks, The Player of Games
```
**Chapter16**

## Project: APlatformGame

Much of my initial fascination with computers, like that of many nerdy
kids, had to do with computer games. I was drawn into the tiny sim-
ulated worlds that I could manipulate and in which stories (sort of)
unfolded—more, I suppose, because of the way I projected my imagi-
nation into them than because of the possibilities they actually offered.
I don’t wish a career in game programming on anyone. As with the
music industry, the discrepancy between the number of eager young
people wanting to work in it and the actual demand for such people
creates a rather unhealthy environment. But writing games for fun is
amusing.
This chapter will walk through the implementation of a small plat-
form game. Platform games (or “jump and run” games) are games that
expect the player to move a figure through a world, which is usually
two-dimensional and viewed from the side, while jumping over and onto
things.


### The game.

Our game will be roughly based on Dark Blue ( _[http://www.lessmilk.com/](http://www.lessmilk.com/)
games/10_ ) by Thomas Palef. I chose that game because it is both
entertaining and minimalist and because it can be built without too
much code. It looks like this:

The dark box represents the player, whose task is to collect the yellow
boxes (coins) while avoiding the red stuff (lava). A level is completed
when all coins have been collected.
The player can walk around with the left and right arrow keys and
can jump with the up arrow. Jumping is this game character’s specialty.
It can reach several times its own height and can change direction in
midair. This may not be entirely realistic, but it helps give the player
the feeling of being in direct control of the on-screen avatar.
The game consists of a static background, laid out like a grid, with
the moving elements overlaid on that background. Each field on the
grid is either empty, solid, or lava. The moving elements are the player,


coins, and certain pieces of lava. The positions of these elements are not
constrained to the grid—their coordinates may be fractional, allowing
smooth motion.

### The technology

We will use the browser DOM to display the game, and we’ll read user
input by handling key events.
The screen- and keyboard-related code is only a small part of the
work we need to do to build this game. Since everything looks like
colored boxes, drawing is uncomplicated: we create DOM elements and
use styling to give them a background color, size, and position.
We can represent the background as a table, since it is an unchang-
ing grid of squares. The free-moving elements can be overlaid using
absolutely positioned elements.
In games and other programs that should animate graphics and re-
spond to user input without noticeable delay, eﬀiciency is important.
Although the DOM was not originally designed for high-performance
graphics, it is actually better at this than you would expect. You saw
some animations inChapter 14. On a modern machine, a simple game
like this performs well, even if we don’t worry about optimization very
much.
In thenext chapter, we will explore another browser technology, the
<canvas>tag, which provides a more traditional way to draw graphics,
working in terms of shapes and pixels rather than DOM elements.


### Levels

We’ll want a human-readable, human-editable way to specify levels.
Since it is okay for everything to start out on a grid, we could use big
strings in which each character represents an element—either a part of
the background grid or a moving element.
The plan for a small level might look like this:
let simpleLevelPlan = `
......................
..#................#..
..#..............=.#..
..#.........o.o....#..
..#.@......#####...#..
..#####............#..
......#++++++++++++#..
......##############..
......................`;

Periods are empty space, hash (#) characters are walls, and plus signs
are lava. The player’s starting position is the at sign (@). Every O
character is a coin, and the equal sign (=) at the top is a block of lava
that moves back and forth horizontally.
We’ll support two additional kinds of moving lava: the pipe charac-
ter (|) creates vertically moving blobs, andvindicates _dripping_ lava—
vertically moving lava that doesn’t bounce back and forth but only
moves down, jumping back to its start position when it hits the floor.
A whole game consists of multiple levels that the player must com-
plete. A level is completed when all coins have been collected. If the


player touches lava, the current level is restored to its starting position,
and the player may try again.

### Reading a level.

The following class stores a level object. Its argument should be the
string that defines the level.

```
class Level {
constructor(plan) {
let rows = plan.trim().split("\n").map(l => [...l]);
this.height = rows.length;
this.width = rows[0].length;
this.startActors = [];
```
```
this.rows = rows.map((row, y) => {
return row.map((ch, x) => {
let type = levelChars[ch];
if (typeof type != "string") {
let pos = new Vec(x, y);
this.startActors.push(type.create(pos, ch));
type = "empty";
}
return type;
});
});
}
}
```
Thetrimmethod is used to remove whitespace at the start and end of


the plan string. This allows our example plan to start with a newline so
that all lines are directly below each other. The remaining string is split
on newline characters, and each line is spread into an array, producing
arrays of characters.
Sorowsholds an array of arrays of characters, the rows of the plan.
We can derive the level’s width and height from these. But we must
still separate the moving elements from the background grid. We’ll call
moving elements _actors_. They’ll be stored in an array of objects. The
background will be an array of arrays of strings, holding field types such
as"empty","wall", or"lava".
To create these arrays, we map over the rows and then over their
content. Remember thatmappasses the array index as a second argu-
ment to the mapping function, which tells us the x- and y-coordinates
of a given character. Positions in the game will be stored as pairs of
coordinates, with the upper left being 0,0 and each background square
being 1 unit high and wide.
To interpret the characters in the plan, theLevelconstructor uses the
levelCharsobject, which, for each character used in the level descrip-
tions, holds a string if it is a background type, and a class if it produces
an actor. Whentypeis an actor class, its staticcreatemethod is used
to create an object, which is added tostartActors, and the mapping
function returns"empty"for this background square.
The position of the actor is stored as a Vec object. This is a two-
dimensional vector, an object withxand yproperties, as seen in the
exercises ofChapter 6.
As the game runs, actors will end up in different places or even dis-


appear entirely (as coins do when collected). We’ll use aStateclass to
track the state of a running game.

```
class State {
constructor(level, actors, status) {
this.level = level;
this.actors = actors;
this.status = status;
}
```
```
static start(level) {
return new State(level, level.startActors, "playing");
}
```
```
get player() {
return this.actors.find(a => a.type == "player");
}
}
```
Thestatusproperty will switch to"lost"or"won"when the game has
ended.
This is again a persistent data structure—updating the game state
creates a new state and leaves the old one intact.

### Actors.

Actor objects represent the current position and state of a given moving
element (player, coin, or mobile lava) in our game. All actor objects
conform to the same interface. They havesizeandposproperties hold-


ing the size and the coordinates of the upper-left corner of the rectangle
representing this actor, and anupdatemethod.
Thisupdatemethod is used to compute their new state and position
after a given time step. It simulates the thing the actor does—moving
in response to the arrow keys for the player and bouncing back and
forth for the lava—and returns a new, updated actor object.
A type property contains a string that identifies the type of the
actor—"player","coin", or "lava". This is useful when drawing the
game—the look of the rectangle drawn for an actor is based on its
type.
Actor classes have a staticcreatemethod that is used by theLevel
constructor to create an actor from a character in the level plan. It is
given the coordinates of the character and the character itself, which is
necessary because theLavaclass handles several different characters.
This is the Vec class that we’ll use for our two-dimensional values,
such as the position and size of actors.

```
class Vec {
constructor(x, y) {
this.x = x; this.y = y;
}
plus(other) {
return new Vec(this.x + other.x, this.y + other.y);
}
times(factor) {
return new Vec(this.x * factor, this.y * factor);
}
}
```

Thetimesmethod scales a vector by a given number. It will be useful
when we need to multiply a speed vector by a time interval to get the
distance traveled during that time.
The different types of actors get their own classes, since their behavior
is very different. Let’s define these classes. We’ll get to theirupdate
methods later.
The player class has aspeedproperty that stores its current speed to
simulate momentum and gravity.

```
class Player {
constructor(pos, speed) {
this.pos = pos;
this.speed = speed;
}
```
```
get type() { return "player"; }
```
```
static create(pos) {
return new Player(pos.plus(new Vec(0, -0.5)),
new Vec(0, 0));
}
}
```
```
Player.prototype.size = new Vec(0.8, 1.5);
```
Because a player is one-and-a-half squares high, its initial position is set
to be half a square above the position where the@character appeared.
This way, its bottom aligns with the bottom of the square where it
appeared.


Thesizeproperty is the same for all instances ofPlayer, so we store
it on the prototype rather than on the instances themselves. We could
have used a getter liketype, but that would create and return a new
Vec object every time the property is read, which would be wasteful.
(Strings, being immutable, don’t have to be re-created every time they
are evaluated.)
When constructing aLavaactor, we need to initialize the object dif-
ferently depending on the character it is based on. Dynamic lava moves
along at its current speed until it hits an obstacle. At that point, if it
has aresetproperty, it will jump back to its start position (dripping).
If it does not, it will invert its speed and continue in the other direction
(bouncing).
Thecreatemethod looks at the character that theLevelconstructor
passes and creates the appropriate lava actor.

```
class Lava {
constructor(pos, speed, reset) {
this.pos = pos;
this.speed = speed;
this.reset = reset;
}
```
```
get type() { return "lava"; }
```
```
static create(pos, ch) {
if (ch == "=") {
return new Lava(pos, new Vec(2, 0));
} else if (ch == "|") {
return new Lava(pos, new Vec(0, 2));
```

```
} else if (ch == "v") {
return new Lava(pos, new Vec(0, 3), pos);
}
}
}
```
```
Lava.prototype.size = new Vec(1, 1);
```
Coin actors are relatively simple. They mostly just sit in their place.
But to liven up the game a little, they are given a “wobble”, a slight
vertical back-and-forth motion. To track this, a coin object stores a
base position as well as awobbleproperty that tracks the phase of the
bouncing motion. Together, these determine the coin’s actual position
(stored in theposproperty).

```
class Coin {
constructor(pos, basePos, wobble) {
this.pos = pos;
this.basePos = basePos;
this.wobble = wobble;
}
```
```
get type() { return "coin"; }
```
```
static create(pos) {
let basePos = pos.plus(new Vec(0.2, 0.1));
return new Coin(basePos, basePos,
Math.random() * Math.PI * 2);
}
}
```

```
Coin.prototype.size = new Vec(0.6, 0.6);
```
InChapter 14, we saw thatMath.singives us the y-coordinate of a point
on a circle. That coordinate goes back and forth in a smooth waveform
as we move along the circle, which makes the sine function useful for
modeling a wavy motion.
To avoid a situation where all coins move up and down synchronously,
the starting phase of each coin is randomized. The period ofMath.sin’s
wave, the width of a wave it produces, is 2π. We multiply the value
returned by Math.random by that number to give the coin a random
starting position on the wave.
We can now define thelevelCharsobject that maps plan characters
to either background grid types or actor classes.

```
const levelChars = {
".": "empty", "#": "wall", "+": "lava",
"@": Player, "o": Coin,
"=": Lava, "|": Lava, "v": Lava
};
```
That gives us all the parts needed to create aLevelinstance.

```
let simpleLevel = new Level(simpleLevelPlan);
console.log(`${simpleLevel.width} by ${simpleLevel.height}`);
// → 22 by 9
```
The task ahead is to display such levels on the screen and to model
time and motion inside them.


### Drawing.

In thenext chapter, we’ll display the same game in a different way. To
make that possible, we put the drawing logic behind an interface and
pass it to the game as an argument. That way, we can use the same
game program with different new display modules.
A game display object draws a given level and state. We pass its
constructor to the game to allow it to be replaced. The display class we
define in this chapter is calledDOMDisplaybecause it uses DOM elements
to show the level.
We’ll be using a style sheet to set the actual colors and other fixed
properties of the elements that make up the game. It would also be
possible to directly assign to the elements’ style property when we
create them, but that would produce more verbose programs.
The following helper function provides a succinct way to create an
element and give it some attributes and child nodes:

```
function elt(name, attrs, ...children) {
let dom = document.createElement(name);
for (let attr of Object.keys(attrs)) {
dom.setAttribute(attr, attrs[attr]);
}
for (let child of children) {
dom.appendChild(child);
}
return dom;
}
```
A display is created by giving it a parent element to which it should


append itself and a level object.

```
class DOMDisplay {
constructor(parent, level) {
this.dom = elt("div", {class: "game"}, drawGrid(level));
this.actorLayer = null;
parent.appendChild(this.dom);
}
```
```
clear() { this.dom.remove(); }
}
```
The level’s background grid, which never changes, is drawn once. Actors
are redrawn every time the display is updated with a given state. The
actorLayer property will be used to track the element that holds the
actors so that they can be easily removed and replaced.
Our coordinates and sizes are tracked in grid units, where a size or
distance of 1 means one grid block. When setting pixel sizes, we will
have to scale these coordinates up—everything in the game would be
ridiculously small at a single pixel per square. Thescaleconstant gives
the number of pixels that a single unit takes up on the screen.

```
const scale = 20;
```
```
function drawGrid(level) {
return elt("table", {
class: "background",
style: `width: ${level.width * scale}px`
}, ...level.rows.map(row =>
elt("tr", {style: `height: ${scale}px`},
```

```
...row.map(type => elt("td", {class: type})))
));
}
```
The<table>element’s form nicely corresponds to the structure of the
rowsproperty of the level—each row of the grid is turned into a table
row (<tr>element). The strings in the grid are used as class names for
the table cell (<td>) elements. The code uses the spread (triple dot)
operator to pass arrays of child nodes toeltas separate arguments.
The following CSS makes the table look like the background we want:
.background { background: rgb(52, 166, 251);
table-layout: fixed;
border-spacing: 0; }
.background td { padding: 0; }
.lava { background: rgb(255, 100, 100); }
.wall { background: white; }

Some of these (table-layout,border-spacing, andpadding) are used to
suppress unwanted default behavior. We don’t want the layout of the
table to depend upon the contents of its cells, and we don’t want space
between the table cells or padding inside them.
The background rule sets the background color. CSS allows colors
to be specified both as words (white) or with a format such asrgb(R
, G, B), where the red, green, and blue components of the color are
separated into three numbers from 0 to 255. In rgb(52, 166, 251),
the red component is 52, green is 166, and blue is 251. Since the blue
component is the largest, the resulting color will be bluish. In the.lava
rule, the first number (red) is the largest.


We draw each actor by creating a DOM element for it and setting
that element’s position and size based on the actor’s properties. The
values must be multiplied byscaleto go from game units to pixels.

```
function drawActors(actors) {
return elt("div", {}, ...actors.map(actor => {
let rect = elt("div", {class: `actor ${actor.type}`});
rect.style.width = `${actor.size.x * scale}px`;
rect.style.height = `${actor.size.y * scale}px`;
rect.style.left = `${actor.pos.x * scale}px`;
rect.style.top = `${actor.pos.y * scale}px`;
return rect;
}));
}
```
To give an element more than one class, we separate the class names
by spaces. In the following CSS code, theactorclass gives the actors
their absolute position. Their type name is used as an extra class to
give them a color. We don’t have to define thelavaclass again because
we’re reusing the class for the lava grid squares we defined earlier.

```
.actor { position: absolute; }
.coin { background: rgb(241, 229, 89); }
.player { background: rgb(64, 64, 64); }
```
ThesyncStatemethod is used to make the display show a given state.
It first removes the old actor graphics, if any, and then redraws the
actors in their new positions. It may be tempting to try to reuse the
DOM elements for actors, but to make that work, we would need a lot
of additional bookkeeping to associate actors with DOM elements and


to make sure we remove elements when their actors vanish. Since there
will typically be only a handful of actors in the game, redrawing all of
them is not expensive.

```
DOMDisplay.prototype.syncState = function(state) {
if (this.actorLayer) this.actorLayer.remove();
this.actorLayer = drawActors(state.actors);
this.dom.appendChild(this.actorLayer);
this.dom.className = `game ${state.status}`;
this.scrollPlayerIntoView(state);
};
```
By adding the level’s current status as a class name to the wrapper, we
can style the player actor slightly differently when the game is won or
lost by adding a CSS rule that takes effect only when the player has an
ancestor element with a given class.

```
.lost .player {
background: rgb(160, 64, 64);
}
.won .player {
box-shadow: -4px -7px 8px white, 4px -7px 8px white;
}
```
After touching lava, the player turns dark red, suggesting scorching.
When the last coin has been collected, we add two blurred white shadows—
one to the upper left and one to the upper right—to create a white halo
effect.
We can’t assume that the level always fits in the _viewport_ , the element
into which we draw the game. That is why we need thescrollPlayerIntoView


call: it ensures that if the level is protruding outside the viewport, we
scroll that viewport to make sure the player is near its center. The
following CSS gives the game’s wrapping DOM element a maximum
size and ensures that anything that sticks out of the element’s box is
not visible. We also give it a relative position so that the actors inside
it are positioned relative to the level’s upper-left corner.

```
.game {
overflow: hidden;
max-width: 600px;
max-height: 450px;
position: relative;
}
```
In thescrollPlayerIntoViewmethod, we find the player’s position and
update the wrapping element’s scroll position. We change the scroll po-
sition by manipulating that element’sscrollLeftand scrollTopprop-
erties when the player is too close to the edge.

```
DOMDisplay.prototype.scrollPlayerIntoView = function(state) {
let width = this.dom.clientWidth;
let height = this.dom.clientHeight;
let margin = width / 3;
```
```
// The viewport
let left = this.dom.scrollLeft, right = left + width;
let top = this.dom.scrollTop, bottom = top + height;
```
```
let player = state.player;
let center = player.pos.plus(player.size.times(0.5))
```

```
.times(scale);
```
```
if (center.x < left + margin) {
this.dom.scrollLeft = center.x - margin;
} else if (center.x > right - margin) {
this.dom.scrollLeft = center.x + margin - width;
}
if (center.y < top + margin) {
this.dom.scrollTop = center.y - margin;
} else if (center.y > bottom - margin) {
this.dom.scrollTop = center.y + margin - height;
}
};
```
The way the player’s center is found shows how the methods on our
Vectype allow computations with objects to be written in a relatively
readable way. To find the actor’s center, we add its position (its upper-
left corner) and half its size. That is the center in level coordinates,
but we need it in pixel coordinates, so we then multiply the resulting
vector by our display scale.
Next, a series of checks verifies that the player position isn’t out-
side of the allowed range. Note that sometimes this will set nonsense
scroll coordinates that are below zero or beyond the element’s scrollable
area. This is okay—the DOM will constrain them to acceptable values.
SettingscrollLeftto-10will cause it to become 0.
While it would have been slightly simpler to always try to scroll the
player to the center of the viewport, this creates a rather jarring effect.
As you are jumping, the view will constantly shift up and down. It’s


more pleasant to have a “neutral” area in the middle of the screen where
you can move around without causing any scrolling.
We are now able to display our tiny level.
<link rel="stylesheet" href="css/game.css">

```
<script>
let simpleLevel = new Level(simpleLevelPlan);
let display = new DOMDisplay(document.body, simpleLevel);
display.syncState(State.start(simpleLevel));
</script>
```
The<link>tag, when used withrel="stylesheet", is a way to load a
CSS file into a page. The filegame.csscontains the styles necessary for
our game.

### Motion and collision.

Now we’re at the point where we can start adding motion. The basic
approach taken by most games like this is to split time into small steps
and, for each step, move the actors by a distance corresponding to their


speed multiplied by the size of the time step. We’ll measure time in
seconds, so speeds are expressed in units per second.
Moving things is easy. The diﬀicult part is dealing with the interac-
tions between the elements. When the player hits a wall or floor, they
should not simply move through it. The game must notice when a given
motion causes an object to hit another object and respond accordingly.
For walls, the motion must be stopped. When hitting a coin, that coin
must be collected. When touching lava, the game should be lost.
Solving this for the general case is a major task. You can find libraries,
usually called _physics engines_ , that simulate interaction between phys-
ical objects in two or three dimensions. We’ll take a more modest
approach in this chapter, handling only collisions between rectangular
objects and handling them in a rather simplistic way.
Before moving the player or a block of lava, we test whether the
motion would take it inside of a wall. If it does, we simply cancel the
motion altogether. The response to such a collision depends on the type
of actor—the player will stop, whereas a lava block will bounce back.
This approach requires our time steps to be rather small, since it
will cause motion to stop before the objects actually touch. If the time
steps (and thus the motion steps) are too big, the player would end up
hovering a noticeable distance above the ground. Another approach,
arguably better but more complicated, would be to find the exact col-
lision spot and move there. We will take the simple approach and hide
its problems by ensuring the animation proceeds in small steps.
This method tells us whether a rectangle (specified by a position and
a size) touches a grid element of the given type.


```
Level.prototype.touches = function(pos, size, type) {
let xStart = Math.floor(pos.x);
let xEnd = Math.ceil(pos.x + size.x);
let yStart = Math.floor(pos.y);
let yEnd = Math.ceil(pos.y + size.y);
```
```
for (let y = yStart; y < yEnd; y++) {
for (let x = xStart; x < xEnd; x++) {
let isOutside = x < 0 || x >= this.width ||
y < 0 || y >= this.height;
let here = isOutside? "wall" : this.rows[y][x];
if (here == type) return true;
}
}
return false;
};
```
The method computes the set of grid squares that the body overlaps
with by usingMath.floorandMath.ceilon its coordinates. Remember
that grid squares are 1 by 1 units in size. By rounding the sides of a
box up and down, we get the range of background squares that the box
touches.

```
We loop over the block of grid squares found by rounding the coordi-
```

nates and returntruewhen a matching square is found. Squares outside
of the level are always treated as"wall"to ensure that the player can’t
leave the world and that we won’t accidentally try to read outside of
the bounds of ourrowsarray.
The stateupdatemethod usestouchesto figure out whether the player
is touching lava.

```
State.prototype.update = function(time, keys) {
let actors = this.actors
.map(actor => actor.update(time, this, keys));
let newState = new State(this.level, actors, this.status);
```
```
if (newState.status != "playing") return newState;
```
```
let player = newState.player;
if (this.level.touches(player.pos, player.size, "lava")) {
return new State(this.level, actors, "lost");
}
```
```
for (let actor of actors) {
if (actor != player && overlap(actor, player)) {
newState = actor.collide(newState);
}
}
return newState;
};
```
The method is passed a time step and a data structure that tells it
which keys are being held down. The first thing it does is call the
update method on all actors, producing an array of updated actors.


The actors also get the time step, the keys, and the state so that they
can base their update on those. Only the player will actually read keys,
since that’s the only actor that’s controlled by the keyboard.
If the game is already over, no further processing has to be done
(the game can’t be won after being lost, or vice versa). Otherwise, the
method tests whether the player is touching background lava. If so, the
game is lost and we’re done. Finally, if the game really is still going on,
it sees whether any other actors overlap the player.
Overlap between actors is detected with theoverlapfunction. It takes
two actor objects and returnstruewhen they touch—which is the case
when they overlap both along the x-axis and along the y-axis.

```
function overlap(actor1, actor2) {
return actor1.pos.x + actor1.size.x > actor2.pos.x &&
actor1.pos.x < actor2.pos.x + actor2.size.x &&
actor1.pos.y + actor1.size.y > actor2.pos.y &&
actor1.pos.y < actor2.pos.y + actor2.size.y;
}
```
If any actor does overlap, itscollidemethod gets a chance to update
the state. Touching a lava actor sets the game status to"lost". Coins
vanish when you touch them and set the status to"won"when they are
the last coin of the level.

```
Lava.prototype.collide = function(state) {
return new State(state.level, state.actors, "lost");
};
```
```
Coin.prototype.collide = function(state) {
```

```
let filtered = state.actors.filter(a => a != this);
let status = state.status;
if (!filtered.some(a => a.type == "coin")) status = "won";
return new State(state.level, filtered, status);
};
```
### Actor updates

Actor objects’ update methods take as arguments the time step, the
state object, and akeysobject. The one for theLavaactor type ignores
thekeysobject.

```
Lava.prototype.update = function(time, state) {
let newPos = this.pos.plus(this.speed.times(time));
if (!state.level.touches(newPos, this.size, "wall")) {
return new Lava(newPos, this.speed, this.reset);
} else if (this.reset) {
return new Lava(this.reset, this.speed, this.reset);
} else {
return new Lava(this.pos, this.speed.times(-1));
}
};
```
Thisupdatemethod computes a new position by adding the product of
the time step and the current speed to its old position. If no obstacle
blocks that new position, it moves there. If there is an obstacle, the
behavior depends on the type of the lava block—dripping lava has a
resetposition, to which it jumps back when it hits something. Bouncing


lava inverts its speed by multiplying it by-1so that it starts moving in
the opposite direction.
Coins use their update method to wobble. They ignore collisions
with the grid, since they are simply wobbling around inside of their
own square.

```
const wobbleSpeed = 8, wobbleDist = 0.07;
```
```
Coin.prototype.update = function(time) {
let wobble = this.wobble + time * wobbleSpeed;
let wobblePos = Math.sin(wobble) * wobbleDist;
return new Coin(this.basePos.plus(new Vec(0, wobblePos)),
this.basePos, wobble);
};
```
Thewobbleproperty is incremented to track time and then used as an
argument toMath.sinto find the new position on the wave. The coin’s
current position is then computed from its base position and an offset
based on this wave.
That leaves the player itself. Player motion is handled separately per
axis because hitting the floor should not prevent horizontal motion, and
hitting a wall should not stop falling or jumping motion.

```
const playerXSpeed = 7;
const gravity = 30;
const jumpSpeed = 17;
```
```
Player.prototype.update = function(time, state, keys) {
let xSpeed = 0;
if (keys.ArrowLeft) xSpeed -= playerXSpeed;
```

```
if (keys.ArrowRight) xSpeed += playerXSpeed;
let pos = this.pos;
let movedX = pos.plus(new Vec(xSpeed * time, 0));
if (!state.level.touches(movedX, this.size, "wall")) {
pos = movedX;
}
```
```
let ySpeed = this.speed.y + time * gravity;
let movedY = pos.plus(new Vec(0, ySpeed * time));
if (!state.level.touches(movedY, this.size, "wall")) {
pos = movedY;
} else if (keys.ArrowUp && ySpeed > 0) {
ySpeed = -jumpSpeed;
} else {
ySpeed = 0;
}
return new Player(pos, new Vec(xSpeed, ySpeed));
};
```
The horizontal motion is computed based on the state of the left and
right arrow keys. When there’s no wall blocking the new position cre-
ated by this motion, it is used. Otherwise, the old position is kept.
Vertical motion works in a similar way but has to simulate jumping
and gravity. The player’s vertical speed (ySpeed) is first accelerated to
account for gravity.
We check for walls again. If we don’t hit any, the new position is
used. If there _is_ a wall, there are two possible outcomes. When the up
arrow is pressed _and_ we are moving down (meaning the thing we hit is
below us), the speed is set to a relatively large, negative value. This


causes the player to jump. If that is not the case, the player simply
bumped into something, and the speed is set to zero.
The gravity strength, jumping speed, and other constants in the game
were determined by simply trying out some numbers and seeing which
ones felt right. You can try experimenting with them.

### Tracking keys

For a game like this, we do not want keys to take effect once per key-
press. Rather, we want their effect (moving the player figure) to stay
active as long as they are held.
We need to set up a key handler that stores the current state of the
left, right, and up arrow keys. We will also want to callpreventDefault
for those keys so that they don’t end up scrolling the page.
The following function, when given an array of key names, will return
an object that tracks the current position of those keys. It registers
event handlers for"keydown"and"keyup"events and, when the key code
in the event is present in the set of codes that it is tracking, updates
the object.

```
function trackKeys(keys) {
let down = Object.create(null);
function track(event) {
if (keys.includes(event.key)) {
down[event.key] = event.type == "keydown";
event.preventDefault();
}
}
```

```
window.addEventListener("keydown", track);
window.addEventListener("keyup", track);
return down;
}
```
```
const arrowKeys =
trackKeys(["ArrowLeft", "ArrowRight", "ArrowUp"]);
```
The same handler function is used for both event types. It looks at the
event object’stypeproperty to determine whether the key state should
be updated to true ("keydown") or false ("keyup").

### Running the game.

TherequestAnimationFramefunction, which we saw inChapter 14, pro-
vides a good way to animate a game. But its interface is quite primitive—
using it requires us to track the time at which our function was called
the last time around and callrequestAnimationFrameagain after every
frame.
Let’s define a helper function that wraps all that in a convenient
interface and allows us to simply callrunAnimation, giving it a function
that expects a time difference as an argument and draws a single frame.
When the frame function returns the valuefalse, the animation stops.

```
function runAnimation(frameFunc) {
let lastTime = null;
function frame(time) {
if (lastTime != null) {
```

```
let timeStep = Math.min(time - lastTime, 100) / 1000;
if (frameFunc(timeStep) === false) return;
}
lastTime = time;
requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
}
```
I have set a maximum frame step of 100 milliseconds (one-tenth of a
second). When the browser tab or window with our page is hidden,
requestAnimationFramecalls will be suspended until the tab or window
is shown again. In this case, the difference betweenlastTimeandtime
will be the entire time in which the page was hidden. Advancing the
game by that much in a single step would look silly and might cause
weird side effects, such as the player falling through the floor.
The function also converts the time steps to seconds, which are an
easier quantity to think about than milliseconds.
TherunLevelfunction takes aLevelobject and a display constructor
and returns a promise. It displays the level (in document.body) and
lets the user play through it. When the level is finished (lost or won),
runLevelwaits one more second (to let the user see what happens) and
then clears the display, stops the animation, and resolves the promise
to the game’s end status.

```
function runLevel(level, Display) {
let display = new Display(document.body, level);
let state = State.start(level);
let ending = 1;
```

```
return new Promise(resolve => {
runAnimation(time => {
state = state.update(time, arrowKeys);
display.syncState(state);
if (state.status == "playing") {
return true;
} else if (ending > 0) {
ending -= time;
return true;
} else {
display.clear();
resolve(state.status);
return false;
}
});
});
}
```
A game is a sequence of levels. Whenever the player dies, the current
level is restarted. When a level is completed, we move on to the next
level. This can be expressed by the following function, which takes an
array of level plans (strings) and a display constructor:

```
async function runGame(plans, Display) {
for (let level = 0; level < plans.length;) {
let status = await runLevel(new Level(plans[level]),
Display);
if (status == "won") level++;
}
console.log("You've won!");
```

```
}
```
Because we made runLevelreturn a promise, runGamecan be written
using anasyncfunction, as shown in Chapter 11. It returns another
promise, which resolves when the player finishes the game.
There is a set of level plans available in theGAME_LEVELSbinding in
this chapter’s sandbox( _https://eloquentjavascript.net/code#16_ ). This
page feeds them torunGame, starting an actual game.

```
<link rel="stylesheet" href="css/game.css">
```
```
<body>
<script>
runGame(GAME_LEVELS, DOMDisplay);
</script>
</body>
```
### Exercises

**Gameover**

It’s traditional for platform games to have the player start with a limited
number of _lives_ and subtract one life each time they die. When the
player is out of lives, the game restarts from the beginning.
AdjustrunGameto implement lives. Have the player start with three.
Output the current number of lives (usingconsole.log) every time a
level starts.


**Pausingthegame**

Make it possible to pause (suspend) and unpause the game by pressing
esc. You can do this by changing the runLevelfunction to set up
a keyboard event handler that interrupts or resumes the animation
wheneverescis hit.
TherunAnimationinterface may not look like it is suitable for this at
first glance, but it is if you rearrange the wayrunLevelcalls it.
When you have that working, there’s something else you can try.
The way we’ve been registering keyboard event handlers is somewhat
problematic. The arrowKeysobject is currently a global binding, and
its event handlers are kept around even when no game is running. You
could say they _leak_ out of our system. Extend trackKeys to provide
a way to unregister its handlers, then changerunLevelto register its
handlers when it starts and unregister them again when it is finished.

**Amonster**

It is traditional for platform games to have enemies that you can defeat
by jumping on top of them. This exercise asks you to add such an actor
type to the game.
We’ll call this actor a monster. Monsters move only horizontally.
You can make them move in the direction of the player, bounce back
and forth like horizontal lava, or have any other movement pattern you
want. The class doesn’t have to handle falling, but it should make sure
the monster doesn’t walk through walls.
When a monster touches the player, the effect depends on whether


the player is jumping on top of them or not. You can approximate this
by checking whether the player’s bottom is near the monster’s top. If
this is the case, the monster disappears. If not, the game is lost.


```
“Drawing is deception.”
—M.C. Escher, cited by Bruno Ernst in The Magic Mirror of
M.C. Escher
```
**Chapter17**

## DrawingonCanvas

Browsers give us several ways to display graphics. The simplest way is
to use styles to position and color regular DOM elements. This can get
us quite far, as the game in theprevious chaptershowed. By adding
partially transparent background images to the nodes, we can make
them look exactly the way we want. It is even possible to rotate or
skew nodes with thetransformstyle.
But we’d be using the DOM for something that it wasn’t originally
designed for. Some tasks, such as drawing a line between arbitrary
points, are extremely awkward to do with regular HTML elements.
There are two alternatives. The first is DOM based but utilizes _Scal-
able Vector Graphics_ (SVG) rather than HTML. Think of SVG as a
document-markup dialect that focuses on shapes rather than text. You
can embed an SVG document directly in an HTML document or include
it with an<img>tag.
The second alternative is called a _canvas_. A canvas is a single DOM
element that encapsulates a picture. It provides a programming in-
terface for drawing shapes onto the space taken up by the node. The


main difference between a canvas and an SVG picture is that in SVG
the original description of the shapes is preserved so that they can be
moved or resized at any time. A canvas, on the other hand, converts the
shapes to pixels (colored dots on a raster) as soon as they are drawn and
does not remember what these pixels represent. The only way to move
a shape on a canvas is to clear the canvas (or the part of the canvas
around the shape) and redraw it with the shape in a new position.

### SVG.

This book won’t go into SVG in detail, but I’ll briefly explain how
it works. At the end of the chapter, I’ll come back to the trade-offs
that you must consider when deciding which drawing mechanism is
appropriate for a given application.
This is an HTML document with a simple SVG picture in it:
<p>Normal HTML here.</p>
<svg xmlns="http://www.w3.org/2000/svg">
<circle r="50" cx="50" cy="50" fill="red"/>
<rect x="120" y="5" width="90" height="90"
stroke="blue" fill="none"/>
</svg>

Thexmlnsattribute changes an element (and its children) to a different
_XML namespace_. This namespace, identified by a URL, specifies the
dialect that we are currently speaking. The<circle>and<rect>tags,
which do not exist in HTML, do have a meaning in SVG—they draw
shapes using the style and position specified by their attributes.


```
The document is displayed like this:
```
These tags create DOM elements, just like HTML tags, that scripts
can interact with. For example, this changes the<circle>element to
be colored cyan instead:

```
let circle = document.querySelector("circle");
circle.setAttribute("fill", "cyan");
```
### The canvas element

Canvas graphics can be drawn onto a<canvas>element. You can give
such an elementwidth and height attributes to determine its size in
pixels.
A new canvas is empty, meaning it is entirely transparent and thus
shows up as empty space in the document.
The<canvas>tag is intended to allow different styles of drawing. To
get access to an actual drawing interface, we first need to create a _con-
text_ , an object whose methods provide the drawing interface. There
are currently three widely supported drawing styles: "2d" for two-
dimensional graphics, "webgl" for three-dimensional graphics through


the OpenGL interface, and"webgpu", a more modern and flexible alter-
native to WebGL.
This book won’t discuss WebGL or WebGPU—we’ll stick to two
dimensions. But if you are interested in three-dimensional graphics, I
do encourage you to look into WebGPU. It provides a direct interface
to graphics hardware and allows you to render even complicated scenes
eﬀiciently, using JavaScript.
You create a context with thegetContext method on the <canvas>
DOM element.

```
<p>Before canvas.</p>
<canvas width="120" height="60"></canvas>
<p>After canvas.</p>
<script>
let canvas = document.querySelector("canvas");
let context = canvas.getContext("2d");
context.fillStyle = "red";
context.fillRect(10, 10, 100, 50);
</script>
```
After creating the context object, the example draws a red rectangle
that is 100 pixels wide and 50 pixels high, with its upper-left corner at
coordinates (10, 10).


Just like in HTML (and SVG), the coordinate system that the canvas
uses puts (0, 0) at the upper-left corner, and the positive y-axis goes
down from there. This means (10, 10) is 10 pixels below and to the
right of the upper-left corner.

### Lines and surfaces

In the canvas interface, a shape can be _filled_ , meaning its area is given
a certain color or pattern, or it can be _stroked_ , which means a line is
drawn along its edge. SVG uses the same terminology.
ThefillRectmethod fills a rectangle. It takes first the x- and y-
coordinates of the rectangle’s upper-left corner, then its width, and
then its height. A similar method calledstrokeRectdraws the outline
of a rectangle.
Neither method takes any further parameters. The color of the fill,
thickness of the stroke, and so on, are not determined by an argument to
the method, as you might reasonably expect, but rather by properties
of the context object.
ThefillStyleproperty controls the way shapes are filled. It can be
set to a string that specifies a color, using the color notation used by


#### CSS.

ThestrokeStyleproperty works similarly but determines the color
used for a stroked line. The width of that line is determined by the
lineWidthproperty, which may contain any positive number.

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
cx.strokeStyle = "blue";
cx.strokeRect(5, 5, 50, 50);
cx.lineWidth = 5;
cx.strokeRect(135, 5, 50, 50);
</script>
```
This code draws two blue squares, using a thicker line for the second
one.

When nowidth orheight attribute is specified, as in the example,
a canvas element gets a default width of 300 pixels and height of 150
pixels.

### Paths

A path is a sequence of lines. The 2D canvas interface takes a peculiar
approach to describing such a path. It is done entirely through side


effects. Paths are not values that can be stored and passed around.
Instead, if you want to do something with a path, you make a sequence
of method calls to describe its shape.

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
cx.beginPath();
for (let y = 10; y < 100; y += 10) {
cx.moveTo(10, y);
cx.lineTo(90, y);
}
cx.stroke();
</script>
```
This example creates a path with a number of horizontal line segments
and then strokes it using thestrokemethod. Each segment created with
lineTostarts at the path’s _current_ position. That position is usually
the end of the last segment, unlessmoveTowas called. In that case, the
next segment would start at the position passed tomoveTo.
The path described by the previous program looks like this:

When filling a path (using the fill method), each shape is filled
separately. A path can contain multiple shapes—eachmoveTo motion


starts a new one. But the path needs to be _closed_ (meaning its start
and end are in the same position) before it can be filled. If the path
is not already closed, a line is added from its end to its start, and the
shape enclosed by the completed path is filled.

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
cx.beginPath();
cx.moveTo(50, 10);
cx.lineTo(10, 70);
cx.lineTo(90, 70);
cx.fill();
</script>
```
This example draws a filled triangle. Note that only two of the triangle’s
sides are explicitly drawn. The third, from the lower-right corner back
to the top, is implied and wouldn’t be there if you stroked the path.

You could also use theclosePathmethod to explicitly close a path by
adding an actual line segment back to the path’s start. This segment
_is_ drawn when stroking the path.


### Curves

A path may also contain curved lines. These are unfortunately a bit
more involved to draw.
The quadraticCurveTomethod draws a curve to a given point. To
determine the curvature of the line, the method is given a control point
as well as a destination point. Imagine this control point as _attracting_
the line, giving it its curve. The line won’t go through the control
point, but its direction at the start and end points will be such that
a straight line in that direction would point toward the control point.
The following example illustrates this:

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
cx.beginPath();
cx.moveTo(10, 90);
// control=(60, 10) goal=(90, 90)
cx.quadraticCurveTo(60, 10, 90, 90);
cx.lineTo(60, 10);
cx.closePath();
cx.stroke();
</script>
```
It produces a path that looks like this:


We draw a quadratic curve from the left to the right, with (60, 10) as
the control point, and then draw two line segments going through that
control point and back to the start of the line. The result somewhat
resembles a _Star Trek_ insignia. You can see the effect of the control
point: the lines leaving the lower corners start off in the direction of
the control point and then curve toward their target.
ThebezierCurveTomethod draws a similar kind of curve. Instead of
a single control point, this method has two—one for each of the line’s
end points. Here is a similar sketch to illustrate the behavior of such a
curve:

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
cx.beginPath();
cx.moveTo(10, 90);
// control1=(10, 10) control2=(90, 10) goal=(50, 90)
cx.bezierCurveTo(10, 10, 90, 10, 50, 90);
cx.lineTo(90, 10);
cx.lineTo(10, 10);
cx.closePath();
cx.stroke();
</script>
```

The two control points specify the direction at both ends of the curve.
The farther they are away from their corresponding point, the more the
curve will “bulge” in that direction.

Such curves can be hard to work with—it’s not always clear how
to find the control points that provide the shape you are looking for.
Sometimes you can compute them, and sometimes you’ll just have to
find a suitable value by trial and error.
Thearcmethod is a way to draw a line that curves along the edge
of a circle. It takes a pair of coordinates for the arc’s center, a radius,
and then a start angle and end angle.
Those last two parameters make it possible to draw only part of the
circle. The angles are measured in radians, not degrees. This means a
full circle has an angle of 2π, or2 * Math.PI, which is about 6.28. The
angle starts counting at the point to the right of the circle’s center and
goes clockwise from there. You can use a start of 0 and an end bigger
than 2π(say, 7) to draw a full circle.

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
cx.beginPath();
// center=(50, 50) radius=40 angle=0 to 7
```

```
cx.arc(50, 50, 40, 0, 7);
// center=(150, 50) radius=40 angle=0 to π½
cx.arc(150, 50, 40, 0, 0.5 * Math.PI);
cx.stroke();
</script>
```
The resulting picture contains a line from the right of the full circle
(first call toarc) to the right of the quarter-circle (second call).

Like other path-drawing methods, a line drawn witharcis connected
to the previous path segment.You can callmoveToor start a new path
to avoid this.

### Drawing a pie chart

Imagine you’ve just taken a job at EconomiCorp, Inc. Your first assign-
ment is to draw a pie chart of its customer satisfaction survey results.
Theresultsbinding contains an array of objects that represent the
survey responses.

```
const results = [
{name: "Satisfied", count: 1043, color: "lightblue"},
{name: "Neutral", count: 563, color: "lightgreen"},
```

```
{name: "Unsatisfied", count: 510, color: "pink"},
{name: "No comment", count: 175, color: "silver"}
];
```
To draw a pie chart, we draw a number of pie slices, each made up of
an arc and a pair of lines to the center of that arc. We can compute
the angle taken up by each arc by dividing a full circle (2π) by the total
number of responses and then multiplying that number (the angle per
response) by the number of people who picked a given choice.

```
<canvas width="200" height="200"></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
let total = results
.reduce((sum, {count}) => sum + count, 0);
// Start at the top
let currentAngle = -0.5 * Math.PI;
for (let result of results) {
let sliceAngle = (result.count / total) * 2 * Math.PI;
cx.beginPath();
// center=100,100, radius=100
// from current angle, clockwise by slice's angle
cx.arc(100, 100, 100,
currentAngle, currentAngle + sliceAngle);
currentAngle += sliceAngle;
cx.lineTo(100, 100);
cx.fillStyle = result.color;
cx.fill();
}
</script>
```

This draws the following chart:

But a chart that doesn’t tell us what the slices mean isn’t very helpful.
We need a way to draw text to the canvas.

### Text

A 2D canvas drawing context provides the methodsfillTextandstrokeText

. The latter can be useful for outlining letters, but usuallyfillTextis
what you need. It will fill the outline of the given text with the current
fillStyle.

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
cx.font = "28px Georgia";
cx.fillStyle = "fuchsia";
cx.fillText("I can draw text, too!", 10, 50);
```

```
</script>
```
You can specify the size, style, and font of the text with thefontprop-
erty. This example just gives a font size and family name. It is also
possible to additalicorboldto the start of the string to select a style.
The last two arguments tofillTextandstrokeTextprovide the posi-
tion at which the font is drawn. By default, they indicate the position of
the start of the text’s alphabetic baseline, which is the line that letters
“stand” on, not counting hanging parts in letters such as _j_ or _p_. You
can change the horizontal position by setting thetextAlignproperty to
"end"or "center"and the vertical position by settingtextBaselineto
"top","middle", or"bottom".
We’ll come back to our pie chart, and the problem of labeling the
slices, in theexercisesat the end of the chapter.

### Images

In computer graphics, a distinction is often made between _vector_ graph-
ics and _bitmap_ graphics. The first is what we have been doing so far
in this chapter—specifying a picture by giving a logical description of
shapes. Bitmap graphics, on the other hand, don’t specify actual shapes
but rather work with pixel data (rasters of colored dots).
ThedrawImage method allows us to draw pixel data onto a canvas.
This pixel data can originate from an<img> element or from another
canvas. The following example creates a detached<img>element and
loads an image file into it. But the method cannot immediately start
drawing from this picture because the browser may not have loaded it


yet. To deal with this, we register a"load"event handler and do the
drawing after the image has loaded.

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
let img = document.createElement("img");
img.src = "img/hat.png";
img.addEventListener("load", () => {
for (let x = 10; x < 200; x += 30) {
cx.drawImage(img, x, 10);
}
});
</script>
```
By default,drawImagewill draw the image at its original size. You can
also give it two additional arguments to specify the width and height
of the drawn image, when those aren’t the same as the origin image.
WhendrawImageis given _nine_ arguments, it can be used to draw only
a fragment of an image. The second through fifth arguments indicate
the rectangle (x, y, width, and height) in the source image that should
be copied, and the sixth to ninth arguments give the rectangle (on the
canvas) into which it should be copied.
This can be used to pack multiple _sprites_ (image elements) into a
single image file and then draw only the part you need. For example,
this picture contains a game character in multiple poses:


By alternating which pose we draw, we can show an animation that
looks like a walking character.
To animate a picture on a canvas, the clearRect method is useful.
It resemblesfillRect, but instead of coloring the rectangle, it makes it
transparent, removing the previously drawn pixels.
We know that each _sprite_ , each subpicture, is 24 pixels wide and 30
pixels high. The following code loads the image and then sets up an
interval (repeated timer) to draw the next frame:

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
let img = document.createElement("img");
img.src = "img/player.png";
let spriteW = 24, spriteH = 30;
img.addEventListener("load", () => {
let cycle = 0;
setInterval(() => {
cx.clearRect(0, 0, spriteW, spriteH);
cx.drawImage(img,
// source rectangle
cycle * spriteW, 0, spriteW, spriteH,
// destination rectangle
0, 0, spriteW, spriteH);
cycle = (cycle + 1) % 8;
}, 120);
});
</script>
```
Thecyclebinding tracks our position in the animation. For each frame,


it is incremented and then clipped back to the 0 to 7 range by using
the remainder operator. This binding is then used to compute the x-
coordinate that the sprite for the current pose has in the picture.

### Transformation

What if we want our character to walk to the left instead of to the
right? We could draw another set of sprites, of course. But we could
also instruct the canvas to draw the picture the other way round.
Calling the scalemethod will cause anything drawn after it to be
scaled. This method takes two parameters, one to set a horizontal scale
and one to set a vertical scale.

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
cx.scale(3, .5);
cx.beginPath();
cx.arc(50, 50, 40, 0, 7);
cx.lineWidth = 3;
cx.stroke();
</script>
```
Because of the call toscale, the circle is drawn three times as wide and
half as high.


Scaling will cause everything about the drawn image, including the
line width, to be stretched out or squeezed together as specified. Scaling
by a negative amount will flip the picture around. The flipping happens
around point (0, 0), which means it will also flip the direction of the
coordinate system. When a horizontal scaling of -1 is applied, a shape
drawn at _x_ position 100 will end up at what used to be position -100.
To turn a picture around, we can’t simply addcx.scale(-1, 1)before
the call to drawImage. That would move our picture outside of the
canvas, where it won’t be visible. We could adjust the coordinates
given to drawImageto compensate for this by drawing the image at _x_
position -50 instead of 0. Another solution, which doesn’t require the
code doing the drawing to know about the scale change, is to adjust
the axis around which the scaling happens.
There are several other methods besidesscalethat influence the coor-
dinate system for a canvas. You can rotate subsequently drawn shapes
with therotate method and move them with thetranslate method.
The interesting—and confusing—thing is that these transformations
_stack_ , meaning that each one happens relative to the previous transfor-
mations.
If we translate by 10 horizontal pixels twice, everything will be drawn
20 pixels to the right. If we first move the center of the coordinate
system to (50, 50) and then rotate by 20 degrees (about 0.1πradians),
that rotation will happen _around_ point (50, 50).


```
translate(50, 50)
rotate(0.1*Math.PI)
```
```
rotate(0.1*Math.PI)
```
```
translate(50, 50)
```
But if we _first_ rotate by 20 degrees and _then_ translate by (50, 50),
the translation will happen in the rotated coordinate system and thus
produce a different orientation. The order in which transformations are
applied matters.
To flip a picture around the vertical line at a given _x_ position, we can
do the following:

```
function flipHorizontally(context, around) {
context.translate(around, 0);
context.scale(-1, 1);
context.translate(-around, 0);
}
```
We move the y-axis to where we want our mirror to be, apply the
mirroring, and finally move the y-axis back to its proper place in the
mirrored universe. The following picture explains why this works:


```
mirror
```
```
3 1 4 2
```
This shows the coordinate systems before and after mirroring across
the central line. The triangles are numbered to illustrate each step. If
we draw a triangle at a positive _x_ position, it would, by default, be
in the place where triangle 1 is. A call toflipHorizontallyfirst does
a translation to the right, which gets us to triangle 2. It then scales,
flipping the triangle over to position 3. This is not where it should be,
if it were mirrored in the given line. The second translate call fixes
this—it “cancels” the initial translation and makes triangle 4 appear
exactly where it should.
We can now draw a mirrored character at position (100, 0) by flipping
the world around the character’s vertical center.

```
<canvas></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
let img = document.createElement("img");
img.src = "img/player.png";
let spriteW = 24, spriteH = 30;
img.addEventListener("load", () => {
flipHorizontally(cx, 100 + spriteW / 2);
```

```
cx.drawImage(img, 0, 0, spriteW, spriteH,
100, 0, spriteW, spriteH);
});
</script>
```
### Storing and clearing transformations

Transformations stick around. Everything else we draw after drawing
that mirrored character would also be mirrored. That might be incon-
venient.
It is possible to save the current transformation, do some drawing and
transforming, and then restore the old transformation. This is usually
the proper thing to do for a function that needs to temporarily trans-
form the coordinate system. First, we save whatever transformation
the code that called the function was using. Then the function does its
thing, adding more transformations on top of the current transforma-
tion. Finally, we revert to the transformation we started with.
The save and restore methods on the 2D canvas context do this
transformation management. They conceptually keep a stack of trans-
formation states. When you callsave, the current state is pushed onto
the stack, and when you callrestore, the state on top of the stack is
taken off and used as the context’s current transformation. You can
also callresetTransformto fully reset the transformation.
The branchfunction in the following example illustrates what you
can do with a function that changes the transformation and then calls
a function (in this case itself), which continues drawing with the given


transformation.
This function draws a treelike shape by drawing a line, moving the
center of the coordinate system to the end of the line, and calling itself
twice—first rotated to the left and then rotated to the right. Every call
reduces the length of the branch drawn, and the recursion stops when
the length drops below 8.

```
<canvas width="600" height="300"></canvas>
<script>
let cx = document.querySelector("canvas").getContext("2d");
function branch(length, angle, scale) {
cx.fillRect(0, 0, 1, length);
if (length < 8) return;
cx.save();
cx.translate(0, length);
cx.rotate(-angle);
branch(length * scale, angle, scale);
cx.rotate(2 * angle);
branch(length * scale, angle, scale);
cx.restore();
}
cx.translate(300, 0);
branch(60, 0.5, 0.8);
</script>
```
The result is a simple fractal.


If the calls tosaveandrestorewere not there, the second recursive
call tobranchwould end up with the position and rotation created by
the first call. It would be connected not to the current branch but
rather to the innermost, rightmost branch drawn by the first call. The
resulting shape might also be interesting, but it is definitely not a tree.

### Back to the game

We now know enough about canvas drawing to start working on a
canvas-based display system for the game from theprevious chapter.
The new display will no longer be showing just colored boxes. Instead,
we’ll usedrawImageto draw pictures that represent the game’s elements.
We define another display object type calledCanvasDisplay, support-
ing the same interface as DOMDisplay from Chapter 16—namely, the
methodssyncStateandclear.
This object keeps a little more information thanDOMDisplay. Rather
than using the scroll position of its DOM element, it tracks its own
viewport, which tells us which part of the level we are currently looking
at. Finally, it keeps aflipPlayerproperty so that even when the player


is standing still, it keeps facing the direction in which it last moved.

```
class CanvasDisplay {
constructor(parent, level) {
this.canvas = document.createElement("canvas");
this.canvas.width = Math.min(600, level.width * scale);
this.canvas.height = Math.min(450, level.height * scale);
parent.appendChild(this.canvas);
this.cx = this.canvas.getContext("2d");
```
```
this.flipPlayer = false;
```
```
this.viewport = {
left: 0,
top: 0,
width: this.canvas.width / scale,
height: this.canvas.height / scale
};
}
```
```
clear() {
this.canvas.remove();
}
}
```
ThesyncStatemethod first computes a new viewport and then draws
the game scene at the appropriate position.

```
CanvasDisplay.prototype.syncState = function(state) {
this.updateViewport(state);
this.clearDisplay(state.status);
```

```
this.drawBackground(state.level);
this.drawActors(state.actors);
};
```
Contrary toDOMDisplay, this display style _does_ have to redraw the back-
ground on every update. Because shapes on a canvas are just pixels,
after we draw them there is no good way to move them (or remove
them). The only way to update the canvas display is to clear it and
redraw the scene. We may also have scrolled, which requires the back-
ground to be in a different position.
TheupdateViewportmethod is similar toDOMDisplay’sscrollPlayerIntoView
method. It checks whether the player is too close to the edge of the
screen and moves the viewport when this is the case.

```
CanvasDisplay.prototype.updateViewport = function(state) {
let view = this.viewport, margin = view.width / 3;
let player = state.player;
let center = player.pos.plus(player.size.times(0.5));
```
```
if (center.x < view.left + margin) {
view.left = Math.max(center.x - margin, 0);
} else if (center.x > view.left + view.width - margin) {
view.left = Math.min(center.x + margin - view.width,
state.level.width - view.width);
}
if (center.y < view.top + margin) {
view.top = Math.max(center.y - margin, 0);
} else if (center.y > view.top + view.height - margin) {
view.top = Math.min(center.y + margin - view.height,
state.level.height - view.height);
```

```
}
};
```
The calls toMath.maxandMath.minensure that the viewport does not
end up showing space outside of the level. Math.max(x, 0)makes sure
the resulting number is not less than zero.Math.minsimilarly guarantees
that a value stays below a given bound.
When clearing the display, we’ll use a slightly different color depend-
ing on whether the game is won (brighter) or lost (darker).

```
CanvasDisplay.prototype.clearDisplay = function(status) {
if (status == "won") {
this.cx.fillStyle = "rgb(68, 191, 255)";
} else if (status == "lost") {
this.cx.fillStyle = "rgb(44, 136, 214)";
} else {
this.cx.fillStyle = "rgb(52, 166, 251)";
}
this.cx.fillRect(0, 0,
this.canvas.width, this.canvas.height);
};
```
To draw the background, we run through the tiles that are visible in
the current viewport, using the same trick used in thetouchesmethod
from theprevious chapter.

```
let otherSprites = document.createElement("img");
otherSprites.src = "img/sprites.png";
```
```
CanvasDisplay.prototype.drawBackground = function(level) {
```

```
let {left, top, width, height} = this.viewport;
let xStart = Math.floor(left);
let xEnd = Math.ceil(left + width);
let yStart = Math.floor(top);
let yEnd = Math.ceil(top + height);
```
```
for (let y = yStart; y < yEnd; y++) {
for (let x = xStart; x < xEnd; x++) {
let tile = level.rows[y][x];
if (tile == "empty") continue;
let screenX = (x - left) * scale;
let screenY = (y - top) * scale;
let tileX = tile == "lava"? scale : 0;
this.cx.drawImage(otherSprites,
tileX, 0, scale, scale,
screenX, screenY, scale, scale);
}
}
};
```
Tiles that are not empty are drawn withdrawImage. TheotherSprites
image contains the pictures used for elements other than the player. It
contains, from left to right, the wall tile, the lava tile, and the sprite
for a coin.

Background tiles are 20 by 20 pixels, since we’ll use the same scale
as inDOMDisplay. Thus, the offset for lava tiles is 20 (the value of the
scalebinding), and the offset for walls is 0.


We don’t bother waiting for the sprite image to load. CallingdrawImage
with an image that hasn’t been loaded yet will simply do nothing.
Thus, we might fail to draw the game properly for the first few frames
while the image is still loading, but that isn’t a serious problem. Since
we keep updating the screen, the correct scene will appear as soon as
the loading finishes.
The walking character shown earlier will be used to represent the
player. The code that draws it needs to pick the right sprite and di-
rection based on the player’s current motion. The first eight sprites
contain a walking animation. When the player is moving along a floor,
we cycle through them based on the current time. We want to switch
frames every 60 milliseconds, so the time is divided by 60 first. When
the player is standing still, we draw the ninth sprite. During jumps,
which are recognized by the fact that the vertical speed is not zero, we
use the tenth, rightmost sprite.
Because the sprites are slightly wider than the player object—24 in-
stead of 16 pixels to allow some space for feet and arms—the method has
to adjust the x-coordinate and width by a given amount (playerXOverlap
).

```
let playerSprites = document.createElement("img");
playerSprites.src = "img/player.png";
const playerXOverlap = 4;
```
```
CanvasDisplay.prototype.drawPlayer = function(player, x, y,
width, height){
width += playerXOverlap * 2;
x -= playerXOverlap;
```

```
if (player.speed.x != 0) {
this.flipPlayer = player.speed.x < 0;
}
```
```
let tile = 8;
if (player.speed.y != 0) {
tile = 9;
} else if (player.speed.x != 0) {
tile = Math.floor(Date.now() / 60) % 8;
}
```
```
this.cx.save();
if (this.flipPlayer) {
flipHorizontally(this.cx, x + width / 2);
}
let tileX = tile * width;
this.cx.drawImage(playerSprites, tileX, 0, width, height,
x, y, width, height);
this.cx.restore();
};
```
ThedrawPlayermethod is called bydrawActors, which is responsible for
drawing all the actors in the game.

```
CanvasDisplay.prototype.drawActors = function(actors) {
for (let actor of actors) {
let width = actor.size.x * scale;
let height = actor.size.y * scale;
let x = (actor.pos.x - this.viewport.left) * scale;
let y = (actor.pos.y - this.viewport.top) * scale;
if (actor.type == "player") {
```

```
this.drawPlayer(actor, x, y, width, height);
} else {
let tileX = (actor.type == "coin"? 2 : 1) * scale;
this.cx.drawImage(otherSprites,
tileX, 0, width, height,
x, y, width, height);
}
}
};
```
When drawing something that is not the player, we look at its type to
find the offset of the correct sprite. The lava tile is found at offset 20,
and the coin sprite is found at 40 (two timesscale).
We have to subtract the viewport’s position when computing the
actor’s position, since (0, 0) on our canvas corresponds to the top left
of the viewport, not the top left of the level. We could also have used
translatefor this. Either way works.
That concludes the new display system. The resulting game looks
something like this:


### Choosing a graphics interface

When you need to generate graphics in the browser, you can choose be-
tween plain HTML, SVG, and canvas. There is no single _best_ approach
that works in all situations. Each option has strengths and weaknesses.
Plain HTML has the advantage of being simple. It also integrates
well with text. Both SVG and canvas allow you to draw text, but they
won’t help you position that text or wrap it when it takes up more than
one line. In an HTML-based picture, it is much easier to include blocks
of text.
SVG can be used to produce crisp graphics that look good at any
zoom level. Unlike HTML, it is designed for drawing and is thus more
suitable for that purpose.
Both SVG and HTML build up a data structure (the DOM) that
represents your picture. This makes it possible to modify elements


after they are drawn. If you need to repeatedly change a small part
of a big picture in response to what the user is doing or as part of
an animation, doing it in a canvas can be needlessly expensive. The
DOM also allows us to register mouse event handlers on every element
in the picture (even on shapes drawn with SVG). You can’t do that
with canvas.
But canvas’s pixel-oriented approach can be an advantage when draw-
ing a huge number of tiny elements. The fact that it does not build up
a data structure but only repeatedly draws onto the same pixel surface
gives canvas a lower cost per shape. There are also effects that are only
practical with a canvas element, such as rendering a scene one pixel
at a time (for example, using a ray tracer) or postprocessing an image
with JavaScript (blurring or distorting it).
In some cases, you may want to combine several of these techniques.
For example, you might draw a graph with SVG or canvas but show
textual information by positioning an HTML element on top of the
picture.
For nondemanding applications, it really doesn’t matter much which
interface you choose. The display we built for our game in this chapter
could have been implemented using any of these three graphics tech-
nologies, since it does not need to draw text, handle mouse interaction,
or work with an extraordinarily large number of elements.


### Summary

In this chapter we discussed techniques for drawing graphics in the
browser, focusing on the<canvas>element.
A canvas node represents an area in a document that our program
may draw on. This drawing is done through a drawing context object,
created with thegetContextmethod.
The 2D drawing interface allows us to fill and stroke various shapes.
The context’sfillStyleproperty determines how shapes are filled. The
strokeStyleandlineWidthproperties control the way lines are drawn.
Rectangles and pieces of text can be drawn with a single method
call. The fillRectand strokeRectmethods draw rectangles, and the
fillTextandstrokeTextmethods draw text. To create custom shapes,
we must first build up a path.
CallingbeginPathstarts a new path. A number of other methods add
lines and curves to the current path. For example,lineTocan add a
straight line. When a path is finished, it can be filled with thefill
method or stroked with thestrokemethod.
Moving pixels from an image or another canvas onto our canvas is
done with thedrawImage method. By default, this method draws the
whole source image, but by giving it more parameters, you can copy
a specific area of the image. We used this for our game by copying
individual poses of the game character out of an image that contained
many such poses.
Transformations allow you to draw a shape in multiple orientations.
A 2D drawing context has a current transformation that can be changed
with thetranslate,scale, androtate methods. These will affect all


subsequent drawing operations. A transformation state can be saved
with thesavemethod and restored with therestoremethod.
When showing an animation on a canvas, theclearRectmethod can
be used to clear part of the canvas before redrawing it.

### Exercises

**Shapes**

Write a program that draws the following shapes on a canvas:

1. A trapezoid (a rectangle that is wider on one side)
2. A red diamond (a rectangle rotated 45 degrees or ¼πradians)
3. A zigzagging line
4. A spiral made up of 100 straight line segments
5. A yellow star

When drawing the last two shapes, you may want to refer to the
explanation of Math.cosand Math.sininChapter 14, which describes
how to get coordinates on a circle using these functions.


I recommend creating a function for each shape. Pass the position,
and optionally other properties such as the size or the number of points,
as parameters. The alternative, which is to hardcode numbers all over
your code, tends to make the code needlessly hard to read and modify.

**Thepiechart**

Earlierin the chapter, we saw an example program that drew a pie
chart. Modify this program so that the name of each category is shown
next to the slice that represents it. Try to find a pleasing-looking way
to automatically position this text that would work for other datasets
as well. You may assume that categories are big enough to leave enough
room for their labels.
You might needMath.sinandMath.cosagain, which are described in
Chapter 14.

**Abouncingball**

Use therequestAnimationFrametechnique that we saw inChapter 14and
Chapter 16to draw a box with a bouncing ball in it. The ball moves
at a constant speed and bounces off the box’s sides when it hits them.

**Precomputedmirroring**

One unfortunate thing about transformations is that they slow down
the drawing of bitmaps. The position and size of each pixel have to be
transformed, and though it is possible that browsers will get cleverer


about transformation in the future, they currently cause a measurable
increase in the time it takes to draw a bitmap.
In a game like ours, where we are drawing only a single transformed
sprite, this is a nonissue. But imagine that we need to draw hundreds
of characters or thousands of rotating particles from an explosion.
Think of a way to draw an inverted character without loading addi-
tional image files and without having to make transformeddrawImage
calls every frame.


```
“What was often diﬀicult for people to understand about the
design was that there was nothing else beyond URLs, HTTP
and HTML. There was no central computer ‘controlling’ the
web, no single network on which these protocols worked, not
even an organisation anywhere that ‘ran’ the Web. The Web
was not a physical ‘thing’ that existed in a certain ‘place’. It
was a ‘space’ in which information could exist.”
—Tim Berners-Lee
```
**Chapter18**

## HTTPandForms

The Hypertext Transfer Protocol, introduced in Chapter 13, is the
mechanism through which data is requested and provided on the World
Wide Web. This chapter describes the protocol in more detail and ex-
plains the way browser JavaScript has access to it.

### The protocol

If you type _eloquentjavascript.net/18_http.html_ in your browser’s ad-
dress bar, the browser first looks up the address of the server associated
with _eloquentjavascript.net_ and tries to open a TCP connection to it
on port 80, the default port for HTTP traﬀic. If the server exists and
accepts the connection, the browser might send something like this:

```
GET /18_http.html HTTP/1.1
Host: eloquentjavascript.net
User-Agent: Your browser's name
```
Then the server responds, through that same connection.


```
HTTP/1.1 200 OK
Content-Length: 87320
Content-Type: text/html
Last-Modified: Fri, 13 Oct 2023 10:05:41 GMT
```
```
<!doctype html>
... the rest of the document
```
The browser takes the part of the response after the blank line, its _body_
(not to be confused with the HTML<body>tag), and displays it as an
HTML document.
The information sent by the client is called the _request_. It starts with
this line:

```
GET /18_http.html HTTP/1.1
```
The first word is the _method_ of the request.GETmeans that we want to
_get_ the specified resource. Other common methods areDELETEto delete
a resource,PUTto create or replace it, andPOSTto send information to
it. Note that the server is not obliged to carry out every request it gets.
If you walk up to a random website and tell it toDELETEits main page,
it’ll probably refuse.
The part after the method name is the path of the _resource_ the re-
quest applies to. In the simplest case, a resource is simply a file on the
server, but the protocol doesn’t require it to be. A resource may be
anything that can be transferred _as if_ it is a file. Many servers gen-
erate the responses they produce on the fly. For example, if you open
_https://github.com/marijnh_ , the server looks in its database for a user
named “marijnh”, and if it finds one, it will generate a profile page for


that user.
After the resource path, the first line of the request mentionsHTTP/1.1
to indicate the version of the HTTP protocol it is using.
In practice, many sites use HTTP version 2, which supports the same
concepts as version 1.1 but is a lot more complicated so that it can be
faster. Browsers will automatically switch to the appropriate protocol
version when talking to a given server, and the outcome of a request
is the same regardless of which version is used. Because version 1.1 is
more straightforward and easier to play around with, we’ll use that to
illustrate the protocol.
The server’s response will start with a version as well, followed by
the status of the response, first as a three-digit status code and then as
a human-readable string.

```
HTTP/1.1 200 OK
```
Status codes starting with a 2 indicate that the request succeeded.
Codes starting with 4 mean there was something wrong with the re-
quest. The most famous HTTP status code is probably 404, which
means that the resource could not be found. Codes that start with 5
mean an error happened on the server and the request is not to blame.
The first line of a request or response may be followed by any number
of _headers_. These are lines in the formname: valuethat specify extra
information about the request or response. These headers were part of
the example response:

```
Content-Length: 87320
Content-Type: text/html
```

```
Last-Modified: Fri, 13 Oct 2023 10:05:41 GMT
```
This tells us the size and type of the response document. In this case,
it is an HTML document of 87,320 bytes. It also tells us when that
document was last modified.
The client and server are free to decide what headers to include in
their requests or responses. But some of them are necessary for things
to work. For example, without aContent-Typeheader in the response,
the browser won’t know how to display the document.
After the headers, both requests and responses may include a blank
line followed by a body, which contains the actual document being sent.
GET andDELETErequests don’t send along any data, but PUTand POST
requests do. Some response types, such as error responses, also don’t
require a body.

### Browsers and HTTP

As we saw, a browser will make a request when we enter a URL in
its address bar. When the resulting HTML page references other files,
such as images and JavaScript files, it will retrieve those as well.
A moderately complicated website can easily include anywhere from
10 to 200 resources. To be able to fetch those quickly, browsers will
make several GETrequests simultaneously, rather than waiting for the
responses one at a time.
HTML pages may include _forms_ , which allow the user to fill out
information and send it to the server. This is an example of a form:


```
<form method="GET" action="example/message.html">
<p>Name: <input type="text" name="name"></p>
<p>Message:<br><textarea name="message"></textarea></p>
<p><button type="submit">Send</button></p>
</form>
```
This code describes a form with two fields: a small one asking for a
name and a larger one to write a message in. When you click the Send
button, the form is _submitted_ , meaning that the content of its field is
packed into an HTTP request and the browser navigates to the result
of that request.
When the <form>element’s methodattribute is GET (or is omitted),
the information in the form is added to the end of theactionURL as
a _query string_. The browser might make a request to this URL:

```
GET /example/message.html?name=Jean&message=Yes%3F HTTP/1.1
```
The question mark indicates the end of the path part of the URL and
the start of the query. It is followed by pairs of names and values,
corresponding to thenameattribute on the form field elements and the
content of those elements, respectively. An ampersand character (&) is
used to separate the pairs.
The actual message encoded in the URL is “Yes?” but the question
mark is replaced by a strange code. Some characters in query strings
must be escaped. The question mark, represented as %3F, is one of
those. There seems to be an unwritten rule that every format needs
its own way of escaping characters. This one, called _URL encoding_ ,
uses a percent sign followed by two hexadecimal (base 16) digits that


encode the character code. In this case, 3F, which is 63 in decimal
notation, is the code of a question mark character. JavaScript provides
theencodeURIComponentanddecodeURIComponentfunctions to encode and
decode this format.

```
console.log(encodeURIComponent("Yes?"));
// → Yes%3F
console.log(decodeURIComponent("Yes%3F"));
// → Yes?
```
If we change themethodattribute of the HTML form in the example we
saw earlier toPOST, the HTTP request made to submit the form will use
thePOSTmethod and put the query string in the body of the request
rather than adding it to the URL.

```
POST /example/message.html HTTP/1.1
Content-length: 24
Content-type: application/x-www-form-urlencoded
```
```
name=Jean&message=Yes%3F
```
GET requests should be used for requests that do not have side effects
but simply ask for information. Requests that change something on the
server, for example creating a new account or posting a message, should
be expressed with other methods, such as POST. Client-side software
such as a browser knows that it shouldn’t blindly makePOSTrequests
but will often implicitly makeGET requests—to prefetch a resource it
believes the user will soon need, for example.
We’ll come back to forms and how to interact with them from JavaScript


later in the chapter.

### Fetch

The interface through which browser JavaScript can make HTTP re-
quests is calledfetch.

```
fetch("example/data.txt").then(response => {
console.log(response.status);
// → 200
console.log(response.headers.get("Content-Type"));
// → text/plain
});
```
Callingfetchreturns a promise that resolves to aResponseobject hold-
ing information about the server’s response, such as its status code and
its headers. The headers are wrapped in aMap-like object that treats its
keys (the header names) as case insensitive because header names are
not supposed to be case sensitive. This meansheaders.get("Content-
Type")andheaders.get("content-TYPE")will return the same value.
Note that the promise returned byfetchresolves successfully even if
the server responded with an error code. It can also be rejected if there
is a network error or if the server to which that the request is addressed
can’t be found.
The first argument to fetchis the URL that should be requested.
When that URL doesn’t start with a protocol name (such as _[http:](http:)_ ), it is
treated as _relative_ , which means it is interpreted relative to the current
document. When it starts with a slash (/), it replaces the current path,


which is the part after the server name. When it does not, the part of
the current path up to and including its last slash character is put in
front of the relative URL.
To get at the actual content of a response, you can use its text
method. Because the initial promise is resolved as soon as the re-
sponse’s headers have been received and because reading the response
body might take a while longer, this again returns a promise.

```
fetch("example/data.txt")
.then(resp => resp.text())
.then(text => console.log(text));
// → This is the content of data.txt
```
A similar method, calledjson, returns a promise that resolves to the
value you get when parsing the body as JSON or rejects if it’s not valid
JSON.
By default,fetchuses theGETmethod to make its request and does
not include a request body. You can configure it differently by passing
an object with extra options as a second argument. For example, this
request tries to deleteexample/data.txt:

```
fetch("example/data.txt", {method: "DELETE"}).then(resp => {
console.log(resp.status);
// → 405
});
```
The 405 status code means “method not allowed”, an HTTP server’s
way of saying “I’m afraid I can’t do that”.
To add a request body for aPUT orPOSTrequest, you can include a


bodyoption. To set headers, there’s theheadersoption. For example,
this request includes aRangeheader, which instructs the server to return
only part of a document.

```
fetch("example/data.txt", {headers: {Range: "bytes=8-19"}})
.then(resp => resp.text())
.then(console.log);
// → the content
```
The browser will automatically add some request headers, such as
“Host” and those needed for the server to figure out the size of the
body. But adding your own headers is often useful to include things
such as authentication information or to tell the server which file format
you’d like to receive.

### HTTP sandboxing.

Making HTTP requests in web page scripts once again raises concerns
about security. The person who controls the script might not have the
same interests as the person on whose computer it is running. More
specifically, if I visit _themafia.org_ , I do not want its scripts to be able
to make a request to _mybank.com_ , using identifying information from
my browser, with instructions to transfer away all my money.
For this reason, browsers protect us by disallowing scripts to make
HTTP requests to other domains (names such as _themafia.org_ and _my-
bank.com_ ).
This can be an annoying problem when building systems that want to
access several domains for legitimate reasons. Fortunately, servers can


include a header like this in their response to explicitly indicate to the
browser that it is okay for the request to come from another domain:

```
Access-Control-Allow-Origin: *
```
### Appreciating HTTP.

When building a system that requires communication between a JavaScript
program running in the browser (client-side) and a program on a server
(server-side), there are several different ways to model this communi-
cation.
A commonly used model is that of _remote procedure calls_. In this
model, communication follows the patterns of normal function calls, ex-
cept that the function is actually running on another machine. Calling
it involves making a request to the server that includes the function’s
name and arguments. The response to that request contains the re-
turned value.
When thinking in terms of remote procedure calls, HTTP is just a
vehicle for communication, and you will most likely write an abstraction
layer that hides it entirely.
Another approach is to build your communication around the concept
of resources and HTTP methods. Instead of a remote procedure called
addUser, you use aPUTrequest to/users/larry. Instead of encoding that
user’s properties in function arguments, you define a JSON document
format (or use an existing format) that represents a user. The body of
thePUTrequest to create a new resource is then such a document. A


resource is fetched by making aGETrequest to the resource’s URL (for
example,/users/larry), which again returns the document representing
the resource.
This second approach makes it easier to use some of the features that
HTTP provides, such as support for caching resources (keeping a copy
of a resource on the client for fast access). The concepts used in HTTP,
which are well designed, can provide a helpful set of principles to design
your server interface around.

### Security and HTTPS

Data traveling over the internet tends to follow a long, dangerous road.
To get to its destination, it must hop through anything from coffee shop
Wi-Fi hotspots to networks controlled by various companies and states.
At any point along its route, it may be inspected or even modified.
If it is important that something remain secret, such as the password
to your email account, or that it arrive at its destination unmodified,
such as the account number you transfer money to via your bank’s
website, plain HTTP is not good enough.
The secure HTTP protocol, used for URLs starting with _https://_ ,
wraps HTTP traﬀic in a way that makes it harder to read and tamper
with. Before exchanging data, the client verifies that the server is who it
claims to be by asking it to prove that it has a cryptographic certificate
issued by a certificate authority that the browser recognizes. Next,
all data going over the connection is encrypted in a way that should
prevent eavesdropping and tampering.


Thus, when it works right, HTTPS prevents other people from im-
personating the website you are trying to talk to _and_ from snooping
on your communication. It’s not perfect, and there have been various
incidents where HTTPS failed because of forged or stolen certificates
and broken software, but it is a _lot_ safer than plain HTTP.

### Form fields

Forms were originally designed for the pre-JavaScript web to allow web-
sites to send user-submitted information in an HTTP request. This
design assumes that interaction with the server always happens by nav-
igating to a new page.
However, the form elements are part of the DOM, like the rest of
the page, and the DOM elements that represent form fields support a
number of properties and events that are not present on other elements.
These make it possible to inspect and control such input fields with
JavaScript programs and do things such as adding new functionality
to a form or using forms and fields as building blocks in a JavaScript
application.
A web form consists of any number of input fields grouped in a<form>
tag. HTML allows several different styles of fields, ranging from simple
on/off checkboxes to drop-down menus and fields for text input. This
book won’t try to comprehensively discuss all field types, but we’ll start
with a rough overview.
A lot of field types use the<input>tag. This tag’stypeattribute is
used to select the field’s style. These are some commonly used<input>


types:
text A single-line text field
password Same astextbut hides the text that is typed
checkbox An on/off switch
color A color
date A calendar date
radio (Part of) a multiple-choice field
file Allows the user to choose a file from their computer
Form fields do not necessarily have to appear in a<form>tag. You
can put them anywhere in a page. Such form-less fields cannot be
submitted (only a form as a whole can), but when responding to input
with JavaScript, we often don’t want to submit our fields normally
anyway.

```
<p><input type="text" value="abc"> (text)</p>
<p><input type="password" value="abc"> (password)</p>
<p><input type="checkbox" checked> (checkbox)</p>
<p><input type="color" value="orange"> (color)</p>
<p><input type="date" value="2023-10-13"> (date)</p>
<p><input type="radio" value="A" name="choice">
<input type="radio" value="B" name="choice" checked>
<input type="radio" value="C" name="choice"> (radio)</p>
<p><input type="file"> (file)</p>
```
The fields created with this HTML code look like this:


The JavaScript interface for such elements differs with the type of
the element.
Multiline text fields have their own tag,<textarea>, mostly because
using an attribute to specify a multiline starting value would be awk-
ward. The<textarea>tag requires a matching</textarea>closing tag
and uses the text between those two, instead of thevalueattribute, as
starting text.

```
<textarea>
one
two
three
</textarea>
```
Finally, the<select>tag is used to create a field that allows the user
to select from a number of predefined options.

```
<select>
<option>Pancakes</option>
<option>Pudding</option>
<option>Ice cream</option>
</select>
```

Such a field looks like this:

Whenever the value of a form field changes, it will fire a "change"
event.

### Focus

Unlike most elements in HTML documents, form fields can get _keyboard
focus_. When clicked, moved to withtab, or activated in some other
way, they become the currently active element and the recipient of
keyboard input.
Thus, you can type into a text field only when it is focused. Other
fields respond differently to keyboard events. For example, a<select>
menu tries to move to the option that contains the text the user typed
and responds to the arrow keys by moving its selection up and down.
We can control focus from JavaScript with thefocusandblurmeth-
ods. The first moves focus to the DOM element it is called on, and the
second removes focus. The value indocument.activeElementcorresponds
to the currently focused element.

```
<input type="text">
<script>
document.querySelector("input").focus();
console.log(document.activeElement.tagName);
// → INPUT
```

```
document.querySelector("input").blur();
console.log(document.activeElement.tagName);
// → BODY
</script>
```
For some pages, the user is expected to want to interact with a form
field immediately. JavaScript can be used to focus this field when the
document is loaded, but HTML also provides theautofocusattribute,
which produces the same effect while letting the browser know what we
are trying to achieve. This gives the browser the option to disable the
behavior when it is not appropriate, such as when the user has put the
focus on something else.
Browsers allow the user to move the focus through the document by
pressingtabto move to the next focusable element, andshift-tabto
move back to the previous element. By default, elements are visited
in the order in which they appear in the document. It is possible to
use thetabindexattribute to change this order. The following example
document will let the focus jump from the text input to the OK button,
rather than going through the help link first:

```
<input type="text" tabindex=1> <a href=".">(help)</a>
<button onclick="console.log('ok')" tabindex=2>OK</button>
```
By default, most types of HTML elements cannot be focused. You
can add atabindexattribute to any element to make it focusable. A
tabindexof 0 makes an element focusable without affecting the focus
order.


### Disabled fields

All form fields can be _disabled_ through theirdisabledattribute. It is an
attribute that can be specified without value—the fact that it is present
at all disables the element.

```
<button>I'm all right</button>
<button disabled>I'm out</button>
```
Disabled fields cannot be focused or changed, and browsers make them
look gray and faded.

When a program is in the process of handling an action caused by
some button or other control that might require communication with
the server and thus take a while, it can be a good idea to disable the
control until the action finishes. That way, when the user gets impatient
and clicks it again, they don’t accidentally repeat their action.

### The form as a whole

When a field is contained in a<form>element, its DOM element will
have aform property linking back to the form’s DOM element. The
<form>element, in turn, has a property calledelementsthat contains an
array-like collection of the fields inside it.
Thenameattribute of a form field determines the way its value will be
identified when the form is submitted. It can also be used as a property


name when accessing the form’selementsproperty, which acts both as
an array-like object (accessible by number) and a map (accessible by
name).

```
<form action="example/submit.html">
Name: <input type="text" name="name"><br>
Password: <input type="password" name="password"><br>
<button type="submit">Log in</button>
</form>
<script>
let form = document.querySelector("form");
console.log(form.elements[1].type);
// → password
console.log(form.elements.password.type);
// → password
console.log(form.elements.name.form == form);
// → true
</script>
```
A button with atypeattribute ofsubmitwill, when pressed, cause the
form to be submitted. Pressingenterwhen a form field is focused has
the same effect.
Submitting a form normally means that the browser navigates to the
page indicated by the form’sactionattribute, using either aGET or a
POSTrequest. But before that happens, a"submit"event is fired. You
can handle this event with JavaScript and prevent this default behavior
by callingpreventDefaulton the event object.

```
<form>
Value: <input type="text" name="value">
```

```
<button type="submit">Save</button>
</form>
<script>
let form = document.querySelector("form");
form.addEventListener("submit", event => {
console.log("Saving value", form.elements.value.value);
event.preventDefault();
});
</script>
```
Intercepting "submit"events in JavaScript has various uses. We can
write code to verify that the values the user entered make sense and
immediately show an error message instead of submitting the form. Or
we can disable the regular way of submitting the form entirely, as in the
example, and have our program handle the input, possibly usingfetch
to send it to a server without reloading the page.

### Text fields

Fields created by<textarea>tags, or<input>tags with a type oftextor
password, share a common interface. Their DOM elements have avalue
property that holds their current content as a string value. Setting this
property to another string changes the field’s content.
TheselectionStartandselectionEndproperties of text fields give us
information about the cursor and selection in the text. When nothing
is selected, these two properties hold the same number, indicating the
position of the cursor. For example, 0 indicates the start of the text,
and 10 indicates the cursor is after the 10thcharacter. When part of


the field is selected, the two properties will differ, giving us the start
and end of the selected text. Likevalue, these properties may also be
written to.
Imagine you are writing an article about Khasekhemwy, last pharaoh
of the Second Dynasty, but have some trouble spelling his name. The
following code wires up a<textarea>tag with an event handler that,
when you press F2, inserts the string “Khasekhemwy” for you.

```
<textarea></textarea>
<script>
let textarea = document.querySelector("textarea");
textarea.addEventListener("keydown", event => {
if (event.key == "F2") {
replaceSelection(textarea, "Khasekhemwy");
event.preventDefault();
}
});
function replaceSelection(field, word) {
let from = field.selectionStart, to = field.selectionEnd;
field.value = field.value.slice(0, from) + word +
field.value.slice(to);
// Put the cursor after the word
field.selectionStart = from + word.length;
field.selectionEnd = from + word.length;
}
</script>
```
ThereplaceSelectionfunction replaces the currently selected part of a
text field’s content with the given word and then moves the cursor after
that word so that the user can continue typing.


The"change"event for a text field does not fire every time something
is typed. Rather, it fires when the field loses focus after its content was
changed. To respond immediately to changes in a text field, you should
register a handler for the"input"event instead, which fires every time
the user types a character, deletes text, or otherwise manipulates the
field’s content.
The following example shows a text field and a counter displaying
the current length of the text in the field:

```
<input type="text"> length: <span id="length">0</span>
<script>
let text = document.querySelector("input");
let output = document.querySelector("#length");
text.addEventListener("input", () => {
output.textContent = text.value.length;
});
</script>
```
### Checkboxes and radio buttons.

A checkbox field is a binary toggle. Its value can be extracted or
changed through itscheckedproperty, which holds a Boolean value.

```
<label>
<input type="checkbox" id="purple"> Make this page purple
</label>
<script>
let checkbox = document.querySelector("#purple");
```

```
checkbox.addEventListener("change", () => {
document.body.style.background =
checkbox.checked? "mediumpurple" : "";
});
</script>
```
The <label>tag associates a piece of document with an input field.
Clicking anywhere on the label will activate the field, which focuses it
and toggles its value when it is a checkbox or radio button.
A radio button is similar to a checkbox, but it’s implicitly linked to
other radio buttons with the samename attribute so that only one of
them can be active at any time.

```
Color:
<label>
<input type="radio" name="color" value="orange"> Orange
</label>
<label>
<input type="radio" name="color" value="lightgreen"> Green
</label>
<label>
<input type="radio" name="color" value="lightblue"> Blue
</label>
<script>
let buttons = document.querySelectorAll("[name=color]");
for (let button of Array.from(buttons)) {
button.addEventListener("change", () => {
document.body.style.background = button.value;
});
}
```

```
</script>
```
The square brackets in the CSS query given to querySelectorAllare
used to match attributes. It selects elements whose nameattribute is
"color".

### Select fields.

Select fields are conceptually similar to radio buttons—they also allow
the user to choose from a set of options. But where a radio button
puts the layout of the options under our control, the appearance of a
<select>tag is determined by the browser.
Select fields also have a variant more akin to a list of checkboxes
rather than radio boxes. When given themultipleattribute, a<select>
tag will allow the user to select any number of options, rather than
just a single option. Whereas a regular select field is drawn as a _drop-
down_ control, which shows the inactive options only when you open it,
a field withmultipleenabled shows multiple options at the same time,
allowing the user to enable or disable them individually.
Each <option> tag has a value. This value can be defined with a
valueattribute. When that is not given, the text inside the option will
count as its value. Thevalueproperty of a<select>element reflects
the currently selected option. For amultiplefield, though, this prop-
erty doesn’t mean much, since it will give the value of only _one_ of the
currently selected options.
The<option>tags for a<select>field can be accessed as an array-like
object through the field’soptionsproperty. Each option has a prop-


erty calledselected, which indicates whether that option is currently
selected. The property can also be written to select or deselect an
option.
This example extracts the selected values from amultipleselect field
and uses them to compose a binary number from individual bits. Hold
ctrl(orcommandon a Mac) to select multiple options.

```
<select multiple>
<option value="1">0001</option>
<option value="2">0010</option>
<option value="4">0100</option>
<option value="8">1000</option>
</select> = <span id="output">0</span>
<script>
let select = document.querySelector("select");
let output = document.querySelector("#output");
select.addEventListener("change", () => {
let number = 0;
for (let option of Array.from(select.options)) {
if (option.selected) {
number += Number(option.value);
}
}
output.textContent = number;
});
</script>
```

### File fields

File fields were originally designed as a way to upload files from the
user’s machine through a form. In modern browsers, they also provide
a way to read such files from JavaScript programs. The field acts as a
kind of gatekeeper. The script cannot simply start reading private files
from the user’s computer, but if the user selects a file in such a field,
the browser interprets that action to mean that the script may read the
file.
A file field usually looks like a button labeled with something like
“choose file” or “browse”, with information about the chosen file next
to it.

```
<input type="file">
<script>
let input = document.querySelector("input");
input.addEventListener("change", () => {
if (input.files.length > 0) {
let file = input.files[0];
console.log("You chose", file.name);
if (file.type) console.log("It has type", file.type);
}
});
</script>
```
Thefilesproperty of a file field element is an array-like object (once
again, not a real array) containing the files chosen in the field. It is
initially empty. The reason there isn’t simply afileproperty is that
file fields also support amultipleattribute, which makes it possible to


select multiple files at the same time.
The objects infileshave properties such asname(the filename),size
(the file’s size in bytes, which are chunks of 8 bits), andtype(the media
type of the file, such astext/plainorimage/jpeg).
What it does not have is a property that contains the content of the
file. Getting at that is a little more involved. Since reading a file from
disk can take time, the interface is asynchronous to avoid freezing the
window.

```
<input type="file" multiple>
<script>
let input = document.querySelector("input");
input.addEventListener("change", () => {
for (let file of Array.from(input.files)) {
let reader = new FileReader();
reader.addEventListener("load", () => {
console.log("File", file.name, "starts with",
reader.result.slice(0, 20));
});
reader.readAsText(file);
}
});
</script>
```
Reading a file is done by creating a FileReader object, registering a
"load"event handler for it, and calling its readAsTextmethod, giving
it the file we want to read. Once loading finishes, the reader’sresult
property contains the file’s content.
FileReaders also fire an"error"event when reading the file fails for


any reason. The error object itself will end up in the reader’serror
property. This interface was designed before promises became part of
the language. You could wrap it in a promise like this:

```
function readFileText(file) {
return new Promise((resolve, reject) => {
let reader = new FileReader();
reader.addEventListener(
"load", () => resolve(reader.result));
reader.addEventListener(
"error", () => reject(reader.error));
reader.readAsText(file);
});
}
```
### Storing data client-side

Simple HTML pages with a bit of JavaScript can be a great format
for “mini applications”—small helper programs that automate basic
tasks. By connecting a few form fields with event handlers, you can do
anything from converting between centimeters and inches to computing
passwords from a master password and a website name.
When such an application needs to remember something between
sessions, you cannot use JavaScript bindings—those are thrown away
every time the page is closed. You could set up a server, connect it
to the internet, and have your application store something there (we’ll
see how to do that inChapter 20). But that’s a lot of extra work and


complexity. Sometimes it’s enough to just keep the data in the browser.
The localStorage object can be used to store data in a way that
survives page reloads. This object allows you to file string values under
names.

```
localStorage.setItem("username", "marijn");
console.log(localStorage.getItem("username"));
// → marijn
localStorage.removeItem("username");
```
A value in localStoragesticks around until it is overwritten or is re-
moved withremoveItem, or the user clears their local data.
Sites from different domains get different storage compartments. That
means data stored inlocalStorageby a given website can, in principle,
be read (and overwritten) only by scripts on that same site.
Browsers do enforce a limit on the size of the data a site can store
inlocalStorage. That restriction, along with the fact that filling up
people’s hard drives with junk is not really profitable, prevents the
feature from eating up too much space.
The following code implements a crude note-taking application. It
keeps a set of named notes and allows the user to edit notes and create
new ones.

```
Notes: <select></select> <button>Add</button><br>
<textarea style="width: 100%"></textarea>
```
```
<script>
let list = document.querySelector("select");
let note = document.querySelector("textarea");
```

let state;
function setState(newState) {
list.textContent = "";
for (let name of Object.keys(newState.notes)) {
let option = document.createElement("option");
option.textContent = name;
if (newState.selected == name) option.selected = true;
list.appendChild(option);
}
note.value = newState.notes[newState.selected];

localStorage.setItem("Notes", JSON.stringify(newState));
state = newState;
}
setState(JSON.parse(localStorage.getItem("Notes")) ?? {
notes: {"shopping list": "Carrots\nRaisins"},
selected: "shopping list"
});

list.addEventListener("change", () => {
setState({notes: state.notes, selected: list.value});
});
note.addEventListener("change", () => {
let {selected} = state;
setState({
notes: {...state.notes, [selected]: note.value},
selected
});
});


```
document.querySelector("button")
.addEventListener("click", () => {
let name = prompt("Note name");
if (name) setState({
notes: {...state.notes, [name]: ""},
selected: name
});
});
</script>
```
The script gets its starting state from the "Notes" value stored in
localStorage or, if that’s missing, creates an example state that has
only a shopping list in it. Reading a field that does not exist from
localStoragewill yield null. Passing nullto JSON.parse will make it
parse the string"null"and returnnull. Thus, the??operator can be
used to provide a default value in a situation like this.
ThesetStatemethod makes sure the DOM is showing a given state
and stores the new state tolocalStorage. Event handlers call this func-
tion to move to a new state.
The... syntax in the example is used to create a new object that
is a clone of the oldstate.notes, but with one property added or over-
written. It uses spread syntax to first add the properties from the old
object and then set a new property. The square brackets notation in
the object literal is used to create a property whose name is based on
some dynamic value.
There is another object, similar tolocalStorage, calledsessionStorage

. The difference between the two is that the content ofsessionStorage
is forgotten at the end of each _session_ , which for most browsers means


whenever the browser is closed.

### Summary

In this chapter, we discussed how the HTTP protocol works. A _client_
sends a request, which contains a method (usually GET) and a path
that identifies a resource. The _server_ then decides what to do with the
request and responds with a status code and a response body. Both
requests and responses may contain headers that provide additional
information.
The interface through which browser JavaScript can make HTTP
requests is calledfetch. Making a request looks like this:

```
fetch("/18_http.html").then(r => r.text()).then(text => {
console.log(`The page starts with ${text.slice(0, 15)}`);
});
```
Browsers make GET requests to fetch the resources needed to display
a web page. A page may also contain forms, which allow information
entered by the user to be sent as a request for a new page when the
form is submitted.
HTML can represent various types of form fields, such as text fields,
checkboxes, multiple-choice fields, and file pickers. Such fields can be
inspected and manipulated with JavaScript. They fire the "change"
event when changed, fire the "input" event when text is typed, and
receive keyboard events when they have keyboard focus. Properties
like value (for text and select fields) or checked (for checkboxes and


radio buttons) are used to read or set the field’s content.
When a form is submitted, a"submit"event is fired on it. A JavaScript
handler can callpreventDefaulton that event to disable the browser’s
default behavior. Form field elements may also occur outside of a form
tag.
When the user has selected a file from their local filesystem in a file
picker field, theFileReaderinterface can be used to access the content
of this file from a JavaScript program.
The localStorage and sessionStorage objects can be used to save
information in a way that survives page reloads. The first object saves
the data forever (or until the user decides to clear it), and the second
saves it until the browser is closed.

### Exercises

**Contentnegotiation**

One of the things HTTP can do is called _content negotiation_. The
Acceptrequest header is used to tell the server what type of document
the client would like to get. Many servers ignore this header, but when
a server knows of various ways to encode a resource, it can look at this
header and send the one that the client prefers.
The URL _https://eloquentjavascript.net/author_ is configured to re-
spond with either plaintext, HTML, or JSON, depending on what the
client asks for. These formats are identified by the standardized _media
types_ text/plain,text/html, andapplication/json.
Send requests to fetch all three formats of this resource. Use the


headersproperty in the options object passed tofetchto set the header
namedAcceptto the desired media type.
Finally, try asking for the media typeapplication/rainbows+unicorns
and see which status code that produces.

**AJavaScriptworkbench**

Build an interface that allows users to type and run pieces of JavaScript
code.
Put a button next to a <textarea> field that, when pressed, uses
theFunctionconstructor we saw in Chapter 10to wrap the text in a
function and call it. Convert the return value of the function, or any
error it raises, to a string and display it below the text field.

**Conway'sGameofLife**

Conway’s Game of Life is a simple simulation that creates artificial “life”
on a grid, each cell of which is either alive or not. In each generation
(turn), the following rules are applied:

- Any live cell with fewer than two or more than three live neighbors
    dies.
- Any live cell with two or three live neighbors lives on to the next
    generation.
- Any dead cell with exactly three live neighbors becomes a live
    cell.


A _neighbor_ is defined as any adjacent cell, including diagonally adja-
cent ones.
Note that these rules are applied to the whole grid at once, not one
square at a time. That means the counting of neighbors is based on
the situation at the start of the generation, and changes happening to
neighbor cells during this generation should not influence the new state
of a given cell.
Implement this game using whichever data structure you find appro-
priate. Use Math.randomto populate the grid with a random pattern
initially. Display it as a grid of checkbox fields, with a button next to
it to advance to the next generation. When the user checks or unchecks
the checkboxes, their changes should be included when computing the
next generation.


```
“I look at the many colors before me. I look at my blank
canvas. Then, I try to apply colors like words that shape
poems, like notes that shape music.”
—Joan Miró
```
**Chapter19**

## Project: APixelArtEditor

The material from the previous chapters gives you all the elements you
need to build a basic web application. In this chapter, we will do just
that.
Our application will be a pixel-drawing program that allows you to
modify a picture pixel by pixel by manipulating a zoomed-in view of it,
shown as a grid of colored squares. You can use the program to open
image files, scribble on them with your mouse or other pointer device,
and save them. This is what it will look like:

```
Painting on a computer is great. You don’t need to worry about
```

materials, skill, or talent. You just start smearing and see where you
end up.

### Components

The interface for the application shows a big<canvas>element on top,
with a number of form fields below it. The user draws on the picture
by selecting a tool from a<select>field and then clicking, touching, or
dragging across the canvas. There are tools for drawing single pixels or
rectangles, for filling an area, and for picking a color from the picture.
We will structure the editor interface as a number of _components_ , ob-
jects that are responsible for a piece of the DOM and that may contain
other components inside them.
The state of the application consists of the current picture, the se-
lected tool, and the selected color. We’ll set things up so that the state
lives in a single value and the interface components always base the way
they look on the current state.
To see why this is important, let’s consider the alternative—distributing
pieces of state throughout the interface. Up to a certain point, this is
easier to program. We can just put in a color field and read its value
when we need to know the current color.
But then we add the color picker—a tool that lets you click the picture
to select the color of a given pixel. To keep the color field showing the
correct color, that tool would have to know that the color field exists and
update it whenever it picks a new color. If you ever add another place
that makes the color visible (maybe the mouse cursor could show it),


you have to update your color-changing code to keep that synchronized
as well.
In effect, this creates a problem where each part of the interface needs
to know about all other parts, which is not very modular. For small
applications like the one in this chapter, that may not be a problem.
For bigger projects, it can turn into a real nightmare.
To avoid this nightmare on principle, we’re going to be strict about
_data flow_. There is a state, and the interface is drawn based on that
state. An interface component may respond to user actions by updating
the state, at which point the components get a chance to synchronize
themselves with this new state.
In practice, each component is set up so that when it is given a new
state, it also notifies its child components, insofar as those need to be
updated. Setting this up is a bit of a hassle. Making this more conve-
nient is the main selling point of many browser programming libraries.
But for a small application like this, we can do it without such infras-
tructure.
Updates to the state are represented as objects, which we’ll call _ac-
tions_. Components may create such actions and _dispatch_ them—give
them to a central state management function. That function computes
the next state, after which the interface components update themselves
to this new state.
We’re taking the messy task of running a user interface and applying
structure to it. Though the DOM-related pieces are still full of side
effects, they are held up by a conceptually simple backbone: the state
update cycle. The state determines what the DOM looks like, and the


only way DOM events can change the state is by dispatching actions to

### The state

There are _many_ variants of this approach, each with its own benefits
and problems, but their central idea is the same: state changes should
go through a single well-defined channel, not happen all over the place.
Our components will be classes conforming to an interface. Their
constructor is given a state—which may be the whole application state
or some smaller value if it doesn’t need access to everything—and uses
that to build up adom property. This is the DOM element that rep-
resents the component. Most constructors will also take some other
values that won’t change over time, such as the function they can use
to dispatch an action.
Each component has asyncStatemethod that is used to synchronize
it to a new state value. The method takes one argument, the state,
which is of the same type as the first argument to its constructor.

### Thestate

The application state will be an object withpicture,tool, andcolor
properties. The picture is itself an object that stores the width, height,
and pixel content of the picture. The pixels are stored in a single array,
row by row, from top to bottom.

```
class Picture {
constructor(width, height, pixels) {
this.width = width;
this.height = height;
```

```
this.pixels = pixels;
}
static empty(width, height, color) {
let pixels = new Array(width * height).fill(color);
return new Picture(width, height, pixels);
}
pixel(x, y) {
return this.pixels[x + y * this.width];
}
draw(pixels) {
let copy = this.pixels.slice();
for (let {x, y, color} of pixels) {
copy[x + y * this.width] = color;
}
return new Picture(this.width, this.height, copy);
}
}
```
We want to be able to treat a picture as an immutable value, for reasons
we’ll get back to later in the chapter. But we also sometimes need to
update a whole bunch of pixels at a time. To be able to do that,
the class has adrawmethod that expects an array of updated pixels—
objects withx,y, andcolorproperties—and creates a new picture with
those pixels overwritten. This method usesslicewithout arguments to
copy the entire pixel array—the start of the slice defaults to 0, and the
end defaults to the array’s length.
The empty method uses two pieces of array functionality that we
haven’t seen before. TheArrayconstructor can be called with a number
to create an empty array of the given length. Thefillmethod can then


be used to fill this array with a given value. These are used to create
an array in which all pixels have the same color.
Colors are stored as strings containing traditional CSS color codes
made up of a hash sign (#) followed by six hexadecimal (base-16)
digits—two for the red component, two for the green component, and
two for the blue component. This is a somewhat cryptic and inconve-
nient way to write colors, but it is the format the HTML color input
field uses, and it can be used in the fillStyle property of a canvas
drawing context, so for the ways we’ll use colors in this program, it is
practical enough.
Black, where all components are zero, is written"#000000", and bright
pink looks like"#ff00ff", where the red and blue components have the
maximum value of 255, writtenffin hexadecimal digits (which use _a_
to _f_ to represent digits 10 to 15).
We’ll allow the interface to dispatch actions as objects whose proper-
ties overwrite the properties of the previous state. The color field, when
the user changes it, could dispatch an object like{color: field.value},
from which this update function can compute a new state.

```
function updateState(state, action) {
return {...state, ...action};
}
```
This pattern, in which object spread is used to first add the proper-
ties an existing object and then override some of those, is common in
JavaScript code that uses immutable objects.


### DOM building

One of the main things that interface components do is create DOM
structure. We again don’t want to directly use the verbose DOM meth-
ods for that, so here’s a slightly expanded version of theeltfunction:

```
function elt(type, props, ...children) {
let dom = document.createElement(type);
if (props) Object.assign(dom, props);
for (let child of children) {
if (typeof child != "string") dom.appendChild(child);
else dom.appendChild(document.createTextNode(child));
}
return dom;
}
```
The main difference between this version and the one we used inChap-
ter 16is that it assigns _properties_ to DOM nodes, not _attributes_. This
means we can’t use it to set arbitrary attributes, but we _can_ use it to
set properties whose value isn’t a string, such asonclick, which can be
set to a function to register a click event handler.
This allows this convenient style for registering event handlers:
<body>
<script>
document.body.appendChild(elt("button", {
onclick: () => console.log("click")
}, "The button"));
</script>
</body>


### The canvas

The first component we’ll define is the part of the interface that displays
the picture as a grid of colored boxes. This component is responsible
for two things: showing a picture and communicating pointer events on
that picture to the rest of the application.
Therefore, we can define it as a component that only knows about
the current picture, not the whole application state. Because it doesn’t
know how the application as a whole works, it cannot directly dispatch
actions. Rather, when responding to pointer events, it calls a callback
function provided by the code that created it, which will handle the
application-specific parts.

```
const scale = 10;
```
```
class PictureCanvas {
constructor(picture, pointerDown) {
this.dom = elt("canvas", {
onmousedown: event => this.mouse(event, pointerDown),
ontouchstart: event => this.touch(event, pointerDown)
});
this.syncState(picture);
}
syncState(picture) {
if (this.picture == picture) return;
this.picture = picture;
drawPicture(this.picture, this.dom, scale);
}
}
```

We draw each pixel as a 10-by-10 square, as determined by thescale
constant. To avoid unnecessary work, the component keeps track of its
current picture and does a redraw only whensyncStateis given a new
picture.
The actual drawing function sets the size of the canvas based on the
scale and picture size and fills it with a series of squares, one for each
pixel.

```
function drawPicture(picture, canvas, scale) {
canvas.width = picture.width * scale;
canvas.height = picture.height * scale;
let cx = canvas.getContext("2d");
```
```
for (let y = 0; y < picture.height; y++) {
for (let x = 0; x < picture.width; x++) {
cx.fillStyle = picture.pixel(x, y);
cx.fillRect(x * scale, y * scale, scale, scale);
}
}
}
```
When the left mouse button is pressed while the mouse is over the
picture canvas, the component calls thepointerDowncallback, giving it
the position of the pixel that was clicked—in picture coordinates. This
will be used to implement mouse interaction with the picture. The
callback may return another callback function to be notified when the
pointer is moved to a different pixel while the button is held down.

```
PictureCanvas.prototype.mouse = function(downEvent, onDown) {
```

```
if (downEvent.button != 0) return;
let pos = pointerPosition(downEvent, this.dom);
let onMove = onDown(pos);
if (!onMove) return;
let move = moveEvent => {
if (moveEvent.buttons == 0) {
this.dom.removeEventListener("mousemove", move);
} else {
let newPos = pointerPosition(moveEvent, this.dom);
if (newPos.x == pos.x && newPos.y == pos.y) return;
pos = newPos;
onMove(newPos);
}
};
this.dom.addEventListener("mousemove", move);
};
```
```
function pointerPosition(pos, domNode) {
let rect = domNode.getBoundingClientRect();
return {x: Math.floor((pos.clientX - rect.left) / scale),
y: Math.floor((pos.clientY - rect.top) / scale)};
}
```
Since we know the size of the pixels and we can usegetBoundingClientRect
to find the position of the canvas on the screen, it is possible to go from
mouse event coordinates (clientXandclientY) to picture coordinates.
These are always rounded down so that they refer to a specific pixel.
With touch events, we have to do something similar, but using differ-
ent events and making sure we callpreventDefaulton the"touchstart"
event to prevent panning.


```
PictureCanvas.prototype.touch = function(startEvent,
onDown) {
let pos = pointerPosition(startEvent.touches[0], this.dom);
let onMove = onDown(pos);
startEvent.preventDefault();
if (!onMove) return;
let move = moveEvent => {
let newPos = pointerPosition(moveEvent.touches[0],
this.dom);
if (newPos.x == pos.x && newPos.y == pos.y) return;
pos = newPos;
onMove(newPos);
};
let end = () => {
this.dom.removeEventListener("touchmove", move);
this.dom.removeEventListener("touchend", end);
};
this.dom.addEventListener("touchmove", move);
this.dom.addEventListener("touchend", end);
};
```
For touch events,clientXandclientYaren’t available directly on the
event object, but we can use the coordinates of the first touch object in
thetouchesproperty.

### The application

To make it possible to build the application piece by piece, we’ll im-
plement the main component as a shell around a picture canvas and a


dynamic set of tools and controls that we pass to its constructor.
The _controls_ are the interface elements that appear below the picture.
They’ll be provided as an array of component constructors.
The _tools_ do things like drawing pixels or filling in an area. The
application shows the set of available tools as a<select> field. The
currently selected tool determines what happens when the user interacts
with the picture with a pointer device. The set of available tools is
provided as an object that maps the names that appear in the drop-
down field to functions that implement the tools. Such functions get a
picture position, a current application state, and adispatchfunction as
arguments. They may return a move handler function that gets called
with a new position and a current state when the pointer moves to a
different pixel.

```
class PixelEditor {
constructor(state, config) {
let {tools, controls, dispatch} = config;
this.state = state;
```
```
this.canvas = new PictureCanvas(state.picture, pos => {
let tool = tools[this.state.tool];
let onMove = tool(pos, this.state, dispatch);
if (onMove) return pos => onMove(pos, this.state);
});
this.controls = controls.map(
Control => new Control(state, config));
this.dom = elt("div", {}, this.canvas.dom, elt("br"),
...this.controls.reduce(
(a, c) => a.concat(" ", c.dom), []));
```

```
}
syncState(state) {
this.state = state;
this.canvas.syncState(state.picture);
for (let ctrl of this.controls) ctrl.syncState(state);
}
}
```
The pointer handler given toPictureCanvascalls the currently selected
tool with the appropriate arguments and, if that returns a move handler,
adapts it to also receive the state.
All controls are constructed and stored inthis.controlsso that they
can be updated when the application state changes. The call toreduce
introduces spaces between the controls’ DOM elements. That way, they
don’t look so pressed together.
The first control is the tool selection menu. It creates a<select>ele-
ment with an option for each tool and sets up a"change"event handler
that updates the application state when the user selects a different tool.

```
class ToolSelect {
constructor(state, {tools, dispatch}) {
this.select = elt("select", {
onchange: () => dispatch({tool: this.select.value})
}, ...Object.keys(tools).map(name => elt("option", {
selected: name == state.tool
}, name)));
this.dom = elt("label", null, "🖌 Tool: ", this.select);
}
syncState(state) { this.select.value = state.tool; }
```

```
}
```
By wrapping the label text and the field in a<label>element, we tell
the browser that the label belongs to that field so that you can, for
example, click the label to focus the field.
We also need to be able to change the color, so let’s add a control for
that. An HTML<input>element with atypeattribute ofcolorgives us
a form field that is specialized for selecting colors. Such a field’s value
is always a CSS color code in"#RRGGBB"format (red, green, and blue
components, two digits per color). The browser will show a color picker
interface when the user interacts with it.
Depending on the browser, the color picker might look like this:

This control creates such a field and wires it up to stay synchronized
with the application state’scolorproperty.


```
class ColorSelect {
constructor(state, {dispatch}) {
this.input = elt("input", {
type: "color",
value: state.color,
onchange: () => dispatch({color: this.input.value})
});
this.dom = elt("label", null, "🎨 Color: ", this.input);
}
syncState(state) { this.input.value = state.color; }
}
```
### Drawing tools

Before we can draw anything, we need to implement the tools that will
control the functionality of mouse or touch events on the canvas.
The most basic tool is the draw tool, which changes any pixel you
click or tap to the currently selected color. It dispatches an action that
updates the picture to a version in which the pointed-at pixel is given
the currently selected color.

```
function draw(pos, state, dispatch) {
function drawPixel({x, y}, state) {
let drawn = {x, y, color: state.color};
dispatch({picture: state.picture.draw([drawn])});
}
drawPixel(pos, state);
return drawPixel;
```

```
}
```
The function immediately calls the drawPixel function but then also
returns it so that it’s called again for newly touched pixels when the
user drags or swipes over the picture.
To draw larger shapes, it can be useful to quickly create rectangles.
Therectangletool draws a rectangle between the point where you start
dragging and the point that you drag to.

```
function rectangle(start, state, dispatch) {
function drawRectangle(pos) {
let xStart = Math.min(start.x, pos.x);
let yStart = Math.min(start.y, pos.y);
let xEnd = Math.max(start.x, pos.x);
let yEnd = Math.max(start.y, pos.y);
let drawn = [];
for (let y = yStart; y <= yEnd; y++) {
for (let x = xStart; x <= xEnd; x++) {
drawn.push({x, y, color: state.color});
}
}
dispatch({picture: state.picture.draw(drawn)});
}
drawRectangle(start);
return drawRectangle;
}
```
An important detail in this implementation is that when dragging, the
rectangle is redrawn on the picture from the _original_ state. That way,
you can make the rectangle larger and smaller again while creating it,


without the intermediate rectangles sticking around in the final picture.
This is one of the reasons why immutable picture objects are useful—
we’ll see another reason later.
Implementing flood fill is somewhat more involved. This is a tool
that fills the pixel under the pointer and all adjacent pixels that have
the same color. “Adjacent” means directly horizontally or vertically
adjacent, not diagonally. This picture illustrates the set of pixels colored
when the flood fill tool is used at the marked pixel:

Interestingly, the way we’ll do this looks a bit like the pathfinding
code fromChapter 7. Whereas that code searched through a graph to
find a route, this code searches through a grid to find all “connected”
pixels. The problem of keeping track of a branching set of possible
routes is similar.

```
const around = [{dx: -1, dy: 0}, {dx: 1, dy: 0},
{dx: 0, dy: -1}, {dx: 0, dy: 1}];
```
```
function fill({x, y}, state, dispatch) {
let targetColor = state.picture.pixel(x, y);
let drawn = [{x, y, color: state.color}];
let visited = new Set();
for (let done = 0; done < drawn.length; done++) {
```

```
for (let {dx, dy} of around) {
let x = drawn[done].x + dx, y = drawn[done].y + dy;
if (x >= 0 && x < state.picture.width &&
y >= 0 && y < state.picture.height &&
!visited.has(x + "," + y) &&
state.picture.pixel(x, y) == targetColor) {
drawn.push({x, y, color: state.color});
visited.add(x + "," + y);
}
}
}
dispatch({picture: state.picture.draw(drawn)});
}
```
The array of drawn pixels doubles as the function’s work list. For each
pixel reached, we have to see whether any adjacent pixels have the
same color and haven’t already been painted over. The loop counter
lags behind the length of thedrawnarray as new pixels are added. Any
pixels ahead of it still need to be explored. When it catches up with
the length, no unexplored pixels remain, and the function is done.
The final tool is a color picker, which allows you to point at a color
in the picture to use it as the current drawing color.

```
function pick(pos, state, dispatch) {
dispatch({color: state.picture.pixel(pos.x, pos.y)});
}
```

### Saving and loading

When we’ve drawn our masterpiece, we’ll want to save it for later. We
should add a button for downloading the current picture as an image
file. This control provides that button:

```
class SaveButton {
constructor(state) {
this.picture = state.picture;
this.dom = elt("button", {
onclick: () => this.save()
}, "💾Save");
}
save() {
let canvas = elt("canvas");
drawPicture(this.picture, canvas, 1);
let link = elt("a", {
href: canvas.toDataURL(),
download: "pixelart.png"
});
document.body.appendChild(link);
link.click();
link.remove();
}
syncState(state) { this.picture = state.picture; }
}
```
The component keeps track of the current picture so that it can access
it when saving. To create the image file, it uses a<canvas>element on
which it draws the picture (at a scale of one pixel per pixel).


ThetoDataURLmethod on a canvas element creates a URL that uses
thedata:scheme. Unlikehttp:andhttps:URLs, data URLs contain
the whole resource in the URL. They are usually very long, but they
allow us to create working links to arbitrary pictures, right here in the
browser.
To actually get the browser to download the picture, we then create
a link element that points at this URL and has adownloadattribute.
Such links, when clicked, make the browser show a file save dialog. We
add that link to the document, simulate a click on it, and remove it
again. You can do a lot with browser technology, but sometimes the
way to do it is rather odd.
And it gets worse. We’ll also want to be able to load existing im-
age files into our application. To do that, we again define a button
component.

```
class LoadButton {
constructor(_, {dispatch}) {
this.dom = elt("button", {
onclick: () => startLoad(dispatch)
}, "📁Load");
}
syncState() {}
}
```
```
function startLoad(dispatch) {
let input = elt("input", {
type: "file",
onchange: () => finishLoad(input.files[0], dispatch)
```

```
});
document.body.appendChild(input);
input.click();
input.remove();
}
```
To get access to a file on the user’s computer, we need the user to select
the file through a file input field. But we don’t want the load button to
look like a file input field, so we create the file input when the button
is clicked and then pretend that this file input itself was clicked.
When the user has selected a file, we can useFileReaderto get access
to its contents, again as a data URL. That URL can be used to create
an<img>element, but because we can’t get direct access to the pixels
in such an image, we can’t create aPictureobject from that.

```
function finishLoad(file, dispatch) {
if (file == null) return;
let reader = new FileReader();
reader.addEventListener("load", () => {
let image = elt("img", {
onload: () => dispatch({
picture: pictureFromImage(image)
}),
src: reader.result
});
});
reader.readAsDataURL(file);
}
```
To get access to the pixels, we must first draw the picture to a<canvas>


element. The canvas context has agetImageDatamethod that allows a
script to read its pixels. So once the picture is on the canvas, we can
access it and construct aPictureobject.

```
function pictureFromImage(image) {
let width = Math.min(100, image.width);
let height = Math.min(100, image.height);
let canvas = elt("canvas", {width, height});
let cx = canvas.getContext("2d");
cx.drawImage(image, 0, 0);
let pixels = [];
let {data} = cx.getImageData(0, 0, width, height);
```
```
function hex(n) {
return n.toString(16).padStart(2, "0");
}
for (let i = 0; i < data.length; i += 4) {
let [r, g, b] = data.slice(i, i + 3);
pixels.push("#" + hex(r) + hex(g) + hex(b));
}
return new Picture(width, height, pixels);
}
```
We’ll limit the size of images to 100 by 100 pixels, since anything bigger
will look _huge_ on our display and might slow down the interface.
Thedataproperty of the object returned bygetImageDatais an array
of color components. For each pixel in the rectangle specified by the
arguments, it contains four values that represent the red, green, blue,
and _alpha_ components of the pixel’s color, as numbers between 0 and

255. The alpha part represents opacity—when it is 0, the pixel is fully


transparent, and when it is 255, it is fully opaque. For our purpose, we
can ignore it.
The two hexadecimal digits per component, as used in our color nota-
tion, correspond precisely to the 0 to 255 range—two base-16 digits can
express 16^2 = 256 different numbers. ThetoStringmethod of numbers
can be given a base as an argument, son.toString(16)will produce a
string representation in base 16. We have to make sure that each num-
ber takes up two digits, so thehexhelper function callspadStartto add
a leading 0 when necessary.
We can load and save now! That leaves just one more feature before
we’re done.

### Undo history.

Because half the process of editing is making little mistakes and cor-
recting them, an important feature in a drawing program is an undo
history.
To be able to undo changes, we need to store previous versions of the
picture. Since pictures are immutable values, that’s easy. But it does
require an additional field in the application state.
We’ll add adonearray to keep previous versions of the picture. Main-
taining this property requires a more complicated state update function
that adds pictures to the array.
We don’t want to store _every_ change, though—just changes that are
a certain amount of time apart. To be able to do that, we’ll need a
second property, doneAt, to track the time at which we last stored a


picture in the history.

```
function historyUpdateState(state, action) {
if (action.undo == true) {
if (state.done.length == 0) return state;
return {
...state,
picture: state.done[0],
done: state.done.slice(1),
doneAt: 0
};
} else if (action.picture &&
state.doneAt < Date.now() - 1000) {
return {
...state,
...action,
done: [state.picture, ...state.done],
doneAt: Date.now()
};
} else {
return {...state, ...action};
}
}
```
When the action is an undo action, the function takes the most recent
picture from the history and makes that the current picture. It sets
doneAtto zero so that the next change is guaranteed to store the picture
back in the history, allowing you to revert to it another time if you want.
Otherwise, if the action contains a new picture and the last time we
stored something is more than a second (1000 milliseconds) ago, the


doneanddoneAtproperties are updated to store the previous picture.
The undo button component doesn’t do much. It dispatches undo
actions when clicked and disables itself when there is nothing to undo.

```
class UndoButton {
constructor(state, {dispatch}) {
this.dom = elt("button", {
onclick: () => dispatch({undo: true}),
disabled: state.done.length == 0
}, "⮪Undo");
}
syncState(state) {
this.dom.disabled = state.done.length == 0;
}
}
```
### Let'sdraw

To set up the application, we need to create a state, a set of tools, a set of
controls, and a dispatch function. We can pass them to thePixelEditor
constructor to create the main component. Since we’ll need to create
several editors in the exercises, we first define some bindings.

```
const startState = {
tool: "draw",
color: "#000000",
picture: Picture.empty(60, 30, "#f0f0f0"),
done: [],
doneAt: 0
```

```
};
```
```
const baseTools = {draw, fill, rectangle, pick};
```
```
const baseControls = [
ToolSelect, ColorSelect, SaveButton, LoadButton, UndoButton
];
```
```
function startPixelEditor({state = startState,
tools = baseTools,
controls = baseControls}) {
let app = new PixelEditor(state, {
tools,
controls,
dispatch(action) {
state = historyUpdateState(state, action);
app.syncState(state);
}
});
return app.dom;
}
```
When destructuring an object or array, you can use=after a binding
name to give the binding a default value, which is used when the prop-
erty is missing or holdsundefined. ThestartPixelEditorfunction makes
use of this to accept an object with a number of optional properties as
an argument. If you don’t provide atoolsproperty, for example,tools
will be bound tobaseTools.
This is how we get an actual editor on the screen:


```
<div></div>
<script>
document.querySelector("div")
.appendChild(startPixelEditor({}));
</script>
```
### Why is this so hard?

Browser technology is amazing. It provides a powerful set of interface
building blocks, ways to style and manipulate them, and tools to inspect
and debug your applications. The software you write for the browser
can be run on almost every computer and phone on the planet.
At the same time, browser technology is ridiculous. You have to
learn a large number of silly tricks and obscure facts to master it, and
the default programming model it provides is so problematic that most
programmers prefer to cover it in several layers of abstraction rather
than deal with it directly.
While the situation is definitely improving, it mostly does so in the
form of more elements being added to address shortcomings—creating
even more complexity. A feature used by a million websites can’t really
be replaced. Even if it could, it would be hard to decide what it should
be replaced with.
Technology never exists in a vacuum—we’re constrained by our tools
and the social, economic, and historical factors that produced them.
This can be annoying, but it is generally more productive to try to build
a good understanding of how the _existing_ technical reality works—and


why it is the way it is—than to rage against it or hold out for another
reality.
New abstractions _can_ be helpful. The component model and data
flow convention I used in this chapter is a crude form of that. As men-
tioned, there are libraries that try to make user interface programming
more pleasant. At the time of writing, React and Svelte are popu-
lar choices, but there’s a whole cottage industry of such frameworks. If
you’re interested in programming web applications, I recommend inves-
tigating a few of them to understand how they work and what benefits
they provide.

### Exercises

There is still room for improvement in our program. Let’s add a few
more features as exercises.

**Keyboardbindings**

Add keyboard shortcuts to the application. The first letter of a tool’s
name selects the tool, andctrl-Z orcommand-Z activates undo.
Do this by modifying thePixelEditor component. Add atabIndex
property of 0 to the wrapping<div> element so that it can receive
keyboard focus. Note that the _property_ corresponding to thetabindex
_attribute_ is calledtabIndex, with a capital I, and oureltfunction ex-
pects property names. Register the key event handlers directly on that
element. This means you have to click, touch, or tab to the application
before you can interact with it with the keyboard.


Remember that keyboard events havectrlKeyandmetaKey(forcom-
mandon Mac) properties that you can use to see whether those keys
are held down.

**Efficientdrawing**

During drawing, the majority of work that our application does happens
indrawPicture. Creating a new state and updating the rest of the DOM
isn’t very expensive, but repainting all the pixels on the canvas is quite
a bit of work.
Find a way to make thesyncStatemethod ofPictureCanvasfaster by
redrawing only the pixels that actually changed.
Remember that drawPicture is also used by the save button, so if
you change it, either make sure the changes don’t break the old use or
create a new version with a different name.
Also note that changing the size of a<canvas>element, by setting
itswidthorheightproperties, clears it, making it entirely transparent
again.

**Circles**

Define a tool calledcirclethat draws a filled circle when you drag. The
center of the circle lies at the point where the drag or touch gesture
starts, and its radius is determined by the distance dragged.


**Properlines**

This is a more advanced exercise than the preceding three, and it will
require you to design a solution to a nontrivial problem. Make sure
you have plenty of time and patience before starting to work on this
exercise, and don’t get discouraged by initial failures.
On most browsers, when you select thedraw tool and quickly drag
across the picture, you don’t get a closed line. Rather, you get dots
with gaps between them because the"mousemove"or"touchmove"events
did not fire quickly enough to hit every pixel.
Improve thedrawtool to make it draw a full line. This means you have
to make the motion handler function remember the previous position
and connect that to the current one.
To do this, since the pixels can be an arbitrary distance apart, you’ll
have to write a general line drawing function.
A line between two pixels is a connected chain of pixels, as straight
as possible, going from the start to the end. Diagonally adjacent pixels
count as connected. A slanted line should look like the picture on the
left, not the picture on the right.

Finally, if we have code that draws a line between two arbitrary
points, we might as well use it to also define alinetool, which draws a


straight line between the start and end of a drag.


```
“A student asked, ‘The programmers of old used only simple
machines and no programming languages, yet they made
beautiful programs. Why do we use complicated machines and
programming languages?’ Fu-Tzu replied, ‘The builders of old
used only sticks and clay, yet they made beautiful huts.”’
—Master Yuan-Ma, The Book of Programming
```
**Chapter20**

## Node.js

So far, we’ve used the JavaScript language in a single environment: the
browser. This chapter and thenext onewill briefly introduce Node.js,
a program that allows you to apply your JavaScript skills outside of
the browser. With it, you can build anything from small command line
tools to HTTP servers that power dynamic websites.
These chapters aim to teach you the main concepts that Node.js uses
and to give you enough information to write useful programs for it.
They do not try to be a complete, or even a thorough, treatment of the
platform.
If you want to follow along and run the code in this chapter, you’ll
need to install Node.js version 18 or higher. To do so, go to _https://nodejs.org_
and follow the installation instructions for your operating system. You
can also find further documentation for Node.js there.


### Background.

When building systems that communicate over the network, the way
you manage input and output—that is, the reading and writing of data
to and from the network and hard drive—can make a big difference in
how quickly a system responds to the user or to network requests.
In such programs, asynchronous programming is often helpful. It
allows the program to send and receive data from and to multiple de-
vices at the same time without complicated thread management and
synchronization.
Node was initially conceived for the purpose of making asynchronous
programming easy and convenient. JavaScript lends itself well to a sys-
tem like Node. It is one of the few programming languages that does
not have a built-in way to do input and output. Thus, JavaScript could
be fit onto Node’s rather eccentric approach to network and filesys-
tem programming without ending up with two inconsistent interfaces.
In 2009, when Node was being designed, people were already doing
callback-based programming in the browser, so the community around
the language was used to an asynchronous programming style.

### The node command

When Node.js is installed on a system, it provides a program called
node, which is used to run JavaScript files. Say you have a filehello.js,
containing this code:

```
let message = "Hello world";
```

```
console.log(message);
```
You can then runnodefrom the command line like this to execute the
program:

```
$ node hello.js
Hello world
```
Theconsole.logmethod in Node does something similar to what it does
in the browser. It prints out a piece of text. But in Node, the text will
go to the process’s standard output stream rather than to a browser’s
JavaScript console. When runningnodefrom the command line, that
means you see the logged values in your terminal.
If you runnodewithout giving it a file, it provides you with a prompt
at which you can type JavaScript code and immediately see the result.

```
$ node
> 1 + 1
2
> [-1, -2, -3].map(Math.abs)
[1, 2, 3]
> process.exit(0)
$
```
Theprocessbinding, just like theconsolebinding, is available globally
in Node. It provides various ways to inspect and manipulate the current
program. Theexitmethod ends the process and can be given an exit
status code, which tells the program that startednode(in this case, the
command line shell) whether the program completed successfully (code
zero) or encountered an error (any other code).


To find the command line arguments given to your script, you can
readprocess.argv, which is an array of strings. Note that it also in-
cludes the name of the node command and your script name, so the
actual arguments start at index 2. Ifshowargv.js contains the state-
mentconsole.log(process.argv), you could run it like this:

```
$ node showargv.js one --and two
["node", "/tmp/showargv.js", "one", "--and", "two"]
```
All the standard JavaScript global bindings, such asArray,Math, and
JSON, are also present in Node’s environment. Browser-related function-
ality, such asdocumentorprompt, is not.

### Modules.

Beyond the bindings I mentioned, such asconsoleandprocess, Node
puts few additional bindings in the global scope. If you want to access
built-in functionality, you have to ask the module system for it.
Node started out using the CommonJS module system, based on the
require function, which we saw inChapter 10. It will still use this
system by default when you load a.jsfile.
But today, Node also supports the more modern ES module system.
When a script’s filename ends in .mjs, it is considered to be such a
module, and you can useimportandexportin it (but notrequire). We
will use ES modules in this chapter.
When importing a module—whether withrequireorimport—Node
has to resolve the given string to an actual file that it can load. Names


that start with/,./, or../are resolved as files, relative to the current
module’s path. Here, .stands for the current directory, ../ for one
directory up, and/for the root of the filesystem. If you ask for "./
graph.mjs"from the file/tmp/robot/robot.mjs, Node will try to load the
file/tmp/robot/graph.mjs.
When a string that does not look like a relative or absolute path is
imported, it is assumed to refer to either a built-in module or a module
installed in a node_modulesdirectory. For example, importing from"
node:fs" will give you Node’s built-in filesystem module. Importing
"robot"might try to load the library found innode_modules/robot/. It’s
common to install such libraries using NPM, which we’ll return to in a
moment.
Let’s set up a small project consisting of two files. The first one,
calledmain.mjs, defines a script that can be called from the command
line to reverse a string.

```
import {reverse} from "./reverse.mjs";
```
```
// Index 2 holds the first actual command line argument
let argument = process.argv[2];
```
```
console.log(reverse(argument));
```
The file reverse.mjsdefines a library for reversing strings, which can
be used both by this command line tool and by other scripts that need
direct access to a string-reversing function.

```
export function reverse(string) {
return Array.from(string).reverse().join("");
```

```
}
```
Remember thatexportis used to declare that a binding is part of the
module’s interface. That allowsmain.mjsto import and use the func-
tion.
We can now call our tool like this:
$ node main.mjs JavaScript
tpircSavaJ

### Installing with NPM

NPM, introduced inChapter 10, is an online repository of JavaScript
modules, many of which are specifically written for Node. When you
install Node on your computer, you also get thenpmcommand, which
you can use to interact with this repository.
NPM’s main use is downloading packages. We saw theinipackage
inChapter 10. We can use NPM to fetch and install that package on
our computer.

```
$ npm install ini
added 1 package in 723ms
```
```
$ node
> const {parse} = require("ini");
> parse("x = 1\ny = 2");
{ x: '1', y: '2' }
```

After running npm install, NPM will have created a directory called
node_modules. Inside that directory will be aninidirectory that con-
tains the library. You can open it and look at the code. When we
import"ini", this library is loaded, and we can call itsparseproperty
to parse a configuration file.
By default, NPM installs packages under the current directory rather
than in a central place. If you are used to other package managers, this
may seem unusual, but it has advantages—it puts each application in
full control of the packages it installs and makes it easier to manage
versions and clean up when removing an application.

**Packagefiles**

After running npm install to install some package, you will find not
only anode_modulesdirectory but also a file calledpackage.jsonin your
current directory. It is recommended to have such a file for each project.
You can create it manually or runnpm init. This file contains infor-
mation about the project, such as its name and version, and lists its
dependencies.
The robot simulation fromChapter 7, as modularized in the exercise
inChapter 10, might have apackage.jsonfile like this:

```
{
"author": "Marijn Haverbeke",
"name": "eloquent-javascript-robot",
"description": "Simulation of a package-delivery robot",
"version": "1.0.0",
"main": "run.mjs",
```

```
"dependencies": {
"dijkstrajs": "^1.0.1",
"random-item": "^1.0.0"
},
"license": "ISC"
}
```
When you runnpm installwithout naming a package to install, NPM
will install the dependencies listed inpackage.json. When you install a
specific package that is not already listed as a dependency, NPM will
add it topackage.json.

**Versions**

Apackage.jsonfile lists both the program’s own version and versions
for its dependencies. Versions are a way to deal with the fact that
packages evolve separately, and code written to work with a package as
it existed at one point may not work with a later, modified version of
the package.
NPM demands that its packages follow a schema called _semantic
versioning_ , which encodes some information about which versions are
_compatible_ (don’t break the old interface) in the version number. A
semantic version consists of three numbers separated by periods, such
as2.3.0. Every time new functionality is added, the middle number has
to be incremented. Every time compatibility is broken, so that existing
code that uses the package might not work with the new version, the
first number has to be incremented.
A caret character (^) in front of the version number for a dependency


inpackage.jsonindicates that any version compatible with the given
number may be installed. For example,"^2.3.0"would mean that any
version greater than or equal to 2.3.0 and less than 3.0.0 is allowed.
Thenpmcommand is also used to publish new packages or new ver-
sions of packages. If you run npm publish in a directory that has a
package.jsonfile, it will publish a package with the name and version
listed in the JSON file to the registry. Anyone can publish packages to
NPM—though only under a package name that isn’t in use yet, since
it wouldn’t be good if random people could update existing packages.
This book won’t delve further into the details of NPM usage. Refer
to _https://npmjs.com_ for further documentation and a way to search
for packages.

### The filesystem module

One of the most commonly used built-in modules in Node is thenode:fs
module, which stands for _filesystem_. It exports functions for working
with files and directories.
For example, the function calledreadFilereads a file and then calls
a callback with the file’s contents.

```
import {readFile} from "node:fs";
readFile("file.txt", "utf8", (error, text) => {
if (error) throw error;
console.log("The file contains:", text);
});
```
The second argument toreadFileindicates the _character encoding_ used


to decode the file into a string. There are several ways in which text
can be encoded to binary data, but most modern systems use UTF-8.
Unless you have reasons to believe another encoding is used, pass"utf8
"when reading a text file. If you do not pass an encoding, Node will
assume you are interested in the binary data and will give you aBuffer
object instead of a string. This is an array-like object that contains
numbers representing the bytes (8-bit chunks of data) in the files.

```
import {readFile} from "node:fs";
readFile("file.txt", (error, buffer) => {
if (error) throw error;
console.log("The file contained", buffer.length, "bytes.",
"The first byte is:", buffer[0]);
});
```
A similar function,writeFile, is used to write a file to disk.

```
import {writeFile} from "node:fs";
writeFile("graffiti.txt", "Node was here", err => {
if (err) console.log(`Failed to write file: ${err}`);
else console.log("File written.");
});
```
Here it was not necessary to specify the encoding—writeFilewill as-
sume that when it is given a string to write, rather than aBufferobject,
it should write it out as text using its default character encoding, which
is UTF-8.
Thenode:fsmodule contains many other useful functions: readdir
will give you the files in a directory as an array of strings, stat will
retrieve information about a file,renamewill rename a file,unlinkwill


remove one, and so on. See the documentation at _https://nodejs.org_ for
specifics.
Most of these take a callback function as the last parameter, which
they call either with an error (the first argument) or with a successful
result (the second). As we saw inChapter 11, there are downsides to
this style of programming—the biggest one being that error handling
becomes verbose and error prone.
Thenode:fs/promisesmodule exports most of the same functions as
the old node:fsmodule but uses promises rather than callback func-
tions.

```
import {readFile} from "node:fs/promises";
readFile("file.txt", "utf8")
.then(text => console.log("The file contains:", text));
```
Sometimes you don’t need asynchronicity and it just gets in the way.
Many of the functions innode:fsalso have a synchronous variant, which
has the same name with Sync added to the end. For example, the
synchronous version ofreadFileis calledreadFileSync.

```
import {readFileSync} from "node:fs";
console.log("The file contains:",
readFileSync("file.txt", "utf8"));
```
Note that while such a synchronous operation is being performed, your
program is stopped entirely. If it should be responding to the user or
to other machines on the network, being stuck on a synchronous action
might produce annoying delays.


### The HTTP module

Another central module is called node:http. It provides functionality
for running an HTTP server.
This is all it takes to start an HTTP server:
import {createServer} from "node:http";
let server = createServer((request, response) => {
response.writeHead(200, {"Content-Type": "text/html"});
response.write(`
<h1>Hello!</h1>
<p>You asked for <code>${request.url}</code></p>`);
response.end();
});
server.listen(8000);
console.log("Listening! (port 8000)");

If you run this script on your own machine, you can point your web
browser at _[http://localhost:8000/hello](http://localhost:8000/hello)_ to make a request to your server.
It will respond with a small HTML page.
The function passed as the argument tocreateServeris called every
time a client connects to the server. Therequestandresponsebindings
are objects representing the incoming and outgoing data. The first
contains information about the request, such as itsurlproperty, which
tells us to what URL the request was made.
When you open that page in your browser, it sends a request to your
own computer. This causes the server function to run and send back a
response, which you can then see in the browser.
To send something to the client, you call methods on theresponse


object. The first,writeHead, will write out the response headers (see
Chapter 18). You give it the status code (200 for “OK” in this case) and
an object that contains header values. The example sets theContent-
Typeheader to inform the client that we’ll be sending back an HTML
document.
Next, the actual response body (the document itself) is sent with
response.write. You’re allowed to call this method multiple times if
you want to send the response piece by piece—for example, to stream
data to the client as it becomes available. Finally,response.endsignals
the end of the response.
The call toserver.listencauses the server to start waiting for con-
nections on port 8000. This is why you have to connect to _localhost:8000_
to speak to this server, rather than just _localhost_ , which would use the
default port 80.
When you run this script, the process just sits there and waits. When
a script is listening for events—in this case, network connections—node
will not automatically exit when it reaches the end of the script. To
close it, pressctrl-C.
A real web server usually does more than the one in the example—it
looks at the request’s method (themethodproperty) to see what action
the client is trying to perform and looks at the request’s URL to find
out on which resource this action is being performed. We’ll see a more
advanced serverlater in this chapter.
Thenode:httpmodule also provides arequestfunction that can be
used to make HTTP requests. However, it is a lot more cumbersome to
use thanfetch, which we saw inChapter 18. Fortunately,fetchis also


available in Node as a global binding. Unless you want to do something
very specific, such as processing the response document piece by piece
as the data comes in over the network, I recommend sticking tofetch.

### Streams

The response object that the HTTP server could write to is an example
of a _writable stream_ object, which is a widely used concept in Node.
Such objects have a write method that can be passed a string or a
Buffer object to write something to the stream. Their end method
closes the stream and optionally takes a value to write to the stream
before closing. Both of these methods can also be given a callback as an
additional argument, which they will call when the writing or closing
has finished.
It is possible to create a writable stream that points at a file with the
createWriteStreamfunction from thenode:fsmodule. You can then use
thewritemethod on the resulting object to write the file one piece at
a time rather than in one shot, as withwriteFile.
_Readable streams_ are a little more involved. Therequestargument
to the HTTP server’s callback is a readable stream. Reading from a
stream is done using event handlers rather than methods.
Objects that emit events in Node have a method called onthat is
similar to theaddEventListenermethod in the browser. You give it an
event name and then a function, and it will register that function to be
called whenever the given event occurs.
Readable streams have"data"and"end"events. The first is fired ev-


ery time data comes in, and the second is called whenever the stream is
at its end. This model is most suited for _streaming_ data that can be im-
mediately processed, even when the whole document isn’t available yet.
A file can be read as a readable stream by using thecreateReadStream
function fromnode:fs.
This code creates a server that reads request bodies and streams them
back to the client as all-uppercase text:

```
import {createServer} from "node:http";
createServer((request, response) => {
response.writeHead(200, {"Content-Type": "text/plain"});
request.on("data", chunk =>
response.write(chunk.toString().toUpperCase()));
request.on("end", () => response.end());
}).listen(8000);
```
Thechunkvalue passed to the data handler will be a binaryBuffer. We
can convert this to a string by decoding it as UTF-8 encoded characters
with itstoStringmethod.
The following piece of code, when run with the uppercasing server
active, will send a request to that server and write out the response it
gets:

```
fetch("http://localhost:8000/", {
method: "POST",
body: "Hello server"
}).then(resp => resp.text()).then(console.log);
// → HELLO SERVER
```

### A file server

Let’s combine our newfound knowledge about HTTP servers and work-
ing with the filesystem to create a bridge between the two: an HTTP
server that allows remote access to a filesystem. Such a server has all
kinds of uses—it allows web applications to store and share data, or it
can give a group of people shared access to a bunch of files.
When we treat files as HTTP resources, the HTTP methodsGET,PUT,
andDELETEcan be used to read, write, and delete the files, respectively.
We will interpret the path in the request as the path of the file that the
request refers to.
We probably don’t want to share our whole filesystem, so we’ll in-
terpret these paths as starting in the server’s working directory, which
is the directory in which it was started. If I ran the server from/tmp/
public/(orC:\tmp\public\on Windows), then a request for/file.txt
should refer to/tmp/public/file.txt(orC:\tmp\public\file.txt).
We’ll build the program piece by piece, using an object calledmethods
to store the functions that handle the various HTTP methods. Method
handlers areasyncfunctions that get the request object as their argu-
ment and return a promise that resolves to an object that describes the
response.

```
import {createServer} from "node:http";
```
```
const methods = Object.create(null);
```
```
createServer((request, response) => {
let handler = methods[request.method] || notAllowed;
```

```
handler(request).catch(error => {
if (error.status != null) return error;
return {body: String(error), status: 500};
}).then(({body, status = 200, type = "text/plain"}) => {
response.writeHead(status, {"Content-Type": type});
if (body?.pipe) body.pipe(response);
else response.end(body);
});
}).listen(8000);
```
```
async function notAllowed(request) {
return {
status: 405,
body: `Method ${request.method} not allowed.`
};
}
```
This starts a server that just returns 405 error responses, which is the
code used to indicate that the server refuses to handle a given method.
When a request handler’s promise is rejected, thecatchcall translates
the error into a response object, if it isn’t one already, so that the server
can send back an error response to inform the client that it failed to
handle the request.
Thestatusfield of the response description may be omitted, in which
case it defaults to 200 (OK). The content type, in thetypeproperty,
can also be left off, in which case the response is assumed to be plain
text.
When the value of body is a readable stream, it will have a pipe
method that we can use to forward all content from a readable stream


to a writable stream. If not, it is assumed to be eithernull(no body),
a string, or a buffer, and it is passed directly to the response’s end
method.
To figure out which file path corresponds to a request URL, the
urlPath function uses the built-inURL class (which also exists in the
browser) to parse the URL. This constructor expects a full URL, not
just the part starting with the slash that we get fromrequest.url, so
we give it a dummy domain name to fill in. It extracts its pathname,
which will be something like"/file.txt", decodes that to get rid of the
%20-style escape codes, and resolves it relative to the program’s working
directory.

```
import {resolve, sep} from "node:path";
```
```
const baseDirectory = process.cwd();
```
```
function urlPath(url) {
let {pathname} = new URL(url, "http://d");
let path = resolve(decodeURIComponent(pathname).slice(1));
if (path != baseDirectory &&
!path.startsWith(baseDirectory + sep)) {
throw {status: 403, body: "Forbidden"};
}
return path;
}
```
As soon as you set up a program to accept network requests, you have
to start worrying about security. In this case, if we aren’t careful, it is
likely that we’ll accidentally expose our whole filesystem to the network.


File paths are strings in Node. To map such a string to an actual file,
there’s a nontrivial amount of interpretation going on. Paths may, for
example, include../to refer to a parent directory. One obvious source
of problems would be requests for paths like/../secret_file.
To avoid such problems,urlPathuses theresolvefunction from the
node:path module, which resolves relative paths. It then verifies that
the result is _below_ the working directory. The process.cwd function
(where cwd stands for _current working directory_ ) can be used to find
this working directory. Thesepbinding from thenode:pathpackage is
the system’s path separator—a backslash on Windows and a forward
slash on most other systems. When the path doesn’t start with the
base directory, the function throws an error response object, using the
HTTP status code indicating that access to the resource is forbidden.
We’ll set up theGETmethod to return a list of files when reading a
directory and to return the file’s content when reading a regular file.
One tricky question is what kind ofContent-Typeheader we should set
when returning a file’s content. Since these files could be anything, our
server can’t simply return the same content type for all of them. NPM
can help us again here. Themime-typespackage (content type indicators
liketext/plainare also called _MIME types_ ) knows the correct type for
a large number of file extensions.
The followingnpmcommand, in the directory where the server script
lives, installs a specific version ofmime:

```
$ npm install mime-types@2.1.0
```
When a requested file does not exist, the correct HTTP status code to


return is 404. We’ll use thestatfunction, which looks up information
about a file, to find out both whether the file exists and whether it is a
directory.

```
import {createReadStream} from "node:fs";
import {stat, readdir} from "node:fs/promises";
import {lookup} from "mime-types";
```
```
methods.GET = async function(request) {
let path = urlPath(request.url);
let stats;
try {
stats = await stat(path);
} catch (error) {
if (error.code != "ENOENT") throw error;
else return {status: 404, body: "File not found"};
}
if (stats.isDirectory()) {
return {body: (await readdir(path)).join("\n")};
} else {
return {body: createReadStream(path),
type: lookup(path)};
}
};
```
Because it has to touch the disk and thus might take a while,statis
asynchronous. Since we’re using promises rather than callback style,
it has to be imported from node:fs/promisesinstead of directly from
node:fs.
When the file does not exist, stat will throw an error object with


a codeproperty of "ENOENT". These somewhat obscure, Unix-inspired
codes are how you recognize error types in Node.
Thestatsobject returned bystattells us a number of things about
a file, such as its size (sizeproperty) and its modification date (mtime
property). Here we are interested in the question of whether it is a
directory or a regular file, which theisDirectorymethod tells us.
We use readdirto read the array of files in a directory and return
it to the client. For normal files, we create a readable stream with
createReadStreamand return that as the body, along with the content
type that themimepackage gives us for the file’s name.
The code to handleDELETErequests is slightly simpler.
import {rmdir, unlink} from "node:fs/promises";

```
methods.DELETE = async function(request) {
let path = urlPath(request.url);
let stats;
try {
stats = await stat(path);
} catch (error) {
if (error.code != "ENOENT") throw error;
else return {status: 204};
}
if (stats.isDirectory()) await rmdir(path);
else await unlink(path);
return {status: 204};
};
```
When an HTTP response does not contain any data, the status code


204 (“no content”) can be used to indicate this. Since the response to
deletion doesn’t need to transmit any information beyond whether the
operation succeeded, that is a sensible thing to return here.
You may be wondering why trying to delete a nonexistent file returns
a success status code rather than an error. When the file being deleted is
not there, you could say that the request’s objective is already fulfilled.
The HTTP standard encourages us to make requests _idempotent_ , which
means that making the same request multiple times produces the same
result as making it once. In a way, if you try to delete something that’s
already gone, the effect you were trying to create has been achieved—
the thing is no longer there.
This is the handler forPUTrequests:
import {createWriteStream} from "node:fs";

```
function pipeStream(from, to) {
return new Promise((resolve, reject) => {
from.on("error", reject);
to.on("error", reject);
to.on("finish", resolve);
from.pipe(to);
});
}
```
```
methods.PUT = async function(request) {
let path = urlPath(request.url);
await pipeStream(request, createWriteStream(path));
return {status: 204};
};
```

We don’t need to check whether the file exists this time—if it does,
we’ll just overwrite it. We again usepipeto move data from a readable
stream to a writable one, in this case from the request to the file. But
sincepipeisn’t written to return a promise, we have to write a wrapper,
pipeStream, that creates a promise around the outcome of callingpipe.
When something goes wrong when opening the file,createWriteStream
will still return a stream, but that stream will fire an "error"event.
The stream from the request may also fail—for example, if the network
goes down. So we wire up both streams’ "error"events to reject the
promise. When pipe is done, it will close the output stream, which
causes it to fire a "finish"event. That’s the point at which we can
successfully resolve the promise (returning nothing).
The full script for the server is available at _https://eloquentjavascript.net/
code/file_server.mjs_. You can download that and, after installing its
dependencies, run it with Node to start your own file server. And, of
course, you can modify and extend it to solve this chapter’s exercises
or to experiment.
The command line toolcurl, widely available on Unix-like systems
(such as macOS and Linux), can be used to make HTTP requests. The
following session briefly tests our server. The-Xoption is used to set
the request’s method, and-dis used to include a request body.

```
$ curl http://localhost:8000/file.txt
File not found
$ curl -X PUT -d CONTENT http://localhost:8000/file.txt
$ curl http://localhost:8000/file.txt
CONTENT
$ curl -X DELETE http://localhost:8000/file.txt
```

```
$ curl http://localhost:8000/file.txt
File not found
```
The first request forfile.txtfails since the file does not exist yet. The
PUT request creates the file, and behold, the next request successfully
retrieves it. After deleting it with aDELETE request, the file is again
missing.

### Summary

Node is a nice, small system that lets us run JavaScript in a nonbrowser
context. It was originally designed for network tasks to play the role of
a node in a network, but it lends itself to all kinds of scripting tasks. If
writing JavaScript is something you enjoy, automating tasks with Node
may work well for you.
NPM provides packages for everything you can think of (and quite a
few things you’d probably never think of), and it allows you to fetch and
install those packages with thenpmprogram. Node comes with a number
of built-in modules, including thenode:fsmodule for working with the
filesystem and thenode:httpmodule for running HTTP servers.
All input and output in Node is done asynchronously, unless you
explicitly use a synchronous variant of a function, such asreadFileSync

. Node originally used callbacks for asynchronous functionality, but
thenode:fs/promisespackage provides a promise-based interface to the
filesystem.


### Exercises

**Searchtool**

On Unix systems, there is a command line tool calledgrepthat can be
used to quickly search files for a regular expression.
Write a Node script that can be run from the command line and
acts somewhat likegrep. It treats its first command line argument as a
regular expression and treats any further arguments as files to search.
It outputs the names of any file whose content matches the regular
expression.
When that works, extend it so that when one of the arguments is a
directory, it searches through all files in that directory and its subdi-
rectories.
Use asynchronous or synchronous filesystem functions as you see fit.
Setting things up so that multiple asynchronous actions are requested
at the same time might speed things up a little, but not a huge amount,
since most filesystems can read only one thing at a time.

**Directorycreation**

Though theDELETEmethod in our file server is able to delete directories
(usingrmdir), the server currently does not provide any way to _create_
a directory.
Add support for theMKCOLmethod (“make collection”), which should
create a directory by callingmkdirfrom thenode:fsmodule.MKCOLis not
a widely used HTTP method, but it does exist for this same purpose


in the _WebDAV_ standard, which specifies a set of conventions on top
of HTTP that make it suitable for creating documents.

**Apublicspaceontheweb**

Since the file server serves up any kind of file and even includes the right
Content-Typeheader, you can use it to serve a website. Given that this
server allows everybody to delete and replace files, this would make for
an interesting kind of website: one that can be modified, improved, and
vandalized by everybody who takes the time to make the right HTTP
request.
Write a basic HTML page that includes a simple JavaScript file. Put
the files in a directory served by the file server and open them in your
browser.
Next, as an advanced exercise or even a weekend project, combine all
the knowledge you gained from this book to build a more user-friendly
interface for modifying the website—from _inside_ the website.
Use an HTML form to edit the content of the files that make up the
website, allowing the user to update them on the server by using HTTP
requests, as described inChapter 18.
Start by making only a single file editable. Then make it so that
the user can select which file to edit. Use the fact that our file server
returns lists of files when reading a directory.
Don’t work directly in the code exposed by the file server, since if
you make a mistake, you are likely to damage the files there. Instead,
keep your work outside of the publicly accessible directory and copy it
there when testing.


```
“If you have knowledge, let others light their candles at it.”
—Margaret Fuller
```
**Chapter21**

## Project: Skill-SharingWebsite

A _skill-sharing_ meeting is an event where people with a shared interest
come together and give small, informal presentations about things they
know. At a gardening skill-sharing meeting, someone might explain
how to cultivate celery. Or in a programming skill-sharing group, you
could drop by and tell people about Node.js.
In this final project chapter, our goal is to set up a website for man-
aging talks given at a skill-sharing meeting. Imagine a small group of
people meeting up regularly in the oﬀice of one of the members to talk
about unicycling. The previous organizer of the meetings moved to
another town, and nobody stepped forward to take over this task. We
want a system that will let the participants propose and discuss talks
among themselves without an active organizer.
The full code for the project can be downloaded from _https://eloquentjavascript.net/
code/skillsharing.zip_.


### Design.

There is a _server_ part to this project, written for Node.js, and a _client_
part, written for the browser. The server stores the system’s data and
provides it to the client. It also serves the files that implement the
client-side system.
The server keeps the list of talks proposed for the next meeting, and
the client shows this list. Each talk has a presenter name, a title, a sum-
mary, and an array of comments associated with it. The client allows
users to propose new talks (adding them to the list), delete talks, and
comment on existing talks. Whenever the user makes such a change,
the client makes an HTTP request to tell the server about it.


The application will be set up to show a _live_ view of the current
proposed talks and their comments. Whenever someone, somewhere,
submits a new talk or adds a comment, all people who have the page
open in their browsers should immediately see the change. This poses a
bit of a challenge—there is no way for a web server to open a connection
to a client, nor is there a good way to know which clients are currently
looking at a given website.
A common solution to this problem is called _long polling_ , which hap-


pens to be one of the motivations for Node’s design.

### Long polling

To be able to immediately notify a client that something changed, we
need a connection to that client. Since web browsers do not traditionally
accept connections and clients are often behind routers that would block
such connections anyway, having the server initiate this connection is
not practical.
We can arrange for the client to open the connection and keep it
around so that the server can use it to send information when it needs
to do so. But an HTTP request allows only a simple flow of information:
the client sends a request, the server comes back with a single response,
and that’s it. A technology called _WebSockets_ makes it possible to
open connections for arbitrary data exchange, but using such sockets
properly is somewhat tricky.
In this chapter, we use a simpler technique, long polling, where clients
continuously ask the server for new information using regular HTTP
requests, and the server stalls its answer when it has nothing new to
report.
As long as the client makes sure it constantly has a polling request
open, it will receive information from the server quickly after it becomes
available. For example, if Fatma has our skill-sharing application open
in her browser, that browser will have made a request for updates and
will be waiting for a response to that request. When Iman submits a
talk on Extreme Downhill Unicycling, the server will notice that Fatma


is waiting for updates and send a response containing the new talk to
her pending request. Fatma’s browser will receive the data and update
the screen to show the talk.
To prevent connections from timing out (being aborted because of a
lack of activity), long polling techniques usually set a maximum time for
each request, after which the server will respond anyway, even though
it has nothing to report. The client can then start a new request. Pe-
riodically restarting the request also makes the technique more robust,
allowing clients to recover from temporary connection failures or server
problems.
A busy server that is using long polling may have thousands of wait-
ing requests, and thus TCP connections, open. Node, which makes it
easy to manage many connections without creating a separate thread
of control for each one, is a good fit for such a system.

### HTTP interface

Before we start designing either the server or the client, let’s think
about the point where they touch: the HTTP interface over which they
communicate.
We will use JSON as the format of our request and response body.
Like in the file server fromChapter 20, we’ll try to make good use of
HTTP methods and headers. The interface is centered around the /
talkspath. Paths that do not start with/talkswill be used for serving
static files—the HTML and JavaScript code for the client-side system.
AGETrequest to/talksreturns a JSON document like this:


```
[{"title": "Unituning",
"presenter": "Jamal",
"summary": "Modifying your cycle for extra style",
"comments": []}]
```
Creating a new talk is done by making a PUT request to a URL like
/talks/Unituning, where the part after the second slash is the title of
the talk. ThePUT request’s body should contain a JSON object that
haspresenterandsummaryproperties.
Since talk titles may contain spaces and other characters that may
not appear normally in a URL, title strings must be encoded with the
encodeURIComponentfunction when building up such a URL.

```
console.log("/talks/" + encodeURIComponent("How to Idle"));
// → /talks/How%20to%20Idle
```
A request to create a talk about idling might look something like this:

```
PUT /talks/How%20to%20Idle HTTP/1.1
Content-Type: application/json
Content-Length: 92
```
```
{"presenter": "Maureen",
"summary": "Standing still on a unicycle"}
```
Such URLs also supportGETrequests to retrieve the JSON representa-
tion of a talk andDELETErequests to delete a talk.
Adding a comment to a talk is done with aPOSTrequest to a URL
like/talks/Unituning/comments, with a JSON body that hasauthorand
messageproperties.


```
POST /talks/Unituning/comments HTTP/1.1
Content-Type: application/json
Content-Length: 72
```
```
{"author": "Iman",
"message": "Will you talk about raising a cycle?"}
```
To support long polling,GETrequests to/talksmay include extra head-
ers that inform the server to delay the response if no new information
is available. We’ll use a pair of headers normally intended to manage
caching: ETagandIf-None-Match.
Servers may include an ETag (“entity tag”) header in a response.
Its value is a string that identifies the current version of the resource.
Clients, when they later request that resource again, may make a _condi-
tional request_ by including anIf-None-Matchheader whose value holds
that same string. If the resource hasn’t changed, the server will re-
spond with status code 304, which means “not modified”, telling the
client that its cached version is still current. When the tag does not
match, the server responds as normal.
We need something like this, where the client can tell the server which
version of the list of talks it has, and the server responds only when that
list has changed. But instead of immediately returning a 304 response,
the server should stall the response and return only when something
new is available or a given amount of time has elapsed. To distinguish
long polling requests from normal conditional requests, we give them
another header,Prefer: wait=90, which tells the server that the client
is willing to wait up to 90 seconds for the response.
The server will keep a version number that it updates every time


the talks change and will use that as theETagvalue. Clients can make
requests like this to be notified when the talks change:

```
GET /talks HTTP/1.1
If-None-Match: "4"
Prefer: wait=90
```
```
(time passes)
```
```
HTTP/1.1 200 OK
Content-Type: application/json
ETag: "5"
Content-Length: 295
```
```
[...]
```
The protocol described here doesn’t do any access control. Everybody
can comment, modify talks, and even delete them. (Since the inter-
net is full of hooligans, putting such a system online without further
protection probably wouldn’t end well.)

### The server

Let’s start by building the server-side part of the program. The code
in this section runs on Node.js.


**Routing**

Our server will use Node’screateServerto start an HTTP server. In the
function that handles a new request, we must distinguish between the
various kinds of requests (as determined by the method and the path)
that we support. This can be done with a long chain ofifstatements,
but there’s a nicer way.
A _router_ is a component that helps dispatch a request to the function
that can handle it. You can tell the router, for example, that PUT
requests with a path that matches the regular expression /^\/talks
\/([^\/]+)$/ (/talks/ followed by a talk title) can be handled by a
given function. In addition, it can help extract the meaningful parts
of the path (in this case the talk title), wrapped in parentheses in the
regular expression, and pass them to the handler function.
There are a number of good router packages on NPM, but here we’ll
write one ourselves to illustrate the principle.
This isrouter.mjs, which we will laterimportfrom our server module:
export class Router {
constructor() {
this.routes = [];
}
add(method, url, handler) {
this.routes.push({method, url, handler});
}
async resolve(request, context) {
let {pathname} = new URL(request.url, "http://d");
for (let {method, url, handler} of this.routes) {
let match = url.exec(pathname);


```
if (!match || request.method != method) continue;
let parts = match.slice(1).map(decodeURIComponent);
return handler(context, ...parts, request);
}
}
}
```
The module exports the Router class. A router object allows you to
register handlers for specific methods and URL patterns with its add
method. When a request is resolved with the resolvemethod, the
router calls the handler whose method and URL match the request and
return its result.
Handler functions are called with thecontextvalue given toresolve.
We will use this to give them access to our server state. Additionally,
they receive the match strings for any groups they defined in their
regular expression, and the request object. The strings have to be
URL-decoded, since the raw URL may contain%20-style codes.

**Servingfiles**

When a request matches none of the request types defined in our router,
the server must interpret it as a request for a file in thepublicdirectory.
It would be possible to use the file server defined inChapter 20to serve
such files, but we neither need nor want to support PUT and DELETE
requests on files, and we would like to have advanced features such as
support for caching. Let’s use a solid, well-tested static file server from
NPM instead.
I opted forserve-static. This isn’t the only such server on NPM,


but it works well and fits our purposes. The serve-static package
exports a function that can be called with a root directory to produce
a request handler function. The handler function accepts therequest
andresponsearguments provided by the server from"node:http", and a
third argument, a function that it will call if no file matches the request.
We want our server to first check for requests we should handle specially,
as defined in the router, so we wrap it in another function.

```
import {createServer} from "node:http";
import serveStatic from "serve-static";
```
```
function notFound(request, response) {
response.writeHead(404, "Not found");
response.end("<h1>Not found</h1>");
}
```
```
class SkillShareServer {
constructor(talks) {
this.talks = talks;
this.version = 0;
this.waiting = [];
```
```
let fileServer = serveStatic("./public");
this.server = createServer((request, response) => {
serveFromRouter(this, request, response, () => {
fileServer(request, response,
() => notFound(request, response));
});
});
}
```

```
start(port) {
this.server.listen(port);
}
stop() {
this.server.close();
}
}
```
TheserveFromRouterfunction has the same interface asfileServer, tak-
ing(request, response, next)arguments. We can use this to “chain”
several request handlers, allowing each to either handle the request or
pass responsibility for that on to the next handler. The final handler,
notFound, simply responds with a “not found” error.
Our serveFromRouter function uses a similar convention to the file
server from theprevious chapterfor responses—handlers in the router
return promises that resolve to objects describing the response.

```
import {Router} from "./router.mjs";
```
```
const router = new Router();
const defaultHeaders = {"Content-Type": "text/plain"};
```
```
async function serveFromRouter(server, request,
response, next) {
let resolved = await router.resolve(request, server)
.catch(error => {
if (error.status != null) return error;
return {body: String(err), status: 500};
});
if (!resolved) return next();
```

```
let {body, status = 200, headers = defaultHeaders} =
await resolved;
response.writeHead(status, headers);
response.end(body);
}
```
**Talksasresources**

The talks that have been proposed are stored in thetalksproperty of
the server, an object whose property names are the talk titles. We’ll
add some handlers to our router that expose these as HTTP resources
under/talks/<title>.
The handler for requests that GET a single talk must look up the
talk and respond either with the talk’s JSON data or with a 404 error
response.

```
const talkPath = /^\/talks\/([^\/]+)$/;
```
```
router.add("GET", talkPath, async (server, title) => {
if (Object.hasOwn(server.talks, title)) {
return {body: JSON.stringify(server.talks[title]),
headers: {"Content-Type": "application/json"}};
} else {
return {status: 404, body: `No talk '${title}' found`};
}
});
```
Deleting a talk is done by removing it from thetalksobject.


```
router.add("DELETE", talkPath, async (server, title) => {
if (Object.hasOwn(server.talks, title)) {
delete server.talks[title];
server.updated();
}
return {status: 204};
});
```
Theupdatedmethod, which we will definelater, notifies waiting long
polling requests about the change.
One handler that needs to read request bodies is thePUT handler,
which is used to create new talks. It has to check whether the data it
was given haspresenterandsummaryproperties, which are strings. Any
data coming from outside the system might be nonsense, and we don’t
want to corrupt our internal data model or crash when bad requests
come in.
If the data looks valid, the handler stores an object that represents
the new talk in thetalksobject, possibly overwriting an existing talk
with this title, and again callsupdated.
To read the body from the request stream, we will use thejsonfunc-
tion from"node:stream/consumers", which collects the data in the stream
and then parses it as JSON. There are similar exports calledtext(to
read the content as a string) andbuffer(to read it as binary data) in
this package. Sincejsonis a very generic name, the import renames it
toreadJSONto avoid confusion.

```
import {json as readJSON} from "node:stream/consumers";
```

```
router.add("PUT", talkPath,
async (server, title, request) => {
let talk = await readJSON(request);
if (!talk ||
typeof talk.presenter != "string" ||
typeof talk.summary != "string") {
return {status: 400, body: "Bad talk data"};
}
server.talks[title] = {
title,
presenter: talk.presenter,
summary: talk.summary,
comments: []
};
server.updated();
return {status: 204};
});
```
Adding a comment to a talk works similarly. We use readJSONto get
the content of the request, validate the resulting data, and store it as a
comment when it looks valid.

```
router.add("POST", /^\/talks\/([^\/]+)\/comments$/,
async (server, title, request) => {
let comment = await readJSON(request);
if (!comment ||
typeof comment.author != "string" ||
typeof comment.message != "string") {
return {status: 400, body: "Bad comment data"};
} else if (Object.hasOwn(server.talks, title)) {
```

```
server.talks[title].comments.push(comment);
server.updated();
return {status: 204};
} else {
return {status: 404, body: `No talk '${title}' found`};
}
});
```
Trying to add a comment to a nonexistent talk returns a 404 error.

**Longpollingsupport**

The most interesting aspect of the server is the part that handles long
polling. When aGET request comes in for/talks, it may be either a
regular request or a long polling request.
There will be multiple places in which we have to send an array of
talks to the client, so we first define a helper method that builds up
such an array and includes anETagheader in the response.

```
SkillShareServer.prototype.talkResponse = function() {
let talks = Object.keys(this.talks)
.map(title => this.talks[title]);
return {
body: JSON.stringify(talks),
headers: {"Content-Type": "application/json",
"ETag": `"${this.version}"`,
"Cache-Control": "no-store"}
};
};
```

The handler itself needs to look at the request headers to see whether
If-None-Match and Prefer headers are present. Node stores headers,
whose names are specified to be case insensitive, under their lowercase
names.

```
router.add("GET", /^\/talks$/, async (server, request) => {
let tag = /"(.*)"/.exec(request.headers["if-none-match"]);
let wait = /\bwait=(\d+)/.exec(request.headers["prefer"]);
if (!tag || tag[1] != server.version) {
return server.talkResponse();
} else if (!wait) {
return {status: 304};
} else {
return server.waitForChanges(Number(wait[1]));
}
});
```
If no tag was given or a tag was given that doesn’t match the server’s
current version, the handler responds with the list of talks. If the
request is conditional and the talks did not change, we consult the
Preferheader to see whether we should delay the response or respond
right away.
Callback functions for delayed requests are stored in the server’s
waitingarray so that they can be notified when something happens.
ThewaitForChanges method also immediately sets a timer to respond
with a 304 status when the request has waited long enough.

```
SkillShareServer.prototype.waitForChanges = function(time) {
return new Promise(resolve => {
```

```
this.waiting.push(resolve);
setTimeout(() => {
if (!this.waiting.includes(resolve)) return;
this.waiting = this.waiting.filter(r => r != resolve);
resolve({status: 304});
}, time * 1000);
});
};
```
Registering a change withupdatedincreases theversionproperty and
wakes up all waiting requests.

```
SkillShareServer.prototype.updated = function() {
this.version++;
let response = this.talkResponse();
this.waiting.forEach(resolve => resolve(response));
this.waiting = [];
};
```
That concludes the server code. If we create an instance ofSkillShareServer
and start it on port 8000, the resulting HTTP server serves files from
thepublicsubdirectory alongside a talk-managing interface under the
/talksURL.

```
new SkillShareServer({}).start(8000);
```

### The client.

The client-side part of the skill-sharing website consists of three files: a
tiny HTML page, a style sheet, and a JavaScript file.

#### HTML

It is a widely used convention for web servers to try to serve a file named
index.htmlwhen a request is made directly to a path that corresponds
to a directory. The file server module we use,serve-static, supports
this convention. When a request is made to the path/, the server looks
for the file./public/index.html(./publicbeing the root we gave it) and
returns that file if found.
Thus, if we want a page to show up when a browser is pointed at our
server, we should put it inpublic/index.html. This is our index file:

```
<!doctype html>
<meta charset="utf-8">
<title>Skill Sharing</title>
<link rel="stylesheet" href="skillsharing.css">
```
```
<h1>Skill Sharing</h1>
```
```
<script src="skillsharing_client.js"></script>
```
It defines the document title and includes a style sheet, which defines
a few styles to, among other things, make sure there is some space
between talks. It then adds a heading at the top of the page and loads
the script that contains the client-side application.


**Actions**

The application state consists of the list of talks and the name of the
user, and we’ll store it in a{talks, user}object. We don’t allow the
user interface to directly manipulate the state or send off HTTP re-
quests. Rather, it may emit _actions_ that describe what the user is
trying to do.
ThehandleActionfunction takes such an action and makes it happen.
Because our state updates are so simple, state changes are handled in
the same function.

```
function handleAction(state, action) {
if (action.type == "setUser") {
localStorage.setItem("userName", action.user);
return {...state, user: action.user};
} else if (action.type == "setTalks") {
return {...state, talks: action.talks};
} else if (action.type == "newTalk") {
fetchOK(talkURL(action.title), {
method: "PUT",
headers: {"Content-Type": "application/json"},
body: JSON.stringify({
presenter: state.user,
summary: action.summary
})
}).catch(reportError);
} else if (action.type == "deleteTalk") {
fetchOK(talkURL(action.talk), {method: "DELETE"})
.catch(reportError);
} else if (action.type == "newComment") {
```

```
fetchOK(talkURL(action.talk) + "/comments", {
method: "POST",
headers: {"Content-Type": "application/json"},
body: JSON.stringify({
author: state.user,
message: action.message
})
}).catch(reportError);
}
return state;
}
```
We’ll store the user’s name inlocalStorageso that it can be restored
when the page is loaded.
The actions that need to involve the server make network requests,
usingfetch, to the HTTP interface described earlier. We use a wrapper
function, fetchOK, which makes sure the returned promise is rejected
when the server returns an error code.

```
function fetchOK(url, options) {
return fetch(url, options).then(response => {
if (response.status < 400) return response;
else throw new Error(response.statusText);
});
}
```
This helper function is used to build up a URL for a talk with a given
title.

```
function talkURL(title) {
```

```
return "talks/" + encodeURIComponent(title);
}
```
When the request fails, we don’t want our page to just sit there doing
nothing without explanation. The function calledreportError, which
we used as thecatchhandler, shows the user a crude dialog to tell them
something went wrong.

```
function reportError(error) {
alert(String(error));
}
```
**Renderingcomponents**

We’ll use an approach similar to the one we saw inChapter 19, splitting
the application into components. However, since some of the compo-
nents either never need to update or are always fully redrawn when
updated, we’ll define those not as classes but as functions that directly
return a DOM node. For example, here is a component that shows the
field where the user can enter their name:

```
function renderUserField(name, dispatch) {
return elt("label", {}, "Your name: ", elt("input", {
type: "text",
value: name,
onchange(event) {
dispatch({type: "setUser", user: event.target.value});
}
}));
```

```
}
```
Theeltfunction used to construct DOM elements is the one we used
inChapter 19.
A similar function is used to render talks, which include a list of com-
ments and a form for adding a new comment.

```
function renderTalk(talk, dispatch) {
return elt(
"section", {className: "talk"},
elt("h2", null, talk.title, " ", elt("button", {
type: "button",
onclick() {
dispatch({type: "deleteTalk", talk: talk.title});
}
}, "Delete")),
elt("div", null, "by ",
elt("strong", null, talk.presenter)),
elt("p", null, talk.summary),
...talk.comments.map(renderComment),
elt("form", {
onsubmit(event) {
event.preventDefault();
let form = event.target;
dispatch({type: "newComment",
talk: talk.title,
message: form.elements.comment.value});
form.reset();
}
}, elt("input", {type: "text", name: "comment"}), " ",
```

```
elt("button", {type: "submit"}, "Add comment")));
}
```
The"submit"event handler callsform.resetto clear the form’s content
after creating a"newComment"action.
When creating moderately complex pieces of DOM, this style of pro-
gramming starts to look rather messy. To avoid this, people often use
a _templating language_ , which allows you to write your interface as an
HTML file with some special markers to indicate where dynamic el-
ements go. Or they use _JSX_ , a nonstandard JavaScript dialect that
allows you to write something very close to HTML tags in your pro-
gram as if they are JavaScript expressions. Both of these approaches
use additional tools to preprocess the code before it can be run, which
we will avoid in this chapter.
Comments are simple to render.
function renderComment(comment) {
return elt("p", {className: "comment"},
elt("strong", null, comment.author),
": ", comment.message);
}

Finally, the form that the user can use to create a new talk is rendered
like this:

```
function renderTalkForm(dispatch) {
let title = elt("input", {type: "text"});
let summary = elt("input", {type: "text"});
return elt("form", {
onsubmit(event) {
```

```
event.preventDefault();
dispatch({type: "newTalk",
title: title.value,
summary: summary.value});
event.target.reset();
}
}, elt("h3", null, "Submit a Talk"),
elt("label", null, "Title: ", title),
elt("label", null, "Summary: ", summary),
elt("button", {type: "submit"}, "Submit"));
}
```
**Polling**

To start the app, we need the current list of talks. Since the initial load
is closely related to the long polling process—the ETagfrom the load
must be used when polling—we’ll write a function that keeps polling
the server for/talksand calls a callback function when a new set of
talks is available.

```
async function pollTalks(update) {
let tag = undefined;
for (;;) {
let response;
try {
response = await fetchOK("/talks", {
headers: tag && {"If-None-Match": tag,
"Prefer": "wait=90"}
});
```

```
} catch (e) {
console.log("Request failed: " + e);
await new Promise(resolve => setTimeout(resolve, 500));
continue;
}
if (response.status == 304) continue;
tag = response.headers.get("ETag");
update(await response.json());
}
}
```
This is anasyncfunction so that looping and waiting for the request
is easier. It runs an infinite loop that, on each iteration, retrieves the
list of talks—either normally or, if this isn’t the first request, with the
headers included that make it a long polling request.
When a request fails, the function waits a moment and then tries
again. This way, if your network connection goes away for a while and
then comes back, the application can recover and continue updating.
The promise resolved viasetTimeoutis a way to force theasyncfunction
to wait.
When the server gives back a 304 response, that means a long polling
request timed out, so the function should just immediately start the
next request. If the response is a normal 200 response, its body is read
as JSON and passed to the callback, and itsETagheader value is stored
for the next iteration.


**Theapplication**

The following component ties the whole user interface together:

```
class SkillShareApp {
constructor(state, dispatch) {
this.dispatch = dispatch;
this.talkDOM = elt("div", {className: "talks"});
this.dom = elt("div", null,
renderUserField(state.user, dispatch),
this.talkDOM,
renderTalkForm(dispatch));
this.syncState(state);
}
```
```
syncState(state) {
if (state.talks != this.talks) {
this.talkDOM.textContent = "";
for (let talk of state.talks) {
this.talkDOM.appendChild(
renderTalk(talk, this.dispatch));
}
this.talks = state.talks;
}
}
}
```
When the talks change, this component redraws all of them. This is
simple but also wasteful. We’ll get back to that in the exercises.
We can start the application like this:


```
function runApp() {
let user = localStorage.getItem("userName") || "Anon";
let state, app;
function dispatch(action) {
state = handleAction(state, action);
app.syncState(state);
}
```
```
pollTalks(talks => {
if (!app) {
state = {user, talks};
app = new SkillShareApp(state, dispatch);
document.body.appendChild(app.dom);
} else {
dispatch({type: "setTalks", talks});
}
}).catch(reportError);
}
```
```
runApp();
```
If you run the server and open two browser windows for _[http://localhost:8000](http://localhost:8000)_
next to each other, you can see that the actions you perform in one win-
dow are immediately visible in the other.

### Exercises

The following exercises will involve modifying the system defined in
this chapter. To work on them, make sure you’ve downloaded the code


( _https://eloquentjavascript.net/code/skillsharing.zip_ ), installed Node ( _https://nodejs.org_ ),
and installed the project’s dependency withnpm install.

**Diskpersistence**

The skill-sharing server keeps its data purely in memory. This means
that when it crashes or is restarted for any reason, all talks and com-
ments are lost.
Extend the server so that it stores the talk data to disk and au-
tomatically reloads the data when it is restarted. Don’t worry about
eﬀiciency—do the simplest thing that works.

**Commentfieldresets**

The wholesale redrawing of talks works pretty well because you usu-
ally can’t tell the difference between a DOM node and its identical
replacement. But there are exceptions. If you start typing something
in the comment field for a talk in one browser window and then, in
another, add a comment to that talk, the field in the first window will
be redrawn, removing both its content and its focus.
When multiple people are adding comments at the same time, this
would be annoying. Can you come up with a way to solve it?


## ExerciseHints

The hints below might help when you are stuck with one of the exercises
in this book. They don’t give away the entire solution, but rather try
to help you find it yourself.

### Program Structure

**Loopingatriangle**

You can start with a program that prints out the numbers 1 to 7,
which you can derive by making a few modifications to theeven number
printing examplegiven earlier in the chapter, where thefor loop was
introduced.
Now consider the equivalence between numbers and strings of hash
characters. You can go from 1 to 2 by adding 1 (+= 1). You can go
from"#"to"##"by adding a character (+= "#"). Thus, your solution
can closely follow the number-printing program.


**FizzBuzz**

Going over the numbers is clearly a looping job, and selecting what to
print is a matter of conditional execution. Remember the trick of using
the remainder (%) operator for checking whether a number is divisible
by another number (has a remainder of zero).
In the first version, there are three possible outcomes for every num-
ber, so you’ll have to create anif/else if/elsechain.
The second version of the program has a straightforward solution and
a clever one. The simple solution is to add another conditional “branch”
to precisely test the given condition. For the clever solution, build up
a string containing the word or words to output and print either this
word or the number if there is no word, potentially by making good use
of the||operator.

**Chessboard**

You can build the string by starting with an empty one ("") and re-
peatedly adding characters. A newline character is written"\n".
To work with two dimensions, you will need a loop inside of a loop.
Put braces around the bodies of both loops to make it easy to see where
they start and end. Try to properly indent these bodies. The order of
the loops must follow the order in which we build up the string (line by
line, left to right, top to bottom). So the outer loop handles the lines,
and the inner loop handles the characters on a line.
You’ll need two bindings to track your progress. To know whether to
put a space or a hash sign at a given position, you could test whether


the sum of the two counters is even (% 2).
Terminating a line by adding a newline character must happen after
the line has been built up, so do this after the inner loop but inside the
outer loop.

### Functions.

**Minimum**

If you have trouble putting braces and parentheses in the right place to
get a valid function definition, start by copying one of the examples in
this chapter and modifying it.
A function may contain multiplereturnstatements.

**Recursion**

Your function will likely look somewhat similar to the innerfindfunc-
tion in the recursive findSolution example in this chapter, with an
if/else if/elsechain that tests which of the three cases applies. The
final else, corresponding to the third case, makes the recursive call.
Each of the branches should contain a return statement or in some
other way arrange for a specific value to be returned.
When given a negative number, the function will recurse again and
again, passing itself an ever more negative number, thus getting further
and further away from returning a result. It will eventually run out of
stack space and abort.


**Beancounting**

Your function will need a loop that looks at every character in the
string. It can run an index from zero to one below its length (< string
.length). If the character at the current position is the same as the one
the function is looking for, it adds 1 to a counter variable. Once the
loop has finished, the counter can be returned.
Take care to make all the bindings used in the function _local_ to the
function by properly declaring them with theletorconstkeyword.

### Data Structures: Objects and Arrays.

**Thesumofarange**

Building up an array is most easily done by first initializing a binding
to[](a fresh, empty array) and repeatedly calling itspushmethod to
add a value. Don’t forget to return the array at the end of the function.
Since the end boundary is inclusive, you’ll need to use the<=operator
rather than<to check for the end of your loop.
The step parameter can be an optional parameter that defaults (using
the=operator) to 1.
Havingrangeunderstand negative step values is probably best done
by writing two separate loops—one for counting up and one for counting
down—because the comparison that checks whether the loop is finished
needs to be>=rather than<=when counting downward.
It might also be worthwhile to use a different default step, namely,
-1, when the end of the range is smaller than the start. That way,


range(5, 2)returns something meaningful rather than getting stuck in
an infinite loop. It is possible to refer to previous parameters in the
default value of a parameter.

**Reversinganarray**

There are two obvious ways to implementreverseArray. The first is to
simply go over the input array from front to back and use theunshift
method on the new array to insert each element at its start. The second
is to loop over the input array backward and use the push method.
Iterating over an array backward requires a (somewhat awkward)for
specification, like(let i = array.length - 1; i >= 0; i--).
Reversing the array in place is harder. You have to be careful not
to overwrite elements that you will later need. UsingreverseArrayor
otherwise copying the whole array (array.slice()is a good way to copy
an array) works but is cheating.
The trick is to _swap_ the first and last elements, then the second and
second-to-last, and so on. You can do this by looping over half the
length of the array (useMath.floorto round down—you don’t need to
touch the middle element in an array with an odd number of elements)
and swapping the element at positioniwith the one at positionarray
.length - 1 - i. You can use a local binding to briefly hold onto one
of the elements, overwrite that one with its mirror image, and then put
the value from the local binding in the place where the mirror image
used to be.


**Alist**

Building up a list is easier when done back to front. SoarrayToList
could iterate over the array backward (see the previous exercise) and,
for each element, add an object to the list. You can use a local binding
to hold the part of the list that was built so far and use an assignment
likelist = {value: X, rest: list}to add an element.
To run over a list (inlistToArrayandnth), aforloop specification
like this can be used:

```
for (let node = list; node; node = node.rest) {}
```
Can you see how that works? Every iteration of the loop,nodepoints
to the current sublist, and the body can read itsvalueproperty to get
the current element. At the end of an iteration,nodemoves to the next
sublist. When that isnull, we have reached the end of the list, and the
loop is finished.
The recursive version of nthwill, similarly, look at an ever smaller
part of the “tail” of the list and at the same time count down the index
until it reaches zero, at which point it can return thevalueproperty of
the node it is looking at. To get the zeroth element of a list, you simply
take thevalueproperty of its head node. To get element _N_ + 1, you
take the _N_ th element of the list that’s in this list’srestproperty.

**Deepcomparison**

Your test for whether you are dealing with a real object will look some-
thing liketypeof x == "object" && x != null. Be careful to compare


properties only when _both_ arguments are objects. In all other cases you
can just immediately return the result of applying===.
UseObject.keysto go over the properties. You need to test whether
both objects have the same set of property names and whether those
properties have identical values. One way to do that is to ensure that
both objects have the same number of properties (the lengths of the
property lists are the same). And then, when looping over one of the
object’s properties to compare them, always first make sure the other
actually has a property by that name. If they have the same number
of properties and all properties in one also exist in the other, they have
the same set of property names.
Returning the correct value from the function is best done by imme-
diately returningfalsewhen a mismatch is found and returningtrue
at the end of the function.

## Higher-Order Functions.

**Everything**

Like the &&operator, the every method can stop evaluating further
elements as soon as it has found one that doesn’t match. So the loop-
based version can jump out of the loop—withbreakorreturn—as soon
as it runs into an element for which the predicate function returnsfalse

. If the loop runs to its end without finding such an element, we know
that all elements matched and we should returntrue.
    To buildeveryon top ofsome, we can apply _De Morgan’s laws_ , which
state thata && bequals!(!a || !b). This can be generalized to arrays,


where all elements in the array match if there is no element in the array
that does not match.

**Dominantwritingdirection**

Your solution might look a lot like the first half of the textScripts
example. You again have to count characters by a criterion based on
characterScriptand then filter out the part of the result that refers to
uninteresting (script-less) characters.
Finding the direction with the highest character count can be done
withreduce. If it’s not clear how, refer to the example earlier in the
chapter, wherereducewas used to find the script with the most char-
acters.

## The Secret Life of Objects

**Avectortype**

Look back to theRabbitclass example if you’re unsure howclassdec-
larations look.
Adding a getter property to the constructor can be done by putting
the wordgetbefore the method name. To compute the distance from
(0, 0) to (x, y), you can use the Pythagorean theorem, which says that
the square of the distance we are looking for is equal to the square of
the x-coordinate plus the square of the y-coordinate. Thus,

√
x^2 +y^2 is
the number you want.Math.sqrtis the way you compute a square root
in JavaScript andx ** 2can be used to square a number.


**Groups**

The easiest way to do this is to store an array of group members in
an instance property. TheincludesorindexOfmethods can be used to
check whether a given value is in the array.
Your class’s constructor can set the member collection to an empty
array. Whenaddis called, it must check whether the given value is in
the array or add it otherwise, possibly usingpush.
Deleting an element from an array, indelete, is less straightforward,
but you can usefilterto create a new array without the value. Don’t
forget to overwrite the property holding the members with the newly
filtered version of the array.
Thefrommethod can use afor/ofloop to get the values out of the
iterable object and calladdto put them into a newly created group.

**Iterablegroups**

It is probably worthwhile to define a new classGroupIterator. Iterator
instances should have a property that tracks the current position in the
group. Every time nextis called, it checks whether it is done and, if
not, moves past the current value and returns it.
TheGroupclass itself gets a method named bySymbol.iteratorthat,
when called, returns a new instance of the iterator class for that group.


## Project: A Robot

**Measuringarobot**

You’ll have to write a variant of therunRobotfunction that, instead of
logging the events to the console, returns the number of steps the robot
took to complete the task.
Your measurement function can then, in a loop, generate new states
and count the steps each of the robots takes. When it has generated
enough measurements, it can useconsole.logto output the average for
each robot, which is the total number of steps taken divided by the
number of measurements.

**Robotefficiency**

The main limitation ofgoalOrientedRobotis that it considers only one
parcel at a time. It will often walk back and forth across the village
because the parcel it happens to be looking at happens to be at the
other side of the map, even if there are others much closer.
One possible solution would be to compute routes for all packages
and then take the shortest one. Even better results can be obtained,
if there are multiple shortest routes, by preferring the ones that go to
pick up a package instead of delivering a package.

**Persistentgroup**

The most convenient way to represent the set of member values is still
as an array, since arrays are easy to copy.


When a value is added to the group, you can create a new group
with a copy of the original array that has the value added (for example,
usingconcat). When a value is deleted, you filter it from the array.
The class’s constructor can take such an array as its argument and
store it as the instance’s (only) property. This array is never updated.
To add theemptyproperty to the constructor, you can declare it as
a static property.
You need only oneemptyinstance because all empty groups are the
same and instances of the class don’t change. You can create many
different groups from that single empty group without affecting it.

## Bugs and Errors

**Retry**

The call toprimitiveMultiplyshould definitely happen in atryblock.
The corresponding catchblock should rethrow the exception when it
is not an instance ofMultiplicatorUnitFailureand ensure the call is
retried when it is.
To do the retrying, you can either use a loop that stops only when
a call succeeds—as in thelookexampleearlier in this chapter—or use
recursion and hope you don’t get a string of failures so long that it
overflows the stack (which is a pretty safe bet).


**Thelockedbox**

This exercise calls for afinallyblock. Your function should first unlock
the box and then call the argument function from inside atry body.
Thefinallyblock after it should lock the box again.
To make sure we don’t lock the box when it wasn’t already locked,
check its lock at the start of the function and unlock and lock it only
when it started out locked.

## Regular Expressions.

**Quotingstyle**

The most obvious solution is to replace only quotes with a nonletter
character on at least one side—something like/\P{L}'|'\P{L}/u. But
you also have to take the start and end of the line into account.
In addition, you must ensure that the replacement also includes the
characters that were matched by the\P{L} pattern so that those are
not dropped. This can be done by wrapping them in parentheses and
including their groups in the replacement string ($1,$2). Groups that
are not matched will be replaced by nothing.

**Numbersagain**

First, do not forget the backslash in front of the period.
Matching the optional sign in front of the number, as well as in front
of the exponent, can be done with[+\-]?or(\+|-|)(plus, minus, or
nothing).


The more complicated part of the exercise is the problem of matching
both"5."and".5"without also matching".". For this, a good solution
is to use the|operator to separate the two cases—either one or more
digits optionally followed by a dot and zero or more digits _or_ a dot
followed by one or more digits.
Finally, to make the _e_ case insensitive, either add anioption to the
regular expression or use[eE].

## Modules.

**Amodularrobot**

Here’s what I would have done (but again, there is no single _right_ way
to design a given module):
The code used to build the road graph lives in thegraph.jsmodule.
Because I’d rather usedijkstrajsfrom NPM than our own pathfinding
code, we’ll make this build the kind of graph data that dijkstrajs
expects. This module exports a single function,buildGraph. I’d have
buildGraphaccept an array of two-element arrays, rather than strings
containing hyphens, to make the module less dependent on the input
format.
Theroads.jsmodule contains the raw road data (theroads array)
and theroadGraph binding. This module depends on./graph.js and
exports the road graph.
TheVillageStateclass lives in thestate.jsmodule. It depends on
the ./roads.js module because it needs to be able to verify that a
given road exists. It also needsrandomPick. Since that is a three-line


function, we could just put it into thestate.jsmodule as an internal
helper function. ButrandomRobotneeds it too. So we’d have to either
duplicate it or put it into its own module. Since this function happens
to exist on NPM in the random-itempackage, a reasonable solution is
to just make both modules depend on that. We can add therunRobot
function to this module as well, since it’s small and closely related to
state management. The module exports both theVillageState class
and therunRobotfunction.
Finally, the robots, along with the values they depend on, such as
mailRoute, could go into anexample-robots.jsmodule, which depends
on ./roads.js and exports the robot functions. To make it possible
forgoalOrientedRobotto do route-finding, this module also depends on
dijkstrajs.
By offloading some work to NPM modules, the code became a little
smaller. Each individual module does something rather simple and can
be read on its own. Dividing code into modules also often suggests
further improvements to the program’s design. In this case, it seems
a little odd that theVillageStateand the robots depend on a specific
road graph. It might be a better idea to make the graph an argument
to the state’s constructor and make the robots read it from the state
object—this reduces dependencies (which is always good) and makes it
possible to run simulations on different maps (which is even better).
Is it a good idea to use NPM modules for things that we could
have written ourselves? In principle, yes—for nontrivial things like
the pathfinding function you are likely to make mistakes and waste
time writing them yourself. For tiny functions likerandom-item, writ-


ing them yourself is easy enough. But adding them wherever you need
them does tend to clutter your modules.
However, you should also not underestimate the work involved in
_finding_ an appropriate NPM package. And even if you find one, it
might not work well or may be missing some feature you need. On top
of that, depending on NPM packages means you have to make sure they
are installed, you have to distribute them with your program, and you
might have to periodically upgrade them.
So again, this is a trade-off, and you can decide either way depending
on how much a given package actually helps you.

**Roadsmodule**

Since this is an ES module, you have to useimportto access the graph
module. That was described as exporting abuildGraphfunction, which
you can pick out of its interface object with a destructuringconstdec-
laration.
To exportroadGraph, you put the keywordexportbefore its definition.
BecausebuildGraphtakes a data structure that doesn’t precisely match
roads, the splitting of the road strings must happen in your module.

**Circulardependencies**

The trick is thatrequireadds the interface object for a module to its
cache _before_ it starts loading the module. That way, if any require
call made while it is running tries to load it, it is already known, and
the current interface will be returned, rather than starting to load the


module once more (which would eventually overflow the stack).

## Asynchronous Programming

**QuietTimes**

You will need to convert the content of these files to an array. The
easiest way to do that is to use thesplitmethod on the string produced
bytextFile. Note that for the logfiles, that will still give you an array
of strings, which you have to convert to numbers before passing them
tonew Date.
Summarizing all the time points into a table of hours can be done by
creating a table (array) that holds a number for each hour in the day.
You can then loop over all the timestamps (over the logfiles and the
numbers in every logfile) and for each one, if it happened on the correct
day, take the hour it occurred in, and add one to the corresponding
number in the table.
Make sure you use await on the result of asynchronous functions
before doing anything with it, or you’ll end up with aPromisewhere
you expected a string.

**RealPromises**

The most straightforward approach to writing this function is to use a
chain ofthencalls. The first promise is produced by reading the list of
logfiles. The first callback can split this list and maptextFileover it
to get an array of promises to pass toPromise.all. It can return the


object returned byPromise.all, so that whatever that returns becomes
the result of the return value of this firstthen.
We now have a promise that returns an array of logfiles. We can
callthenagain on that, and put the timestamp-counting logic in there.
Something like this:

```
function activityTable(day) {
return textFile("camera_logs.txt").then(files => {
return Promise.all(files.split("\n").map(textFile));
}).then(logs => {
// analyze...
});
}
```
Or you could, for even better work scheduling, put the analysis of each
file inside of thePromise.all, so that that work can be started for the
first file that comes back from disk, even before the other files come
back.

```
function activityTable(day) {
let table = []; // init...
return textFile("camera_logs.txt").then(files => {
return Promise.all(files.split("\n").map(name => {
return textFile(name).then(log => {
// analyze...
});
}));
}).then(() => table);
}
```

This shows that the way you structure your promises can have a real
effect on the way the work is scheduled. A simple loop withawaitin it
will make the process completely linear—it waits for each file to load
before proceeding. Promise.allmakes it possible for multiple tasks to
conceptually be worked on at the same time, allowing them to make
progress while files are still being loaded. This can be faster, but it also
makes the order in which things will happen less predictable. In this
case, we’re only going to be incrementing numbers in a table, which
isn’t hard to do in a safe way. For other kinds of problems, it may be
a lot more diﬀicult.
When a file in the list doesn’t exist, the promise returned bytextFile
will be rejected. BecausePromise.allrejects if any of the promises given
to it fail, the return value of the callback given to the firstthenwill also
be a rejected promise. That makes the promise returned bythenfail,
so the callback given to the secondthenisn’t even called, and a rejected
promise is returned from the function.

**BuildingPromise.all**

The function passed to thePromiseconstructor will have to callthenon
each of the promises in the given array. When one of them succeeds,
two things need to happen. The resulting value needs to be stored in
the correct position of a result array, and we must check whether this
was the last pending promise and finish our own promise if it was.
The latter can be done with a counter that is initialized to the length
of the input array and from which we subtract 1 every time a promise
succeeds. When it reaches 0, we are done. Make sure you take into


account the situation where the input array is empty (and thus no
promise will ever resolve).
Handling failure requires some thought but turns out to be extremely
simple. Just pass therejectfunction of the wrapping promise to each
of the promises in the array as acatchhandler or as a second argument
to then so that a failure in one of them triggers the rejection of the
whole wrapper promise.

## Project: A Programming Language

**Arrays**

The easiest way to do this is to represent Egg arrays with JavaScript
arrays.
The values added to the top scope must be functions. By using a
rest argument (with triple-dot notation), the definition ofarraycan be
_very_ simple.

**Closure**

Again, we are riding along on a JavaScript mechanism to get the equiv-
alent feature in Egg. Special forms are passed the local scope in which
they are evaluated so that they can evaluate their subforms in that
scope. The function returned byfunhas access to thescopeargument
given to its enclosing function and uses that to create the function’s
local scope when it is called.


This means that the prototype of the local scope will be the scope
in which the function was created, which makes it possible to access
bindings in that scope from the function. This is all there is to imple-
menting closure (though to compile it in a way that is actually eﬀicient,
you’d need to do some more work).

**Comments**

Make sure your solution handles multiple comments in a row, with
whitespace potentially between or after them.
A regular expression is probably the easiest way to solve this. Write
something that matches “whitespace or a comment, zero or more times”.
Use theexecormatchmethod and look at the length of the first element
in the returned array (the whole match) to find out how many characters
to slice off.

**Fixingscope**

You will have to loop through one scope at a time, using Object.
getPrototypeOf to go to the next outer scope. For each scope, use
Object.hasOwnto find out whether the binding, indicated by thename
property of the first argument toset, exists in that scope. If it does,
set it to the result of evaluating the second argument tosetand then
return that value.
If the outermost scope is reached (Object.getPrototypeOfreturnsnull
) and we haven’t found the binding yet, it doesn’t exist, and an error
should be thrown.


## The Document Object Model

**Buildatable**

You can usedocument.createElementto create new element nodes,document
.createTextNode to create text nodes, and theappendChildmethod to
put nodes into other nodes.
You’ll want to loop over the key names once to fill in the top row
and then again for each object in the array to construct the data rows.
To get an array of key names from the first object,Object.keyswill be
useful.
To add the table to the correct parent node, you can usedocument.
getElementByIdordocument.querySelectorwith"#mountains"to find the
node.

**Elementsbytagname**

The solution is most easily expressed with a recursive function, similar
to thetalksAboutfunctiondefined earlier in this chapter.
You could callbyTagnameitself recursively, concatenating the resulting
arrays to produce the output. Or you could create an inner function
that calls itself recursively and that has access to an array binding
defined in the outer function, to which it can add the matching elements
it finds. Don’t forget to call the inner function once from the outer
function to start the process.
The recursive function must check the node type. Here we are in-
terested only in node type 1 (Node.ELEMENT_NODE). For such nodes, we


must loop over their children and, for each child, see whether the child
matches the query while also doing a recursive call on it to inspect its
own children.

**Thecat'shat**

Math.cosandMath.sinmeasure angles in radians, where a full circle is
2 π. For a given angle, you can get the opposite angle by adding half
of this, which isMath.PI. This can be useful for putting the hat on the
opposite side of the orbit.

## Handling Events.

**Balloon**

You’ll want to register a handler for the "keydown"event and look at
event.keyto figure out whether the up or down arrow key was pressed.
The current size can be kept in a binding so that you can base the
new size on it. It’ll be helpful to define a function that updates the
size—both the binding and the style of the balloon in the DOM—so
that you can call it from your event handler, and possibly also once
when starting, to set the initial size.
You can change the balloon to an explosion by replacing the text node
with another one (using replaceChild) or by setting the textContent
property of its parent node to a new string.


**Mousetrail**

Creating the elements is best done with a loop. Append them to the
document to make them show up. To be able to access them later to
change their position, you’ll want to store the elements in an array.
Cycling through them can be done by keeping a counter variable and
adding 1 to it every time the "mousemove"event fires. The remainder
operator (% elements.length) can then be used to get a valid array index
to pick the element you want to position during a given event.
Another interesting effect can be achieved by modeling a simple
physics system. Use the"mousemove"event only to update a pair of bind-
ings that track the mouse position. Then userequestAnimationFrameto
simulate the trailing elements being attracted to the position of the
mouse pointer. At every animation step, update their position based
on their position relative to the pointer (and, optionally, a speed that
is stored for each element). Figuring out a good way to do this is up to
you.

**Tabs**

One pitfall you might run into is that you can’t directly use the node’s
childNodesproperty as a collection of tab nodes. For one thing, when
you add the buttons, they will also become child nodes and end up
in this object because it is a live data structure. For another, the
text nodes created for the whitespace between the nodes are also in
childNodes but should not get their own tabs. You can usechildren
instead ofchildNodesto ignore text nodes.


You could start by building up an array of tabs so that you have
easy access to them. To implement the styling of the buttons, you
could store objects that contain both the tab panel and its button.
I recommend writing a separate function for changing tabs. You
can either store the previously selected tab and change only the styles
needed to hide that and show the new one, or you can just update the
style of all tabs every time a new tab is selected.
You might want to call this function immediately to make the inter-
face start with the first tab visible.

## Project: A Platform Game.

**Pausingthegame**

An animation can be interrupted by returning false from the func-
tion given torunAnimation. It can be continued by callingrunAnimation
again.
So we need to communicate the fact that we are pausing the game
to the function given torunAnimation. For that, you can use a binding
that both the event handler and that function have access to.
When finding a way to unregister the handlers registered bytrackKeys
, remember that the _exact_ same function value that was passed to
addEventListenermust be passed toremoveEventListenerto successfully
remove a handler. Thus, thehandlerfunction value created intrackKeys
must be available to the code that unregisters the handlers.
You can add a property to the object returned bytrackKeys, contain-
ing either that function value or a method that handles the unregistering


directly.

**Amonster**

If you want to implement a type of motion that is stateful, such as
bouncing, make sure you store the necessary state in the actor object—
include it as a constructor argument and add it as a property.
Remember thatupdatereturns a _new_ object rather than changing the
old one.
When handling collision, find the player instate.actorsand compare
its position to the monster’s position. To get the _bottom_ of the player,
you have to add its vertical size to its vertical position. The creation of
an updated state will resemble eitherCoin’scollidemethod (removing
the actor) orLava’s (changing the status to"lost"), depending on the
player position.

## Drawing on Canvas

**Shapes**

The trapezoid (1) is easiest to draw using a path. Pick suitable center
coordinates and add each of the four corners around the center.
The diamond (2) can be drawn the straightforward way, with a
path, or the interesting way, with a rotate transformation. To use
rotation, you will have to apply a trick similar to what we did in the
flipHorizontallyfunction. Because you want to rotate around the cen-
ter of your rectangle and not around the point (0, 0), you must first


translateto there, then rotate, and then translate back.
Make sure you reset the transformation after drawing any shape that
creates one.
For the zigzag (3) it becomes impractical to write a new call tolineTo
for each line segment. Instead, you should use a loop. You can have
each iteration draw either two line segments (right and then left again)
or one, in which case you must use the evenness (% 2) of the loop index
to determine whether to go left or right.
You’ll also need a loop for the spiral (4). If you draw a series of points,
with each point moving farther along a circle around the spiral’s center,
you get a circle. If, during the loop, you vary the radius of the circle
on which you are putting the current point and go around more than
once, the result is a spiral.
The star (5) depicted is built out ofquadraticCurveTolines. You could
also draw one with straight lines. Divide a circle into eight pieces for
a star with eight points, or however many pieces you want. Draw lines
between these points, making them curve toward the center of the star.
WithquadraticCurveTo, you can use the center as the control point.

**Thepiechart**

You will need to call fillText and set the context’s textAlign and
textBaselineproperties in such a way that the text ends up where you
want it.
A sensible way to position the labels would be to put the text on the
line going from the center of the pie through the middle of the slice.
You don’t want to put the text directly against the side of the pie but


rather move the text out to the side of the pie by a given number of
pixels.
The angle of this line iscurrentAngle + 0.5 * sliceAngle. The fol-
lowing code finds a position on this line 120 pixels from the center:

```
let middleAngle = currentAngle + 0.5 * sliceAngle;
let textX = Math.cos(middleAngle) * 120 + centerX;
let textY = Math.sin(middleAngle) * 120 + centerY;
```
FortextBaseline, the value"middle"is probably appropriate when using
this approach. What to use fortextAligndepends on which side of the
circle we are on. On the left, it should be"right", and on the right, it
should be"left", so that the text is positioned away from the pie.
If you are not sure how to find out which side of the circle a given
angle is on, look to the explanation ofMath.cosinChapter 14. The
cosine of an angle tells us which x-coordinate it corresponds to, which
in turn tells us exactly which side of the circle we are on.

**Abouncingball**

A box is easy to draw withstrokeRect. Define a binding that holds
its size, or define two bindings if your box’s width and height differ.
To create a round ball, start a path and callarc(x, y, radius, 0, 7),
which creates an arc going from zero to more than a whole circle. Then
fill the path.
To model the ball’s position and speed, you can use the Vec class
fromChapter 16. Give it a starting speed, preferably one that is not
purely vertical or horizontal, and for every frame multiply that speed


by the amount of time that elapsed. When the ball gets too close to a
vertical wall, invert the _x_ component in its speed. Likewise, invert the
_y_ component when it hits a horizontal wall.
After finding the ball’s new position and speed, use clearRect to
delete the scene and redraw it using the new position.

**Precomputedmirroring**

The key to the solution is the fact that we can use a canvas element as
a source image when usingdrawImage. It is possible to create an extra
<canvas>element, without adding it to the document, and draw our
inverted sprites to it, once. When drawing an actual frame, we just
copy the already inverted sprites to the main canvas.
Some care would be required because images do not load instantly.
We do the inverted drawing only once, and if we do it before the image
loads, it won’t draw anything. A"load"handler on the image can be
used to draw the inverted images to the extra canvas. This canvas can
be used as a drawing source immediately (it’ll simply be blank until we
draw the character onto it).

## HTTP and Forms

**Contentnegotiation**

Base your code on thefetchexamplesearlier in the chapter.
Asking for a bogus media type will return a response with code 406,
“Not acceptable”, which is the code a server should return when it can’t


fulfill theAcceptheader.

**AJavaScriptworkbench**

Usedocument.querySelectorordocument.getElementByIdto get access to
the elements defined in your HTML. An event handler for"click"or
"mousedown"events on the button can get thevalueproperty of the text
field and callFunctionon it.
Make sure you wrap both the call toFunctionand the call to its result
in atryblock so you can catch the exceptions it produces. In this case,
we really don’t know what type of exception we are looking for, so catch
everything.
ThetextContentproperty of the output element can be used to fill it
with a string message. Or, if you want to keep the old content around,
create a new text node usingdocument.createTextNodeand append it to
the element. Remember to add a newline character to the end so that
not all output appears on a single line.

**Conway'sGameofLife**

To solve the problem of having the changes conceptually happen at
the same time, try to see the computation of a generation as a pure
function, which takes one grid and produces a new grid that represents
the next turn.
Representing the matrix can be done with a single array of width ×
height elements, storing values row by row, so, for example, the third
element in the fifth row is (using zero-based indexing) stored at position


4 × _width_ + 2. You can count live neighbors with two nested loops,
looping over adjacent coordinates in both dimensions. Take care not
to count cells outside of the field and to ignore the cell in the center,
whose neighbors we are counting.
Ensuring that changes to checkboxes take effect on the next gener-
ation can be done in two ways. An event handler could notice these
changes and update the current grid to reflect them, or you could gen-
erate a fresh grid from the values in the checkboxes before computing
the next turn.
If you choose to go with event handlers, you might want to attach
attributes that identify the position that each checkbox corresponds to
so that it is easy to find out which cell to change.
To draw the grid of checkboxes, you can either use a<table>element
(seeChapter 14) or simply put them all in the same element and put
<br>(line break) elements between the rows.

## Project: A Pixel Art Editor

**Keyboardbindings**

Thekeyproperty of events for letter keys will be the lowercase letter
itself, ifshiftisn’t being held. We’re not interested in key events with
shifthere.
A"keydown"handler can inspect its event object to see whether it
matches any of the shortcuts. You can automatically get the list of first
letters from thetoolsobject so that you don’t have to write them out.


When the key event matches a shortcut, callpreventDefaulton it and
dispatch the appropriate action.

**Efficientdrawing**

This exercise is a good example of how immutable data structures can
make code _faster_. Because we have both the old and the new picture,
we can compare them and redraw only the pixels that changed color,
saving more than 99 percent of the drawing work in most cases.
You can either write a new functionupdatePictureor havedrawPicture
take an extra argument, which may be undefined or the previous pic-
ture. For each pixel, the function checks whether a previous picture was
passed with the same color at this position and skips the pixel when
that is the case.
Because the canvas gets cleared when we change its size, you should
also avoid touching itswidthandheightproperties when the old picture
and the new picture have the same size. If they are different, which will
happen when a new picture has been loaded, you can set the binding
holding the old picture tonullafter changing the canvas size because
you shouldn’t skip any pixels after you’ve changed the canvas size.

**Circles**

You can take some inspiration from therectangletool. As with that
tool, you’ll want to keep drawing on the _starting_ picture, rather than
the current picture, when the pointer moves.
To figure out which pixels to color, you can use the Pythagorean


theorem. First figure out the distance between the current pointer
position and the start position by taking the square root (Math.sqrt)
of the sum of the square (x ** 2) of the difference in x-coordinates and
the square of the difference in y-coordinates. Then loop over a square
of pixels around the start position, whose sides are at least twice the
radius, and color those that are within the circle’s radius, again using
the Pythagorean formula to figure out their distance from the center.
Make sure you don’t try to color pixels that are outside of the pic-
ture’s boundaries.

**Properlines**

The thing about the problem of drawing a pixelated line is that it is
really four similar but slightly different problems. Drawing a horizontal
line from the left to the right is easy—you loop over the x-coordinates
and color a pixel at every step. If the line has a slight slope (less than
45 degrees or ¼πradians), you can interpolate the y-coordinate along
the slope. You still need one pixel per _x_ position, with the _y_ position
of those pixels determined by the slope.
But as soon as your slope goes across 45 degrees, you need to switch
the way you treat the coordinates. You now need one pixel per _y_ posi-
tion, since the line goes up more than it goes left. And then, when you
cross 135 degrees, you have to go back to looping over the x-coordinates,
but from right to left.
You don’t actually have to write four loops. Since drawing a line
from _A_ to _B_ is the same as drawing a line from _B_ to _A_ , you can swap
the start and end positions for lines going from right to left and treat


them as going left to right.
So you need two different loops. The first thing your line draw-
ing function should do is check whether the difference between the x-
coordinates is larger than the difference between the y-coordinates. If
it is, this is a horizontalish line, and if not, a verticalish one.
Make sure you compare the _absolute_ values of the _x_ and _y_ difference,
which you can get withMath.abs.
Once you know along which axis you will be looping, you can check
whether the start point has a higher coordinate along that axis than
the endpoint and swap them if necessary. A succinct way to swap the
values of two bindings in JavaScript uses destructuring assignment like
this:

```
[start, end] = [end, start];
```
Then you can compute the slope of the line, which determines the
amount the coordinate on the other axis changes for each step you take
along your main axis. With that, you can run a loop along the main
axis while also tracking the corresponding position on the other axis,
and you can draw pixels on every iteration. Make sure you round the
nonmain axis coordinates, since they are likely to be fractional and the
drawmethod doesn’t respond well to fractional coordinates.


## Node.js

**Searchtool**

Your first command line argument, the regular expression, can be found
inprocess.argv[2]. The input files come after that. You can use the
RegExpconstructor to go from a string to a regular expression object.
Doing this synchronously, withreadFileSync, is more straightforward,
but if you usenode:fs/promisesto get promise-returning functions and
write anasyncfunction, the code looks similar.
To figure out whether something is a directory, you can again use
stat(orstatSync) and the stats object’sisDirectorymethod.
Exploring a directory is a branching process. You can do it either
by using a recursive function or by keeping an array of work (files that
still need to be explored). To find the files in a directory, you can
call readdiror readdirSync. Note the strange capitalization—Node’s
filesystem function naming is loosely based on standard Unix functions,
such as readdir, that are all lowercase, but then it adds Sync with a
capital letter.
To go from a filename read withreaddirto a full path name, you
have to combine it with the name of the directory, either puttingsep
fromnode:pathbetween them or using thejoinfunction from that same
package.


**Directorycreation**

You can use the function that implements the DELETE method as a
blueprint for the MKCOL method. When no file is found, try to cre-
ate a directory withmkdir. When a directory exists at that path, you
can return a 204 response so that directory creation requests are idem-
potent. If a nondirectory file exists here, return an error code. Code
400 (“bad request”) would be appropriate.

**Apublicspaceontheweb**

You can create a<textarea>element to hold the content of the file that
is being edited. A GET request, usingfetch, can retrieve the current
content of the file. You can use relative URLs like _index.html_ , instead
of _[http://localhost:8000/index.html](http://localhost:8000/index.html)_ , to refer to files on the same server
as the running script.
Then, when the user clicks a button (you can use a<form>element
and "submit"event), make aPUT request to the same URL, with the
content of the<textarea>as the request body, to save the file.
You can then add a<select>element that contains all the files in the
server’s top directory by adding<option>elements containing the lines
returned by aGETrequest to the URL/. When the user selects another
file (a"change"event on the field), the script must fetch and display
that file. When saving a file, use the currently selected filename.


## Project: Skill-Sharing Website.

**Diskpersistence**

The simplest solution I can come up with is to encode the wholetalks
object as JSON and dump it to a file withwriteFile. There is already
a method (updated) that is called every time the server’s data changes.
It can be extended to write the new data to disk.
Pick a filename, for example./talks.json. When the server starts, it
can try to read that file withreadFile, and if that succeeds, the server
can use the file’s contents as its starting data.

**Commentfieldresets**

The best way to do this is probably to make the talk component an
object, with asyncStatemethod, so that they can be updated to show
a modified version of the talk. During normal operation, the only way
a talk can be changed is by adding more comments, so thesyncState
method can be relatively simple.
The diﬀicult part is that when a changed list of talks comes in, we
have to reconcile the existing list of DOM components with the talks on
the new list—deleting components whose talk was deleted and updating
components whose talk changed.
To do this, it might be helpful to keep a data structure that stores
the talk components under the talk titles so that you can easily figure
out whether a component exists for a given talk. You can then loop
over the new array of talks, and for each of them, either synchronize


an existing component or create a new one. To delete components for
deleted talks, you’ll have to also loop over the components and check
whether the corresponding talks still exist.


## Index

! operator, 26 , 46
!= operator, 25
!== operator, 29
* operator, 19 , 28 , 220
** operator, 45
*= operator, 50
+ operator, 19 , 22 , 28 , 220
++ operator, 50
+= operator, 50 , 295
− operator, 19 , 23 , 28
−− operator, 50
−= operator, 50
/ operator, 19
/= operator, 50
< operator, 24
<= operator, 25

```
= operator, 34 , 91 , 520
as expression, 243
for default value, 69
in Egg, 311
== operator, 25 , 28 , 95 , 121
=== operator, 29 , 121 , 173 , 586
> operator, 24
>= operator, 25
?: operator, 26 , 31 , 309
?? operator, 30 , 75 , 490
[] (array), 86 , 110
[] (subscript), 86 , 87
% operator, 19 , 49 , 440 , 582 , 603 ,
606
&& operator, 25 , 30 , 142
| | operator, 26 , 29 , 142 , 582
```

{} (block), 42
{} (object), 90 , 96 , 110
200 (HTTP status code), 463 , 537 ,
542
204 (HTTP status code), 546 , 548
2d (canvas context), 426
304 (HTTP status code), 558 , 568 ,
577
400 (HTTP status code), 615
403 (HTTP status code), 544
404 (HTTP status code), 463 , 544 ,
564 , 567
405 (HTTP status code), 468 , 542
406 (HTTP status code), 608
500 (HTTP status code), 542

a (HTML tag), 327 , 347 , 350 ,
476 , 514
Abelson, Hal, 300
absolute positioning, 356 , 362 , 373 ,
379 , 388
absolute value, 113 , 613
abstract data type, 144 , 150
abstract syntax tree, _see_ syntax
tree
abstraction, 8 , 58 , 123 , 124 , 126 ,
300 , 339 , 470 , 521 , 522

```
in Egg, 300
of the network, 323
with higher-order functions,
123
acceleration, 416
Accept header, 492 , 608
access control, 213 , 559
Access-Control-Allow-Origin header,
469
action, 497 , 500 , 502
activeElement property, 475
actor, 396 , 405 , 414
add method, 173
addEntry function, 96
addEventListener method, 364 ,
417 , 539
addition, 18 , 172
address, 116 , 461
address bar, 325 , 461 , 464
adoption, 214
ages example, 157
alert function, 329
alpha, 516
alphanumeric character, 217
alt attribute, 343
alt key, 371
```

altKey property, 371
ambiguity, 319
American English, 220
ampersand character, 327 , 465
analysis, 191 , 198
ancestor element, 406
Android, 372
angle, 358 , 434 , 436 , 607
angle brackets, 326 , 327
animation, 357 , 378 , 388 , 392 ,
400 , 456 , 607
bouncing ball, 459
platform game, 409 , 410 , 416 ,
418 , 419 , 439 , 440 , 452 ,
604
spinning cat, 356 , 362
appendChild method, 342 , 601
Apple, 332
appliance, 144
application, 1 , 495 , 554
arc, 434 , 436
arc method, 434 , 435 , 607
argument, 38 , 68 , 75 , 109 , 301
argv property, 528
arithmetic, 18 , 28 , 312
array, 88 – 90 , 93 , 119

```
as matrix, 395
as table, 99
counting, 139
creation, 86 , 135 , 499 , 584 ,
590
filtering, 130
flattening, 142
in Egg, 318
indexing, 86 , 101 , 106 , 584 ,
603
iteration, 101 , 124 , 128
length of, 88
methods, 105 , 119 , 128 , 130 –
132 , 136 , 141 , 142
notation, 116
of rest arguments, 109
random element, 183
RegExp match, 222
representation, 116
searching, 101 , 105
Array constructor, 499
Array prototype, 149 , 156
array-like object, 160 , 338 , 339 ,
341 , 377 , 477 , 485 , 535
Array.from function, 530
arrays in egg (exercise), 318 , 599
```

arrow function, 65 , 147 , 295
arrow key, 388
artificial intelligence, 175
artificial life, 391 , 493
assert function, 210
assertion, 210
assignment, 34 , 50 , 243 , 319 , 600
assumption, 208 , 211
asterisk, 19 , 220
async function, 283 – 285 , 295 , 297 ,
298 , 577 , 596
asynchronous programming, 269 –
271 , 273 , 283 , 292 , 294 ,
421 , 597
in Node.js, 527 , 536 , 539 , 545 ,
550
reading files, 486
at sign, 393
attribute, 327 , 338 , 346 , 477 , 501 ,
610
autofocus attribute, 476
automatic semicolon insertion, 33
automation, 189 , 196
automaton, 175
avatar, 391
average function, 134

```
await keyword, 283 , 284 , 286 , 295 ,
298 , 596 , 597
axis, 415 , 428 , 442 , 443 , 613
```
```
Babbage, Charles, 84
background, 391 , 403 , 411
background (CSS), 388 , 392 , 404
backslash character
as path separator, 544
in regular expressions, 215 ,
217 , 236 , 592
in strings, 21 , 327
backtick, 20 , 22
backtracking, 229 , 230 , 234
ball, 459 , 607
balloon, 388
balloon (exercise), 388 , 602
banking example, 204
Banks, Iain, 390
baseControls constant, 519
baseTools constant, 519
bean counting (exercise), 83 , 584
beforeunload event, 382
behavior, 246
benchmark, 349
Berners-Lee, Tim, 321
best practices, 4
```

bezierCurveTo method, 433
big ball of mud, 249 , 250
binary data, 4 , 15 , 535
binary number, 15 , 17 , 99 , 198 ,
229 , 484
binary operator, 18 , 23 , 32
binding, 6 , 45 , 91
as
state, 45 , 48
as state, 95 , 487
assignment, 34 , 63
compilation of, 600
definition, 34 , 59 , 63 , 315 , 319
destructuring, 114
from parameter, 60 , 71
global, 60 , 193 , 251 , 422 , 528 ,
529
in Egg, 311
local, 60
model of, 35 , 91 , 95
naming, 36 , 37 , 52 , 77 , 111 ,
194
scope of, 60
undefined, 207
visibility, 61
bit, 5 , 15 , 17 , 24 , 99

```
bitfield, 376
bitmap graphics, 438 , 459
black, 500
block, 42 , 46 , 59 , 61 , 65 , 91 , 203 ,
205 , 301
block comment, 53 , 234
block element, 347 , 350 , 351
blocking, 269 , 357 , 385 , 536
blue, 500
blur event, 380 , 381
blur method, 475
body (HTML tag), 326 , 328 , 336
body (HTTP), 464 , 466 , 468 , 538 ,
546 , 548
body property, 336 , 337 , 341 , 468
bold, 350
Book of Programming, 15 , 249 ,
526
Boolean, 24 , 41 , 45 , 94 , 216 , 310 ,
312
conversion to, 29 , 40 , 46
Boolean function, 40
border (CSS), 347 , 351
border-radius (CSS), 373
bouncing, 393 , 399 , 410 , 414 , 459
bound, 130
```

boundary, 226 , 242 , 247 , 450 , 592
box, 213 , 334 , 391 , 392 , 459 , 607
box shadow (CSS), 406
br (HTML tag), 506 , 610
braces
block, 7 , 42 , 582
body, 126
class, 151
function body, 59 , 65
in regular expression, 221
object, 90 , 91 , 96 , 114
branching, 227 , 229
branching recursion, 73 , 445
break keyword, 49 , 51
breakpoint, 199
British English, 220
browser, 2 , 8 , 270 , 321 , 325 , 328 ,
330 – 332 , 364 , 392 , 459 , 461 ,
464 , 470 , 478 , 488 , 514 ,
521 , 553
environment, 37 – 39 , 461
security, 469 , 555
storage, 487 , 490
window, 364
browser wars, 332
browsers, 12 , 261

```
bubbling, see event propagation
Buffer class, 534 , 535 , 539 , 540
bug, 122 , 191 , 198 , 235 , 238 , 246 ,
254 , 332
building Promise.all (exercise), 298 ,
598
bundler, 261
button, 363 , 465 , 477 , 494
button (HTML tag), 330 , 365 ,
372 , 389 , 478 , 488 , 493 ,
501
button property, 366 , 376 , 503
buttons property, 376 , 503
```
```
call method, 146 , 156
call stack, 66 , 67 , 70 , 75 , 90 , 202 ,
203 , 207 , 292
callback function, 269 , 271 , 273 ,
276 , 364 , 418 , 419 , 502 ,
534 , 536 , 539 , 568 , 576
camel case, 52 , 352
cancelAnimationFrame function,
384
canvas, 392 , 424 , 428 – 433 , 437 ,
438 , 440 – 442 , 444 , 445 , 447 ,
454 – 456 , 458 , 608
context, 426 , 427
```

path, 429
size, 426 , 429
canvas (HTML tag), 426 , 496 ,
502 , 513 , 515 , 523 , 611
CanvasDisplay class, 447 , 449 , 452
capitalization, 52 , 152 , 222 , 352 ,
361 , 540
capture group, 223 , 225 , 232 , 233 ,
561
career, 390
caret character, 218 , 226 , 242 ,
533
Carla the crow, 279 , 280 , 287 ,
297
carriage return, 241
cascading, 353
Cascading Style Sheets, _see_ CSS
case conversion, 88
case keyword, 51
case sensitivity, 222 , 593
casual computing, 2
cat’s hat (exercise), 362
catch keyword, 202 , 203 , 207 , 208 ,
212 , 292 , 591
catch method, 277
CD, 15

```
celery, 552
cell, 493
Celsius, 162
center, 408
centering, 357
certificate, 471
change event, 475 , 480 , 507 , 610 ,
615
character, 20 , 21 , 137 , 138 , 479
character category, 219
character encoding, 534 , 535
characterCount function, 133
characterScript function, 140 , 143 ,
588
charCodeAt method, 137
checkbox, 473 , 481 , 494 , 610
checked attribute, 473 , 481
chess board (exercise), 582
chessboard (exercise), 56
child node, 337 , 339 , 341
childNodes property, 339 , 344 ,
603
children property, 340
Chinese characters, 137 , 140
choice, 227
Chrome, 332
```

circle, 358 , 434 , 435
circle (SVG tag), 425
circles (exercise), 523 , 611
circular dependency, 267 , 595
class, 145 , 150 , 151 , 172 , 178 ,
394 , 498
class attribute, 342 , 347 , 353 , 402 ,
405 , 406
class declaration, 151 , 153
class hierarchy, 170
className property, 347
cleaning up, 204
clearing, 424 , 440 , 449 , 450 , 608
clearInterval function, 384
clearRect method, 440 , 608
clearTimeout function, 384 , 385
click event, 364 , 365 , 367 , 373 ,
376 , 501 , 609
client, 323 , 470 , 553 , 570
clientHeight property, 347
clientWidth property, 347
clientX property, 373 , 377 , 504 ,
505
clientY property, 373 , 377 , 504 ,
505
clipboard, 331

```
clipping, 450
closePath method, 431
closing tag, 327 , 329
closure, 71 , 318 , 599 , 601 , 604
closure in egg (exercise), 318 , 599
code, 11 , 234 , 391
structure of, 32 , 46 , 58 , 249 ,
262
code golf, 247
code unit, 137
codePointAt method, 138
coin, 391 , 393 , 415 , 454
Coin class, 400 , 415
collaboration, 321
collection, 8 , 86 , 89 , 93 , 119 , 166
collision detection, 410 , 414 – 416 ,
605 , 607
colon character, 26 , 51 , 90 , 351
color, 426 , 428 , 450 , 496 , 516
color (CSS), 351
color code, 500
color component, 500
color field, 496 , 500 , 508
color picker, 496 , 508 , 512
color property, 498
ColorSelect class, 508
```

comma character, 301
command key, 371 , 522
command line, 255 , 526 , 528 , 530 ,
550
comment, 53 , 116 , 234 , 240 , 319 ,
337 , 553 , 557 , 566 , 574
comment field reset (exercise), 580 ,
616
COMMENT_NODE code, 337
comments in egg (exercise), 319 ,
600
CommonJS, 529
CommonJS modules, 257 , 259 ,
267
communication, 322 , 470
community, 527
compareRobots function, 189
comparison, 24 , 29 , 312 , 584
deep, 121 , 586
of NaN, 25
of numbers, 24 , 39
of objects, 95
of strings, 24
of undefined values, 28
compatibility, 9 , 193 , 321 , 332 ,
523 , 533

```
compilation, 261 , 315 , 316 , 599
complexity, 4 , 5 , 122 , 170 , 230 ,
354 , 521
component, 496 – 498 , 506 , 519
composability, 8 , 134 , 262
computed property, 87 , 490
computer, 1 , 3
concat method, 106 , 142 , 590 ,
601
concatenation, 22 , 106 , 601
conditional execution, 26 , 41 , 50 ,
56 , 309
conditional operator, 26 , 31 , 309
conditional request, 558
configuration, 240
connected graph, 188
connection, 323 , 461 , 471 , 554 –
556
consistency, 52 , 321 , 338
console.log, 7 , 14 , 23 , 39 , 66 , 69 ,
81 , 199 , 528
const keyword, 36 , 61 , 95 , 111 ,
114
constant, 36 , 112 , 417
constructor, 52 , 150 – 152 , 170 , 190 ,
193 , 203 , 224 , 236 , 589 ,
```

#### 591

content negotiation (exercise), 492 ,
608
Content-Length header, 464
Content-Type header, 464 , 537 ,
542 , 544 , 551
context, 426 , 427
context menu, 369
continuation, 272
continue keyword, 49
control, 506 , 508 , 513 , 514 , 519
control flow, 40 , 127
asynchronous, 270 , 284
conditional, 41
exceptions, 202 , 204
functions, 66
loop, 44 , 46 , 48
control key, 371 , 522
control point, 432 – 434
convention, 52
Conway’s Game of Life, 493
coordinates, 172 , 358 , 373 , 403 ,
408 , 411 , 428 , 434 , 442 ,
443
copy-paste programming, 78 , 254
copyright, 255

```
correlation, 97 , 98 , 101 , 103 , 104
cosine, 111 , 358
countBy function, 139 , 143
counter variable, 44 , 47 , 359 , 582 ,
584 , 598 , 603
CPU, 269
crash, 207 , 211 , 565 , 580
createElement method, 344 , 501 ,
601
createReadStream function, 539 ,
545
createServer function, 537 , 539 ,
560 , 561
createTextNode method, 343 , 609
createWriteStream function, 539 ,
548
crisp, 455
cross-domain request, 469
crying, 222
cryptography, 471
CSS, 351 , 352 , 354 , 402 , 404 –
407 , 409 , 424 , 429 , 500 ,
570
ctrlKey property, 371 , 522
curl program, 548
curly braces, see braces
```

cursor, 479 , 480
curve, 432 – 434
cwd function, 544
cycle, 336

Dark Blue (game), 391
data, 3 , 15 , 84
data attribute, 346 , 389
data event, 539
data flow, 497 , 498 , 522
data format, 116 , 338
data loss, 580
data structure, 84 , 263 , 265 , 334 ,
494
collection, 86
immutable, 180
list, 119 , 166
map, 157
stack, 89
tree, 301 , 336 , 455
data URL, 513 , 515
dataset, 100 , 128 , 129
date, 217 , 221 , 224
Date class, 224 , 225 , 251 , 257 ,
297 , 596
date-names package, 257
Date.now function, 225 , 297 , 517

```
dblclick event, 373
De Morgan’s laws, 587
debouncing, 385
debugger statement, 199
debugging, 9 , 191 , 192 , 194 , 197 ,
199 , 203 , 208 , 210 , 246
decentralization, 321
decimal number, 15 , 198 , 229
declaration, 351
decodeURIComponent function,
465 , 543 , 561
deep comparison, 95 , 121
deep comparison (exercise), 121 ,
586
default behavior, 350 , 369
default keyword, 51
default value, 30 , 69 , 429 , 490 ,
520
defineProperty function, 588
degree, 434 , 442
DELETE method, 462 , 464 , 468 ,
541 , 546 , 564
delete method, 173
delete operator, 91
dependence, 97
dependency, 250 , 252 , 254 , 257 ,
```

#### 267 , 329 , 532 , 533

deserialization, 117
design, 265
destructuring, 226
destructuring assignment, 613
destructuring binding, 114 , 258 ,
520 , 595
developer tools, 11 , 39 , 199 , 200 ,
207
dialect, 261
dialog, 38
diamond, 458 , 605
digit, 15 , 17 , 198 , 216 , 217 , 220 ,
221 , 223 , 500
Dijkstra’s algorithm, 264
Dijkstra, Edsger, 175 , 264
dijkstrajs package, 264 , 593
dimensions, 172 , 347 , 390 , 393 ,
410 , 426 , 582
direct child node, 354
direction (writing), 143
directory, 530 , 534 , 535 , 541 , 544 –
546 , 550 , 615
directory creation (exercise), 550 ,
615
disabled attribute, 477

```
discretization, 391 , 410 , 419
dispatch, 50 , 497 , 498 , 500 , 506 ,
519 , 560 , 611
display, 402 , 419 , 420 , 447 , 454 ,
456
display (CSS), 351 , 389
distance, 612
division, 19
division by zero, 20
do loop, 46 , 184
doctype, 326 , 328
document, 324 , 325 , 334 , 381 ,
424
document format, 470 , 492
Document Object Model, see DOM
documentation, 526
documentElement property, 336
dollar sign, 36 , 226 , 232 , 242
DOM, 336 , 346
attributes, 346
components, 496 , 497
construction, 338 , 342 , 345 ,
501
events, 364 , 372
fields, 472 , 479
graphics, 392 , 402 , 404 – 406 ,
```

#### 424 , 426 , 455

interface, 338
modification, 342
querying, 341 , 354
tree, 336
dom property, 498
domain, 325 , 469 , 488
domain-specific language, 123 , 197 ,
214 , 317 , 354
DOMDisplay class, 402 , 403 , 447
dominant direction (exercise), 143 ,
588
done property, 517
doneAt property, 517
dot character, _see_ period charac-
ter
double click, 373
double-quote character, 20 , 248 ,
301 , 327
download, 11 , 254 , 513 , 531 , 548 ,
552 , 579
download attribute, 514
draggable bar example, 374
dragging, 374 , 496 , 510 , 523
draw function, 509 , 524
drawImage method, 438 , 439 , 442 ,

#### 447 , 451 , 608

```
drawing, 334 , 347 , 348 , 357 , 425 ,
426 , 428 , 432 , 445 , 451 ,
452 , 454 , 495 , 496 , 610
drawing program example, 373 ,
495
drawPicture function, 503 , 513 ,
523 , 611
drop-down menu, 474 , 483
duplication, 254
```
```
ECMAScript, 9 , 10 , 193
ECMAScript 6, 10
economic factors, 521
editor, 47
eﬀiciency, 72 , 119 , 135 , 315 , 348 ,
392 , 405 , 427 , 503 , 523
eﬀicient drawing (exercise), 523 ,
611
Egg language, 300 , 301 , 306 , 307 ,
309 , 311 , 313 , 314 , 316 ,
318 , 319 , 336
electronic life, 391
elegance, 73 , 303
element, 327 , 337 , 340 , 344
ELEMENT_NODE code, 337 , 601
elements property, 477
```

ellipse, 356 , 359
else keyword, 42
elt function, 345 , 501 , 522 , 574
email, 471
emoji, 22 , 137 , 244 , 388
empty set, 234
encapsulation, 145 , 158 , 170 , 365 ,
402
encodeURIComponent function,
465 , 557 , 572
encoding, 322
encryption, 471
end event, 539
end method, 538 , 539 , 542
enemies example, 240
engineering, 332
ENOENT (status code), 545
enter key, 478
entity, 327
enum (reserved word), 37
environment, 37 , 309
equality, 25
error, 137 , 192 – 194 , 197 , 200 , 201 ,
207 , 209 , 276
error event, 486 , 548
error handling, 191 , 201 , 202 , 207 ,

#### 536 , 542 , 545 , 573 , 577

```
error message, 307 , 493
error recovery, 200
error response, 463 , 542 , 547
error tolerance, 327
Error type, 203 , 207 , 209 , 545
ES modules, 251 , 252 , 330 , 529 ,
531
escape key, 422
escaping
in HTML, 327 , 330
in regexps, 215 , 218 , 236
in strings, 21 , 301
in URLs, 465 , 543 , 557 , 561
Escher, M.C., 424
ETag header, 558 , 567 , 577
eval, 259
evaluate function, 307 , 309 , 311
evaluation, 307 , 316
even number, 43 , 82
event handling, 364 , 366 , 367 , 369 ,
370 , 378 , 380 , 382 , 392 ,
417 , 421 , 422 , 438 , 455 ,
478 , 480 , 501 , 539 , 604 ,
610
event loop, 292
```

event object, 366 , 373 , 377
event propagation, 367 , 368 , 380 ,
382
event type, 366
every method, 142
everything (exercise), 142 , 587
evolution, 214 , 521 , 533
exception handling, 202 – 204 , 207 ,
209 , 212 , 213 , 276 , 279 ,
284 , 292 , 609
exception safety, 206
exec method, 222 – 224 , 237 , 239
execution order, 40 , 64 , 66
exercises, 3 , 11 , 54 , 198
exit method, 528
expectation, 369
experiment, 4 , 11 , 246
exploit, 331
exponent, 18 , 248 , 592 , 593
exponentiation, 45 , 48
export keyword, 531
exports object, 257 , 260 , 595
expression, 32 – 34 , 40 , 45 , 48 , 63 ,
301 , 308
expressivity, 317
extraction, 224

```
factorial function, 13
Fahrenheit, 162
fallthrough, 51
false, 24
farm example, 77 , 80 , 227
fetch function, 467 , 492 , 538 , 572 ,
576 , 615
field, 372 , 465 , 472 , 477 , 482 , 487 ,
494 , 496 , 580
Fielding, Roy, 461
file, 485 , 529 , 546 , 616
access, 259 , 261 , 515 , 534 , 535
image, 495 , 513 , 514
resource, 462 , 464 , 541 , 544
stream, 539
file extension, 544
file field, 473 , 485
file format, 240
file reading, 486
file server, 570
file server example, 541 , 544 , 546 –
548 , 550 , 551 , 615
file size, 261
File type, 486
FileReader class, 486 , 515
files property, 485
```

fileSizes function, 294 , 295
filesystem, 485 , 534 , 535 , 541 , 543 ,
616
fill function, 511
fill method, 430 , 499
filling, 428 , 430 , 437 , 457
fillRect method, 428 , 440
fillStyle property, 428 , 437 , 500
fillText method, 437 , 438 , 606
filter method, 130 , 134 , 140 , 179 ,
588 – 590
finally keyword, 205 , 213 , 592
find method, 140
findInStorage function, 283
findRoute function, 187
finish event, 548
Firefox, 332
firstChild property, 339
fixed positioning, 379
fixing scope (exercise), 319 , 600
FizzBuzz (exercise), 56 , 582
flattening (exercise), 142
flexibility, 10
flipHorizontally function, 452 , 605
flipHorizontally method, 443
flipping, _see_ mirroring

```
floating-point number, 17 , 18
flood fill, 506 , 511
flow diagram, 228 , 229
focus, 372 , 380 , 475 – 477 , 481 , 482 ,
522 , 580
focus event, 380 , 381
focus method, 475
fold, see reduce method
font, 438
font-family (CSS), 352
font-size (CSS), 388
font-weight (CSS), 353
for attribute, 482
for loop, 47 , 49 , 101 , 124 , 142 ,
208 , 584 , 586
for/of loop, 102 , 138 , 163 , 165 ,
168 , 589
forEach method, 128 , 160
form, 464 – 466 , 477 , 478 , 551
form (HTML tag), 472 , 473 , 477 ,
575 , 615
form property, 477
formatDate module, 257
fractal example, 445
fractional number, 18 , 248 , 391
frame, 440 , 452 , 607
```

framework, 80 , 497
frequency table, 97
function, 8 , 38 , 58 , 65 , 192 , 300 ,
301 , 314
application, 38 , 40 , 60 , 66 ,
68 , 72 , 110 , 130 , 207 , 301 ,
308
as property, 88
as value, 59 , 63 , 70 , 125 , 126 ,
130 , 366 , 418 , 604
body, 59 , 65
callback, _see_ callback function
declaration, 64
definition, 59 , 64 , 76
higher-order, 64 , 125 , 126 , 130 –
132 , 134 , 233 , 418
model of, 71
naming, 77 , 78
purity, 80
scope, 63 , 256 , 318
Function constructor, 259 , 312 ,
316 , 493 , 609
function keyword, 59 , 64
Function prototype, 149 , 156
future, 10 , 37 , 64 , 460

game, 390 – 393 , 417 , 421 , 447

```
screenshot, 409 , 454
with canvas, 454
game of life (exercise), 493 , 609
GAME_LEVELS dataset, 421
garbage collection, 16
garble example, 530
gardening, 552
gaudy home pages, 388
generation, 493 , 494 , 609
generator, 285
GET method, 462 , 464 , 465 , 468 ,
478 , 541 , 544 , 556 , 564
get method, 158
getAttribute method, 346 , 347
getBoundingClientRect method,
348 , 504
getContext method, 427
getDate method, 225
getElementById method, 341 , 601
getElementsByClassName method,
342
getElementsByTagName method,
341 , 344 , 361 , 601
getFullYear method, 225
getHours method, 225
getImageData method, 515 , 516
```

getItem method, 488 , 490
getMinutes method, 225
getMonth method, 225
getPrototypeOf function, 149 , 152 ,
319 , 600
getSeconds method, 225
getter, 161 , 173 , 399
getTime method, 225
getYear method, 225
GitHub, 462
global object, 193
global scope, 60 , 251 , 257 , 312 ,
383 , 384 , 528 , 529 , 600
goalOrientedRobot function, 188
Google, 332
grammar, 32 , 192 , 241
graph, 176 , 186 , 264 , 456
graphics, 392 , 402 , 405 , 424 , 426 ,
427 , 438 , 455 , 456
grave accent, _see_ backtick
gravity, 416
greater than, 24
greed, 234 , 235
green, 500
grep, 550
grid, 391 , 392 , 403 , 411 , 493 , 609

```
Group class, 173 , 174 , 190 , 286 ,
589
groupBy function, 143
grouping, 19 , 42 , 221 , 223 , 232 ,
233 , 592
groups (exercise), 173 , 174 , 589
```
```
h1 (HTML tag), 326 , 347
handleAction function, 571
hard disk, 262 , 268
hard drive, 16 , 485 , 488 , 527 , 580
hard-coding, 341
hardcoding, 458
has method, 158 , 173
hash character, 319
hash sign, 500
hasOwn function, 159 , 319 , 564 ,
600
head (HTML tag), 326 , 328 , 336
head property, 336
header, 463 , 464 , 469 , 470 , 538 ,
556
headers property, 467 , 468 , 492
height property, 523 , 611
help text example, 380
hexadecimal number, 229 , 465 ,
500 , 517
```

hidden element, 351 , 389
higher-order function, _see_ func-
tion, higher-order
history, 8 , 521
historyUpdateState function, 517
hooligan, 559
href attribute, 327 , 341 , 346
HTML, 325 , 334 , 462 , 487 , 551
notation, 326
structure, 334 , 337
html (HTML tag), 328 , 336
HTTP, 321 , 322 , 324 , 325 , 461 –
464 , 466 , 469 – 471 , 537 , 546 ,
547 , 551 , 555 , 556
client, 538 , 548 , 553
server, 537 , 541 , 569
HTTPS, 324 , 471 , 472
human language, 32
HyperText Markup Language, _see_
HTML
HyperText Transfer Protocol, _see_
HTTP
hyphen character, 19 , 217 , 352

id attribute, 341 , 353 , 482
idempotence, 547
idempotency, 615

```
identifier, 302
identity, 94
if keyword, 41 , 243
chaining, 42 , 50 , 582 , 583
If-None-Match header, 558 , 568 ,
576
image, 343 , 382 , 424 , 464
imagination, 390
IME, 372
img (HTML tag), 327 , 343 , 350 ,
382 , 424 , 438 , 440 , 515
immediately invoked function ex-
pression, 256
immutable, 94 , 180 , 399 , 499 , 500 ,
511 , 517 , 611
implements (reserved word), 37
import keyword, 252 , 529 , 530 ,
560
in operator, 92 , 159
includes method, 101 , 102 , 589
indentation, 46
index, 86
index property, 222
index.html, 570
indexOf method, 105 , 107 , 173 ,
216 , 237 , 589
```

infinite loop, 49 , 67 , 208 , 585
infinity, 20
infrastructure, 254
inheritance, 149 , 168 – 171 , 209 ,
545
INI file, 240
ini package, 255 , 256 , 262 , 531
initialization, 381
inline element, 347 , 350
inner function, 62 , 601
inner loop, 231
innerHeight property, 379
innerWidth property, 379
input, 200 , 363 , 392 , 475 , 527 ,
565
input (HTML tag), 380 , 472 , 479 ,
481 , 482 , 485 , 508 , 515
input event, 480
insertBefore method, 342 , 343
installation, 254
instance, 150 , 153
instanceof operator, 170 , 209
instruction, 5
integer, 18
integration, 214 , 338
interface, 153

```
canvas, 424 , 426
design, 79 , 214 , 224 , 237 , 338 ,
429
HTTP, 470 , 556
module, 250 , 256 , 257 , 260 ,
262 , 467 , 531
object, 145 , 158 , 160 , 161 , 174 ,
190 , 396 , 447 , 479 , 498
interface (reserved word), 37
internationalization, 218
internet, 240 , 322 – 324 , 330
Internet Explorer, 331 , 332
interpolation, 22
interpretation, 11 , 307 , 309 , 315
interview question, 56
inversion, 218
IP address, 325 , 461
isDirectory method, 546 , 614
isEven (exercise), 82 , 583
isolation, 145 , 249 , 257 , 330
iterable interface, 165 , 589
iterator, 285
iterator interface, 163 , 165 , 174
```
```
Jacques, 85
Java, 9
JavaScript, 8
```

availability of, 2
flexibility of, 10
history of, 8 , 321
in HTML, 329
syntax, 32
uses of, 10
versions of, 10
weaknesses of, 9
JavaScript console, 11 , 23 , 39 ,
199 , 207 , 493 , 528
JavaScript Object Notation, _see_
JSON
job, 435
join method, 141 , 156 , 530
journal, 85 , 90 , 93 , 96 , 102
JOURNAL dataset, 100
journalEvents function, 102
JSON, 116 , 262 , 468 , 490 , 556 ,
557 , 565 , 577 , 616
json method, 468
JSON.parse function, 117 , 616
JSON.stringify function, 117
JSX, 575
jump, 6
jump-and-run game, 390
jumping, 391 , 416 , 417

```
Kernighan, Brian, 191
key code, 417
key property, 371 , 602 , 610
keyboard, 37 , 363 , 369 , 370 , 391 ,
392 , 416 , 417 , 422 , 475 ,
476 , 480 , 522
keyboard bindings (exercise), 522 ,
610
keyboard focus, see focus
keydown event, 370 , 385 , 418 , 522 ,
602 , 610
keyup event, 370 , 418
keyword, 34 , 37 , 347
Khasekhemwy, 480
kill process, 538
Knuth, Donald, 58
```
```
label, 438 , 459
label (HTML tag), 482 , 508
labeling, 482
landscape example, 62
Laozi, 268
Last-Modified header, 464
lastChild property, 339
lastIndex property, 237 – 239
lastIndexOf method, 105
latency, 261
```

lava, 391 , 393 , 394 , 406 , 410 , 414 ,
454
Lava class, 399 , 414
layering, 323
layout, 347 , 349 , 351
laziness, 348
Le Guin, Ursula K., 3
leaf node, 336 , 337
leak, 331 , 422
learning, 2 , 10 , 11
left (CSS), 356 , 357 , 359 , 362
LEGO, 250
length property
for array, 88 , 499
for string, 78 , 83 , 87 , 109 ,
584
LengthList class, 168
less than, 24
let keyword, 34 , 35 , 61 , 95 , 111 ,
114 , 193
level, 391 , 393 , 394 , 402 , 403 ,
406 , 420 , 421
Level class, 394
lexical scoping, 62 , 63
library, 338 , 497 , 531 , 532
license, 255

```
line, 33 , 46 , 241 , 424 , 428 – 433 ,
435 , 436 , 458 , 606
line break, 20 , 241
line comment, 53 , 234
line drawing, 524 , 612
line width, 429 , 442
lines of code, 313
lineTo method, 430
lineWidth property, 429
link, 327 , 339 , 341 , 369 , 372 , 514
link (HTML tag), 409
linked list, 119 , 166 , 168 , 586
Liskov, Barbara, 144
list (exercise), 119 , 586
listen method, 537 , 538
listening (TCP), 323 , 537
ListIterator class, 167
literal expression, 32 , 215 , 305 ,
308
live data structure, 334 , 344 , 355 ,
603
live view, 554 , 555 , 578 , 616
lives (exercise), 421
load event, 381 , 438 , 451 , 486 ,
608
LoadButton class, 514
```

local binding, 70 , 319 , 584
local scope, 60 , 315
localhost, 537
localStorage object, 488 , 572
locked box (exercise), 212 , 592
logging, 199
logical and, 25
logical operators, 25
logical or, 26
long polling, 554 – 556 , 558 , 565 ,
567 , 568 , 576
look-ahead, 226
loop, 6 , 7 , 44 , 47 , 55 , 56 , 72 , 101 ,
124 , 125 , 134 , 135 , 239 ,
582 , 584 , 606
termination of, 49
loop body, 46 , 126
lycanthropy, 85 , 96

machine code, 4 , 316
magic, 300
mailRoute array, 185
maintenance, 255
malicious script, 330
man-in-the-middle, 471
map, 401 , 478
map (data structure), 157

```
Map class, 158 , 161
map method, 131 , 134 , 141 , 157 ,
179 , 395 , 507
Marcus Aurelius, 363
match method, 223 , 239
matching, 216 , 226 , 237 , 247
algorithm, 228 – 230
Math object, 82 , 87 , 111
Math.abs function, 113 , 613
Math.acos function, 111
Math.asin function, 111
Math.atan function, 111
Math.ceil function, 113 , 411 , 450
Math.cos function, 111 , 358 , 359 ,
607
Math.floor function, 113 , 183 , 411 ,
450
Math.max function, 39 , 87 , 109 ,
111 , 450
Math.min function, 40 , 82 , 111 ,
450
Math.PI constant, 111 , 434
Math.random function, 112 , 183 ,
401 , 494
Math.round function, 113
Math.sin function, 111 , 358 , 359 ,
```

#### 401 , 415

Math.sqrt function, 100 , 111 , 588
Math.tan function, 111
mathematics, 72 , 126
max example, 109
max-height (CSS), 406
max-width (CSS), 406
maximum, 39 , 111 , 133 , 134
Meadowfield, 175
measuring a robot (exercise), 189 ,
590
media type, 470 , 492 , 544
meetup, 552
memory, 5 , 15
call
stack, 67
organization, 16 , 34 , 86 , 94 ,
116
persistence, 580
speed, 268 , 315
structure
sharing, 120
mesh, 324
message event, 383
meta key, 371
metaKey property, 371 , 522

```
method, 88 , 146 , 153 , 193 , 538
array, 105
HTTP, 462 , 470 , 538 , 548 ,
556 , 560
private, 153
method attribute, 465
method call, 146
method property, 468
methods object, 541
Microsoft, 331 , 332
MIME type, 492 , 544
mime-types package, 544
mini application, 487
minifier, 261
minimalism, 391
minimum, 40 , 82 , 111
minimum (exercise), 82 , 583
minus, 19 , 248
mirror, 443 , 459 , 608
mirroring, 441 , 443
Miró, Joan, 495
mixer example, 144
MKCOL method, 550 , 615
mkdir function, 550 , 615
modification date, 546
modifier key, 371
```

modular robot (exercise), 266 , 593
modularity, 145 , 497
module, 250 , 256 , 266 , 402 , 530 ,
531 , 560
design, 262
resolution, 252
module loader, 529
module object, 260
module system, 256
modulo operator, 19
Mongolian vowel separator, 219
monster (exercise), 422 , 605
Mosaic, 331
motion, 392
mouse, 37
mouse button, 366 , 368 , 373
mouse cursor, 373
mouse trail (exercise), 388 , 603
mousedown event, 367 , 373 , 376 ,
502 , 503 , 609
mousemove event, 374 , 376 , 385 ,
386 , 389 , 503 , 524 , 603
mouseup event, 373 , 376
moveTo method, 430 , 435
Mozilla, 332
multiple attribute, 483 – 485

```
multiple choice, 474
multiple-choice, 473 , 482 , 483
multiplication, 18 , 398 , 414
multiplier function, 71
music, 390
mutability, 91 , 94 , 180
```
```
name attribute, 477 , 483
namespace, 111
naming, 6 , 9 , 36
NaN, 20 , 25 , 27 , 192
negation, 23 , 26
neighbor, 493 , 610
nerd, 236
nesting
in regexps, 231
of arrays, 99
of expressions, 32 , 303
of functions, 62
of loops, 56 , 582
of objects, 336 , 340
of scope, 62
Netscape, 8 , 331 , 332
network, 269 , 322 , 555
abstraction, 470
protocol, 322
security, 471
```

speed, 261 , 268 , 527
new operator, 151
newline character, 20 , 56 , 217 ,
234 , 241 , 395 , 609
next method, 165 , 286 , 589
nextSibling property, 339
node, 336
node program, 527 , 528
Node.js, 11 , 12 , 39 , 257 , 270 , 526 ,
527 , 529 – 531 , 534 , 536 –
539 , 541 , 544 , 546 – 549 , 553 ,
554 , 556 , 559 , 579
node:fs package, 534 – 536
node:fs/promises package, 536
node:http package, 537 , 538
node:path package, 544
node:stream/consumers package,
565
node_modules directory, 530 , 531
NodeList type, 338 , 354
nodeName property, 361
nodeType property, 337 , 601 , 603
nodeValue property, 341
nonbreaking space, 219
not a number, 20
note-taking example, 488

```
notification, 555
NPM, 254 – 257 , 264 , 266 , 530 –
532 , 534 , 544 , 560 , 561 ,
579 , 594
npm program, 531 , 533 , 544
null, 27 , 28 , 30 , 75 , 87 , 114 , 121 ,
200
number, 17 , 94 , 216 , 248 , 592
conversion to, 28 , 40
notation, 17 , 18
precision of, 18
representation, 17
special values, 20
Number function, 40 , 41 , 52 , 220
number puzzle example, 73
Number.isNaN function, 41
```
```
object, 84 , 90 , 92 , 170
as
module, 256
as map, 401
creation, 116 , 151 , 490
identity, 94
mutability, 94
property, 39 , 87 , 111 , 114 ,
148
representation, 116
```

Object prototype, 148 , 149
object-oriented programming, 144 ,
150 , 159 , 160 , 168 , 178 ,
263
Object.create function, 149 , 158 ,
313
Object.keys function, 92 , 121 , 587 ,
601
Object.prototype, 157
obstacle, 410
offsetHeight property, 347 , 348
offsetWidth property, 347
on method, 539
onclick attribute, 330 , 365
onclick property, 501
OpenGL, 426
opening tag, 327
operator, 18 , 23 , 24 , 29 , 301 , 312
application, 19
optimization, 73 , 81 , 349 , 385 ,
392 , 405 , 456 , 459 , 536
option (HTML tag), 474 , 475 ,
483 , 615
optional, 220
optional argument, 69 , 118
optional chaining, 115

```
options property, 483
ordering, 323
ordinal package, 257 , 260
organic growth, 249
organization, 249
outline, 428
output, 23 , 38 , 39 , 199 , 200 , 312 ,
527 , 609
overflow, 17
overflow (CSS), 406
overlap, 411
overlay, 353
overriding, 155 , 159 , 169 , 595
overwriting, 548 , 551 , 565
```
```
p (HTML tag), 326 , 347
package, 254 , 257 , 533
package (reserved word), 37
package manager, 254
package.json, 532 , 533
padding (CSS), 404
page reload, 382 , 478 , 488
pageX property, 373 , 377
pageXOffset property, 348
pageY property, 373 , 377
pageYOffset property, 348 , 379
Palef, Thomas, 391
```

panning, 504
paragraph, 327
parallelism, 269 , 464
parameter, 38 , 59 , 60 , 65 , 68 , 69 ,
109 , 114 , 146 , 194 , 260
parent node, 367
parentheses, 19
arguments, 38 , 59 , 65 , 126 ,
301
expression, 32
in regular expressions, 221 ,
225 , 228 , 243 , 592
statement, 41 , 45 , 48
parentNode property, 339
parse function, 306
parseApply function, 305
parseExpression function, 303
parseINI function, 242 , 254
parser generator, 317
parsing, 117 , 191 , 242 , 300 , 301 ,
303 , 306 , 309 , 313 , 327 ,
334 , 543 , 567
password, 471
password field, 473
path
canvas, 435

```
canvas, 429 , 430 , 432 , 605
closing, 430 , 431
filesystem, 529 , 541
URL, 462 , 467 , 541 , 543 , 556 ,
560
pathfinding, 186 , 264 , 511
patience, 524
pattern, 214 – 216 , 218 , 236
pausing (exercise), 422 , 604
pea soup, 123
peanuts, 104
percent sign, 465
percentage, 141 , 379
performance, 230 , 261 , 270 , 298 ,
315 , 348 , 392 , 456 , 536
period character, 39 , 87 , 109 , 115 ,
217 , 234 , 248 , 500
persistence, 487 , 553 , 580 , 616
persistent data structure, 178 , 180 ,
190 , 197 , 499 , 510 , 517 ,
605
persistent group (exercise), 190
persistent map (exercise), 590
PGroup class, 190 , 590
phase, 400 , 415
phi coeﬀicient, 97 – 99
```

phi function, 99 , 113
phone, 372
physics, 409 , 416 , 603
physics engine, 410
pi, 18 , 111 , 358 , 401 , 434
PI constant, 111 , 358
pick function, 512
picture, 424 , 425 , 440 , 456 , 496 ,
517
Picture class, 498 , 515
picture property, 498
PictureCanvas class, 502 , 523
pictureFromImage function, 515
pie chart example, 435 , 436 , 438 ,
459 , 606
pink, 500
pipe, 323
pipe character, 227 , 592
pipe method, 542 , 548
pipeline, 261
pixel, 347 , 359 , 373 , 392 , 403 ,
425 – 427 , 438 , 440 , 449 , 456 ,
459 , 495 , 498 , 504 , 509 ,
511 , 516 , 524 , 611
pixel art, 439
PixelEditor class, 506 , 519 , 522

```
pizza, 97 , 99
platform game, 390 , 421
Plauger, P.J., 191
player, 390 , 391 , 393 , 406 , 410 ,
415 , 420 , 439 , 452 , 454
Player class, 398 , 415
plus character, 19 , 220 , 248
Poignant Guide, 32
pointer, 339
pointer event, 367 , 502
pointerPosition function, 503
polling, 363 , 364
pollTalks function, 576
polymorphism, 159
pop method, 89 , 105
Popper, Karl, 345
port, 323 , 461 , 537 , 538
pose, 439
position, 348
position (CSS), 356 , 362 , 379 , 392 ,
405 , 406
POST method, 464 , 466 , 478 , 557
postMessage method, 383
power example, 72
precedence, 19 , 26 , 353 , 354
predicate function, 130 , 136 , 141 ,
```

#### 142

Prefer header, 558 , 568 , 576
premature optimization, 73
preventDefault method, 369 , 378 ,
380 , 382 , 417 , 478 , 504 ,
610
previousSibling property, 339
primitiveMultiply (exercise), 212 ,
591
privacy, 331
private (reserved word), 37
private property, 213
process object, 528 , 544
processor, 268
profiling, 73
program, 33 , 40
nature of, 3
program size, 122 , 247
programming, 1
diﬀiculty of, 2
history of, 5
joy of, 1 , 4
programming language, 1 , 4 , 300 ,
338 , 527
power of, 8
programming style, 4 , 33 , 46 , 52

```
progress bar, 378
project chapter, 175 , 300 , 390 ,
495 , 552
promise, 298 , 598
Promise class, 273 , 277 , 283 , 292 ,
293 , 298 , 467 , 468 , 486 ,
536 , 541 , 577 , 596 , 598
Promise.all function, 290 , 295 , 298 ,
596 , 598
Promise.reject function, 277
Promise.resolve function, 273
promptDirection function, 208 , 209
promptNumber function, 200
propagation, see event propaga-
tion
proper lines (exercise), 524 , 612
property, 490
access, 39 , 87 , 146 , 191 , 520
assignment, 91
definition, 90 , 96 , 161
deletion, 91
inheritance, 148 , 150 , 155
model of, 91
naming, 158 , 163 , 164
private, 153
public, 153
```

testing for, 92
protected (reserved word), 37
protocol, 322 – 324 , 461 , 463
prototype, 148 – 151 , 155 , 158 , 169 ,
313 , 319 , 600
diagram, 155
prototype property, 151 , 152
pseudorandom number, 112
public, 154
public (reserved word), 37
public space (exercise), 551 , 615
publishing, 534
punch card, 5
pure function, 79 , 80 , 119 , 130 ,
263 , 494 , 609
push method, 89 , 102 , 105 , 589
pushing data, 554
PUT method, 462 , 464 , 541 , 547 ,
557 , 565 , 615
Pythagoras, 588
Pythagorean theorem, 611

quadratic curve, 433
quadraticCurveTo method, 432 ,
606
query string, 465 , 466 , 558 , 567
querySelector method, 355 , 601

```
querySelectorAll method, 354 , 483
question mark, 26 , 220 , 235 , 465
queue, 293
quiet times (exercise), 297 , 596
quotation mark, 20 , 248
quoting
in JSON, 116
of object properties, 90
quoting style (exercise), 248 , 592
```
```
rabbit example, 146 , 149 , 151
radian, 358 , 434 , 442
radio button, 473 , 482
radius, 523 , 612
raising (exception), 202
random number, 112 , 401
random-item package, 593
randomPick function, 183
randomRobot function, 183
range, 129 , 217 , 221
range function, 8 , 118 , 584
Range header, 468
ray tracer, 456
read-eval-print loop, 528
readability, 6 , 8 , 53 , 72 , 79 , 201 ,
249 , 309 , 408 , 458
readable stream, 539 , 542 , 565
```

readAsDataURL method, 515
readAsText method, 486
readdir function, 535 , 546 , 614
readdirSync function, 614
readFile function, 259 , 534 , 616
readFileSync function, 536 , 614
reading code, 11 , 175
readTextFile function, 271
real promises (exercise), 298 , 596
real-time, 363
reasoning, 25
recipe analogy, 123
record, 90
rect (SVG tag), 425
rectangle, 392 , 410 , 427 , 428 , 458 ,
510
rectangle function, 510 , 611
recursion, 67 , 72 , 73 , 82 , 120 ,
283 , 303 , 306 , 309 , 340 ,
361 , 445 , 583 , 586 , 591 ,
601
red, 500
reduce method, 132 , 134 , 141 ,
142 , 507 , 588
ReferenceError type, 319
RegExp class, 215 , 236 , 614

```
regexp golf (exercise), 247
regular expression, 214 , 216 , 218 ,
232 , 234 , 235 , 237 , 240 ,
247 , 305 , 550 , 560 , 561 ,
600 , 614
alternatives, 227
backtracking, 229
boundary, 226
creation, 215 , 236
escaping, 215 , 236 , 592
flags, 222 , 232 , 236 , 593
global, 232 , 237 , 239 , 240
grouping, 221 , 222 , 232
internationalization, 218
matching, 228 , 237
methods, 216 , 224 , 237
repetition, 220
rejecting (a promise), 276 , 293 ,
298 , 598
relative path, 329 , 529 , 541 , 615
relative positioning, 356 , 357
relative URL, 467
remainder operator, 19 , 49 , 440 ,
582 , 603 , 606
remote access, 541
remote procedure call, 470
```

removeChild method, 342
removeEventListener method, 365 ,
604
removeItem method, 488
rename function, 535
rendering, 427
renderTalk function, 574
renderTalkForm function, 575
renderUserField function, 573
repeat method, 109 , 379
repeating key, 371
repetition, 76 , 220 , 221 , 230 , 235 ,
384
replace method, 232 , 248 , 592
replaceChild method, 343 , 602
replaceSelection function, 480
reportError function, 573
request, 323 , 462 – 464 , 478 , 537 ,
548 , 553
request function, 538 , 539
requestAnimationFrame function,
357 , 382 , 384 , 418 , 459 ,
603
require function, 257 , 259 , 267 ,
529 , 531
reserved word, 37

```
resolution, 252 , 529
resolve function, 544
resolving (a promise), 273 , 276 ,
293
resource, 322 , 324 , 462 , 464 , 470 ,
541 , 564
response, 462 – 464 , 470 , 538 , 543 ,
546
Response class, 467
responsiveness, 363 , 527
rest parameter, 110
restore method, 445 , 447
result property, 486
return keyword, 60 , 67 , 284 , 583 ,
587
return value, 39 , 60 , 200 , 587
reuse, 80 , 170 , 249 , 254 , 530
reverse method, 119
reversing (exercise), 119 , 585
rgb (CSS), 404
right-aligning, 361
rmdir function, 546 , 550
roadGraph object, 176
roads array, 175
roads module (exercise), 267 , 595
robot, 175 , 177 , 182 , 185 , 186 ,
```

#### 189 , 266

robot eﬀiciency (exercise), 189 ,
590
robustness, 556
root, 336
rotate method, 442 , 447
rotation, 458 , 605
rounding, 113 , 199 , 411 , 450 , 613
roundTo example, 59 , 69
router, 555 , 560
Router class, 560 , 561
routeRobot function, 185
row, 361
rule (CSS), 352 – 354
run function, 313
run-time error, 196 , 197 , 200 , 211 ,
600
runAnimation function, 418 , 422
runGame function, 420 , 421
runLevel function, 419 , 422
running code, 11
runRobot function, 182 , 590

Safari, 332
sandbox, 11 , 84 , 330 , 334 , 469
save method, 445 , 447
SaveButton class, 513

```
scale constant, 502
scale method, 441 , 444
scaling, 403 , 439 , 441 , 451 , 608
scheduling, 292 , 597
scientific notation, 18 , 248
scope, 60 – 63 , 70 , 260 , 308 , 311 ,
312 , 318 , 319 , 599 , 600
script (HTML tag), 329 , 381 , 382
SCRIPTS dataset, 129 , 132 , 136 ,
139 , 143
scroll event, 378 , 385
scrolling, 369 , 378 , 379 , 406 , 407 ,
417 , 449
search method, 237
search problem, 186 , 228 , 230 ,
341 , 550
search tool (exercise), 550 , 614
section, 241
Secure HTTP, see HTTPS
security, 259 , 330 , 331 , 469 , 471 ,
485 , 488 , 543 , 559
security camera, 297
select (HTML tag), 474 , 475 , 483 ,
488 , 496 , 506 , 507 , 615
selected attribute, 483
selection, 479
```

selectionEnd property, 479
selectionStart property, 479
selector, 354
self-closing tag, 327
semantic versioning, 533
semicolon, 33 , 48 , 351
sep binding, 544
sequence, 220
serialization, 116 , 117
serve-static package, 561
server, 323 , 324 , 461 – 463 , 467 ,
469 , 470 , 526 , 537 , 538 ,
540 , 541 , 553 , 559
session, 490
sessionStorage object, 490
set, 216 , 218 , 336
set (data structure), 173 , 190
Set class, 173 , 190 , 590
set method, 158
setAttribute method, 346 , 347 ,
501
setInterval function, 384 , 440
setItem method, 488
setter, 161
setTimeout function, 271 , 292 ,
384 , 385 , 568 , 577

```
shape, 424 , 430 , 434 , 438 , 458
shapes (exercise), 458 , 605
shared property, 150 , 155 , 156
shift key, 371 , 610
shift method, 105
shiftKey property, 371
short-circuit evaluation, 31 , 75 ,
310 , 587
SICP, 300
side effect, 33 , 34 , 39 , 50 , 60 ,
80 , 94 , 119 , 130 , 238 , 262 ,
295 , 338 , 342 , 343 , 349 ,
429 , 445 , 466 , 497 , 499
sign, 17 , 248 , 592
sign bit, 17
signal, 15
simplicity, 316
simulation, 178 , 182 , 390 , 398 ,
493 , 603
sine, 111 , 358 , 401 , 415
single-quote character, 20 , 248 ,
330
singleton, 190
skill, 496
skill-sharing, 552
skill-sharing project, 552 , 553 , 556 ,
```

#### 559 , 570

SkillShareApp class, 578
skipSpace function, 304 , 319
slash character, 19 , 53 , 215 , 234 ,
468 , 544
slice method, 106 , 107 , 129 , 344 ,
585 , 599
slope, 613
sloppy programming, 386
smooth animation, 357
SMTP, 323
social factors, 521
socket, 555
some method, 136 , 142
sorting, 336
source property, 237
special form, 301 , 308 , 309
special return value, 200 , 201
specialForms object, 309
specificity, 354
speed, 1 , 3 , 459 , 607
spiral, 458 , 606
split method, 108 , 177 , 394 , 596
spread, 109 , 110 , 168 , 490 , 500
spread operator, 404
sprite, 439 , 440 , 451 , 452

```
spy, 378
square, 40
square bracket, 165
square brackets, 86 , 87 , 114 , 218 ,
483 , 490 , 584
square example, 59 , 64 , 65
square root, 100 , 111 , 588
src attribute, 327 , 329
stack, see call stack, 89
stack overflow, 67 , 72 , 83 , 583
stack trace, 203
standard, 9 , 37 , 52 , 130 , 203 , 218 ,
521 , 527 , 529
standard environment, 37
standard output, 528
standards, 321 , 332
star, 458 , 606
Star Trek, 433
startPixelEditor function, 519
startState constant, 519
startsWith method, 543
stat function, 535 , 544 , 546 , 614
state, 48 , 178
in
binding, 34 , 45 , 50
iterator, 286
```

objects, 178 , 395
in objects, 447
of application, 405 , 496 , 502 ,
517 , 580
of canvas, 428 , 445
persistence, 510
transitions, 294 , 497 , 500
statement, 33 , 34 , 40 , 45 , 48 , 59 ,
91
static (reserved word), 37
static file, 556 , 561
static method, 162 , 173 , 395
static property, 162 , 591
Stats type, 546
statSync function, 614
status code, 463 , 528
status property, 467 , 572
stoicism, 363
stopPropagation method, 367
stream, 323 , 538 , 539 , 542 , 548
strict mode, 192 , 193
string, 20 , 86 , 88 , 94 , 137
indexing, 83 , 106 , 109 , 137 ,
222
length, 55 , 137
methods, 107 , 223

```
notation, 20
properties, 107
representation, 21
searching, 107
String function, 40 , 159
stroke method, 430 , 431 , 433
strokeRect method, 428 , 607
strokeStyle property, 429
strokeText method, 437 , 438
stroking, 428 , 429 , 437 , 457
strong (HTML tag), 347 , 350
structure, 254 , 326 , 334 , 497
structure sharing, 120
style, 350
style (HTML tag), 352 , 353
style attribute, 350 , 351 , 353 , 402
style sheet, see CSS
subclass, 169
submit, 473 , 477 , 478
submit event, 478 , 479 , 575 , 615
substitution, 80
subtraction, 19 , 172
sum function, 8 , 118
summing (exercise), 118 , 584
summing example, 6 , 122 , 132 ,
313
```

superclass, 169
survey, 435
Sussman, Gerald, 300
SVG, 424 , 425 , 428 , 455 , 456
swapping bindings, 613
swipe, 510
switch keyword, 51
symbol, 163
Symbol function, 163
Symbol.iterator symbol, 165
synchronization, 578 , 616
synchronous programming, 269 ,
283 , 536 , 550
syncState method, 498 , 503 , 507 ,
508 , 523 , 616
syntax
error, 37 , 191 , 192
expression, 32
function, 59 , 64
identifier, 37
number, 17 , 248
object, 90
of Egg, 300 , 301
operator, 18
statement, 33 , 34 , 41 , 44 , 47 ,
50 , 202

```
string, 20
syntax tree, 302 , 303 , 306 , 307 ,
336
SyntaxError type, 305
```
```
tab character, 21 , 47
tab key, 476
tabbed interface (exercise), 389 ,
603
tabindex attribute, 372 , 476 , 522
table, 99 , 100 , 404
table (HTML tag), 360 , 392 , 404 ,
610
table example, 601
tableFor function, 100
tag, 325 , 327 , 334 , 353
talk, 552 , 553 , 564 – 566
talkResponse method, 567
talksAbout function, 340
talkURL function, 572
Tamil, 128
tampering, 471
tangent, 111
target property, 368
task management example, 105
TCP, 323 , 324 , 461 , 556
td (HTML tag), 361 , 404
```

temperature example, 161
template, 257 , 580 , 616
template literals, 22
templating language, 575
tentacle (analogy), 35 , 91 , 95
terminal, 528
ternary operator, 26 , 31 , 309
test method, 216
test runners, 197
test suite, 196
test suites, 197
testing, 189 , 196
text, 20 , 325 , 326 , 334 , 337 , 437 ,
455 , 456 , 459 , 479 , 483 ,
535 , 609
text field, 380 , 473 – 475 , 479 – 481
text method, 468
text node, 337 , 340 , 344 , 603
text wrapping, 455
text-align (CSS), 361
TEXT_NODE code, 337 , 603
textAlign property, 438 , 606
textarea (HTML tag), 385 , 474 ,
479 , 480 , 488 , 493 , 615
textBaseline property, 438 , 606
textContent property, 602 , 609

```
textFile function, 274 , 277 , 297 ,
596
textScripts function, 140 , 588
th (HTML tag), 361
then method, 273 , 274 , 276 , 277 ,
596 , 598
theory, 199
this binding, 89 , 146 , 147 , 151 ,
193
thread, 269 , 270 , 293 , 383
throw keyword, 202 , 203 , 209 ,
212 , 591
tile, 451
time, 217 , 221 , 224 , 357 , 386 ,
409 , 410 , 414 , 419 , 452 ,
517
time zone, 225
timeline, 269 , 292 , 329 , 357 , 363 ,
382
timeout, 384 , 556 , 558 , 568
times method, 398
timestamp, 225 , 297
title, 570
title (HTML tag), 326 , 328
toDataURL method, 513
toLowerCase method, 88 , 361
```

tool, 214 , 246 , 261 , 496 , 506 , 507 ,
509 – 512 , 519 , 523 , 524 , 533
tool property, 498
ToolSelect class, 507
top (CSS), 356 , 357 , 359 , 362
top-level scope, _see_ global scope
toString method, 148 , 156 , 157 ,
159 , 517 , 540
touch, 376 , 496
touchend event, 377
touches method, 410
touches property, 377 , 505
touchmove event, 377 , 504 , 524
touchstart event, 377 , 502 , 504
toUpperCase method, 88 , 196 , 361 ,
540
tr (HTML tag), 361 , 404
trackKeys function, 417 , 422
transform (CSS), 424
transformation, 441 , 442 , 444 , 445 ,
459 , 605
translate method, 442 , 444
Transmission Control Protocol,
_see_ TCP
transparency, 516
transparent, 426 , 440

```
transpilation, 316
trapezoid, 458 , 605
traversal, 228
tree, 302 , 336 , 337
trial and error, 198 , 434
triangle (exercise), 55 , 581
trigonometry, 112 , 358
trim method, 108 , 394
true, 24
trust, 330
try keyword, 203 , 205 , 591 , 592 ,
609
type, 16 , 23 , 144 , 170
type attribute, 472 , 478
type checking, 195 , 261
type coercion, 27 – 29 , 40
type property, 301 , 366
type variable, 195
typeof operator, 23 , 121 , 586
TypeScript, 195
typing, 385
typo, 191
```
```
unary operator, 23 , 32
uncaught exception, 207 , 279
undefined, 27 , 28 , 30 , 35 , 60 , 68 ,
87 , 91 , 114 , 192 , 193 , 200
```

underline, 350
underscore character, 36 , 52 , 226 ,
236
undo history, 517 , 518
UndoButton class, 519
Unicode, 21 , 22 , 25 , 128 , 137 ,
217 – 219
property, 219
unicycling, 552
uniform resource locator, _see_ URL
uniformity, 301
uniqueness, 353
unit (CSS), 359 , 379
Unix, 546 , 548 , 550
Unix time, 225
unlink function, 535 , 546
unshift method, 105
unwinding the stack, 202
upcasing server example, 540
updated method, 565 , 569 , 616
updateState function, 500
upgrading, 254
upload, 485
URL, 324 , 330 , 425 , 464 , 467 ,
471 , 538 , 557 , 572
URL class, 543

```
URL encoding, 465
url package, 567
urlPath function, 543
usability, 370
use strict, see strict mode
user experience, 363 , 477 , 554 ,
573
user interface, 207 , 497
UTF16, 22 , 137
UTF8, 535
```
```
validation, 200 , 211 , 300 , 408 ,
479 , 565
value, 16
value attribute, 473 , 479 , 483
var keyword, 36 , 60 , 61 , 114
variable, see binding
Vec class, 172 , 395 , 396 , 414 , 607
vector (exercise), 172 , 588
vector graphics, 438
verbosity, 66 , 270
version, 254 , 326 , 463 , 532 , 533
viewport, 406 , 408 , 447 , 449 , 454
VillageState class, 178
virtual keyboard, 372
virtual world, 175 , 178 , 182
virus, 330
```

vocabulary, 58 , 123 , 124
void operator, 37
volatile data storage, 16

waitForChanges method, 568
waiting, 271
walking, 452
wave, 401 , 415
Web, _see_ World Wide Web
web application, 8 , 487 , 495
web browser, _see_ browser
web page, 261
web worker, 383
WebDAV, 551
webgl (canvas context), 426
website, 330 , 331 , 464 , 526 , 551 ,
552
WebSockets, 555
weekDay module, 251
weekend project, 551
weresquirrel example, 85 , 90 , 93 ,
96 , 102 , 104
while loop, 7 , 45 , 47 , 78
whitespace, 319
in HTML, 341 , 507 , 603
in URLs, 557
indentation, 46

```
matching, 217 , 218
syntax, 52 , 301 , 304 , 600
trimming, 108 , 394
why, 32
width property, 523 , 611
window, 367 , 376 , 381
window object, 364
with statement, 194
wizard (mighty), 5
word boundary, 226
word character, 217 , 218 , 226
work list, 187 , 512
workbench (exercise), 493 , 609
world, 390
World Wide Web, 8 , 116 , 321 ,
324 , 330 , 331 , 461
writable stream, 538 , 539 , 543
write method, 538 , 539
writeFile function, 535 , 539 , 616
writeHead method, 537
writing code, 11 , 175
writing system, 128
WWW, see World Wide Web
```
```
XML, 338 , 425
XML namespace, 425
xmlns attribute, 425
```

yield (reserved word), 37
yield keyword, 286
your own loop (example), 142
Yuan-Ma, 15 , 249 , 526

Zawinski, Jamie, 214
zero-based counting, 83 , 86 , 224
zeroPad function, 79
zigzag, 606
zooming, 455


