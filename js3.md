# JavaScript

## For Impatient Programmers

**ECMAScript 2022 Edition**

**Dr. Axel Rauschmayer**



**JavaScript for impatient programmers**

**(ES2022 edition)**

Dr. Axel Rauschmayer

2022

## “An exhaustive resource, yet cuts out the fluff that clutters many

## programming books – with explanations that are understandable and to

## the point, as promised by the title! The quizzes and exercises are a very

## useful feature to check and lock in your knowledge. And you can

## definitely tear through the book fairly quickly, to get up and running in

## JavaScript.”

```
— Pam Selle , thewebivore.com
```
## “The best introductory book for modern JavaScript.”

```
— Tejinder Singh , Senior Software Engineer, IBM
```
## “This is JavaScript. No filler. No frameworks. No third-party libraries.

## If you want to learn JavaScript, you need this book.”

```
— Shelley Powers , Software Engineer/Writer
```

```
Copyright © 2022 by Dr. Axel Rauschmayer
Cover by Fran Caye
```
All rights reserved. This book or any portion thereof may not be reproduced or used in
any manner whatsoever withoutthe express written permission of the publisherexcept
for the use of brief quotations in a book review or scholarly journal.
ISBN 978-1-09-121009-
exploringjs.com


## Contents






-
- I Background
- 1 Before you buy the book
- 1.1 About the content.
- 1.2 Previewing and buying this book
- 1.3 About the author
- 1.4 Acknowledgements.
- 2 FAQ: book and supplementary material
- 2.1 How to read this book
- 2.2 I own a digital version
- 2.3 I own the print version
- 2.4 Notations and conventions.
- 3 History and evolution of JavaScript
- 3.1 How JavaScript was created
- 3.2 Standardizing JavaScript
- 3.3 Timeline of ECMAScript versions
- 3.4 Ecma Technical Committee 39 (TC39)
- 3.5 The TC39 process
- 3.6 FAQ: TC39 process
- 3.7 Evolving JavaScript: Don’t break the web.
- 4 New JavaScript features
- 4.1 New in ECMAScript
- 4.2 New in ECMAScript
- 4.3 New in ECMAScript
- 4.4 New in ECMAScript
- 4.5 New in ECMAScript
- 4.6 New in ECMAScript
- 4.7 New in ECMAScript
- 4.8 Source of this chapter.
- 5 FAQ: JavaScript
- 5.1 What are good references for JavaScript?
- 5.2 How do I find out what JavaScript features are supported where?
- 5.3 Where can I look up what features are planned for JavaScript?
-
- 5.4 Why does JavaScript fail silently so often? 4 CONTENTS
- tures? 5.5 Why can’t we clean up JavaScript, by removing quirks and outdated fea-
- 5.6 How can I quickly try out a piece of JavaScript code?
- II First steps
- 6 Using JavaScript: the big picture
- 6.1 What are you learning in this book?
- 6.2 The structure of browsers and Node.js
- 6.3 JavaScript references
- 6.4 Further reading
- 7 Syntax
- 7.1 An overview of JavaScript’s syntax
- 7.2 (Advanced)
- 7.3 Identifiers
- 7.4 Statement vs. expression
- 7.5 Ambiguous syntax
- 7.6 Semicolons
- 7.7 Automatic semicolon insertion (ASI)
- 7.8 Semicolons: best practices
- 7.9 Strict mode vs. sloppy mode
- 8 Consoles: interactive JavaScript command lines
- 8.1 Trying out JavaScript code
- 8.2 Theconsole.*API: printing data and more
- 9 Assertion API
- 9.1 Assertions in software development.
- 9.2 How assertions are used in this book
- 9.3 Normal comparison vs. deep comparison.
- 9.4 Quick reference: moduleassert.
- 10 Getting started with quizzes and exercises
- 10.1 Quizzes
- 10.2 Exercises.
- 10.3 Unit tests in JavaScript
- III Variables and values
- 11 Variables and assignment
- 11.1 let.
- 11.2 const
- 11.3 Deciding betweenconstandlet
- 11.4 The scope of a variable
- 11.5 (Advanced)
- 11.6 Terminology: static vs. dynamic
- CONTENTS
- 11.7 Global variables and the global object.
- 11.8 Declarations: scope and activation.
- 11.9 Closures
- 12 Values
- 12.1 What’s a type?.
- 12.2 JavaScript’s type hierarchy
- 12.3 The types of the language specification
- 12.4 Primitive values vs. objects.
- 12.5 The operatorstypeofandinstanceof: what’s the type of a value?.
- 12.6 Classes and constructor functions
- 12.7 Converting between types
- 13 Operators
- 13.1 Making sense of operators
- 13.2 The plus operator (+)
- 13.3 Assignment operators
- 13.4 Equality:==vs.===.
- 13.5 Ordering operators
- 13.6 Various other operators.
- IV Primitive values
- 14 The non-valuesundefinedandnull
- 14.1undefinedvs.null
- 14.2 Occurrences ofundefinedandnull.
- 14.3 Checking forundefinedornull.
- 14.4 The nullish coalescing operator (??) for default values [ES2020].
- 14.5undefinedandnulldon’t have properties
- 14.6 The history ofundefinedandnull
- 15 Booleans
- 15.1 Converting to boolean
- 15.2 Falsy and truthy values.
- 15.3 Truthiness-based existence checks
- 15.4 Conditional operator (? :)
- 15.5 Binary logical operators: And (x && y), Or (x || y)
- 15.6 Logical Not (!)
- 16 Numbers
- 16.1 Numbers are used for both floating point numbers and integers
- 16.2 Number literals
- 16.3 Arithmetic operators
- 16.4 Converting to number
- 16.5 Error values.
- 16.6 The precision of numbers: careful with decimal fractions
- 16.7 (Advanced)
- 16.8 Background: floating point precision
- 16.9 Integer numbers in JavaScript 6 CONTENTS
- 16.10Bitwise operators
- 16.11Quick reference: numbers
- 17 Math
- 17.1 Data properties
- 17.2 Exponents, roots, logarithms.
- 17.3 Rounding
- 17.4 Trigonometric Functions
- 17.5 Various other functions.
- 17.6 Sources
- 18 Bigints – arbitrary-precision integers [ES2020] (advanced)
- 18.1 Why bigints?
- 18.2 Bigints.
- 18.3 Bigint literals
- 18.4 Reusing number operators for bigints (overloading)
- 18.5 The wrapper constructorBigInt.
- 18.6 Coercing bigints to other primitive types
- 18.7 TypedArrays and DataView operations for 64-bit values.
- 18.8 Bigints and JSON
- 18.9 FAQ: Bigints.
- 19 Unicode – a brief introduction (advanced)
- 19.1 Code points vs. code units
- 19.2 Encodings used in web development: UTF-16 and UTF-8
- 19.3 Grapheme clusters – the real characters.
- 20 Strings
- 20.1 Cheat sheet: strings.
- 20.2 Plain string literals
- 20.3 Accessing JavaScript characters
- 20.4 String concatenation via+
- 20.5 Converting to string
- 20.6 Comparing strings
- 20.7 Atoms of text: code points, JavaScript characters, grapheme clusters
- 20.8 Quick reference: Strings
- 21 Using template literals and tagged templates
- 21.1 Disambiguation: “template”
- 21.2 Template literals
- 21.3 Tagged templates
- 21.4 Examples of tagged templates (as provided via libraries)
- 21.5 Raw string literals.
- 21.6 (Advanced)
- 21.7 Multiline template literals and indentation
- 21.8 Simple templating via template literals
- 22 Symbols
- CONTENTS
- 22.1 Symbols are primitives that are also like objects
- 22.2 The descriptions of symbols
- 22.3 Use cases for symbols.
- 22.4 Publicly known symbols
- 22.5 Converting symbols
- V Control flow and data flow
- 23 Control flow statements
- 23.1 Controlling loops:breakandcontinue
- 23.2 Conditions of control flow statements.
- 23.3ifstatements [ES1].
- 23.4switchstatements [ES3]
- 23.5whileloops [ES1]
- 23.6do-whileloops [ES3]
- 23.7forloops [ES1]
- 23.8for-ofloops [ES6]
- 23.9for-await-ofloops [ES2018]
- 23.10for-inloops (avoid) [ES1]
- 23.11Recomendations for looping
- 24 Exception handling
- 24.1 Motivation: throwing and catching exceptions
- 24.2throw
- 24.3 Thetrystatement.
- 24.4Errorand its subclasses
- 24.5 Chaining errors
- 25 Callable values
- 25.1 Kinds of functions
- 25.2 Ordinary functions
- 25.3 Specialized functions
- 25.4 Summary: kinds of callable values.
- 25.5 Returning values from functions and methods
- 25.6 Parameter handling.
- 25.7 Methods of functions:.call(),.apply(),.bind().
- 26 Evaluating code dynamically:eval(),new Function()(advanced)
- 26.1eval()
- 26.2new Function().
- 26.3 Recommendations
- VI Modularity
- 27 Modules
- 27.1 Cheat sheet: modules.
- 27.2 JavaScript source code formats.
- 27.3 Before we had modules, we had scripts.
- 27.4 Module systems created prior to ES6 8 CONTENTS
- 27.5 ECMAScript modules
- 27.6 Named exports and imports
- 27.7 Default exports and imports
- 27.8 More details on exporting and importing
- 27.9 npm packages.
- 27.10Naming modules
- 27.11Module specifiers.
- 27.12import.meta– metadata for the current module [ES2020]
- 27.13Loading modules dynamically viaimport()[ES2020] (advanced)
- 27.14Top-levelawaitin modules [ES2022] (advanced).
- 27.15Polyfills: emulating native web platform features (advanced).
- 28 Objects
- 28.1 Cheat sheet: objects.
- 28.2 What is an object?.
- 28.3 Fixed-layout objects.
- 28.4 Spreading into object literals (...) [ES2018].
- 28.5 Methods and the special variablethis
- (advanced). 28.6 Optional chaining for property getting and method calls [ES2020]
- 28.7 Dictionary objects (advanced)
- 28.8 Property attributes and freezing objects (advanced)
- 28.9 Prototype chains
- 28.10FAQ: objects.
- 29 Classes [ES6]
- 29.1 Cheat sheet: classes.
- 29.2 The essentials of classes
- 29.3 The internals of classes
- 29.4 Prototype members of classes
- 29.5 Instance members of classes [ES2022]
- 29.6 Static members of classes.
- 29.7 Subclassing
- 29.8 The methods and accessors ofObject.prototype(advanced).
- 29.9 FAQ: classes.
- 30 Where are the remaining chapters?


**Part I**

**Background**

```
9
```


**Chapter 1**

**Before you buy the book**

## Contents

```
1.1 About the content............................ 11
1.1.1 What’s in this book?....................... 11
1.1.2 What is not covered by this book?................ 12
1.1.3 Isn’t this book too long for impatient people?.......... 12
1.2 Previewing and buying this book................... 12
1.2.1 How can I preview the book, the exercises, and the quizzes?. 12
1.2.2 How can I buy a digital version of this book?.......... 12
1.2.3 How can I buy the print version of this book?......... 12
1.3 About the author............................. 12
1.4 Acknowledgements........................... 13
```
**1.1 About the content**

## 1.1.1 What’s in this book?

ThisbookmakesJavaScriptlesschallengingtolearnfornewcomersbyofferingamodern
view that is as consistent as possible.

```
Highlights:
```
- Get started quickly by initially focusing on modern features.
- Test-driven exercises and quizzes available for most chapters.
- Covers all essential features of JavaScript, up to and including ES2022.
- Optional advanced sections let you dig deeper.

```
No prior knowledge of JavaScript is required, but you should know how to program.
```
```
11
```

```
12 1 Before you buy the book
```
## 1.1.2 What is not covered by this book?

- Some advanced language features are not explained, but references to appropri-
    ate material are provided – for example, to my other JavaScript books atExplor-
    ingJS.com, which are free to read online.
- This book deliberately focuses on the language. Browser-only features, etc. are
    not described.

## 1.1.3 Isn’t this book too long for impatient people?

Thereare several ways in which you can read this book. One of them involves skipping
muchofthecontentinordertogetstartedquickly. Fordetails,see§2.1.1“Inwhichorder
should I read the content in this book?”.

**1.2 Previewing and buying this book**

## 1.2.1 How can I preview the book, the exercises, and the quizzes?

```
Go tothe homepage of this book:
```
- All essential chapters of this book are free to read online.
- The first half of the test-driven exercises can be downloaded.
- The first half of the quizzes can be tried online.

## 1.2.2 How can I buy a digital version of this book?

There are two digital versions of _JavaScript for impatient programmers_ :

- Ebooks: PDF, EPUB, MOBI, HTML (all without DRM)
- Ebooks plus exercises and quizzes

```
The home page of this bookdescribes how you can buy them.
```
## 1.2.3 How can I buy the print version of this book?

The print version of _JavaScript for impatient programmers_ is available on Amazon.

**1.3 About the author**

Dr. Axel Rauschmayer specializes in JavaScript and web development. He has been de-
veloping web applications since 1995. In 1999, he was technical manager at a German
internetstartupthatlaterexpandedinternationally. In2006,heheldhisfirsttalkonAjax.
In 2010, he received a PhD in Informatics from the University of Munich.

```
Since 2011, he has been blogging about web development at 2ality.com and has written
severalbooksonJavaScript. HehasheldtrainingsandtalksforcompaniessuchaseBay,
Bank of America, and O’Reilly Media.
```
```
He lives in Munich, Germany.
```

_1.4 Acknowledgements_ 13

**1.4 Acknowledgements**

- Cover byFran Caye
- Parts of this book were edited byAdaobi Obi Tulton.
- Thanks for answering questions, discussing language topics, etc.:
    **-** Allen Wirfs-Brock (@awbjs)
    **-** Benedikt Meurer (@bmeurer)
    **-** Brian Terlson (@bterlson)
    **-** Daniel Ehrenberg (@littledan)
    **-** Jordan Harband (@ljharb)
    **-** Maggie Johnson-Pint (@maggiepint)
    **-** Mathias Bynens (@mathias)
    **-** Myles Borins (@MylesBorins)
    **-** Rob Palmer (@robpalmer2)
    **-** Šime Vidas (@simevidas)
    **-** And many others
- Thanks for reviewing:
    **-** Johannes Weber (@jowe)

[Generated: 2022-01-03 14:16]


14 _1 Before you buy the book_


**Chapter 2**

**FAQ: book and supplementary**

**material**

## Contents

```
2.1 How to read this book.......................... 15
2.1.1 In which order should I read the content in this book?..... 15
2.1.2 Whyaresomechaptersandsectionsmarkedwith“(advanced)”? 16
2.1.3 Why are some chapters marked with “(bonus)”?........ 16
2.2 I own a digital version.......................... 16
2.2.1 How do I submit feedback and corrections?.......... 16
2.2.2 How do I get updates for the downloads I bought at Payhip?. 16
2.2.3 Can I upgrade from package “Ebooks” to package “Ebooks +
exercises + quizzes”?....................... 16
2.3 I own the print version.......................... 16
2.3.1 Can I get a discount for a digital version?............ 17
2.3.2 Can I submit an error or see submitted errors?......... 17
2.3.3 Is there an online list with the URLs in this book?....... 17
2.4 Notations and conventions....................... 17
2.4.1 What is a type signature? Why am I seeing static types in this
book?............................... 17
2.4.2 What do the notes with icons mean?............... 17
```
This chapter answers questions you may have and gives tips for reading this book.

**2.1 How to read this book**

## 2.1.1 In which order should I read the content in this book?

This book is three books in one:

- YoucanuseittogetstartedwithJavaScriptasquicklyaspossible. This“mode”is
    for impatient people:

```
15
```

```
16 2 FAQ: book and supplementary material
```
**-** Start reading with§6 “Using JavaScript: the big picture”.
**-** Skip all chapters and sections marked as “advanced”, and all quick refer-
    ences.
- ItgivesyouacomprehensivelookatcurrentJavaScript. Inthis“mode”,youread
everything and don’t skip advanced content and quick references.
- It serves as a reference. If there is a topic that you are interested in, you can find
information on it via the table of contents or via the index. Due to basic and ad-
vanced content being mixed, everything you need is usually in a single location.

Thequizzesandexercisesplayanimportantpartinhelpingyoupracticeandretainwhat
you have learned.

## 2.1.2 Whyaresomechaptersandsectionsmarkedwith“(advanced)”?

```
Several chapters and sections are marked with “(advanced)”. The idea is that you can
initiallyskipthem. Thatis,youcangetaquickworkingknowledgeofJavaScriptbyonly
reading the basic (non-advanced) content.
```
As your knowledge evolves, you can later come back to some or all of the advanced
content.

## 2.1.3 Why are some chapters marked with “(bonus)”?

Thebonuschaptersareonlyavailableinthepaidversionsofthisbook(printandebook).
They are listed inthe full table of contents.

**2.2 I own a digital version**

## 2.2.1 How do I submit feedback and corrections?

TheHTMLversionofthisbook(online,orad-freearchiveinthepaidversion)hasalink
at the end of each chapter that enables you to give feedback.

## 2.2.2 How do I get updates for the downloads I bought at Payhip?

- The receipt email for the purchase includes a link. You’ll always be able to down-
    load the latest version of the files at that location.
- If you opted into emails while buying, you’ll get an email whenever there is new
    content. To opt in later, you must contact Payhip (see bottom ofpayhip.com).

## 2.2.3 CanIupgradefrompackage“Ebooks”topackage“Ebooks+ex-

## ercises + quizzes”?

Yes. The instructions for doing so areon the homepage of this book.

**2.3 I own the print version**


```
2.4 Notations and conventions 17
```
## 2.3.1 Can I get a discount for a digital version?

```
If you bought the print version, you can get a discount for a digital version.The home-
page of the print versionexplains how.
```
Alas, the reverse is not possible: you cannot get a discount for the print version if you
bought a digital version.

## 2.3.2 Can I submit an error or see submitted errors?

```
Onthe homepage of the print version, you can submit errors and see submitted errors.
```
## 2.3.3 Is there an online list with the URLs in this book?

```
ThehomepageoftheprintversionhasalistwithalltheURLsthatyouseeinthefootnotes
of the print version.
```
**2.4 Notations and conventions**

## 2.4.1 What is a type signature? Why am I seeing static types in this

## book?

```
For example, you may see:
Number .isFinite(num:number):boolean
```
Thatiscalledthe _typesignature_ ofNumber.isFinite(). Thisnotation,especiallythestatic
typesnumberofnumandbooleanof the result, are not real JavaScript. The notation
is borrowed from the compile-to-JavaScript language TypeScript (which is mostly just
JavaScript plus static typing).

Whyisthisnotationbeingused? Ithelpsgiveyouaquickideaofhowafunctionworks.
The notation is explained in detail in“Tackling TypeScript”, but is usually relatively in-
tuitive.

## 2.4.2 What do the notes with icons mean?

```
Reading instructions
Explains how to best read the content.
```
```
External content
Points to additional, external, content.
```

18 _2 FAQ: book and supplementary material_

```
Tip
Gives a tip related to the current content.
```
```
Question
Asks and answers a question pertinent to the current content (think FAQ).
```
```
Warning
Warns about pitfalls, etc.
```
```
Details
Provides additional details, complementing the current content. It is similar to a
footnote.
```
```
Exercise
Mentions the path of a test-driven exercise that you can do at that point.
```
```
Quiz
Indicates that there is a quiz for the current (part of a) chapter.
```

**Chapter 3**

**History and evolution of**

**JavaScript**

## Contents

```
3.1 How JavaScript was created....................... 19
3.2 Standardizing JavaScript........................ 20
3.3 Timeline of ECMAScript versions................... 20
3.4 Ecma Technical Committee 39 (TC39)................. 21
3.5 The TC39 process............................. 21
3.5.1 Tip: Think in individual features and stages, not ECMAScript
versions.............................. 21
3.6 FAQ: TC39 process............................ 21
3.6.1 How is [my favorite proposed feature] doing?......... 23
3.6.2 Is there an official list of ECMAScript features?......... 23
3.7 Evolving JavaScript: Don’t break the web............... 23
```
**3.1 How JavaScript was created**

```
JavaScriptwascreatedinMay1995in10days,byBrendanEich. EichworkedatNetscape
and implemented JavaScript for their web browser, Netscape Navigator.
```
Theideawasthatmajorinteractivepartsoftheclient-sidewebweretobeimplemented
inJava. JavaScriptwassupposedtobeagluelanguageforthosepartsandtoalsomake
HTML slightly more interactive. Given its role of assisting Java, JavaScript had to look
like Java. That ruled out existing solutions such as Perl, Python, TCL, and others.
Initially, JavaScript’s name changed several times:

- Its code name was _Mocha_.
- In the Netscape Navigator 2.0 betas (September 1995), it was called _LiveScript_.
- In Netscape Navigator 2.0 beta 3 (December 1995), it got its final name, _JavaScript_.

```
19
```

```
20 3 History and evolution of JavaScript
```
**3.2 Standardizing JavaScript**

```
There are two standards for JavaScript:
```
- ECMA-262 is hosted by Ecma International. It is the primary standard.
- ISO/IEC 16262 is hosted by the International Organization for Standardization
    (ISO)andtheInternationalElectrotechnicalCommission(IEC).Thisisasecondary
    standard.
Thelanguagedescribedbythesestandardsiscalled _ECMAScript_ ,not _JavaScript_. Adiffer-
entnamewaschosenbecauseSun(nowOracle)hadatrademarkforthelattername. The
“ECMA”in“ECMAScript”comesfromtheorganizationthathoststheprimarystandard.

```
The original name of that organization was ECMA , an acronym for European Computer
Manufacturers Association. It was later changed to Ecma International (with “Ecma” be-
ing a proper name, not an acronym) because the organization’s activities had expanded
beyond Europe. The initial all-caps acronym explains the spelling of ECMAScript.
Inprinciple,JavaScriptandECMAScriptmeanthesamething. Sometimesthefollowing
distinction is made:
```
- The term _JavaScript_ refers to the language and its implementations.
- The term _ECMAScript_ refers to the language standard and language versions.
Therefore, _ECMAScript 6_ is a version of the language (its 6th edition).

**3.3 Timeline of ECMAScript versions**

```
This is a brief timeline of ECMAScript versions:
```
- ECMAScript 1 (June 1997): First version of the standard.
- ECMAScript 2 (June 1998): Small update to keep ECMA-262 in sync with the ISO
    standard.
- ECMAScript 3 (December 1999): Adds many core features – “[...] regular expres-
    sions,betterstringhandling,newcontrolstatements[do-while,switch],try/catch
    exception handling, [...]”
- ECMAScript 4 (abandoned in July 2008): Would have been a massive upgrade
    (withstatictyping,modules,namespaces,andmore),butendedupbeingtooam-
    bitious and dividing the language’s stewards.
- ECMAScript 5 (December 2009): Brought minor improvements – a few standard
    library features and _strict mode_.
- ECMAScript 5.1 (June 2011): Another small update to keep Ecma and ISO stan-
    dards in sync.
- ECMAScript 6 (June 2015): A large update that fulfilled many of the promises of
    ECMAScript4. Thisversionisthefirstonewhoseofficialname– _ECMAScript2015_
- is based on the year of publication.
- ECMAScript 2016 (June 2016): First yearly release. The shorter release life cycle
    resulted in fewer new features compared to the large ES6.
- ECMAScript 2017 (June 2017). Second yearly release.
- Subsequent ECMAScript versions (ES2018, etc.) are always ratified in June.


```
3.4 Ecma Technical Committee 39 (TC39) 21
```
**3.4 Ecma Technical Committee 39 (TC39)**

TC39 is the committee that evolves JavaScript. Its members are, strictly speaking, com-
panies: Adobe,Apple,Facebook,Google,Microsoft,Mozilla,Opera,Twitter,andothers.
Thatis,companiesthatareusuallyfiercecompetitorsareworkingtogetherforthegood
of the language.

```
Every two months, TC39 has meetings that member-appointed delegates and invited
experts attend. The minutes of those meetings are public ina GitHub repository.
```
**3.5 The TC39 process**

With ECMAScript 6, two issues with the release process used at that time became obvi-
ous:

- If too much time passes between releases then features that are ready early, have
    towaitalongtimeuntiltheycanbereleased. Andfeaturesthatarereadylate,risk
    being rushed to make the deadline.
- Features were often designed long before they were implemented and used. De-
    signdeficienciesrelatedtoimplementationandusewerethereforediscoveredtoo
    late.

```
In response to these issues, TC39 instituted the new TC39 process :
```
- ECMAScriptfeaturesaredesignedindependentlyandgothroughstages,starting
    at 0 (“strawman”), ending at 4 (“finished”).
- Especiallythelaterstagesrequireprototypeimplementationsandreal-worldtest-
    ing, leading to feedback loops between designs and implementations.
- ECMAScriptversionsarereleasedonceperyearandincludeallfeaturesthathave
    reached stage 4 prior to a release deadline.

The result: smaller, incremental releases, whose features have already been field-tested.
Fig.3.1illustrates the TC39 process.

```
ES2016 was the first ECMAScript version that was designed according to the TC39 pro-
cess.
```
## 3.5.1 Tip: Think in individual features and stages, not ECMAScript

## versions

```
Up to and including ES6, it was most common to think about JavaScript in terms of
ECMAScript versions – for example, “Does this browser support ES6 yet?”
```
Starting with ES2016, it’s better to think in individual features: once a feature reaches
stage4,youcansafelyuseit(ifit’ssupportedbytheJavaScriptenginesyouaretargeting).
You don’t have to wait until the next ECMAScript release.

**3.6 FAQ: TC39 process**


```
22 3 History and evolution of JavaScript
```
```
Stage 0: strawman
```
```
Stage 1: proposal
```
```
Stage 2: draft
```
```
Stage 3: candidate
```
```
Stage 4: finished
```
```
Pick champions
```
```
First spec text, 2 implementations
```
```
Spec complete
```
```
Test 262 acceptance tests
```
```
Review at TC39 meeting
```
```
TC39 helps
```
```
Likely to be standardized
```
```
Done, needs feedback from implementations
```
```
Ready for standardization
```
```
Sketch
```
Figure 3.1:Each ECMAScript feature proposal goes through stages that are numbered
from 0 to 4. _Champions_ are TC39 members that support the authors of a feature. Test
262 is a suite of tests that checks JavaScript engines for compliance with the language
specification.


```
3.7 Evolving JavaScript: Don’t break the web 23
```
## 3.6.1 How is [my favorite proposed feature] doing?

```
If you are wondering what stages various proposed features are in, consultthe GitHub
repositoryproposals.
```
## 3.6.2 Is there an official list of ECMAScript features?

Yes,theTC39repolistsfinishedproposalsandmentionsinwhichECMAScriptversions
they were introduced.

**3.7 Evolving JavaScript: Don’t break the web**

```
One idea that occasionally comes up is to clean up JavaScript by removing old features
and quirks. While the appeal of that idea is obvious, it has significant downsides.
Let’sassumewecreateanewversionofJavaScriptthatisnotbackwardcompatibleand
fix all of its flaws. As a result, we’d encounter the following problems:
```
- JavaScriptenginesbecomebloated: theyneedtosupportboththeoldandthenew
    version. The same is true for tools such as IDEs and build tools.
- Programmers need to know, and be continually conscious of, the differences be-
    tween the versions.
- You can either migrate all of an existing code base to the new version (which can
    bealotofwork). Oryoucanmixversionsandrefactoringbecomesharderbecause
    you can’t move code between versions without changing it.
- You somehow have to specify per piece of code – be it a file or code embedded in
    a web page – what version it is written in. Every conceivable solution has pros
    and cons. For example, _strict mode_ is a slightly cleaner version of ES5. One of the
    reasons why it wasn’t as popular as it should have been: it was a hassle to opt in
    via a directive at the beginning of a file or a function.
Sowhatisthesolution? Canwehaveourcakeandeatit? Theapproachthatwaschosen
for ES6 is called “One JavaScript”:
- New versions are always completely backward compatible (but there may occa-
sionally be minor, hardly noticeable clean-ups).
- Old features aren’t removed or fixed. Instead, better versions of them are intro-
duced. Oneexampleisdeclaringvariablesvialet–whichisanimprovedversion
ofvar.
- If aspects of the language are changed, it is done inside new syntactic constructs.
That is, you opt in implicitly. For example,yieldis only a keyword inside gen-
erators (which were introduced in ES6). And all code inside modules and classes
(both introduced in ES6) is implicitly in strict mode.

```
Quiz
Seequiz app.
```

24 _3 History and evolution of JavaScript_


**Chapter 4**

**New JavaScript features**

## Contents

```
4.1 New in ECMAScript 2022........................ 25
4.2 New in ECMAScript 2021........................ 26
4.3 New in ECMAScript 2020........................ 27
4.4 New in ECMAScript 2019........................ 28
4.5 New in ECMAScript 2018........................ 28
4.6 New in ECMAScript 2017........................ 30
4.7 New in ECMAScript 2016........................ 30
4.8 Source of this chapter.......................... 30
```
This chapter lists what’s new in ES2016–ES2022 in reverse chronological order. It starts
after ES2015 (ES6) because that release has too many features to list here.

**4.1 New in ECMAScript 2022**

```
ES2022 will probably become a standard in June 2022. The following proposals have
reached stage 4 and are scheduled to be part of that standard:
```
- New members of classes:
    **-** Properties (public slots) can now be created via:

## *Instance public fields

## *Static public fields

**-** Private slotsare new and can be created via:

## *Private fields (instance private fieldsandstatic private fields)

## 29.8 The methods and accessors ofObject.prototype(advanced).

**-** Static initialization blocks
- Private slot checks(“ergonomic brand checks for private fields”): The following
expression checks ifobjhas a private slot#privateSlot:
#privateSlot **in** obj

```
25
```

```
26 4 New JavaScript features
```
- Top-levelawaitin modules: We can now useawaitat the top levels of modules
    and don’t have to enter async functions or methods anymore.
- error.cause:Errorand its subclasses now let us specify which error caused the
    current one:

```
newError ('Something went wrong',{cause:otherError})
```
- Method.at()ofindexablevaluesletsusreadanelementatagivenindex(likethe
    bracket operator[]) and supports negative indices (unlike the bracket operator).

```
> ['a', 'b', 'c'].at(0)
'a'
> ['a', 'b', 'c'].at(-1)
'c'
```
```
The following “indexable” types have method.at():
```
**-** string
**-** Array
**-** All Typed Array classes:Uint8Arrayetc.
- RegExp match indices: If we add a flag to a regular expression, using it produces
match objects that record the start and end index of each group capture.
- Object.hasOwn(obj, propKey) provides a safe way to check if an ob-
jectobj has an own property with the key propKey. In contrast toOb-
ject.prototype.hasOwnProperty, it works with all objects.

```
More features may still be added to ES2022
If that happens, this book will be updated accordingly.
```
**4.2 New in ECMAScript 2021**

The following features were added in ECMAScript 2021:

- String.prototype.replaceAll()lets us replace all matches of a regular expres-
    sion or a string (.replace()only replaces the first occurrence of a string):

```
> 'abbbaab'.replaceAll('b', 'x')
'axxxaax'
```
- Promise.any()andAggregateError:Promise.any()returnsaPromisethatisful-
    filledassoonasthefirstPromiseinaniterableofPromisesisfulfilled. Ifthereare
    only rejections, they are put into anAggregateErrorwhich becomes the rejection
    value.

```
We usePromise.any()when we are only interested in the first fulfilled Promise
among several.
```
- Logical assignment operators:


```
4.3 New in ECMAScript 2020 27
```
```
a||=b
a&&=b
a??=b
```
- Underscores (_) as separators in:
    **-** Number literals:123_456.789_012
    **-** Bigint literals:6_000_000_000_000_000_000_000_000n
- WeakRefs: Thisfeatureisbeyondthescopeofthisbook. Formoreinformationon
    it, seeits proposal.

**4.3 New in ECMAScript 2020**

The following features were added in ECMAScript 2020:

- New module features:
    **-** Dynamic imports viaimport(): The normalimportstatement is static: We
       canonlyuseitatthetoplevelsofmodulesanditsmodulespecifierisafixed
       string.import()changes that. It can be used anywhere (including condi-
       tional statements) and we can compute its argument.
    **-** import.metacontains metadata for the current module. Its first widely sup-
       portedpropertyisimport.meta.urlwhichcontainsastringwiththeURLof
       the current module’s file.
    **-** Namespace re-exporting: The following expression imports all exports of
       module'mod'in a namespace objectnsand exports that object.

```
export*asnsfrom'mod';
```
- Optional chaining for property accesses and method calls. One example of op-
    tional chaining is:
       value.?prop

```
This expression evaluates toundefinedifvalueis eitherundefinedornull. Oth-
erwise, it evaluates tovalue.prop. This feature is especially useful in chains of
property reads when some of the properties may be missing.
```
- Nullish coalescing operator (??):

```
value??defaultValue
This expression isdefaultValueifvalueis eitherundefinedornullandvalue
otherwise. This operator lets us use a default value whenever something is miss-
ing.
Previously the Logical Or operator (||) was used in this case but it has down-
sidesherebecauseitreturnsthedefaultvaluewhenevertheleft-handsideisfalsy
(which isn’t always correct).
```
- Bigints–arbitrary-precisionintegers: Bigintsareanewprimitivetype. Itsupports
    integernumbersthatcanbearbitrarilylarge(storageforthemgrowsasnecessary).


```
28 4 New JavaScript features
```
- String.prototype.matchAll(): Thismethodthrowsifflag/gisn’tsetandreturns
    an iterable with all match objects for a given string.
- Promise.allSettled()receives an iterable of Promises. It returns a Promise that
    isfulfilledoncealltheinputPromisesaresettled. ThefulfillmentvalueisanArray
    with one object per input Promise – either one of:
       **-** { status: 'fulfilled', value: «fulfillment value» }
       **-** { status: 'rejected', reason: «rejection value» }
- globalThisprovidesawaytoaccesstheglobalobjectthatworksbothonbrowsers
    and server-side platforms such as Node.js and Deno.
- for-inmechanics: This feature is beyond the scope of this book. For more infor-
    mation on it, seeits proposal.

**4.4 New in ECMAScript 2019**

The following features were added in ECMAScript 2019:

- Array method.flatMap()works like.map()but lets the callback return Arrays
    ofzeroormorevaluesinsteadofsinglevalues. ThereturnedArraysarethencon-
    catenated and become the result of.flatMap(). Use cases include:
       **-** Filtering and mapping at the same time
       **-** Mapping single input values to multiple output values
- Arraymethod.flat()convertsnestedArraysintoflatArrays. Optionally,wecan
    tell it at which depth of nesting it should stop flattening.
- Object.fromEntries()creates an object from an iterable over _entries_. Each entry
    is a two-element Array with a property key and a property value.
- String methods: .trimStart()and.trimEnd()work like.trim()but remove
    whitespace only at the start or only at the end of a string.
- Optionalcatchbinding: We can now omit the parameter of acatchclause if we
    don’t use it.
- Symbol.prototype.descriptionisagetterforreadingthedescriptionofasymbol.
    Previously,thedescriptionwasincludedintheresultof.toString()butcouldn’t
    be accessed individually.

These new ES2019 features are beyond the scope of this book:

- JSON superset: See2ality blog post.
- Well-formedJSON.stringify(): See2ality blog post.
- Function.prototype.toString()revision: See2ality blog post.

**4.5 New in ECMAScript 2018**

The following features were added in ECMAScript 2018:


_4.5 New in ECMAScript 2018_ 29

- Asynchronous iterationis the asynchronous version of synchronous iteration. It
    is based on Promises:
       **-** Withsynchronousiterables,wecanimmediatelyaccesseachitem. Withasyn-
          chronous iterables, we have toawaitbefore we can access an item.
       **-** With synchronous iterables, we usefor-ofloops. With asynchronous iter-
          ables, we usefor-await-ofloops.
- Spreadingintoobjectliterals: Byusingspreading(...) insideanobjectliteral,we
    can copy the properties of another object into the current one. One use case is to
    create a shallow copy of an objectobj:

```
const shallowCopy={...obj};
```
- Rest properties (destructuring): When object-destructuring a value, we can now
    use rest syntax (...) to get all previously unmentioned properties in an object.

```
const {a,...remaining}={a: 1 ,b: 2 ,c: 3 };
assert.deepEqual(remaining,{b: 2 ,c: 3 });
```
- Promise.prototype.finally()is related to thefinallyclause of a try-catch-
    finally statement – similarly to how the Promise method.then()is related to the
    tryclause and.catch()is related to thecatchclause.

```
On other words: The callback of.finally()is executed regardless of whether a
Promise is fulfilled or rejected.
```
- New Regular expression features:
    **-** RegExpnamed capture groups: In addition to accessing groups by number,
       we can now name them and access them by name:

```
const matchObj='---756---'.match(/(?<digits>[0-9]+)/)
assert.equal(matchObj.groups.digits,'756');
```
**-** RegExplookbehind assertionscomplement lookahead assertions:

## *Positive lookbehind:(?<=X)matches if the current location is preceded

```
by'X'.
```
## *Negative lookbehind:(?<!X)matches if the current location is not pre-

```
ceded by'(?<!X)'.
```
**-** s(dotAll) flag for regular expressions. If this flag is active, the dot matches
    line terminators (by default, it doesn’t).
**-** RegExpUnicode property escapesgive us more power when matching sets
    of Unicode code points – for example:

```
> /^\p{Lowercase_Letter}+$/u.test('aüπ')
true
> /^\p{White_Space}+$/u.test('\n \t')
true
> /^\p{Script=Greek}+$/u.test('ΩΔΨ')
true
```

```
30 4 New JavaScript features
```
- Template literal revisionallows text with backslashes in tagged templates that is
    illegal in string literals – for example:
       windowsPath`C:\uuu\xxx\111`
       latex`\unicode`

**4.6 New in ECMAScript 2017**

The following features were added in ECMAScript 2017:

- Async functions (async/await)let us use synchronous-looking syntax to write
    asynchronous code.
- Object.values()returnsanArraywiththevaluesofallenumerablestring-keyed
    properties of a given object.
- Object.entries()returns an Array with the key-value pairs of all enumerable
    string-keyed properties of a given object. Each pair is encoded as a two-element
    Array.
- String padding: The string methods.padStart()and.padEnd()insert padding
    text until the receivers are long enough:
       > '7'.padStart(3, '0')
       **'007'**
       > 'yes'.padEnd(6, '!')
       **'yes!!!'**
- Trailingcommasinfunctionparameterlistsandcalls: Trailingcommashavebeen
    allowedinArraysliteralssinceES3andinObjectliteralssinceES5. Theyarenow
    also allowed in function calls and method calls.
- The following two features are beyond the scope of this book:
    **-** Object.getOwnPropertyDescriptors()(see“Deep JavaScript”)
    **-** Shared memory and atomics (seeproposal)

**4.7 New in ECMAScript 2016**

The following features were added in ECMAScript 2016:

- Array.prototype.includes()checks if an Array contains a given value.
- Exponentiation operator (**):
    > 4 ** 2
    **16**

**4.8 Source of this chapter**

```
ECMAScript feature lists were taken fromthe TC39 page on finished proposals.
```

**Chapter 5**

**FAQ: JavaScript**

## Contents

```
5.1 What are good references for JavaScript?............... 31
5.2 How do I find out what JavaScript features are supported where?.. 31
5.3 Where can I look up what features are planned for JavaScript?... 32
5.4 Why does JavaScript fail silently so often?.............. 32
5.5 Whycan’twecleanupJavaScript,byremovingquirksandoutdated
features?.................................. 32
5.6 How can I quickly try out a piece of JavaScript code?......... 32
```
**5.1 What are good references for JavaScript?**

```
Please consult§6.3 “JavaScript references”.
```
```
5.2 How do I find out what JavaScript features are sup-
ported where?
```
This book usually mentions if a feature is part of ECMAScript 5 (as required by older
browsers) or a newer version. For more detailed information (including pre-ES5 ver-
sions), there are several good compatibility tables available online:

- ECMAScript compatibility tables for various engines(bykangax,webbedspace,
    zloirock)
- Node.js compatibility tables(byWilliam Kapke)
- Mozilla’sMDNwebdocshavetablesforeachfeaturethatdescriberelevantECMA-
    Script versions and browser support.
- “Can I use...”documents what features (including JavaScript language features)
    are supported by web browsers.

```
31
```

```
32 5 FAQ: JavaScript
```
```
5.3 Where can I look up what features are planned for
JavaScript?
```
```
Please consult the following sources:
```
- §3.5 “The TC39 process”describes how upcoming features are planned.
- §3.6 “FAQ: TC39 process” answers various questions regarding upcoming
    features.

**5.4 Why does JavaScript fail silently so often?**

JavaScript often fails silently. Let’s look at two examples.

```
First example: If the operands of an operator don’t have the appropriate types, they are
converted as necessary.
> '3' * '5'
15
Secondexample: Ifanarithmeticcomputationfails,yougetanerrorvalue,notanexcep-
tion.
> 1 / 0
Infinity
```
The reason for the silent failures is historical: JavaScript did not have exceptions until
ECMAScript 3. Since then, its designers have tried to avoid silent failures.

```
5.5 Whycan’twecleanupJavaScript,byremovingquirks
and outdated features?
```
This question is answered in§3.7 “Evolving JavaScript: Don’t break the web”.

**5.6 How can I quickly try out a piece of JavaScript code?**

```
§8.1 “Trying out JavaScript code”explains how to do that.
```

**Part II**

**First steps**

```
33
```


**Chapter 6**

**Using JavaScript: the big picture**

## Contents

```
6.1 What are you learning in this book?.................. 35
6.2 The structure of browsers and Node.js................. 35
6.3 JavaScript references........................... 36
6.4 Further reading.............................. 36
```
```
In this chapter, I’d like to paint the big picture: what are you learning in this book, and
how does it fit into the overall landscape of web development?
```
**6.1 What are you learning in this book?**

This book teaches the JavaScript language. It focuses on just the language, but offers
occasional glimpses at two platforms where JavaScript can be used:

- Web browser
- Node.js

```
Node.js is important for web development in three ways:
```
- You can use it to write server-side software in JavaScript.
- You can also use it to write software for the command line (think Unix shell, Win-
    dowsPowerShell,etc.). ManyJavaScript-relatedtoolsarebasedon(andexecuted
    via) Node.js.
- Node’s software registry, npm, has become the dominant way of installing tools
    (such as compilers and build tools) and libraries – even for client-side develop-
       ment.

**6.2 The structure of browsers and Node.js**

ThestructuresofthetwoJavaScriptplatforms _webbrowser_ and _Node.js_ aresimilar(fig.6.1):

```
35
```

```
36 6 Using JavaScript: the big picture
```
JavaScript engine Platform core

```
JS standard
library
Platform API
```
Figure 6.1:The structure of the two JavaScript platforms _web browser_ and _Node.js_. The
APIs “standard library” and “platform API” are hosted on top of a foundational layer
with a JavaScript engine and a platform-specific “core”.

- The foundational layer consists of the JavaScript engine and platform-specific
    “core” functionality.
- Two APIs are hosted on top of this foundation:
    **-** The JavaScript standard library is part of JavaScript proper and runs on top
       of the engine.
    **-** The platform API are also available from JavaScript – it provides access to
       platform-specific functionality. For example:

## *Inbrowsers,youneedtousetheplatform-specificAPIifyouwanttodo

```
anythingrelatedtotheuserinterface: reacttomouseclicks,playsounds,
etc.
```
## *InNode.js,theplatform-specificAPIletsyoureadandwritefiles,down-

```
load data via HTTP, etc.
```
**6.3 JavaScript references**

When you have a question about a JavaScript, a web search usually helps. I can recom-
mend the following online sources:

- MDN web docs: cover various web technologies such as CSS, HTML, JavaScript,
    and more. An excellent reference.
- Node.js Docs: document the Node.js API.
- ExploringJS.com: My other books on JavaScript go into greater detail than this
    bookandarefreetoreadonline. YoucanlookupfeaturesbyECMAScriptversion:
       **-** ES1–ES5: _Speaking JavaScript_
       **-** ES6: _Exploring ES6_
       **-** ES2016–ES2017: _Exploring ES2016 and ES2017_
       **-** Etc.

**6.4 Further reading**

- A bonus chapterprovides a more comprehensive look at web development.


**Chapter 7**

**Syntax**

## Contents

```
7.1 An overview of JavaScript’s syntax................... 38
7.1.1 Basic constructs.......................... 38
7.1.2 Modules.............................. 42
7.1.3 Classes............................... 42
7.1.4 Exception handling........................ 43
7.1.5 Legal variable and property names............... 43
7.1.6 Casing styles........................... 44
7.1.7 Capitalization of names..................... 44
7.1.8 More naming conventions.................... 44
7.1.9 Where to put semicolons?.................... 44
7.2 (Advanced)................................ 45
7.3 Identifiers................................. 45
7.3.1 Valid identifiers (variable names, etc.).............. 45
7.3.2 Reserved words.......................... 46
7.4 Statement vs. expression......................... 46
7.4.1 Statements............................. 46
7.4.2 Expressions............................ 47
7.4.3 What is allowed where?..................... 47
7.5 Ambiguous syntax............................ 48
7.5.1 Same syntax: function declaration and function expression.. 48
7.5.2 Same syntax: object literal and block.............. 48
7.5.3 Disambiguation.......................... 48
7.6 Semicolons................................ 49
7.6.1 Rule of thumb for semicolons.................. 49
7.6.2 Semicolons: control statements................. 49
7.7 Automatic semicolon insertion (ASI).................. 50
7.7.1 ASI triggered unexpectedly................... 50
7.7.2 ASI unexpectedly not triggered................. 51
```
```
37
```

```
38 7 Syntax
```
```
7.8 Semicolons: best practices........................ 51
7.9 Strict mode vs. sloppy mode...................... 52
7.9.1 Switching on strict mode..................... 52
7.9.2 Improvements in strict mode................... 52
```
**7.1 An overview of JavaScript’s syntax**

This is a very first look at JavaScript’s syntax. Don’t worry if some things don’t make
sense, yet. They will all be explained in more detail later in this book.

This overview is not exhaustive, either. It focuses on the essentials.

## 7.1.1 Basic constructs

```
7.1.1.1 Comments
```
```
// single-line comment
```
```
/*
Comment with
multiple lines
*/
```
```
7.1.1.2 Primitive (atomic) values
```
```
Booleans:
true
false
```
```
Numbers:
1.141
```
- 123

The basic number type is used for both floating point numbers (doubles) and integers.

```
Bigints:
```
```
17 n
```
- 49 n

Thebasicnumbertypecanonlyproperlyrepresentintegerswithinarangeof53bitsplus
sign. Bigints can grow arbitrarily large in size.

```
Strings:
'abc'
"abc"
`String with interpolated values:${ 256 }and${ true }`
```
JavaScript has no extra type for characters. It uses strings to represent them.


```
7.1 An overview of JavaScript’s syntax 39
```
```
7.1.1.3 Assertions
```
An _assertion_ describeswhattheresultofacomputationisexpectedtolooklikeandthrows
an exception if those expectations aren’t correct. For example, the following assertion
states that the result of the computation 7 plus 1 must be 8:
assert.equal( 7 + 1 , 8 );

```
assert.equal()isamethodcall(theobjectisassert,themethodis.equal())withtwo
arguments: theactualresultandtheexpectedresult. ItispartofaNode.jsassertionAPI
that is explainedlater in this book.
```
There is alsoassert.deepEqual()that compares objects deeply.

```
7.1.1.4 Logging to the console
```
```
Logging tothe consoleof a browser or Node.js:
// Printing a value to standard out (another method call)
console .log('Hello!');
```
```
// Printing error information to standard error
console .error('Something went wrong!');
```
```
7.1.1.5 Operators
// Operators for booleans
assert.equal( true && false , false );// And
assert.equal( true || false , true );// Or
```
```
// Operators for numbers
assert.equal( 3 + 4 , 7 );
assert.equal( 5 - 1 , 4 );
assert.equal( 3 * 4 , 12 );
assert.equal( 10 / 4 ,2.5);
```
```
// Operators for bigints
assert.equal( 3 n+ 4 n, 7 n);
assert.equal( 5 n- 1 n, 4 n);
assert.equal( 3 n* 4 n, 12 n);
assert.equal( 10 n/ 4 n, 2 n);
```
```
// Operators for strings
assert.equal('a'+'b','ab');
assert.equal('I see '+ 3 +' monkeys','I see 3 monkeys');
```
```
// Comparison operators
assert.equal( 3 < 4 , true );
assert.equal( 3 <= 4 , true );
assert.equal('abc'==='abc', true );
assert.equal('abc'!=='def', true );
```

```
40 7 Syntax
```
JavaScriptalsohasa==comparisonoperator. Irecommendtoavoidit–whyisexplained
in§13.4.3 “Recommendation: always use strict equality”.

```
7.1.1.6 Declaring variables
```
```
constcreates immutable variable bindings : Each variable must be initialized immediately
and we can’t assign a different value later. However, the value itself may be mutable
andwemaybeabletochangeitscontents. Inotherwords:constdoesnotmakevalues
immutable.
```
```
// Declaring and initializing x (immutable binding):
const x= 8 ;
```
```
// Would cause a TypeError:
// x = 9;
```
```
letcreates mutable variable bindings :
```
```
// Declaring y (mutable binding):
let y;
```
```
// We can assign a different value to y:
y= 3 * 5 ;
```
```
// Declaring and initializing z:
let z= 3 * 5 ;
```
```
7.1.1.7 Ordinary function declarations
```
```
// add1() has the parameters a and b
function add1(a,b) {
return a+b;
}
// Calling function add1()
assert.equal(add1( 5 , 2 ), 7 );
```
```
7.1.1.8 Arrow function expressions
```
Arrow function expressions are used especially as arguments of function calls and
method calls:

```
const add2=(a,b) => { return a+b };
// Calling function add2()
assert.equal(add2( 5 , 2 ), 7 );
```
```
// Equivalent to add2:
const add3=(a,b) => a+b;
```
The previous code contains the following two arrow functions (the terms _expression_ and
_statement_ are explainedlater in this chapter):


_7.1 An overview of JavaScript’s syntax_ 41

```
// An arrow function whose body is a code block
(a,b) => { return a+b }
```
```
// An arrow function whose body is an expression
(a,b) => a+b
```
**7.1.1.9 Plain objects**

```
// Creating a plain object via an object literal
const obj={
first:'Jane',// property
last:'Doe',// property
getFullName() {// property (method)
returnthis .first+' '+ this .last;
},
};
```
```
// Getting a property value
assert.equal(obj.first,'Jane');
// Setting a property value
obj.first='Janey';
```
```
// Calling the method
assert.equal(obj.getFullName(),'Janey Doe');
```
**7.1.1.10 Arrays**

```
// Creating an Array via an Array literal
const arr=['a','b','c'];
assert.equal(arr.length, 3 );
```
```
// Getting an Array element
assert.equal(arr[ 1 ],'b');
// Setting an Array element
arr[ 1 ]='β';
```
```
// Adding an element to an Array:
arr.push('d');
```
```
assert.deepEqual(
arr,['a','β','c','d']);
```
## 23 Control flow statements

Conditional statement:

```
if (x< 0 ) {
x=-x;
}
```

```
42 7 Syntax
```
```
for-ofloop:
const arr=['a','b'];
for ( const element of arr) {
console .log(element);
}
// Output:
// 'a'
// 'b'
```
## 27 Modules

```
Eachmoduleisasinglefile. Consider,forexample,thefollowingtwofileswithmodules
in them:
file-tools.mjs
main.mjs
```
The module infile-tools.mjsexports its functionisTextFilePath():

```
export function isTextFilePath(filePath) {
return filePath.endsWith('.txt');
}
```
The module in main.mjsimports the whole modulepath and the functionis-
TextFilePath():

```
// Import whole module as namespace object `path`
import*aspathfrom'path';
// Import a single export of module file-tools.mjs
import{isTextFilePath}from'./file-tools.mjs';
```
## 7.1.3 Classes

```
class Person {
constructor(name) {
this .name=name;
}
describe() {
return `Person named${ this .name}`;
}
static logNames(persons) {
for ( const person of persons) {
console .log(person.name);
}
}
}
```
```
class Employee extends Person {
constructor(name,title) {
super (name);
```

```
7.1 An overview of JavaScript’s syntax 43
```
```
this .title=title;
}
describe() {
returnsuper .describe()+
` (${ this .title})`;
}
}
```
```
const jane= new Employee('Jane','CTO');
assert.equal(
jane.describe(),
'Person named Jane (CTO)');
```
## 24 Exception handling

```
function throwsException() {
thrownewError ('Problem!');
}
```
```
function catchesException() {
try {
throwsException();
} catch (err) {
assert.ok(err instanceofError );
assert.equal(err.message,'Problem!');
}
}
Note:
```
- try-finallyandtry-catch-finallyare also supported.
- We can throw any value, but features such as stack traces are only supported by
    Errorand its subclasses.

## 7.1.5 Legal variable and property names

The grammatical category of variable names and property names is called _identifier_.

```
Identifiers are allowed to have the following characters:
```
- Unicode letters:A–Z,a–z(etc.)
- $,_
- Unicode digits: 0 – 9 (etc.)
    **-** Variable names can’t start with a digit
Some words have special meaning in JavaScript and are called _reserved_. Examples in-
clude:if,true,const.
Reserved words can’t be used as variable names:
**constif** = 123 ;
// SyntaxError: Unexpected token if


```
44 7 Syntax
```
```
But they are allowed as names of properties:
> const obj = { if: 123 };
> obj.if
123
```
## 7.1.6 Casing styles

```
Common casing styles for concatenating words are:
```
- Camel case:threeConcatenatedWords
- Underscore case (also called _snake case_ ):three_concatenated_words
- Dash case (also called _kebab case_ ):three-concatenated-words

## 7.1.7 Capitalization of names

```
In general, JavaScript uses camel case, except for constants.
Lowercase:
```
- Functions, variables:myFunction
- Methods:obj.myMethod
- CSS:
    **-** CSS entity:special-class
    **-** Corresponding JavaScript variable:specialClass

```
Uppercase:
```
- Classes:MyClass
- Constants:MY_CONSTANT
    **-** Constants are also often written in camel case:myConstant

## 7.1.8 More naming conventions

The following naming conventions are popular in JavaScript.

```
If the name of a parameter starts with an underscore (or is an underscore) it means that
this parameter is not used – for example:
arr.map((_x,i) => i)
```
```
If the name of a property of an object starts with an underscore then that property is
considered private:
class ValueWrapper {
constructor(value) {
this ._value=value;
}
}
```
## 7.1.9 Where to put semicolons?

At the end of a statement:


```
7.2 (Advanced) 45
```
```
const x= 123 ;
func();
```
```
But not if that statement ends with a curly brace:
```
```
while ( false ) {
// ···
}// no semicolon
```
```
function func() {
// ···
}// no semicolon
```
```
However,addingasemicolonaftersuchastatementisnotasyntaxerror–itisinterpreted
as an empty statement:
```
```
// Function declaration followed by empty statement:
function func() {
// ···
};
```
```
Quiz: basic
Seequiz app.
```
**7.2 (Advanced)**

All remaining sections of this chapter are advanced.

**7.3 Identifiers**

## 7.3.1 Valid identifiers (variable names, etc.)

```
First character:
```
- Unicodeletter(includingaccentedcharacterssuchaséandüandcharactersfrom
    non-latin alphabets, such asα)
- $
- _

```
Subsequent characters:
```
- Legal first characters
- Unicode digits (including Eastern Arabic numerals)
- Some other Unicode marks and punctuations

```
Examples:
```
```
const ε=0.0001;
const строка='';
```

```
46 7 Syntax
```
```
let _tmp= 0 ;
const $foo2= true ;
```
## 7.3.2 Reserved words

```
Reserved words can’t be variable names, but they can be property names.
```
All JavaScript _keywords_ are reserved words:

```
await break case catch class const continue debugger default delete
do else export extends finally for function if import in instanceof
let new return static super switch this throw try typeof var void while
with yield
```
The following tokens are also keywords, but currently not used in the language:

```
enum implements package protected interface private public
```
The following literals are reserved words:

```
true false null
```
Technically,thesewordsarenotreserved,butyoushouldavoidthem,too,becausethey
effectively are keywords:
Infinity NaN undefined async

You shouldn’t use the names of global variables (String,Math, etc.) for your own vari-
ables and parameters, either.

**7.4 Statement vs. expression**

```
Inthissection,weexplorehowJavaScriptdistinguishestwokindsofsyntacticconstructs:
statements and expressions. Afterward,we’llseethatthatcancauseproblemsbecausethe
same syntax can mean different things, depending on where it is used.
```
```
We pretend there are only statements and expressions
Forthesakeofsimplicity,wepretendthatthereareonlystatementsandexpressions
in JavaScript.
```
## 7.4.1 Statements

A _statement_ isapieceofcodethatcanbeexecutedandperformssomekindofaction. For
example,ifis a statement:
**let** myStr;
**if** (myBool) {
myStr='Yes';
} **else** {
myStr='No';
}


```
7.4 Statement vs. expression 47
```
```
One more example of a statement: a function declaration.
function twice(x) {
return x+x;
}
```
## 7.4.2 Expressions

An _expression_ isapieceofcodethatcanbe _evaluated_ toproduceavalue. Forexample,the
code between the parentheses is an expression:

```
let myStr=(myBool?'Yes':'No');
```
The operator_?_:_used between the parentheses is called the _ternary operator_. It is the
expression version of theifstatement.
Let’slookatmoreexamplesofexpressions. WeenterexpressionsandtheREPLevaluates
them for us:

```
> 'ab' + 'cd'
'abcd'
> Number('123')
123
> true || false
true
```
## 7.4.3 What is allowed where?

The current location within JavaScript source code determines which kind of syntactic
constructs you are allowed to use:

- The body of a function must be a sequence of statements:
    **function** max(x,y) {
       **if** (x>y) {
          **return** x;
       } **else** {
          **return** y;
       }
    }
- The arguments of a function call or a method call must be expressions:

```
console .log('ab'+'cd', Number ('123'));
However, expressions can be used as statements. Then they are called expression state-
ments. The opposite is not true: when the context requires an expression, you can’t use
a statement.
```
The following code demonstrates that any expressionbar()can be either expression or
statement – it depends on the context:

```
function f() {
console .log(bar());// bar() is expression
```

```
48 7 Syntax
```
```
bar();// bar(); is (expression) statement
}
```
**7.5 Ambiguous syntax**

JavaScript has several programming constructs that are syntactically ambiguous: the
samesyntaxisinterpreteddifferently,dependingonwhetheritisusedinstatementcon-
text or in expression context. This section explores the phenomenon and the pitfalls it
causes.

## 7.5.1 Same syntax: function declaration and function expression

A _function declaration_ is a statement:

```
function id(x) {
return x;
}
```
A _function expression_ is an expression (right-hand side of=):

```
const id= function me(x) {
return x;
};
```
## 7.5.2 Same syntax: object literal and block

```
In the following code,{}is an object literal : an expression that creates an empty object.
```
```
const obj={};
```
This is an empty code block (a statement):

```
{
}
```
## 7.5.3 Disambiguation

The ambiguities are only a problem in statement context: If the JavaScript parser en-
counters ambiguous syntax, it doesn’t know if it’s a plain statement or an expression
statement. For example:

- If a statement starts withfunction: Is it a function declaration or a function ex-
    pression?
- If a statement starts with{: Is it an object literal or a code block?

Toresolvetheambiguity,statementsstartingwithfunctionor{areneverinterpretedas
expressions. Ifyouwantanexpressionstatementtostartwitheitheroneofthesetokens,
you must wrap it in parentheses:

```
( function (x) { console .log(x) })('abc');
```

```
7.6 Semicolons 49
```
```
// Output:
// 'abc'
```
```
In this code:
```
```
1.We first create a function via a function expression:
```
```
function (x) { console .log(x) }
```
```
2.Then we invoke that function:('abc')
```
Thecodefragmentshownin(1)isonlyinterpretedasanexpressionbecausewewrapitin
parentheses. Ifwedidn’t,wewouldgetasyntaxerrorbecausethenJavaScriptexpectsa
functiondeclarationandcomplainsaboutthemissingfunctionname. Additionally,you
can’t put a function call immediately after a function declaration.

```
Later in this book, we’ll see more examples of pitfalls caused by syntactic ambiguity:
```
- Assigning via object destructuring
- Returning an object literal from an arrow function

**7.6 Semicolons**

## 7.6.1 Rule of thumb for semicolons

```
Each statement is terminated by a semicolon:
```
```
const x= 3 ;
someFunction('abc');
i++;
```
```
except statements ending with blocks:
```
```
function foo() {
// ···
}
if (y> 0 ) {
// ···
}
```
The following case is slightly tricky:

```
const func=() => {};// semicolon!
```
The wholeconstdeclaration (a statement) ends with a semicolon, but inside it, there is
anarrowfunctionexpression. Thatis,it’snotthestatementpersethatendswithacurly
brace; it’s the embedded arrow function expression. That’s why there is a semicolon at
the end.

## 7.6.2 Semicolons: control statements

The body of a control statement is itself a statement. For example, this is the syntax of
thewhileloop:


```
50 7 Syntax
```
```
while (condition)
statement
```
The body can be a single statement:

```
while (a> 0 ) a--;
But blocks are also statements and therefore legal bodies of control statements:
while (a> 0 ) {
a--;
}
Ifyouwantalooptohaveanemptybody,yourfirstoptionisanemptystatement(which
is just a semicolon):
while (processNextItem()> 0 );
```
Your second option is an empty block:

```
while (processNextItem()> 0 ) {}
```
**7.7 Automatic semicolon insertion (ASI)**

WhileIrecommendtoalwayswritesemicolons,mostofthemareoptionalinJavaScript.
The mechanism that makes this possible is called _automatic semicolon insertion_ (ASI). In a
way, it corrects syntax errors.

ASI works as follows. Parsing of a statement continues until there is either:

- A semicolon
- A line terminator followed by an illegal token

```
In other words, ASI can be seen as inserting semicolons at line breaks. The next subsec-
tions cover the pitfalls of ASI.
```
## 7.7.1 ASI triggered unexpectedly

The good news about ASI is that – if you don’t rely on it and always write semicolons

- there is only one pitfall that you need to be aware of. It is that JavaScript forbids line
    breaks after some tokens. If you do insert a line break, a semicolon will be inserted, too.

The token where this is most practically relevant isreturn. Consider, for example, the
following code:

```
return
{
first:'jane'
};
```
This code is parsed as:

```
return ;
{
first:'jane';
```

```
7.8 Semicolons: best practices 51
```
### }

### ;

That is:

- Return statement without operand:return;
- Start of code block:{
- Expression statement'jane';withlabelfirst:
- End of code block:}
- Empty statement:;

Why does JavaScript do this? It protects against accidentally returning a value in a line
after areturn.

## 7.7.2 ASI unexpectedly not triggered

```
In some cases, ASI is not triggered when you think it should be. That makes life more
complicatedforpeoplewhodon’tlikesemicolonsbecausetheyneedtobeawareofthose
cases. The following are three examples. There are more.
```
```
Example 1: Unintended function call.
a=b+c
(d +e).print()
Parsed as:
```
```
a=b+c(d+e).print();
Example 2: Unintended division.
```
```
a=b
/hi/g.exec(c).map(d)
Parsed as:
```
```
a=b/hi/g.exec(c).map(d);
Example 3: Unintended property access.
someFunction()
['ul','ol'].map(x => x+x)
```
```
Executed as:
const propKey=('ul','ol');// comma operator
assert.equal(propKey,'ol');
```
```
someFunction()[propKey].map(x => x+x);
```
**7.8 Semicolons: best practices**

```
I recommend that you always write semicolons:
```
- I like the visual structure it gives code – you clearly see where a statement ends.


```
52 7 Syntax
```
- There are less rules to keep in mind.
- The majority of JavaScript programmers use semicolons.
However, there are also many people who don’t like the added visual clutter of semi-
colons. If you are one of them: Code without them _is_ legal. I recommend that you use
tools to help you avoid mistakes. The following are two examples:
- The automatic code formatterPrettiercan be configured to not use semicolons. It
then automatically fixes problems. For example, if it encounters a line that starts
with a square bracket, it prefixes that line with a semicolon.
- ThestaticcheckerESLinthasarulethatyoutellyourpreferredstyle(alwayssemi-
colons or as few semicolons as possible) and that warns you about critical issues.

**7.9 Strict mode vs. sloppy mode**

```
Starting with ECMAScript 5, JavaScript has two modes in which JavaScript can be exe-
cuted:
```
- Normal “sloppy” mode is the default in scripts (code fragments that are a precur-
    sor to modules and supported by browsers).
- Strictmodeisthedefaultinmodulesandclasses,andcanbeswitchedoninscripts
    (howisexplainedlater). Inthismode,severalpitfallsofnormalmodeareremoved
    and more exceptions are thrown.

You’llrarelyencountersloppymodeinmodernJavaScriptcode,whichisalmostalways
located in modules. In this book, I assume that strict mode is always switched on.

## 7.9.1 Switching on strict mode

```
InscriptfilesandCommonJSmodules,youswitchonstrictmodeforacompletefile,by
putting the following code in the first line:
'use strict';
```
Theneatthingaboutthis“directive”isthatECMAScriptversionsbefore5simplyignore
it: it’s an expression statement that does nothing.

You can also switch on strict mode for just a single function:

```
function functionInStrictMode() {
'use strict';
}
```
## 7.9.2 Improvements in strict mode

```
Let’slook atthree things thatstrict mode does betterthan sloppy mode. Justin this one
section, all code fragments are executed in sloppy mode.
```
```
7.9.2.1 Sloppy mode pitfall: changing an undeclared variable creates a global vari-
able
```
```
In non-strict mode, changing an undeclared variable creates a global variable.
```

```
7.9 Strict mode vs. sloppy mode 53
```
```
function sloppyFunc() {
undeclaredVar1= 123 ;
}
sloppyFunc();
// Created global variable `undeclaredVar1`:
assert.equal(undeclaredVar1, 123 );
```
```
Strict mode does it better and throws aReferenceError. That makes it easier to detect
typos.
```
```
function strictFunc() {
'use strict';
undeclaredVar2= 123 ;
}
assert.throws(
() => strictFunc(),
{
name:'ReferenceError',
message:'undeclaredVar2 is not defined',
});
```
Theassert.throws()statesthatitsfirstargument,afunction,throwsaReferenceError
when it is called.

```
7.9.2.2 Function declarations are block-scoped in strict mode, function-scoped in
sloppy mode
```
```
In strict mode, a variable created via a function declaration only exists within the inner-
most enclosing block:
```
```
function strictFunc() {
'use strict';
{
function foo() { return 123 }
}
return foo();// ReferenceError
}
assert.throws(
() => strictFunc(),
{
name:'ReferenceError',
message:'foo is not defined',
});
```
```
In sloppy mode, function declarations are function-scoped:
```
```
function sloppyFunc() {
{
function foo() { return 123 }
}
return foo();// works
```

54 _7 Syntax_

### }

```
assert.equal(sloppyFunc(), 123 );
```
**7.9.2.3 Sloppy mode doesn’t throw exceptions when changing immutable data**

In strict mode, you get an exception if you try to change immutable data:

```
function strictFunc() {
'use strict';
true .prop= 1 ;// TypeError
}
assert.throws(
() => strictFunc(),
{
name:'TypeError',
message:"Cannot create property 'prop' on boolean 'true'",
});
```
In sloppy mode, the assignment fails silently:

```
function sloppyFunc() {
true .prop= 1 ;// fails silently
returntrue .prop;
}
assert.equal(sloppyFunc(), undefined );
```
```
Further reading: sloppy mode
For more information on how sloppy mode differs from strict mode, seeMDN.
```
```
Quiz: advanced
Seequiz app.
```

**Chapter 8**

**Consoles: interactive JavaScript**

**command lines**

## Contents

```
8.1 Trying out JavaScript code........................ 55
8.1.1 Browser consoles......................... 55
8.1.2 The Node.js REPL......................... 57
8.1.3 Other options........................... 57
8.2 Theconsole.*API: printing data and more.............. 57
8.2.1 Printing values:console.log()(stdout)............ 58
8.2.2 Printing error information:console.error()(stderr)..... 59
8.2.3 Printing nested objects viaJSON.stringify()......... 59
```
**8.1 Trying out JavaScript code**

You have many options for quickly running pieces of JavaScript code. The following
subsections describe a few of them.

## 8.1.1 Browser consoles

Webbrowsershaveso-called _consoles_ : interactivecommandlinestowhichyoucanprint
textviaconsole.log()andwhereyoucanrunpiecesofcode. Howtoopentheconsole
differs from browser to browser. Fig.8.1shows the console of Google Chrome.

To find out how to open the console in your web browser, you can do a web search
for “console «name-of-your-browser»”. These are pages for a few commonly used web
browsers:

- Apple Safari
- Google Chrome
- Microsoft Edge
- Mozilla Firefox

```
55
```

56 _8 Consoles: interactive JavaScript command lines_

Figure8.1:Theconsoleofthewebbrowser“GoogleChrome”isopen(inthebottomhalf
of window) while visiting a web page.


```
8.2 Theconsole.*API: printing data and more 57
```
## 8.1.2 The Node.js REPL

_REPL_ standsfor _read-eval-printloop_ andbasicallymeans _commandline_. Touseit,youmust
firststartNode.jsfromanoperatingsystemcommandline,viathecommandnode. Then
an interaction with it looks as depicted in fig.8.2: The text after>is input from the user;
everything else is output from Node.js.

```
Figure 8.2:Starting and using the Node.js REPL (interactive command line).
```
```
Reading: REPL interactions
IoccasionallydemonstrateJavaScriptviaREPLinteractions. ThenIalsousegreater-
than symbols (>) to mark input – for example:
> 3 + 5
8
```
## 8.1.3 Other options

```
Other options include:
```
- TherearemanywebappsthatletyouexperimentwithJavaScriptinwebbrowsers
    - for example,Babel’s REPL.
- There are also native apps and IDE plugins for running JavaScript.

```
Consoles often run in non-strict mode
In modern JavaScript, most code (e.g., modules) is executed instrict mode. How-
ever, consoles often run in non-strict mode. Therefore, you may occasionally get
slightly different results when using a console to execute code from this book.
```
**8.2 Theconsole.*API: printing data and more**

```
In browsers, the console is something you can bring up that is normally hidden. For
Node.js, the console is the terminal that Node.js is currently running in.
```

```
58 8 Consoles: interactive JavaScript command lines
```
Thefullconsole.*APIisdocumentedonMDNwebdocsandontheNode.jswebsite. It
is not part of the JavaScript language standard, but much functionality is supported by
both browsers and Node.js.
In this chapter, we only look at the following two methods for printing data (“printing”
means displaying in the console):

- console.log()
- console.error()

## 8.2.1 Printing values:console.log()(stdout)

There are two variants of this operation:

```
console .log(...values:any[]):void
console .log(pattern:string,...values:any[]):void
```
```
8.2.1.1 Printing multiple values
```
The first variant prints (text representations of) values on the console:

```
console .log('abc', 123 , true );
// Output:
// abc 123 true
```
At the end,console.log()always prints a newline. Therefore, if you call it with zero
arguments, it just prints a newline.

```
8.2.1.2 Printing a string with substitutions
```
The second variant performs string substitution:

```
console .log('Test: %s %j', 123 ,'abc');
// Output:
// Test: 123 "abc"
```
These are some of the directives you can use for substitutions:

- %sconverts the corresponding value to a string and inserts it.
    **console** .log('%s %s','abc', 123 );
    // Output:
    // abc 123
- %oinserts a string representation of an object.
    **console** .log('%o',{foo: 123 ,bar:'abc'});
    // Output:
    // { foo: 123, bar: 'abc' }
- %jconverts a value to a JSON string and inserts it.
    **console** .log('%j',{foo: 123 ,bar:'abc'});
    // Output:
    // {"foo":123,"bar":"abc"}


_8.2 Theconsole.*API: printing data and more_ 59

- %%inserts a single%.
    **console** .log('%s%%', 99 );
    // Output:
    // 99%

## 8.2.2 Printing error information:console.error()(stderr)

console.error()worksthesameasconsole.log(),butwhatitlogsisconsiderederror
information. For Node.js, that means that the output goes to stderr instead of stdout on
Unix.

## 8.2.3 Printing nested objects viaJSON.stringify()

JSON.stringify()is occasionally useful for printing nested objects:

```
console .log( JSON .stringify({first:'Jane',last:'Doe'}, null , 2 ));
```
Output:

```
{
"first": "Jane",
"last": "Doe"
}
```

60 _8 Consoles: interactive JavaScript command lines_


**Chapter 9**

**Assertion API**

## Contents

```
9.1 Assertions in software development.................. 61
9.2 How assertions are used in this book.................. 61
9.2.1 Documenting results in code examples via assertions..... 62
9.2.2 Implementing test-driven exercises via assertions....... 62
9.3 Normal comparison vs. deep comparison............... 62
9.4 Quick reference: moduleassert.................... 63
9.4.1 Normal equality.......................... 63
9.4.2 Deep equality........................... 63
9.4.3 Expecting exceptions....................... 63
9.4.4 Another tool function....................... 64
```
**9.1 Assertions in software development**

```
In software development, assertions state facts about values or pieces of code that must
betrue. Iftheyaren’t,anexceptionisthrown. Node.jssupportsassertionsviaitsbuilt-in
moduleassert– for example:
```
```
import *asassertfrom'assert/strict';
assert.equal( 3 + 5 , 8 );
```
This assertion states that the expected result of 3 plus 5 is 8. The import statement uses
the recommendedstrictversionofassert.

**9.2 How assertions are used in this book**

```
Inthisbook,assertionsareusedintwoways: todocumentresultsincodeexamplesand
to implement test-driven exercises.
```
```
61
```

```
62 9 Assertion API
```
## 9.2.1 Documenting results in code examples via assertions

```
In code examples, assertions express expected results. Take, for example, the following
function:
```
```
function id(x) {
return x;
}
```
```
id()returns its parameter. We can show it in action via an assertion:
assert.equal(id('abc'),'abc');
```
```
In the examples, I usually omit the statement for importingassert.
```
The motivation behind using assertions is:

- You can specify precisely what is expected.
- Code examples can be tested automatically, which ensures that they really work.

## 9.2.2 Implementing test-driven exercises via assertions

Theexercisesforthisbookaretest-driven,viathetestframeworkMocha. Checksinside
the tests are made via methods ofassert.

The following is an example of such a test:

```
// For the exercise, you must implement the function hello().
// The test checks if you have done it properly.
test('First exercise',() => {
assert.equal(hello('world'),'Hello world!');
assert.equal(hello('Jane'),'Hello Jane!');
assert.equal(hello('John'),'Hello John!');
assert.equal(hello(''),'Hello !');
});
```
```
For more information, consult§10 “Getting started with quizzes and exercises”.
```
**9.3 Normal comparison vs. deep comparison**

Thestrictequal()uses===tocomparevalues. Therefore,anobjectisonlyequaltoitself
–evenifanotherobjecthasthesamecontent(because===doesnotcomparethecontents
of objects, only their identities):
assert.notEqual({foo: 1 },{foo: 1 });

```
deepEqual()is a better choice for comparing objects:
```
```
assert.deepEqual({foo: 1 },{foo: 1 });
```
This method works for Arrays, too:

```
assert.notEqual(['a','b','c'],['a','b','c']);
assert.deepEqual(['a','b','c'],['a','b','c']);
```

```
9.4 Quick reference: moduleassert 63
```
**9.4 Quick reference: moduleassert**

```
For the full documentation, seethe Node.js docs.
```
## 9.4.1 Normal equality

- function equal(actual: any, expected: any, message?: string): void
    actual === expectedmust betrue. If not, anAssertionErroris thrown.
       assert.equal( 3 + 3 , 6 );
- function notEqual(actual: any, expected: any, message?: string): void
    actual !== expectedmust betrue. If not, anAssertionErroris thrown.
       assert.notEqual( 3 + 3 , 22 );

Theoptionallastparametermessagecanbeusedtoexplainwhatisasserted. Iftheasser-
tion fails, the message is used to set up theAssertionErrorthat is thrown.
**let** e;
**try** {
**const** x= 3 ;
assert.equal(x, 8 ,'x must be equal to 8')
} **catch** (err) {
assert.equal(
**String** (err),
'AssertionError [ERR_ASSERTION]: x must be equal to 8');
}

## 9.4.2 Deep equality

- function deepEqual(actual: any, expected: any, message?: string): void
    actualmust be deeply equal toexpected. If not, anAssertionErroris thrown.
       assert.deepEqual([ 1 , 2 , 3 ],[ 1 , 2 , 3 ]);
       assert.deepEqual([],[]);

```
// To .equal(), an object is only equal to itself:
assert.notEqual([],[]);
```
- function notDeepEqual(actual: any, expected: any, message?: string):
    void
    actualmustnotbedeeplyequaltoexpected. Ifitis,anAssertionErroristhrown.
       assert.notDeepEqual([ 1 , 2 , 3 ],[ 1 , 2 ]);

## 9.4.3 Expecting exceptions

If you want to (or expect to) receive an exception, you needthrows(): This function
calls its first parameter, the functionblock, and only succeeds if it throws an exception.
Additional parameters can be used to specify what that exception must look like.


64 _9 Assertion API_

- function throws(block: Function, message?: string): void
    assert.throws(
       () **=>** {
          **null** .prop;
       }
    );
- function throws(block: Function, error: Function, message?: string):
    void

```
assert.throws(
() => {
null .prop;
},
TypeError
);
```
- function throws(block: Function, error: RegExp, message?: string): void

```
assert.throws(
() => {
null .prop;
},
/^TypeError: Cannot read properties of null\(reading 'prop'\)$/
);
```
- function throws(block: Function, error: Object, message?: string): void

```
assert.throws(
() => {
null .prop;
},
{
name:'TypeError',
message:"Cannot read properties of null (reading 'prop')",
}
);
```
## 9.4.4 Another tool function

- function fail(message: string | Error): never

```
Always throws anAssertionErrorwhen it is called. That is occasionally useful
for unit testing.
```
```
try {
functionThatShouldThrow();
assert.fail();
} catch (_) {
// Success
}
```

_9.4 Quick reference: moduleassert_ 65

```
Quiz
Seequiz app.
```

66 _9 Assertion API_


**Chapter 10**

**Getting started with quizzes and**

**exercises**

## Contents

```
10.1 Quizzes.................................. 67
10.2 Exercises................................. 67
10.2.1 Installing the exercises...................... 67
10.2.2 Running exercises......................... 68
10.3 Unit tests in JavaScript.......................... 68
10.3.1 A typical test........................... 68
10.3.2 Asynchronous tests in Mocha.................. 69
```
Throughoutmostchapters,therearequizzesandexercises. Theseareapaidfeature,but
a comprehensive preview is available. This chapter explains how to get started with
them.

**10.1 Quizzes**

```
Installation:
```
- Download and unzipimpatient-js-quiz.zip
Running the quiz app:
- Openimpatient-js-quiz/index.htmlin a web browser
- You’ll see a TOC of all the quizzes.

**10.2 Exercises**

## 10.2.1 Installing the exercises

To install the exercises:

```
67
```

```
68 10 Getting started with quizzes and exercises
```
- Download and unzipimpatient-js-code.zip
- Follow the instructions inREADME.txt

## 10.2.2 Running exercises

- Exercises are referred to by path in this book.
    **-** For example:exercises/quizzes-exercises/first_module_test.mjs
- Within each file:
    **-** The first line contains the command for running the exercise.
    **-** The following lines describe what you have to do.

**10.3 Unit tests in JavaScript**

AllexercisesinthisbookareteststhatarerunviathetestframeworkMocha. Thissection
gives a brief introduction.

## 10.3.1 A typical test

Typical test code is split into two parts:

- Part 1: the code to be tested.
- Part 2: the tests for the code.

Take, for example, the following two files:

- id.mjs(code to be tested)
- id_test.mjs(tests)

```
10.3.1.1 Part 1: the code
```
The code itself resides inid.mjs:

```
export function id(x) {
return x;
}
```
The key thing here is: everything we want to test must be exported. Otherwise, the test
code can’t access it.

```
10.3.1.2 Part 2: the tests
```
```
Don’t worry about the exact details of tests
You don’t need to worry about the exact details of tests: They are always imple-
mented for you. Therefore, you only need to read them, but not write them.
```
The tests for the code reside inid_test.mjs:

```
// npm t demos/quizzes-exercises/id_test.mjs
suite('id_test.mjs');
```

```
10.3 Unit tests in JavaScript 69
```
```
import *asassertfrom'assert/strict';// (A)
import {id}from'./id.mjs';// (B)
```
```
test('My test',() => {// (C)
assert.equal(id('abc'),'abc');// (D)
});
```
The core of this test file is line D –an assertion:assert.equal()specifies that the ex-
pected result ofid('abc')is'abc'.

As for the other lines:

- Thecommentattheverybeginningshowstheshellcommandforrunningthetest.
- Line A: We import the Node.js assertion library (in _strict assertion mode_ ).
- Line B: We import the function to test.
- Line C: We define a test. This is done by calling the functiontest():
    **-** First parameter: the name of the test.
    **-** Second parameter: the test code, which is provided via an arrow function.
       The parametertgives us access to AVA’s testing API (assertions, etc.).

To run the test, we execute the following in a command line:

```
npm t demos/quizzes-exercises/id_test.mjs
```
Thetis an abbreviation fortest. That is, the long version of this command is:

```
npm test demos/quizzes-exercises/id_test.mjs
```
```
Exercise: Your first exercise
The following exercise gives you a first taste of what exercises are like:
```
- exercises/quizzes-exercises/first_module_test.mjs

## 10.3.2 Asynchronous tests in Mocha

```
Reading
You may want to postpone reading this section until you get to the chapters on
asynchronous programming.
```
Writing tests for asynchronous code requires extra work: The test receives its results
later and has to signal to Mocha that it isn’t finished yet when it returns. The following
subsections examine three ways of doing so.

```
10.3.2.1 Asynchronicity via callbacks
```
```
Ifthecallbackwepasstotest()hasaparameter(e.g.,done),Mochaswitchestocallback-
based asynchronicity. When we are done with our asynchronous work, we have to call
done:
```

```
70 10 Getting started with quizzes and exercises
```
```
test('divideCallback',(done) => {
divideCallback( 8 , 4 ,(error,result) => {
if (error) {
done(error);
} else {
assert.strictEqual(result, 2 );
done();
}
});
});
```
This is whatdivideCallback()looks like:

```
function divideCallback(x,y,callback) {
if (y=== 0 ) {
callback( newError ('Division by zero'));
} else {
callback( null ,x/y);
}
}
```
```
10.3.2.2 Asynchronicity via Promises
If a test returns a Promise, Mocha switches to Promise-based asynchronicity. A test is
considered successful if the Promise is fulfilled and failed if the Promise is rejected or if
a settlement takes longer than a timeout.
```
```
test('dividePromise 1',() => {
return dividePromise( 8 , 4 )
.then(result => {
assert.strictEqual(result, 2 );
});
});
dividePromise()is implemented as follows:
function dividePromise(x,y) {
returnnewPromise ((resolve,reject) => {
if (y=== 0 ) {
reject( newError ('Division by zero'));
} else {
resolve(x/y);
}
});
}
```
```
10.3.2.3 Async functions as test “bodies”
```
Async functions always return Promises. Therefore, an async function is a convenient
wayofimplementinganasynchronoustest. Thefollowingcodeisequivalenttothepre-
vious example.


```
10.3 Unit tests in JavaScript 71
```
```
test('dividePromise 2', async () => {
const result= await dividePromise( 8 , 4 );
assert.strictEqual(result, 2 );
// No explicit return necessary!
});
```
We don’t need to explicitly return anything: The implicitly returnedundefinedis used
to fulfill the Promise returned by this async function. And if the test code throws an
exception, then the async function takes care of rejecting the returned Promise.


72 _10 Getting started with quizzes and exercises_


**Part III**

**Variables and values**

```
73
```


**Chapter 11**

**Variables and assignment**

## Contents

```
11.1let..................................... 76
11.2const................................... 76
11.2.1 constand immutability..................... 76
11.2.2 constand loops.......................... 77
11.3 Deciding betweenconstandlet.................... 77
11.4 The scope of a variable.......................... 77
11.4.1 Shadowing variables....................... 78
11.5 (Advanced)................................ 79
11.6 Terminology: static vs. dynamic.................... 79
11.6.1 Static phenomenon: scopes of variables............. 79
11.6.2 Dynamic phenomenon: function calls.............. 79
11.7 Global variables and the global object................. 80
11.7.1 globalThis[ES2020]....................... 80
11.8 Declarations: scope and activation................... 82
11.8.1 constandlet: temporal dead zone............... 82
11.8.2 Function declarations and early activation........... 83
11.8.3 Class declarations are not activated early............ 85
11.8.4 var: hoisting (partial early activation).............. 85
11.9 Closures.................................. 86
11.9.1 Bound variables vs. free variables................ 86
11.9.2 What is a closure?......................... 86
11.9.3 Example: A factory for incrementors.............. 87
11.9.4 Use cases for closures....................... 88
```
These are JavaScript’s main ways of declaring variables:

- letdeclares mutable variables.
- constdeclares _constants_ (immutable variables).
BeforeES6,therewasalsovar. Butithasseveralquirks,soit’sbesttoavoiditinmodern
JavaScript. You can read more about it in _Speaking JavaScript_.

```
75
```

```
76 11 Variables and assignment
```
**11.1 let**

Variables declared vialetare mutable:

```
let i;
i= 0 ;
i=i+ 1 ;
assert.equal(i, 1 );
```
You can also declare and assign at the same time:

```
let i= 0 ;
```
**11.2 const**

Variables declared viaconstare immutable. You must always initialize immediately:

```
const i= 0 ;// must initialize
```
```
assert.throws(
() => { i=i+ 1 },
{
name:'TypeError',
message:'Assignment to constant variable.',
}
);
```
## 11.2.1 constand immutability

InJavaScript,constonlymeansthatthe _binding_ (theassociationbetweenvariablename
and variable value) is immutable. The value itself may be mutable, likeobjin the fol-
lowing example.

```
const obj={prop: 0 };
```
```
// Allowed: changing properties of `obj`
obj.prop=obj.prop+ 1 ;
assert.equal(obj.prop, 1 );
```
```
// Not allowed: assigning to `obj`
assert.throws(
() => { obj={} },
{
name:'TypeError',
message:'Assignment to constant variable.',
}
);
```

```
11.3 Deciding betweenconstandlet 77
```
## 11.2.2 constand loops

Youcanuseconstwithfor-ofloops,whereafreshbindingiscreatedforeachiteration:

```
const arr=['hello','world'];
for ( const elem of arr) {
console .log(elem);
}
// Output:
// 'hello'
// 'world'
In plainforloops, you must uselet, however:
```
```
const arr=['hello','world'];
for ( let i= 0 ;i<arr.length;i++) {
const elem=arr[i];
console .log(elem);
}
```
**11.3 Deciding betweenconstandlet**

```
I recommend the following rules to decide betweenconstandlet:
```
- constindicatesanimmutablebindingandthatavariableneverchangesitsvalue.
    Prefer it.
- letindicates that the value of a variable changes. Use it only when you can’t use
    const.

```
Exercise:const
exercises/variables-assignment/const_exrc.mjs
```
**11.4 The scope of a variable**

The _scope_ ofa variable is the region ofa program whereit can be accessed. Consider the
following code.

```
{// // Scope A. Accessible: x
const x= 0 ;
assert.equal(x, 0 );
{// Scope B. Accessible: x, y
const y= 1 ;
assert.equal(x, 0 );
assert.equal(y, 1 );
{// Scope C. Accessible: x, y, z
const z= 2 ;
assert.equal(x, 0 );
assert.equal(y, 1 );
```

```
78 11 Variables and assignment
```
```
assert.equal(z, 2 );
}
}
}
// Outside. Not accessible: x, y, z
assert.throws(
() =>console .log(x),
{
name:'ReferenceError',
message:'x is not defined',
}
);
```
- Scope A is the _(direct) scope_ ofx.
- Scopes B and C are _inner scopes_ of scope A.
- Scope A is an _outer scope_ of scope B and scope C.

```
Each variable is accessible in its direct scope and all scopes nested within that scope.
```
The variables declared viaconstandletarecalled _block-scoped_ because theirscopesare
always the innermost surrounding blocks.

## 11.4.1 Shadowing variables

You can’t declare the same variable twice at the same level:

```
assert.throws(
() => {
eval('let x = 1; let x = 2;');
},
{
name:'SyntaxError',
message:"Identifier 'x' has already been declared",
});
```
```
Whyeval()?
eval()delays parsing (and therefore theSyntaxError), until the callback ofas-
sert.throws()isexecuted. Ifwedidn’tuseit,we’dalreadygetanerrorwhenthis
code is parsed andassert.throws()wouldn’t even be executed.
```
You can, however, nest a block and use the same variable namexthat you used outside
the block:

```
const x= 1 ;
assert.equal(x, 1 );
{
const x= 2 ;
assert.equal(x, 2 );
```

```
11.5 (Advanced) 79
```
### }

```
assert.equal(x, 1 );
```
```
Insidetheblock,theinnerxistheonlyaccessiblevariablewiththatname. Theinnerxis
said to shadow the outerx. Once you leave the block, you can access the old value again.
```
```
Quiz: basic
Seequiz app.
```
**11.5 (Advanced)**

All remaining sections are advanced.

**11.6 Terminology: static vs. dynamic**

These two adjectives describe phenomena in programming languages:

- _Static_ meansthatsomethingisrelatedtosourcecodeandcanbedeterminedwith-
    out executing code.
- _Dynamic_ means at runtime.

```
Let’s look at examples for these two terms.
```
## 11.6.1 Static phenomenon: scopes of variables

Variable scopes are a static phenomenon. Consider the following code:

```
function f() {
const x= 3 ;
// ···
}
```
```
xis statically (or lexically ) scoped. Thatis,itsscopeisfixedanddoesn’tchangeatruntime.
```
Variable scopes form a static tree (via static nesting).

## 11.6.2 Dynamic phenomenon: function calls

```
Function calls are a dynamic phenomenon. Consider the following code:
```
```
function g(x) {}
function h(y) {
if ( Math .random())g(y);// (A)
}
```
Whether or not the function call in line A happens, can only be decided at runtime.

```
Function calls form a dynamic tree (via dynamic calls).
```

```
80 11 Variables and assignment
```
**11.7 Global variables and the global object**

JavaScript’s variable scopes are nested. They form a tree:

- The outermost scope is the root of the tree.
- The scopes directly contained in that scope are the children of the root.
- And so on.

The root is also called the _global scope_. In web browsers, the only location where one is
directly in that scope is at the top level of a script. The variables of the global scope are
called _globalvariables_ andaccessibleeverywhere. Therearetwokindsofglobalvariables:

- _Global declarative variables_ are normal variables.
    **-** Theycanonlybecreatedwhileatthetoplevelofascript,viaconst,let,and
       class declarations.
- _Global object variables_ are stored in properties of the so-called _global object_.
    **-** Theyarecreatedinthetoplevelofascript,viavarandfunctiondeclarations.
    **-** The global object can be accessed via the global variableglobalThis. It can
       be used to create, read, and delete global object variables.
    **-** Other than that, global object variables work like normal variables.

The following HTML fragment demonstratesglobalThisand the two kinds of global
variables.

```
<script>
const declarativeVariable='d';
var objectVariable='o';
</script>
<script>
// All scripts share the same top-level scope:
console .log(declarativeVariable);// 'd'
console .log(objectVariable);// 'o'
```
```
// Not all declarations create properties of the global object:
console .log(globalThis.declarativeVariable);// undefined
console .log(globalThis.objectVariable);// 'o'
</script>
```
```
Each ECMAScript module has its own scope. Therefore, variables that exist at the top
level of a module are not global. Fig.11.1illustrates how the various scopes are related.
```
## 11.7.1 globalThis[ES2020]

The global variableglobalThisis the new standard way of accessing the global object.
It got its name from the fact that it has the same value asthisin global scope.

```
globalThisdoes not always directly point to the global object
For example, in browsers,there is an indirection. That indirection is normally not
noticable, but it is there and can be observed.
```

```
11.7 Global variables and the global object 81
```
```
Object variables
```
```
Global scope
```
Module scope 1 ···

```
Declarative variables
```
```
Top level of scripts:
```
```
var, function declarations
```
```
const, let, class declarations
```
```
Module scope 2
```
```
Figure 11.1:The global scope is JavaScript’s outermost scope. It has two kinds of vari-
ables: objectvariables (managedviathe globalobject )andnormal declarative variables. Each
ECMAScript module has its own scope which is contained in the global scope.
```
```
11.7.1.1 Alternatives toglobalThis
Older ways of accessing the global object depend on the platform:
```
- Global variablewindow: is the classic way of referring to the global object. But it
    doesn’t work in Node.js and in Web Workers.
- Global variableself: is available in Web Workers and browsers in general. But it
    isn’t supported by Node.js.
- Global variableglobal: is only available in Node.js.

```
11.7.1.2 Use cases forglobalThis
```
The global object is now considered a mistake that JavaScript can’t get rid of, due to
backward compatibility. It affects performance negatively and is generally confusing.
ECMAScript 6 introduced several features that make it easier to avoid the global object

- for example:
    - const,let,andclassdeclarationsdon’tcreateglobalobjectpropertieswhenused
       in global scope.
    - Each ECMAScript module has its own local scope.
It is usually better to access global object variables via variables and not via properties
ofglobalThis. The former has always worked the same on all JavaScript platforms.

Tutorials on the web occasionally access global variablesglobVarviawindow.globVar.
But the prefix “window.” is not necessary and I recommend to omit it:
**window** .encodeURIComponent(str);// no
encodeURIComponent(str);// yes

Therefore, there are relatively few use cases forglobalThis– for example:


```
82 11 Variables and assignment
```
- _Polyfills_ that add new features to old JavaScript engines.
- Feature detection, to find out what features a JavaScript engine supports.

**11.8 Declarations: scope and activation**

These are two key aspects of declarations:

- Scope: Where can a declared entity be seen? This is a static trait.
- Activation: When can I access an entity? This is a dynamic trait. Some entities
    canbeaccessedassoonasweentertheirscopes. Forothers,wehavetowaituntil
    execution reaches their declarations.

Tbl.11.1summarizes how various declarations handle these aspects.

```
Table 11.1: Aspects of declarations. “Duplicates” describes if a declara-
tion can be used twice with the same name (per scope). “Global prop.”
describesifadeclarationaddsapropertytotheglobalobject,whenitis
executed in the global scope of a script. TDZ means temporal dead zone
(which is explained later). (*) Function declarations are normally block-
scoped, but function-scoped insloppy mode.
```
```
Scope Activation Duplicates Global prop.
const Block decl. (TDZ) ✘ ✘
let Block decl. (TDZ) ✘ ✘
function Block (*) start ✔ ✔
class Block decl. (TDZ) ✘ ✘
import Module same as export ✘ ✘
var Function start, partially ✔ ✔
```
```
importis described in§27.5 “ECMAScript modules”. The following sections describe
the other constructs in more detail.
```
## 11.8.1 constandlet: temporal dead zone

ForJavaScript,TC39neededtodecidewhathappensifyouaccessaconstantinitsdirect
scope, before its declaration:

```
{
console .log(x);// What happens here?
const x;
}
```
```
Some possible approaches are:
```
```
1.The name is resolved in the scope surrounding the current scope.
2.You getundefined.
3.There is an error.
```

```
11.8 Declarations: scope and activation 83
```
Approach1wasrejectedbecausethereisnoprecedentinthelanguageforthisapproach.
It would therefore not be intuitive to JavaScript programmers.

Approach2wasrejectedbecausethenxwouldn’tbeaconstant–itwouldhavedifferent
values before and after its declaration.

```
letusesthesameapproach3asconst,sothatbothworksimilarlyandit’seasytoswitch
between them.
```
Thetimebetweenenteringthescopeofavariableandexecutingitsdeclarationiscalled
the _temporal dead zone_ (TDZ) of that variable:

- During this time, the variable is considered to be uninitialized (as if that were a
    special value it has).
- If you access an uninitialized variable, you get aReferenceError.
- Once you reach a variable declaration, the variable is set to either the value of
    the initializer (specified via the assignment symbol) orundefined– if there is no
    initializer.

The following code illustrates the temporal dead zone:

```
if ( true ) {// entering scope of `tmp`, TDZ starts
// `tmp` is uninitialized:
assert.throws(() => (tmp='abc'), ReferenceError );
assert.throws(() =>console .log(tmp), ReferenceError );
```
```
let tmp;// TDZ ends
assert.equal(tmp, undefined );
}
```
The next example shows that the temporal dead zone is truly _temporal_ (related to time):

```
if ( true ) {// entering scope of `myVar`, TDZ starts
const func=() => {
console .log(myVar);// executed later
};
```
```
// We are within the TDZ:
// Accessing `myVar` causes `ReferenceError`
```
```
let myVar= 3 ;// TDZ ends
func();// OK, called outside TDZ
}
Eventhoughfunc()islocatedbeforethedeclarationofmyVarandusesthatvariable,we
can callfunc(). But we have to wait until the temporal dead zone ofmyVaris over.
```
## 11.8.2 Function declarations and early activation

```
More information on functions
```

```
84 11 Variables and assignment
```
```
Inthissection,weareusingfunctions–beforewehadachancetolearnthemprop-
erly. Hopefully, everything still makes sense. Whenever it doesn’t, please see§25
“Callable values”.
```
Afunctiondeclarationisalwaysexecutedwhenenteringitsscope,regardlessofwhereit
islocatedwithinthatscope. Thatenablesyoutocallafunctionfoo()beforeitisdeclared:
assert.equal(foo(), 123 );// OK
**function** foo() { **return** 123 ;}

The early activation offoo()means that the previous code is equivalent to:

```
function foo() { return 123 ;}
assert.equal(foo(), 123 );
If you declare a function viaconstorlet, then it is not activated early. In the following
example, you can only usebar()after its declaration.
assert.throws(
() => bar(),// before declaration
ReferenceError );
```
```
const bar=() => { return 123 ;};
```
```
assert.equal(bar(), 123 );// after declaration
```
```
11.8.2.1 Calling ahead without early activation
```
Even if a functiong()is not activated early, it can be called by a preceding functionf()
(in the same scope) if we adhere to the following rule:f()must be invoked after the
declaration ofg().

```
const f=() => g();
const g=() => 123 ;
```
```
// We call f() after g() was declared:
assert.equal(f(), 123 );
```
Thefunctionsofamoduleareusuallyinvokedafteritscompletebodyisexecuted. There-
fore, in modules, you rarely need to worry about the order of functions.
Lastly, note how early activation automatically keeps the aforementioned rule: when
entering a scope, all function declarations are executed first, before any calls are made.

```
11.8.2.2 A pitfall of early activation
```
```
If you rely on early activation to call a function before its declaration, then you need to
be careful that it doesn’t access data that isn’t activated early.
funcDecl();
```
```
const MY_STR='abc';
function funcDecl() {
```

```
11.8 Declarations: scope and activation 85
```
```
assert.throws(
() => MY_STR,
ReferenceError );
}
```
The problem goes away if you make the call tofuncDecl()after the declaration ofMY_-
STR.

```
11.8.2.3 The pros and cons of early activation
```
We have seen that early activation has a pitfall and that you can get most of its benefits
withoutusingit. Therefore,itisbettertoavoidearlyactivation. ButIdon’tfeelstrongly
about this and, as mentioned before, often use function declarations because I like their
syntax.

## 11.8.3 Class declarations are not activated early

```
Even though they are similar to function declarations in some ways,class declarations
are not activated early:
assert.throws(
() =>new MyClass(),
ReferenceError );
```
```
class MyClass {}
```
```
assert.equal( new MyClass() instanceof MyClass, true );
```
Why is that? Consider the following class declaration:

```
class MyClass extendsObject {}
```
The operand ofextendsis an expression. Therefore, you can do things like this:

```
const identity=x => x;
class MyClass extends identity( Object ) {}
Evaluatingsuchanexpressionmustbedoneatthelocationwhereitismentioned. Any-
thing else would be confusing. That explains why class declarations are not activated
early.
```
## 11.8.4 var: hoisting (partial early activation)

```
varis an older way of declaring variables that predatesconstandlet(which are pre-
ferred now). Consider the followingvardeclaration.
var x= 123 ;
```
This declaration has two parts:

- Declarationvar x: Thescopeofavar-declaredvariableistheinnermostsurround-
    ing function and not the innermost surrounding block, as for most other declara-
    tions. Suchavariableisalreadyactiveatthebeginningofitsscopeandinitialized
withundefined.


```
86 11 Variables and assignment
```
- Assignmentx = 123: The assignment is always executed in place.

The following code demonstrates the effects ofvar:

```
function f() {
// Partial early activation:
assert.equal(x, undefined );
if ( true ) {
var x= 123 ;
// The assignment is executed in place:
assert.equal(x, 123 );
}
// Scope is function, not block:
assert.equal(x, 123 );
}
```
**11.9 Closures**

```
Before we can explore closures, we need to learn about bound variables and free vari-
ables.
```
## 11.9.1 Bound variables vs. free variables

```
Per scope, there is a set of variables that are mentioned. Among these variables we dis-
tinguish:
```
- _Bound variables_ are declared within the scope. They are parameters and local vari-
    ables.
- _Free variables_ are declared externally. They are also called _non-local variables_.
Consider the following code:

```
function func(x) {
const y= 123 ;
console .log(z);
}
```
```
In the body offunc(),xandyare bound variables.zis a free variable.
```
## 11.9.2 What is a closure?

What is a closure then?

```
A closure isafunctionplusaconnectiontothevariablesthatexistatits“birth
place”.
```
Whatisthepointofkeepingthisconnection? Itprovidesthevaluesforthefreevariables
of the function – for example:

```
function funcFactory(value) {
return () => {
return value;
```

```
11.9 Closures 87
```
### };

### }

```
const func=funcFactory('abc');
assert.equal(func(),'abc');// (A)
```
```
funcFactoryreturnsaclosurethatisassignedtofunc. Becausefunchastheconnection
tothevariablesatitsbirthplace,itcanstillaccessthefreevariablevaluewhenitiscalled
in line A (even though it “escaped” its scope).
```
```
All functions in JavaScript are closures
Static scoping is supported via closures in JavaScript. Therefore, every function is
a closure.
```
## 11.9.3 Example: A factory for incrementors

Thefollowingfunctionreturns _incrementors_ (anamethatIjustmadeup). Anincrementor
is a function that internally stores a number. When it is called, it updates that number
by adding the argument to it and returns the new value.

```
function createInc(startValue) {
return (step) => {// (A)
startValue+= step;
return startValue;
};
}
const inc=createInc( 5 );
assert.equal(inc( 2 ), 7 );
```
WecanseethatthefunctioncreatedinlineAkeepsitsinternalnumberinthefreevariable
startValue. This time, we don’t just read from the birth scope, we use it to store data
that we change and that persists across function calls.

We can create more storage slots in the birth scope, via local variables:

```
function createInc(startValue) {
let index=- 1 ;
return (step) => {
startValue+= step;
index++;
return [index,startValue];
};
}
const inc=createInc( 5 );
assert.deepEqual(inc( 2 ),[ 0 , 7 ]);
assert.deepEqual(inc( 2 ),[ 1 , 9 ]);
assert.deepEqual(inc( 2 ),[ 2 , 11 ]);
```

```
88 11 Variables and assignment
```
## 22.3 Use cases for symbols.

What are closures good for?

- For starters, they are simply an implementation of static scoping. As such, they
    provide context data for callbacks.
- Theycanalsobeusedbyfunctionstostorestatethatpersistsacrossfunctioncalls.
    createInc()is an example of that.
- And they can provide private data for objects (produced via literals or classes).
    The details of how that works are explained in _Exploring ES6_.

```
Quiz: advanced
Seequiz app.
```

**Chapter 12**

**Values**

## Contents

```
12.1 What’s a type?.............................. 89
12.2 JavaScript’s type hierarchy....................... 90
12.3 The types of the language specification................ 90
12.4 Primitive values vs. objects....................... 91
12.4.1 Primitive values (short: primitives)............... 91
12.4.2 Objects............................... 92
12.5 The operatorstypeofandinstanceof: what’s the type of a value?. 94
12.5.1typeof............................... 94
12.5.2instanceof............................ 95
12.6 Classes and constructor functions................... 95
12.6.1 Constructor functions associated with primitive types..... 96
12.7 Converting between types........................ 96
12.7.1 Explicit conversion between types................ 97
12.7.2 Coercion (automatic conversion between types)........ 97
```
In this chapter, we’ll examine what kinds of values JavaScript has.

```
Supporting tool:===
Inthischapter,we’lloccasionallyusethestrictequalityoperator.a === bevaluates
totrueifaandbareequal. Whatexactlythatmeansisexplainedin§13.4.2“Strict
equality (===and!==)”.
```
**12.1 What’s a type?**

For this chapter, I consider types to be sets of values – for example, the typebooleanis
the set {false,true}.

```
89
```

```
90 12 Values
```
**12.2 JavaScript’s type hierarchy**

```
(any)
```
```
(primitive value) (object)
```
```
boolean
```
```
number
```
```
string
```
```
symbol
```
```
undefined
```
```
null
```
```
Object
```
```
Array
```
```
Map
```
```
Set
```
```
Function
```
```
RegExp
```
```
Date
```
```
Figure 12.1:A partial hierarchy of JavaScript’s types. Missing are the classes for errors,
theclassesassociatedwithprimitivetypes,andmore. Thediagramhintsatthefactthat
not all objects are instances ofObject.
```
```
Fig.12.1shows JavaScript’s type hierarchy. What do we learn from that diagram?
```
- JavaScript distinguishes two kinds of values: primitive values and objects. We’ll
    see soon what the difference is.
- The diagram differentiates objects and instances of classObject. Each instance
    ofObjectis also an object, but not vice versa. However, virtually all objects that
    you’ll encounter in practice are instances ofObject– for example, objects created
    viaobjectliterals. Moredetailsonthistopicareexplainedin§29.7.3“Notallobjects
    are instances ofObject”.

**12.3 The types of the language specification**

The ECMAScript specification only knows a total of eight types. The names of those
types are (I’m using TypeScript’s names, not the spec’s names):

- undefinedwith the only elementundefined
- nullwith the only elementnull
- booleanwith the elementsfalseandtrue
- numberthe type of all numbers (e.g.,-123,3.141)
- bigintthe type of all big integers (e.g.,-123n)
- stringthe type of all strings (e.g.,'abc')
- symbolthe type of all symbols (e.g.,Symbol('My Symbol'))
- objectthe type of all objects (different fromObject, the type of all instances of
    classObjectand its subclasses)


```
12.4 Primitive values vs. objects 91
```
**12.4 Primitive values vs. objects**

The specification makes an important distinction between values:

- _Primitive values_ are the elements of the typesundefined,null,boolean,number,
    bigint,string,symbol.
- All other values are _objects_.
In contrast to Java (that inspired JavaScript here), primitive values are not second-class
citizens. The difference between them and objects is more subtle. In a nutshell:
- Primitive values: are atomic building blocks of data in JavaScript.
**-** They are _passed by value_ : when primitive values are assigned to variables or
passed to functions, their contents are copied.
**-** Theyare _compared by value_ : whencomparingtwoprimitivevalues,theircon-
tents are compared.
- Objects: are compound pieces of data.
**-** They are _passed by identity_ (my term): when objects are assigned to variables
or passed to functions, their _identities_ (think pointers) are copied.
**-** They are _compared by identity_ (my term): when comparing two objects, their
identities are compared.
Other than that, primitive values and objects are quite similar: they both have _properties_
(key-value entries) and can be used in the same locations.

```
Next, we’ll look at primitive values and objects in more depth.
```
## 12.4.1 Primitive values (short: primitives)

```
12.4.1.1 Primitives are immutable
```
You can’t change, add, or remove properties of primitives:

```
const str='abc';
assert.equal(str.length, 3 );
assert.throws(
() => { str.length= 1 },
/^TypeError: Cannot assign to read only property 'length'/
);
```
```
12.4.1.2 Primitives are passed by value
Primitives are passed by value : variables (including parameters) store the contents of the
primitives. When assigning a primitive value to a variable or passing it as an argument
to a function, its content is copied.
const x= 123 ;
const y=x;
// `y` is the same as any other number 123
assert.equal(y, 123 );
```

```
92 12 Values
```
```
Observingthedifferencebetweenpassingbyvalueandpassingbyrefer-
ence
Due to primitive values being immutable and compared by value (see next sub-
section), there is no way to observe the difference between passing by value and
passing by identity (as used for objects in JavaScript).
```
```
12.4.1.3 Primitives are compared by value
Primitives are compared by value : when comparing two primitive values, we compare
their contents.
assert.equal( 123 === 123 , true );
assert.equal('abc'==='abc', true );
```
To see what’s so special about this way of comparing, read on and find out how objects
are compared.

## 28 Objects

Objectsarecoveredindetailin§28“Objects”andthefollowingchapter. Here,wemainly
focus on how they differ from primitive values.
Let’s first explore two common ways of creating objects:

- Object literal:
    **const** obj={
       first:'Jane',
       last:'Doe',
    };
The object literal starts and ends with curly braces{}. It creates an object with
two properties. The first property has the key'first'(a string) and the value
'Jane'. The second property has the key'last'and the value'Doe'. For more
information on object literals, consult§28.3.1 “Object literals: properties”.
- Array literal:
    **const** fruits =['strawberry','apple'];
TheArrayliteralstartsandendswithsquarebrackets[]. ItcreatesanArraywith
two _elements_ :'strawberry'and'apple'. For more information on Array literals,
consult[content not included].

```
12.4.2.1 Objects are mutable by default
```
```
By default, you can freely change, add, and remove the properties of objects:
const obj={};
```
```
obj.count= 2 ;// add a property
assert.equal(obj.count, 2 );
```

```
12.4 Primitive values vs. objects 93
```
```
obj.count= 3 ;// change a property
assert.equal(obj.count, 3 );
```
```
12.4.2.2 Objects are passed by identity
Objectsare passed by identity (myterm): variables(includingparameters)storethe identi-
ties of objects.
```
Theidentityofanobjectislikeapointer(oratransparentreference)totheobject’sactual
data on the _heap_ (think shared main memory of a JavaScript engine).

When assigning an object to a variable or passing it as an argument to a function, its
identity is copied. Each object literal creates a fresh object on the heap and returns its
identity.
**const** a={};// fresh empty object
// Pass the identity in `a` to `b`:
**const** b=a;

```
// Now `a` and `b` point to the same object
// (they “share” that object):
assert.equal(a===b, true );
```
```
// Changing `a` also changes `b`:
a.name='Tessa';
assert.equal(b.name,'Tessa');
JavaScript uses garbage collection to automatically manage memory:
```
**let** obj={prop:'value'};
obj={};
Now the old value{ prop: 'value' }ofobjis _garbage_ (not used anymore). JavaScript
willautomatically _garbage-collect_ it(removeitfrommemory),atsomepointintime(pos-
sibly never if there is enough free memory).

```
Details: passing by identity
“Passing by identity” means that the identity of an object (a transparent reference)
is passed by value. This approach is also called“passing by sharing”.
```
```
12.4.2.3 Objects are compared by identity
```
```
Objects are compared by identity (my term): two variables are only equal if they contain
thesameobjectidentity. Theyarenotequaliftheyrefertodifferentobjectswiththesame
content.
const obj={};// fresh empty object
assert.equal(obj===obj, true );// same identity
assert.equal({}==={}, false );// different identities, same content
```

```
94 12 Values
```
```
12.5 Theoperatorstypeofandinstanceof: what’sthetype
of a value?
```
The two operatorstypeofandinstanceoflet you determine what type a given valuex
has:
**if** ( **typeof** x==='string') ···
**if** (x **instanceofArray** ) ···
How do they differ?

- typeofdistinguishesthe7typesofthespecification(minusoneomission,plusone
    addition).
- instanceoftests which class created a given value.

```
Rule of thumb:typeofis for primitive values;instanceofis for objects
```
## 12.5.1 typeof

```
Table 12.1: The results of thetypeofoperator.
```
```
x typeof x
undefined 'undefined'
null 'object'
Boolean 'boolean'
Number 'number'
Bigint 'bigint'
String 'string'
Symbol 'symbol'
Function 'function'
All other objects 'object'
```
Tbl.12.1listsallresultsoftypeof. Theyroughlycorrespondtothe7typesofthelanguage
specification. Alas, there are two differences, and they are language quirks:

- typeof nullreturns'object'and not'null'. That’s a bug. Unfortunately, it
    can’t be fixed. TC39 tried to do that, but it broke too much code on the web.
- typeofof a function should be'object'(functions are objects). Introducing a
    separate category for functions is confusing.

These are a few examples of usingtypeof:

```
> typeof undefined
'undefined'
> typeof 123n
'bigint'
> typeof 'abc'
'string'
```

```
12.6 Classes and constructor functions 95
```
```
> typeof {}
'object'
```
```
Exercises: Two exercises ontypeof
```
- exercises/values/typeof_exrc.mjs
- Bonus:exercises/values/is_object_test.mjs

## 12.5.2 instanceof

This operator answers the question: has a valuexbeen created by a classC?

```
x instanceof C
```
```
For example:
```
```
> (function() {}) instanceof Function
true
> ({}) instanceof Object
true
> [] instanceof Array
true
```
```
Primitive values are not instances of anything:
```
```
> 123 instanceof Number
false
> '' instanceof String
false
> '' instanceof Object
false
```
```
Exercise:instanceof
exercises/values/instanceof_exrc.mjs
```
**12.6 Classes and constructor functions**

```
JavaScript’soriginalfactoriesforobjectsare constructorfunctions : ordinaryfunctionsthat
return “instances” of themselves if you invoke them via thenewoperator.
```
```
ES6 introduced classes , which are mainly better syntax for constructor functions.
```
```
In this book, I’m using the terms constructor function and class interchangeably.
```
```
Classes can be seen as partitioning the single typeobjectof the specification into sub-
types–theygiveusmoretypesthanthelimited7onesofthespecification. Eachclassis
the type of the objects that were created by it.
```

```
96 12 Values
```
## 12.6.1 Constructor functions associated with primitive types

```
Each primitive type (except for the spec-internal types forundefinedandnull) has an
associated constructor function (think class):
```
- The constructor functionBooleanis associated with booleans.
- The constructor functionNumberis associated with numbers.
- The constructor functionStringis associated with strings.
- The constructor functionSymbolis associated with symbols.

```
Each of these functions plays several roles – for example,Number:
```
- You can use it as a function and convert values to numbers:
    assert.equal( **Number** ('123'), 123 );
- Number.prototypeprovides the properties for numbers – for example, method
    .toString():

```
assert.equal(( 123 ).toString, Number .prototype.toString);
```
- Numberisanamespace/containerobjectfortoolfunctionsfornumbers–forexam-
    ple:
       assert.equal( **Number** .isInteger( 123 ), **true** );
- Lastly,youcanalsouseNumberasaclassandcreatenumberobjects. Theseobjects
    are different from real numbers and should be avoided.

```
assert.notEqual( newNumber ( 123 ), 123 );
assert.equal( newNumber ( 123 ).valueOf(), 123 );
```
```
12.6.1.1 Wrapping primitive values
```
Theconstructorfunctionsrelatedtoprimitivetypesarealsocalled _wrappertypes_ because
theyprovidethecanonicalwayofconvertingprimitivevaluestoobjects. Intheprocess,
primitive values are “wrapped” in objects.

```
const prim= true ;
assert.equal( typeof prim,'boolean');
assert.equal(prim instanceofBoolean , false );
```
```
const wrapped= Object (prim);
assert.equal( typeof wrapped,'object');
assert.equal(wrapped instanceofBoolean , true );
```
```
assert.equal(wrapped.valueOf(),prim);// unwrap
```
Wrappingrarelymattersinpractice,butitisusedinternallyinthelanguagespecification,
to give primitives properties.

**12.7 Converting between types**

There are two ways in which values are converted to other types in JavaScript:


```
12.7 Converting between types 97
```
- Explicit conversion: via functions such asString().
- _Coercion_ (automatic conversion): happens when an operation receives operands/-
    parameters that it can’t work with.

## 12.7.1 Explicit conversion between types

The function associated with a primitive type explicitly converts values to that type:

```
> Boolean(0)
false
> Number('123')
123
> String(123)
'123'
```
You can also useObject()to convert values to objects:

```
> typeof Object(123)
'object'
```
The following table describes in more detail how this conversion works:

```
x Object(x)
undefined {}
null {}
boolean new Boolean(x)
number new Number(x)
bigint An instance ofBigInt(newthrowsTypeError)
string new String(x)
symbol An instance ofSymbol(newthrowsTypeError)
object x
```
## 12.7.2 Coercion (automatic conversion between types)

```
Formanyoperations,JavaScriptautomaticallyconvertstheoperands/parametersiftheir
types don’t fit. This kind of automatic conversion is called coercion.
```
```
For example, the multiplication operator coerces its operands to numbers:
```
```
> '7' * '3'
21
```
```
Manybuilt-infunctionscoerce,too. Forexample,Number.parseInt()coercesitsparam-
eter to a string before parsing it. That explains the following result:
```
```
> Number.parseInt(123.45)
123
```
Thenumber123.45isconvertedtothestring'123.45'beforeitisparsed. Parsingstops
before the first non-digit character, which is why the result is 123.


98 _12 Values_

```
Exercise: Converting values to primitives
exercises/values/conversion_exrc.mjs
```
```
Quiz
Seequiz app.
```

**Chapter 13**

**Operators**

## Contents

```
13.1 Making sense of operators........................ 99
13.1.1 Operators coerce their operands to appropriate types..... 100
13.1.2 Most operators only work with primitive values........ 100
13.2 The plus operator (+)........................... 100
13.3 Assignment operators.......................... 101
13.3.1 The plain assignment operator.................. 101
13.3.2 Compound assignment operators................ 101
13.4 Equality:==vs.===............................ 102
13.4.1 Loose equality (==and!=).................... 102
13.4.2 Strict equality (===and!==)................... 103
13.4.3 Recommendation: always use strict equality.......... 104
13.4.4 Even stricter than===:Object.is()............... 104
13.5 Ordering operators............................ 105
13.6 Various other operators......................... 106
13.6.1 Comma operator......................... 106
13.6.2voidoperator........................... 106
```
**13.1 Making sense of operators**

JavaScript’soperatorsmayseemquirky. Withthefollowingtworules,theyareeasierto
understand:

- Operators coerce their operands to appropriate types
- Most operators only work with primitive values

```
99
```

```
100 13 Operators
```
## 13.1.1 Operators coerce their operands to appropriate types

```
If an operator gets operands that don’t have the proper types, it rarely throws an excep-
tion. Instead, it coerces (automatically converts) the operands so that it can work with
them. Let’s look at two examples.
```
```
First, the multiplication operator can only work with numbers. Therefore, it converts
strings to numbers before computing its result.
> '7' * '3'
21
```
```
Second, the square brackets operator ([ ]) for accessing the properties of an object can
only handle strings and symbols. All other values are coerced to string:
const obj={};
obj['true']= 123 ;
```
```
// Coerce true to the string 'true'
assert.equal(obj[ true ], 123 );
```
## 13.1.2 Most operators only work with primitive values

As mentioned before, most operators only work with primitive values. If an operand is
an object, it is usually coerced to a primitive value – for example:
> [1,2,3] + [4,5,6]
**'1,2,34,5,6'**

Why? The plus operator first coerces its operands to primitive values:

```
> String([1,2,3])
'1,2,3'
> String([4,5,6])
'4,5,6'
```
```
Next, it concatenates the two strings:
> '1,2,3' + '4,5,6'
'1,2,34,5,6'
```
**13.2 The plus operator (+)**

The plus operator works as follows in JavaScript:

- First,itconvertsbothoperandstoprimitivevalues. Thenitswitchestooneoftwo
    modes:
       **-** String mode: If one of the two primitive values is a string, then it converts
          the other one to a string, concatenates both strings, and returns the result.
       **-** Numbermode: Otherwise,Itconvertsbothoperandstonumbers,addsthem,
          and returns the result.

```
String mode lets us use+to assemble strings:
```

```
13.3 Assignment operators 101
```
```
> 'There are ' + 3 + ' items'
'There are 3 items'
Number mode means that if neither operand is a string (or an object that becomes a
string) then everything is coerced to numbers:
> 4 + true
5
Number(true)is 1.
```
**13.3 Assignment operators**

## 13.3.1 The plain assignment operator

The plain assignment operator is used to change storage locations:

```
x=value;// assign to a previously declared variable
obj.propKey=value;// assign to a property
arr[index]=value;// assign to an Array element
Initializers in variable declarations can also be viewed as a form of assignment:
const x=value;
let y=value;
```
## 13.3.2 Compound assignment operators

```
JavaScript supports the following assignment operators:
```
- Arithmetic assignment operators:+= -= *= /= %=[ES1]
    **-** +=can also be used for string concatenation
    **-** Introduced later:**=[ES2016]
- Bitwise assignment operators:&= ^= |=[ES1]
- Bitwise shift assignment operators:<<= >>= >>>=[ES1]
- Logical assignment operators:||= &&= ??=[ES2021]

```
13.3.2.1 Logical assignment operators [ES2021]
Logicalassignmentoperatorsworkdifferentlyfromothercompoundassignmentopera-
tors:
```
```
Assignment operator Equivalent to Only assigns ifais
a ||= b a || (a = b) Falsy
a &&= b a && (a = b) Truthy
a ??= b a ?? (a = b) Nullish
```
Why isa ||= bequivalent to the following expression?

```
a || (a = b)
```

```
102 13 Operators
```
Why not to this expression?

```
a = a || b
```
The former expression has the benefit ofshort-circuiting: The assignment is only evalu-
atedifaevaluatestofalse. Therefore,theassignmentisonlyperformedifit’snecessary.
In contrast, the latter expression always performs an assignment.
Formoreon??=,see§14.4.5“Thenullishcoalescingassignmentoperator(??=)[ES2021]”.

```
13.3.2.2 The remaining compound assignment operators
Foroperatorsopotherthan|| && ??,thefollowingtwowaysofassigningareequivalent:
```
```
myvar op= value
myvar = myvar op value
If, for example,opis+, then we get the operator+=that works as follows.
```
```
let str='';
str+='<b>';
str+='Hello!';
str+='</b>';
```
```
assert.equal(str,'<b>Hello!</b>');
```
**13.4 Equality:==vs.===**

JavaScript has two kinds of equality operators: loose equality (==) and strict equality
(===). The recommendation is to always use the latter.

```
Other names for==and===
```
- ==is also called _double equals_. Its official name in the language specification
    is _abstract equality comparison_.
- ===is also called _triple equals_.

## 13.4.1 Loose equality (==and!=)

```
Loose equality is one of JavaScript’s quirks. It often coerces operands. Some of those
coercions make sense:
```
```
> '123' == 123
true
> false == 0
true
```
Others less so:

```
> '' == 0
true
```

```
13.4 Equality:==vs.=== 103
```
```
Objects are coerced to primitives if (and only if!) the other operand is primitive:
> [1, 2, 3] == '1,2,3'
true
> ['1', '2', '3'] == '1,2,3'
true
If both operands are objects, they are only equal if they are the same object:
```
```
> [1, 2, 3] == ['1', '2', '3']
false
> [1, 2, 3] == [1, 2, 3]
false
```
```
> const arr = [1, 2, 3];
> arr == arr
true
```
```
Lastly,==considersundefinedandnullto be equal:
> undefined == null
true
```
## 13.4.2 Strict equality (===and!==)

```
Strictequalitynevercoerces. Twovaluesareonlyequaliftheyhavethesametype. Let’s
revisitourpreviousinteractionwiththe==operatorandseewhatthe===operatordoes:
```
```
> false === 0
false
> '123' === 123
false
```
An object is only equal to another value if that value is the same object:

```
> [1, 2, 3] === '1,2,3'
false
> ['1', '2', '3'] === '1,2,3'
false
```
```
> [1, 2, 3] === ['1', '2', '3']
false
> [1, 2, 3] === [1, 2, 3]
false
```
```
> const arr = [1, 2, 3];
> arr === arr
true
```
The===operator does not considerundefinedandnullto be equal:

```
> undefined === null
false
```

```
104 13 Operators
```
## 13.4.3 Recommendation: always use strict equality

```
Irecommendtoalwaysuse===. Itmakesyourcodeeasiertounderstandandsparesyou
from having to think about the quirks of==.
```
```
Let’s look at two use cases for==and what I recommend to do instead.
```
```
13.4.3.1 Use case for==: comparing with a number or a string
```
```
==lets you check if a valuexis a number or that number as a string – with a single
comparison:
```
```
if (x == 123 ) {
// x is either 123 or '123'
}
I prefer either of the following two alternatives:
```
```
if (x === 123 || x==='123') ···
if ( Number (x)=== 123 ) ···
You can also convertxto a number when you first encounter it.
```
```
13.4.3.2 Use case for==: comparing withundefinedornull
Another use case for==is to check if a valuexis eitherundefinedornull:
```
```
if (x == null ) {
// x is either null or undefined
}
The problem with this code is that you can’t be sure if someone meant to write it that
way or if they made a typo and meant=== null.
```
```
I prefer either of the following two alternatives:
if (x === undefined ||x=== null ) ···
if (!x) ···
```
A downside of the second alternative is that it accepts values other thanundefinedand
null, but it is a well-established pattern in JavaScript (to be explained in detail in§15.3
“Truthiness-based existence checks”).

```
The following three conditions are also roughly equivalent:
if (x != null ) ···
if (x !== undefined &&x!== null ) ···
if (x) ···
```
## 13.4.4 Even stricter than===:Object.is()

```
MethodObject.is()compares two values:
```
```
> Object.is(123, 123)
true
```

```
13.5 Ordering operators 105
```
```
> Object.is(123, '123')
false
Itisevenstricterthan===. Forexample,itconsidersNaN,theerrorvalueforcomputations
involving numbers, to be equal to itself:
> Object.is(NaN, NaN)
true
> NaN === NaN
false
```
That is occasionally useful. For example, you can use it to implement an improved ver-
sion of the Array method.indexOf():
**const** myIndexOf=(arr,elem) **=>** {
**return** arr.findIndex(x **=>Object** .is(x,elem));
};
myIndexOf()findsNaNin an Array, while.indexOf()doesn’t:
> myIndexOf([0,NaN,2], NaN)
**1**
> [0,NaN,2].indexOf(NaN)
**-1**

The result-1means that.indexOf()couldn’t find its argument in the Array.

**13.5 Ordering operators**

```
Table 13.2: JavaScript’s ordering operators.
```
```
Operator name
< less than
<= Less than or equal
> Greater than
>= Greater than or equal
```
```
JavaScript’s ordering operators (tbl.13.2) work for both numbers and strings:
> 5 >= 2
true
> 'bar' < 'foo'
true
<=and>=are based on strict equality.
```
```
The ordering operators don’t work well for human languages
```

```
106 13 Operators
```
```
The ordering operators don’t work well for comparing text in a human language,
e.g.,whencapitalizationoraccentsareinvolved. Thedetailsareexplainedin§20.6
“Comparing strings”.
```
**13.6 Various other operators**

The following operators are covered elsewhere in this book:

- Operators forbooleans,numbers,strings,objects
- The nullish coalescing operator (??) for default values

The next two subsections discuss two operators that are rarely used.

## 13.6.1 Comma operator

The comma operator has two operands, evaluates both of them and returns the second
one:
> 'a', 'b'
**'b'**
For more information on this operator, see _Speaking JavaScript_.

## 13.6.2 voidoperator

Thevoidoperator evaluates its operand and returnsundefined:

```
> void (3 + 2)
undefined
For more information on this operator, see Speaking JavaScript.
```
```
Quiz
Seequiz app.
```

**Part IV**

**Primitive values**

```
107
```


**Chapter 14**

**The non-values undefinedand**

**null**

## Contents

```
14.1undefinedvs.null............................ 109
14.2 Occurrences ofundefinedandnull................... 110
14.2.1 Occurrences ofundefined.................... 110
14.2.2 Occurrences ofnull....................... 110
14.3 Checking forundefinedornull..................... 111
14.4 The nullish coalescing operator (??) for default values [ES2020].. 111
14.4.1 Example: counting matches................... 111
14.4.2 Example: specifying a default value for a property....... 112
14.4.3 Using destructuring for default values............. 112
14.4.4 Legacy approach: using logical Or (||) for default values... 112
14.4.5 The nullish coalescing assignment operator (??=) [ES2021].. 113
14.5undefinedandnulldon’t have properties............... 114
14.6 The history ofundefinedandnull................... 115
```
Manyprogramminglanguageshaveone“non-value”callednull. Itindicatesthatavari-
able does not currently point to an object – for example, when it hasn’t been initialized
yet.

```
In contrast, JavaScript has two of them:undefinedandnull.
```
**14.1 undefinedvs.null**

```
Bothvaluesareverysimilarandoftenusedinterchangeably. Howtheydifferistherefore
subtle. The language itself makes the following distinction:
```
- undefinedmeans “not initialized” (e.g., a variable) or “not existing” (e.g., a prop-
    erty of an object).

```
109
```

```
110 14 The non-valuesundefinedandnull
```
- nullmeans “the intentional absence of any object value” (a quote fromthe lan-
    guage specification).
Programmers may make the following distinction:
- undefinedisthenon-valueusedbythelanguage(whensomethingisuninitialized,
etc.).
- nullmeans “explicitly switched off”. That is, it helps implement a type that com-
prises both meaningful values and a meta-value that stands for “no meaningful
value”. Such a type is called _option type_ or _maybe type_ in functional programming.

**14.2 Occurrences ofundefinedandnull**

The following subsections describe whereundefinedandnullappear in the language.
We’ll encounter several mechanisms that are explained in more detail later in this book.

## 14.2.1 Occurrences ofundefined

```
Uninitialized variablemyVar:
let myVar;
assert.equal(myVar, undefined );
Parameterxis not provided:
function func(x) {
return x;
}
assert.equal(func(), undefined );
Property.unknownPropis missing:
const obj={};
assert.equal(obj.unknownProp, undefined );
If we don’t explicitly specify the result of a function via areturnstatement, JavaScript
returnsundefinedfor us:
function func() {}
assert.equal(func(), undefined );
```
## 14.2.2 Occurrences ofnull

Theprototypeofanobjectiseitheranobjector,attheendofachainofprototypes,null.
Object.prototypedoes not have a prototype:
> Object.getPrototypeOf(Object.prototype)
**null**
Ifwematcharegularexpression(suchas/a/)againstastring(suchas'x'),weeitherget
an object with matching data (if matching was successful) ornull(if matching failed):

```
> /a/.exec('x')
null
```

```
14.3 Checking forundefinedornull 111
```
TheJSON data formatdoes not supportundefined, onlynull:

```
> JSON.stringify({a: undefined, b: null})
'{"b":null}'
```
**14.3 Checking forundefinedornull**

```
Checking for either:
```
```
if (x=== null ) ···
if (x=== undefined ) ···
```
```
Doesxhave a value?
```
```
if (x!== undefined &&x!== null ) {
// ···
}
if (x) {// truthy?
// x is neither: undefined, null, false, 0, NaN, ''
}
```
```
Isxeitherundefinedornull?
```
```
if (x=== undefined ||x=== null ) {
// ···
}
if (!x) {// falsy?
// x is: undefined, null, false, 0, NaN, ''
}
```
_Truthy_ means“istrueifcoercedtoboolean”. _Falsy_ means“isfalseifcoercedtoboolean”.
Both concepts are explained properly in§15.2 “Falsy and truthy values”.

```
14.4 The nullish coalescing operator (??) for default val-
ues [ES2020]
```
```
Sometimeswereceiveavalueandonlywanttouseitifitisn’teithernullorundefined.
Otherwise, we’d like to use a default value, as a fallback. We can do that via the nullish
coalescing operator (??):
```
```
const valueToUse=receivedValue?? defaultValue;
```
The following two expressions are equivalent:

```
a??b
a!== undefined &&a!== null ?a:b
```
## 14.4.1 Example: counting matches

The following code shows a real-world example:


```
112 14 The non-valuesundefinedandnull
```
```
function countMatches(regex,str) {
const matchResult=str.match(regex);// null or Array
return (matchResult??[]).length;
}
```
```
assert.equal(
countMatches(/a/g,'ababa'), 3 );
assert.equal(
countMatches(/b/g,'ababa'), 2 );
assert.equal(
countMatches(/x/g,'ababa'), 0 );
```
```
If there are one or more matches forregexinsidestr, then.match()returns an Array.
If there are no matches, it unfortunately returnsnull(and not the empty Array). We fix
that via the??operator.
```
We also could have usedoptional chaining:

```
return matchResult?.length?? 0 ;
```
## 14.4.2 Example: specifying a default value for a property

```
function getTitle(fileDesc) {
return fileDesc.title??'(Untitled)';
}
```
```
const files=[
{path:'index.html',title:'Home'},
{path:'tmp.html'},
];
assert.deepEqual(
files.map(f => getTitle(f)),
['Home','(Untitled)']);
```
## 14.4.3 Using destructuring for default values

```
In some cases, destructuring can also be used for default values – for example:
```
```
function getTitle(fileDesc) {
const {title='(Untitled)'}=fileDesc;
return title;
}
```
## 14.4.4 Legacy approach: using logical Or (||) for default values

Before ECMAScript 2020 and the nullish coalescing operator, logical Or was used for
default values. That has a downside.

```
||works as expected forundefinedandnull:
```

```
14.4 The nullish coalescing operator (??) for default values [ES2020] 113
```
```
> undefined || 'default'
'default'
> null || 'default'
'default'
```
```
But it also returns the default for all other falsy values – for example:
```
```
> false || 'default'
'default'
> 0 || 'default'
'default'
> 0n || 'default'
'default'
> '' || 'default'
'default'
Compare that to how??works:
```
```
> undefined ?? 'default'
'default'
> null ?? 'default'
'default'
```
```
> false ?? 'default'
false
> 0 ?? 'default'
0
> 0n ?? 'default'
0n
> '' ?? 'default'
''
```
## 14.4.5 The nullish coalescing assignment operator (??=) [ES2021]

```
??=isalogicalassignmentoperator. Thefollowingtwoexpressionsareroughlyequiva-
lent:
```
```
a??=b
a??(a=b)
```
That means that??=isshort-circuiting: The assignment is only made ifaisundefined
ornull.

```
14.4.5.1 Example: using??=to add missing properties
```
```
const books=[
{
isbn:'123',
},
{
title:'ECMAScript Language Specification',
```

```
114 14 The non-valuesundefinedandnull
```
```
isbn:'456',
},
];
```
```
// Add property .title where it’s missing
for ( const book of books) {
book.title??='(Untitled)';
}
```
```
assert.deepEqual(
books,
[
{
isbn:'123',
title:'(Untitled)',
},
{
title:'ECMAScript Language Specification',
isbn:'456',
},
]);
```
**14.5 undefinedandnulldon’t have properties**

undefinedandnullare the only two JavaScript values where we get an exception if
we try to read a property. To explore this phenomenon, let’s use the following function,
which reads (“gets”) property.fooand returns the result.

```
function getFoo(x) {
return x.foo;
}
```
```
If we applygetFoo()to various values, we can see that it only fails forundefinedand
null:
```
```
> getFoo(undefined)
TypeError: Cannot read properties of undefined (reading 'foo')
> getFoo(null)
TypeError: Cannot read properties of null (reading 'foo')
```
```
> getFoo(true)
undefined
> getFoo({})
undefined
```

```
14.6 The history ofundefinedandnull 115
```
**14.6 The history ofundefinedandnull**

```
In Java (which inspired many aspects of JavaScript), initialization values depend on the
static type of a variable:
```
- Variables with object types are initialized withnull.
- Each primitive type has its own initialization value. For example,intvariables
    are initialized with 0.
InJavaScript,eachvariablecanholdbothobjectvaluesandprimitivevalues. Therefore,
ifnullmeans “not an object”, JavaScript also needs an initialization value that means
“neither an object nor a primitive value”. That initialization value isundefined.

```
Quiz
Seequiz app.
```

116 _14 The non-valuesundefinedandnull_


**Chapter 15**

**Booleans**

## Contents

```
15.1 Converting to boolean.......................... 117
15.2 Falsy and truthy values......................... 118
15.2.1 Checking for truthiness or falsiness............... 119
15.3 Truthiness-based existence checks................... 119
15.3.1 Pitfall: truthiness-based existence checks are imprecise.... 120
15.3.2 Use case: was a parameter provided?.............. 120
15.3.3 Use case: does a property exist?................. 121
15.4 Conditional operator (? :)........................ 121
15.5 Binary logical operators: And (x && y), Or (x || y)......... 122
15.5.1 Value-preservation........................ 122
15.5.2 Short-circuiting.......................... 122
15.5.3 Logical And (x && y)....................... 122
15.5.4 Logical Or (||).......................... 123
15.6 Logical Not (!).............................. 124
```
The primitive type _boolean_ comprises two values –falseandtrue:

```
> typeof false
'boolean'
> typeof true
'boolean'
```
**15.1 Converting to boolean**

```
The meaning of “converting to [type]”
“Converting to [type]” is short for “Converting arbitrary values to values of type
[type]”.
```
```
117
```

```
118 15 Booleans
```
These are three ways in which you can convert an arbitrary valuexto a boolean.

- Boolean(x)
    Most descriptive; recommended.
- x? true : false
    Uses the conditional operator (explainedlater in this chapter).
- !!x
    Usesthe logical Not operator (!). This operator coerces its operand to boolean. It
    is applied a second time to get a non-negated result.

Tbl.15.1describes how various values are converted to boolean.

```
Table 15.1: Converting values to booleans.
```
```
x Boolean(x)
undefined false
null false
boolean x(no change)
number 0 → false,NaN → false
Other numbers→ true
bigint 0 → false
Other numbers→ true
string '' → false
Other strings→ true
symbol true
object Alwaystrue
```
**15.2 Falsy and truthy values**

When checking the condition of anifstatement, awhileloop, or ado-whileloop,
JavaScript works differently than you may expect. Take, for example, the following
condition:
**if** (value) {}
In many programming languages, this condition is equivalent to:
**if** (value=== **true** ) {}
However, in JavaScript, it is equivalent to:
**if** ( **Boolean** (value)=== **true** ) {}

Thatis,JavaScriptchecksifvalueistruewhenconvertedtoboolean. Thiskindofcheck
is so common that the following names were introduced:

- A value is called _truthy_ if it istruewhen converted to boolean.
- A value is called _falsy_ if it isfalsewhen converted to boolean.
Each value is either truthy or falsy. Consulting tbl.15.1, we can make an exhaustive list
of falsy values:


```
15.3 Truthiness-based existence checks 119
```
- undefined
- null
- Boolean:false
- Numbers: 0 ,NaN
- Bigint:0n
- String:''

All other values (including all objects) are truthy:

```
> Boolean('abc')
true
> Boolean([])
true
> Boolean({})
true
```
## 15.2.1 Checking for truthiness or falsiness

```
if (x) {
// x is truthy
}
```
```
if (!x) {
// x is falsy
}
```
```
if (x) {
// x is truthy
} else {
// x is falsy
}
```
```
const result=x?'truthy':'falsy';
```
The conditional operator that is used in the last line, is explainedlater in this chapter.

```
Exercise: Truthiness
exercises/booleans/truthiness_exrc.mjs
```
**15.3 Truthiness-based existence checks**

```
In JavaScript, if you read something that doesn’t exist (e.g., a missing parameter or a
missing property), you usually getundefinedas a result. In these cases, an existence
check amounts to comparing a value withundefined. For example, the following code
checks if objectobjhas the property.prop:
```
```
if (obj.prop!== undefined ) {
// obj has property .prop
```

```
120 15 Booleans
```
### }

```
Due toundefinedbeing falsy, we can shorten this check to:
```
```
if (obj.prop) {
// obj has property .prop
}
```
## 15.3.1 Pitfall: truthiness-based existence checks are imprecise

Truthiness-based existence checks have one pitfall: they are not very precise. Consider
this previous example:

```
if (obj.prop) {
// obj has property .prop
}
```
The body of theifstatement is skipped if:

- obj.propis missing (in which case, JavaScript returnsundefined).

However, it is also skipped if:

- obj.propisundefined.
- obj.propis any other falsy value (null, 0 ,'', etc.).

```
In practice, this rarely causes problems, but you have to be aware of this pitfall.
```
## 15.3.2 Use case: was a parameter provided?

Atruthinesscheckisoftenusedtodetermineifthecallerofafunctionprovidedaparam-
eter:

```
function func(x) {
if (!x) {
thrownewError ('Missing parameter x');
}
// ···
}
```
On the plus side, this pattern is established and short. It correctly throws errors forun-
definedandnull.

Ontheminusside,thereisthepreviouslymentionedpitfall: thecodealsothrowserrors
for all other falsy values.

An alternative is to check forundefined:

```
if (x === undefined ) {
thrownewError ('Missing parameter x');
}
```

```
15.4 Conditional operator (? :) 121
```
## 15.3.3 Use case: does a property exist?

Truthiness checks are also often used to determine if a property exists:

```
function readFile(fileDesc) {
if (!fileDesc.path) {
thrownewError ('Missing property: .path');
}
// ···
}
readFile({path:'foo.txt'});// no error
```
Thispatternisalsoestablishedandhastheusualcaveat: itnotonlythrowsiftheproperty
is missing, but also if it exists and has any of the falsy values.

```
If you truly want to check if the property exists, you have to usetheinoperator:
```
```
if (!('path' in fileDesc)) {
thrownewError ('Missing property: .path');
}
```
**15.4 Conditional operator (? :)**

The conditional operator is the expression version of theifstatement. Its syntax is:

```
«condition»? «thenExpression» : «elseExpression»
```
```
It is evaluated as follows:
```
- Ifconditionis truthy, evaluate and returnthenExpression.
- Otherwise, evaluate and returnelseExpression.

The conditional operator is also called _ternary operator_ because it has three operands.

```
Examples:
```
```
> true? 'yes' : 'no'
'yes'
> false? 'yes' : 'no'
'no'
> ''? 'yes' : 'no'
'no'
```
The following code demonstrates that whichever of the two branches “then” and “else”
is chosen via the condition, only that branch is evaluated. The other branch isn’t.

```
const x=( true? console .log('then'): console .log('else'));
```
```
// Output:
// 'then'
```

```
122 15 Booleans
```
**15.5 Binary logical operators: And (x && y), Or (x || y)**

The binary logical operators&&and||are _value-preserving_ and _short-circuiting_.

## 15.5.1 Value-preservation

_Value-preservation_ means that operands are interpreted as booleans but returned
unchanged:
> 12 || 'hello'
**12**
> 0 || 'hello'
**'hello'**

## 15.5.2 Short-circuiting

_Short-circuiting_ means if the first operand already determines the result, then the second
operand is not evaluated. The only other operator that delays evaluating its operands
is the conditional operator. Usually, all operands are evaluated before performing an
operation.
Forexample,logicalAnd(&&)doesnotevaluateitssecondoperandifthefirstoneisfalsy:

```
const x= false && console .log('hello');
// No output
If the first operand is truthy,console.log()is executed:
```
```
const x= true && console .log('hello');
```
```
// Output:
// 'hello'
```
## 15.5.3 Logical And (x && y)

The expressiona && b(“aAndb”) is evaluated as follows:

```
1.Evaluatea.
2.Is the result falsy? Return it.
3.Otherwise, evaluateband return the result.
In other words, the following two expressions are roughly equivalent:
```
```
a&&b
!a?a:b
Examples:
```
```
> false && true
false
> false && 'abc'
false
```

```
15.5 Binary logical operators: And (x && y), Or (x || y) 123
```
```
> true && false
false
> true && 'abc'
'abc'
```
```
> '' && 'abc'
''
```
## 15.5.4 Logical Or (||)

The expressiona || b(“aOrb”) is evaluated as follows:

```
1.Evaluatea.
2.Is the result truthy? Return it.
3.Otherwise, evaluateband return the result.
```
```
In other words, the following two expressions are roughly equivalent:
```
```
a|| b
a?a:b
```
```
Examples:
```
```
> true || false
true
> true || 'abc'
true
```
```
> false || true
true
> false || 'abc'
'abc'
```
```
> 'abc' || 'def'
'abc'
```
```
15.5.4.1 Legacy use case for logical Or (||): providing default values
```
```
ECMAScript2020introducedthenullishcoalescingoperator(??) fordefaultvalues. Be-
fore that, logical Or was used for this purpose:
```
```
const valueToUse=receivedValue|| defaultValue;
```
```
See§14.4 “The nullish coalescing operator (??) for default values [ES2020]”for more
information on??and the downsides of||in this case.
```
```
Legacy exercise: Default values via the Or operator (||)
exercises/booleans/default_via_or_exrc.mjs
```

```
124 15 Booleans
```
**15.6 Logical Not (!)**

The expression!x(“Notx”) is evaluated as follows:

```
1.Evaluatex.
2.Is it truthy? Returnfalse.
3.Otherwise, returntrue.
Examples:
> !false
true
> !true
false
```
```
> !0
true
> !123
false
```
```
> !''
true
> !'abc'
false
```
```
Quiz
Seequiz app.
```

**Chapter 16**

**Numbers**

## Contents

```
16.1 Numbers are used for both floating point numbers and integers.. 126
16.2 Number literals.............................. 126
16.2.1 Integer literals........................... 126
16.2.2 Floating point literals....................... 127
16.2.3 Syntactic pitfall: properties of integer literals.......... 127
16.2.4 Underscores (_) as separators in number literals [ES2021]... 127
16.3 Arithmetic operators........................... 128
16.3.1 Binary arithmetic operators................... 128
16.3.2 Unary plus (+) and negation (-)................. 129
16.3.3 Incrementing (++) and decrementing (--)............ 130
16.4 Converting to number.......................... 131
16.5 Error values................................ 132
16.5.1 Error value:NaN.......................... 132
16.5.2 Error value:Infinity...................... 133
16.6 The precision of numbers: careful with decimal fractions...... 134
16.7 (Advanced)................................ 134
16.8 Background: floating point precision.................. 135
16.8.1 A simplified representation of floating point numbers..... 135
16.9 Integer numbers in JavaScript..................... 136
16.9.1 Converting to integer....................... 137
16.9.2 Ranges of integer numbers in JavaScript............ 137
16.9.3 Safe integers............................ 138
16.10Bitwise operators............................. 139
16.10.1Internally, bitwise operators work with 32-bit integers..... 139
16.10.2Bitwise Not............................ 140
16.10.3Binary bitwise operators..................... 140
16.10.4Bitwise shift operators...................... 141
16.10.5b32(): displaying unsigned 32-bit integers in binary notation. 141
```
```
125
```

```
126 16 Numbers
```
```
16.11Quick reference: numbers........................ 142
16.11.1 Global functions for numbers.................. 142
16.11.2 Static properties ofNumber.................... 142
16.11.3 Static methods ofNumber..................... 142
16.11.4 Methods ofNumber.prototype.................. 144
16.11.5 Sources.............................. 146
```
JavaScript has two kinds of numeric values:

- _Numbers_ are 64-bit floating point numbers and are also used for smaller integers
    (within a range of plus/minus 53 bits).
- _Bigints_ represent integers with an arbitrary precision.

This chapter covers numbers. Bigints are coveredlater in this book.

```
16.1 Numbers are used for both floating point numbers
and integers
```
The typenumberis used for both integers and floating point numbers in JavaScript:

98
123.45
However,allnumbersare _doubles_ ,64-bitfloatingpointnumbersimplementedaccording
to the _IEEE Standard for Floating-Point Arithmetic_ (IEEE 754).
Integer numbers are simply floating point numbers without a decimal fraction:
> 98 === 98.0
**true**
Note that, under the hood, most JavaScript engines are often able to use real integers,
with all associated performance and storage size benefits.

**16.2 Number literals**

```
Let’s examine literals for numbers.
```
## 16.2.1 Integer literals

```
Several integer literals let us express integers with various bases:
// Binary (base 2)
assert.equal(0b11, 3 );// ES6
```
```
// Octal (base 8)
assert.equal(0o10, 8 );// ES6
```
```
// Decimal (base 10)
assert.equal( 35 , 35 );
```

```
16.2 Number literals 127
```
```
// Hexadecimal (base 16)
assert.equal(0xE7, 231 );
```
## 16.2.2 Floating point literals

```
Floating point numbers can only be expressed in base 10.
Fractions:
> 35.0
35
Exponent:eNmeans ×10N
> 3e2
300
> 3e-2
0.03
> 0.3e2
30
```
## 16.2.3 Syntactic pitfall: properties of integer literals

Accessing a property of an integer literal entails a pitfall: If the integer literal is immedi-
ately followed by a dot, then that dot is interpreted as a decimal dot:
7.toString(); // syntax error

There are four ways to work around this pitfall:

```
7.0.toString()
( 7 ).toString()
7..toString()
7 .toString() // space before dot
```
## 16.2.4 Underscores (_) as separators in number literals [ES2021]

```
Groupingdigitstomakelongnumbersmorereadablehasalongtradition. Forexample:
```
- In 1825, London had 1,335,000 inhabitants.
- The distance between Earth and Sun is 149,600,000 km.

```
Since ES2021, we can use underscores as separators in number literals:
const inhabitantsOfLondon=1_335_000;
const distanceEarthSunInKm=149_600_000;
```
With other bases, grouping is important, too:

```
const fileSystemPermission=0b111_111_000;
const bytes=0b1111_10101011_11110000_00001101;
const words=0xFAB_F00D;
```
We can also use the separator in fractions and exponents:


```
128 16 Numbers
```
```
const massOfElectronInKg=9.109_383_56e-31;
const trillionInShortScale=1e1_2;
```
```
16.2.4.1 Where can we put separators?
```
The locations of separators are restricted in two ways:

- We can only put underscores between two digits. Therefore, all of the following
    number literals are illegal:
       3 _.141
       3._141

```
1 _e12
1 e_12
```
```
_1464301 // valid variable name!
1464301 _
```
```
0 _b111111000
0 b_111111000
```
- We can’t use more than one underscore in a row:
    123 __456// two underscores – not allowed

The motivation behind these restrictions is to keep parsing simple and to avoid strange
edge cases.

```
16.2.4.2 Parsing numbers with separators
```
The following functions for parsing numbers do not support separators:

- Number()
- Number.parseInt()
- Number.parseFloat()
For example:
> Number('123_456')
**NaN**
> Number.parseInt('123_456')
**123**

The rationale is that numeric separators are for code. Other kinds of input should be
processed differently.

**16.3 Arithmetic operators**

## 16.3.1 Binary arithmetic operators

Tbl.16.1lists JavaScript’s binary arithmetic operators.


```
16.3 Arithmetic operators 129
```
```
Table 16.1: Binary arithmetic operators.
```
```
Operator Name Example
n + m Addition ES1 3 + 4 → 7
n - m Subtraction ES1 9 - 1 → 8
n * m Multiplication ES1 3 * 2.25 → 6.75
n / m Division ES1 5.625 / 5 → 1.125
n % m Remainder ES1 8 % 5 → 3
-8 % 5 → -3
n ** m Exponentiation ES2016 4 ** 2 → 16
```
```
16.3.1.1 %is a remainder operator
%is a remainder operator, not a modulo operator. Its result has the sign of the first
operand:
> 5 % 3
2
> -5 % 3
-2
For more information on the difference between remainder and modulo, see the blog
post“Remainder operator vs. modulo operator (with JavaScript code)”on 2ality.
```
## 16.3.2 Unary plus (+) and negation (-)

Tbl.16.2summarizes the two operators _unary plus_ (+) and _negation_ (-).

```
Table 16.2: The operators unary plus (+) and negation (-).
```
```
Operator Name Example
+n Unary plus ES1 +(-7) → -7
-n Unary negation ES1 -(-7) → 7
```
```
Both operators coerce their operands to numbers:
```
### > +'5'

### 5

### > +'-12'

### -12

### > -'9'

### -9

Thus, unary plus lets us convert arbitrary values to numbers.


```
130 16 Numbers
```
## 16.3.3 Incrementing (++) and decrementing (--)

Theincrementationoperator++existsinaprefixversionandasuffixversion. Inbothver-
sions, it destructively adds one to its operand. Therefore, its operand must be a storage
location that can be changed.

Thedecrementationoperator--worksthesame,butsubtractsonefromitsoperand. The
next two examples explain the difference between the prefix and the suffix version.

Tbl.16.3summarizes the incrementation and decrementation operators.

```
Table 16.3: Incrementation operators and decrementation operators.
```
```
Operator Name Example
v++ Increment ES1 let v=0; [v++, v] → [0, 1]
++v Increment ES1 let v=0; [++v, v] → [1, 1]
v-- Decrement ES1 let v=1; [v--, v] → [1, 0]
--v Decrement ES1 let v=1; [--v, v] → [0, 0]
```
```
Next, we’ll look at examples of these operators in use.
```
```
Prefix++and prefix--change their operands and then return them.
```
```
let foo= 3 ;
assert.equal(++foo, 4 );
assert.equal(foo, 4 );
```
```
let bar= 3 ;
assert.equal(--bar, 2 );
assert.equal(bar, 2 );
```
```
Suffix++and suffix--return their operands and then change them.
```
```
let foo= 3 ;
assert.equal(foo++, 3 );
assert.equal(foo, 4 );
```
```
let bar= 3 ;
assert.equal(bar--, 3 );
assert.equal(bar, 2 );
```
```
16.3.3.1 Operands: not just variables
```
We can also apply these operators to property values:

```
const obj={a: 1 };
++obj.a;
assert.equal(obj.a, 2 );
```
And to Array elements:


```
16.4 Converting to number 131
```
```
const arr=[ 4 ];
arr[ 0 ]++;
assert.deepEqual(arr,[ 5 ]);
```
```
Exercise: Number operators
exercises/numbers-math/is_odd_test.mjs
```
**16.4 Converting to number**

These are three ways of converting values to numbers:

- Number(value)
- +value
- parseFloat(value)(avoid; different than the other two!)
Recommendation: use the descriptiveNumber(). Tbl.16.4summarizes how it works.

```
Table 16.4: Converting values to numbers.
```
```
x Number(x)
undefined NaN
null 0
boolean false → 0,true → 1
number x(no change)
bigint -1n → -1,1n → 1, etc.
string '' → 0
Other→parsed number, ignoring leading/trailing whitespace
symbol ThrowsTypeError
object Configurable (e.g. via.valueOf())
```
```
Examples:
```
```
assert.equal( Number (123.45),123.45);
```
```
assert.equal( Number (''), 0 );
assert.equal( Number ('\n123.45\t'),123.45);
assert.equal( Number ('xyz'), NaN );
```
```
assert.equal( Number (- 123 n),- 123 );
```
```
How objects are converted to numbers can be configured – for example, by overriding
.valueOf():
```
```
> Number({ valueOf() { return 123 } })
123
```

```
132 16 Numbers
```
```
Exercise: Converting to number
exercises/numbers-math/parse_number_test.mjs
```
**16.5 Error values**

Two number values are returned when errors happen:

- NaN
- Infinity

## 16.5.1 Error value:NaN

```
NaNisan abbreviation of “nota number”. Ironically,JavaScript considers itto be a num-
ber:
> typeof NaN
'number'
```
When isNaNreturned?

```
NaNis returned if a number can’t be parsed:
> Number('$$$')
NaN
> Number(undefined)
NaN
NaNis returned if an operation can’t be performed:
> Math.log(-1)
NaN
> Math.sqrt(-1)
NaN
NaNis returned if an operand or argument isNaN(to propagate errors):
```
```
> NaN - 3
NaN
> 7 ** NaN
NaN
```
```
16.5.1.1 Checking forNaN
NaNis the only JavaScript value that is not strictly equal to itself:
const n= NaN ;
assert.equal(n===n, false );
```
These are several ways of checking if a valuexisNaN:

```
const x= NaN ;
```

```
16.5 Error values 133
```
```
assert.equal( Number .isNaN(x), true );// preferred
assert.equal( Object .is(x, NaN ), true );
assert.equal(x!==x, true );
In the last line, we use the comparison quirk to detectNaN.
```
```
16.5.1.2 FindingNaNin Arrays
Some Array methods can’t findNaN:
> [NaN].indexOf(NaN)
-1
Others can:
> [NaN].includes(NaN)
true
> [NaN].findIndex(x => Number.isNaN(x))
0
> [NaN].find(x => Number.isNaN(x))
NaN
```
Alas,thereisnosimpleruleofthumb. Wehavetocheckforeachmethodhowithandles
NaN.

## 16.5.2 Error value:Infinity

When is the error valueInfinityreturned?

```
Infinity is returned if a number is too large:
> Math.pow(2, 1023)
8.98846567431158e+307
> Math.pow(2, 1024)
Infinity
Infinity is returned if there is a division by zero:
> 5 / 0
Infinity
> -5 / 0
-Infinity
```
```
16.5.2.1 Infinityas a default value
Infinityis larger than all other numbers (exceptNaN), making it a good default value:
function findMinimum(numbers) {
let min= Infinity ;
for ( const n of numbers) {
if (n<min) min=n;
}
return min;
}
```

```
134 16 Numbers
```
```
assert.equal(findMinimum([ 5 ,- 1 , 2 ]),- 1 );
assert.equal(findMinimum([]), Infinity );
```
```
16.5.2.2 Checking forInfinity
```
These are two common ways of checking if a valuexisInfinity:

```
const x= Infinity ;
```
```
assert.equal(x=== Infinity , true );
assert.equal( Number .isFinite(x), false );
```
```
Exercise: Comparing numbers
exercises/numbers-math/find_max_test.mjs
```
```
16.6 The precision of numbers: careful with decimal frac-
tions
```
```
Internally, JavaScript floating point numbers are represented with base 2 (according to
the IEEE 754 standard). That means that decimal fractions (base 10) can’t always be
represented precisely:
```
```
> 0.1 + 0.2
0.30000000000000004
> 1.3 * 3
3.9000000000000004
> 1.4 * 100000000000000
139999999999999.98
```
We therefore need to take rounding errors into consideration when performing arith-
metic in JavaScript.

```
Read on for an explanation of this phenomenon.
```
```
Quiz: basic
Seequiz app.
```
**16.7 (Advanced)**

All remaining sections of this chapter are advanced.


```
16.8 Background: floating point precision 135
```
**16.8 Background: floating point precision**

```
In JavaScript, computations with numbers don’t always produce correct results – for
example:
> 0.1 + 0.2
0.30000000000000004
Tounderstandwhy,weneedtoexplorehowJavaScriptrepresentsfloatingpointnumbers
internally. Itusesthreeintegerstodoso,whichtakeupatotalof64bitsofstorage(double
precision):
```
```
Component Size Integer range
Sign 1 bit [0, 1]
Fraction 52 bits [0, 2^52 −1]
Exponent 11 bits [−1023, 1024]
```
The floating point number represented by these integers is computed as follows:
(–1)sign× 0b1.fraction × 2exponent
This representation can’t encode a zero because its second component (involving the
fraction) always has a leading 1. Therefore, a zero is encoded via the special exponent
−1023 and a fraction 0.

## 16.8.1 A simplified representation of floating point numbers

```
To make further discussions easier, we simplify the previous representation:
```
- Insteadofbase2(binary),weusebase10(decimal)becausethat’swhatmostpeo-
    ple are more familiar with.
- The _fraction_ isanaturalnumberthatisinterpretedasafraction(digitsafterapoint).
    We switch to a _mantissa_ , an integer that is interpreted as itself. As a consequence,
       the exponent is used differently, but its fundamental role doesn’t change.
- As the mantissa is an integer (with its own sign), we don’t need a separate sign,
    anymore.
The new representation works like this:
mantissa × 10exponent
Let’s try out this representation for a few floating point numbers.
- For the integer −123, we mainly need the mantissa:
> -123 * (10 ** 0)
**-123**
- For the number 1.5, we imagine there being a point after the mantissa. We use a
negative exponent to move that point one digit to the left:
> 15 * (10 ** -1)
**1.5**


```
136 16 Numbers
```
- For the number 0.25, we move the point two digits to the left:
    > 25 * (10 ** -2)
    **0.25**

```
Representations with negative exponents can also be written as fractions with positive
exponents in the denominators:
> 15 * (10 ** -1) === 15 / (10 ** 1)
true
> 25 * (10 ** -2) === 25 / (10 ** 2)
true
```
These fractions help with understanding why there are numbers that our encoding can-
not represent:

- 1/10can be represented. It already has the required format: a power of 10 in the
    denominator.
- 1/2can be represented as5/10. We turned the 2 in the denominator into a power
    of 10 by multiplying the numerator and denominator by 5.
- 1/4canberepresentedas25/100. Weturnedthe4inthedenominatorintoapower
    of 10 by multiplying the numerator and denominator by 25.
- 1/3cannot be represented. There is no way to turn the denominator into a power
    of 10. (The prime factors of 10 are 2 and 5. Therefore, any denominator that only
    hastheseprimefactorscanbeconvertedtoapowerof10,bymultiplyingboththe
    numerator and denominator by enough twos and fives. If a denominator has a
    different prime factor, then there’s nothing we can do.)

To conclude our excursion, we switch back to base 2:

- 0.5 = 1/2can be represented with base 2 because the denominator is already a
    power of 2.
- 0.25 = 1/4can be represented with base 2 because the denominator is already a
    power of 2.
- 0.1 = 1/10cannot be represented because the denominator cannot be converted
    to a power of 2.
- 0.2 = 2/10cannot be represented because the denominator cannot be converted
    to a power of 2.

```
Now we can see why0.1 + 0.2doesn’t produce a correct result: internally, neither of
the two operands can be represented precisely.
```
The only way to compute precisely with decimal fractions is by internally switching to
base 10. For many programming languages, base 2 is the default and base 10 an option.
For example, Java has the classBigDecimaland Python has the moduledecimal. There
are plans to add something similar to JavaScript:the ECMAScript proposal “Decimal”.

**16.9 Integer numbers in JavaScript**

```
Integer numbers are normal (floating point) numbers without decimal fractions:
```

```
16.9 Integer numbers in JavaScript 137
```
### > 1 === 1.0

```
true
> Number.isInteger(1.0)
true
In this section, we’ll look at a few tools for working with these pseudo-integers.
JavaScript also supports bigints , which are real integers.
```
## 16.9.1 Converting to integer

The recommended way of converting numbers to integers is to use one of the rounding

## 25.7 Methods of functions:.call(),.apply(),.bind().

- Math.floor(n): returns the largest integeri≤n
    > Math.floor(2.1)
    **2**
    > Math.floor(2.9)
    **2**
- Math.ceil(n): returns the smallest integeri≥n
    > Math.ceil(2.1)
    **3**
    > Math.ceil(2.9)
    **3**
- Math.round(n): returns the integer that is “closest” tonwith__.5being rounded
    up – for example:
       > Math.round(2.4)
       **2**
       > Math.round(2.5)
       **3**
- Math.trunc(n): removesanydecimalfraction(afterthepoint)thatnhas,therefore
    turning it into an integer.
       > Math.trunc(2.1)
       **2**
       > Math.trunc(2.9)
       **2**
For more information on rounding, consult§17.3 “Rounding”.

## 16.9.2 Ranges of integer numbers in JavaScript

These are important ranges of integer numbers in JavaScript:

- **Safeintegers:** canberepresented“safely”byJavaScript(moreonwhatthatmeans
    in the next subsection)
       **-** Precision: 53 bits plus sign
       **-** Range: (−2^53 , 2^53 )
- **Array indices**


```
138 16 Numbers
```
**-** Precision: 32 bits, unsigned
**-** Range: [0, 2^32 −1) (excluding the maximum length)
**-** Typed Arrays have a larger range of 53 bits (safe and unsigned)
- **Bitwise operators** (bitwise Or, etc.)
**-** Precision: 32 bits
**-** Range of unsigned right shift (>>>): unsigned, [0, 2^32 )
**-** Range of all other bitwise operators: signed, [−2^31 , 2^31 )

## 16.9.3 Safe integers

This is the range of integer numbers that are _safe_ in JavaScript (53 bits plus a sign):

```
[–(2^53 )+1, 2^53 –1]
```
An integer is _safe_ if it is represented by exactly one JavaScript number. Given that
JavaScript numbers are encoded as a fraction multiplied by 2 to the power of an
exponent, higher integers can also be represented, but then there are gaps between
them.

```
For example (18014398509481984 is 2^54 ):
```
```
> 18014398509481984
18014398509481984
> 18014398509481985
18014398509481984
> 18014398509481986
18014398509481984
> 18014398509481987
18014398509481988
```
The following properties ofNumberhelp determine if an integer is safe:

```
assert.equal( Number .MAX_SAFE_INTEGER,( 2 ** 53 )- 1 );
assert.equal( Number .MIN_SAFE_INTEGER,- Number .MAX_SAFE_INTEGER);
```
```
assert.equal( Number .isSafeInteger( 5 ), true );
assert.equal( Number .isSafeInteger('5'), false );
assert.equal( Number .isSafeInteger(5.1), false );
assert.equal( Number .isSafeInteger( Number .MAX_SAFE_INTEGER), true );
assert.equal( Number .isSafeInteger( Number .MAX_SAFE_INTEGER+ 1 ), false );
```
```
Exercise: Detecting safe integers
exercises/numbers-math/is_safe_integer_test.mjs
```
```
16.9.3.1 Safe computations
```
```
Let’s look at computations involving unsafe integers.
```
The following result is incorrect and unsafe, even though both of its operands are safe:


```
16.10 Bitwise operators 139
```
### > 9007199254740990 + 3

### 9007199254740992

```
Thefollowingresultissafe,butincorrect. Thefirstoperandisunsafe;thesecondoperand
is safe:
> 9007199254740995 - 10
9007199254740986
Therefore, the result of an expressiona op bis correct if and only if:
isSafeInteger(a)&&isSafeInteger(b)&& isSafeInteger(a op b)
That is, both operands and the result must be safe.
```
**16.10 Bitwise operators**

## 16.10.1 Internally, bitwise operators work with 32-bit integers

```
Internally, JavaScript’s bitwise operators work with 32-bit integers. They produce their
results in the following steps:
```
- Input (JavaScript numbers): The 1–2 operands are first converted to JavaScript
    numbers (64-bit floating point numbers) and then to 32-bit integers.
- Computation (32-bit integers): The actual operation processes 32-bit integers and
    produces a 32-bit integer.
- Output (JavaScript number): Before returning the result, it is converted back to a
    JavaScript number.

```
16.10.1.1 The types of operands and results
For each bitwise operator, this book mentions the types of its operands and its result.
Each type is always one of the following two:
```
```
Type Description Size Range
Int32 signed 32-bit integer 32 bits incl. sign [−2^31 , 2^31 )
Uint32 unsigned 32-bit integer 32 bits [0, 2^32 )
```
Consideringthepreviouslymentionedsteps,Irecommendtopretendthatbitwiseoper-
ators internally work with unsigned 32-bit integers (step “computation”) and that Int32
andUint32onlyaffecthowJavaScriptnumbersareconvertedtoandfromintegers(steps
“input” and “output”).

```
16.10.1.2 Displaying JavaScript numbers as unsigned 32-bit integers
```
```
While exploring the bitwise operators, it occasionally helps to display JavaScript num-
bers as unsigned 32-bit integers in binary notation. That’s whatb32()does (whose im-
plementation is shown later):
```

```
140 16 Numbers
```
```
assert.equal(
b32(- 1 ),
'11111111111111111111111111111111');
assert.equal(
b32( 1 ),
'00000000000000000000000000000001');
assert.equal(
b32( 2 ** 31 ),
'10000000000000000000000000000000');
```
## 16.10.2 Bitwise Not

```
Table 16.7: The bitwise Not operator.
```
```
Operation Name Type signature
~num Bitwise Not, ones’ complement Int32→Int32 ES1
```
The bitwise Not operator (tbl.16.7) inverts each binary digit of its operand:

```
> b32(~0b100)
'11111111111111111111111111111011'
```
This so-called _ones’ complement_ is similar to a negative for some arithmetic operations.
For example, adding an integer to its ones’ complement is always-1:

```
> 4 + ~4
-1
> -11 + ~-11
-1
```
## 16.10.3 Binary bitwise operators

```
Table 16.8: Binary bitwise operators.
```
```
Operation Name Type signature
num1 & num2 Bitwise And Int32 × Int32→Int32 ES1
num1 ¦ num2 Bitwise Or Int32 × Int32→Int32 ES1
num1 ^ num2 Bitwise Xor Int32 × Int32→Int32 ES1
```
The binary bitwise operators (tbl.16.8) combine the bits of their operands to produce
their results:

```
> (0b1010 & 0b0011).toString(2).padStart(4, '0')
'0010'
> (0b1010 | 0b0011).toString(2).padStart(4, '0')
'1011'
```

```
16.10 Bitwise operators 141
```
```
> (0b1010 ^ 0b0011).toString(2).padStart(4, '0')
'1001'
```
## 16.10.4 Bitwise shift operators

```
Table 16.9: Bitwise shift operators.
```
```
Operation Name Type signature
num << count Left shift Int32 × Uint32→Int32 ES1
num >> count Signed right shift Int32 × Uint32→Int32 ES1
num >>> count Unsigned right shift Uint32 × Uint32→Uint32 ES1
```
The shift operators (tbl.16.9) move binary digits to the left or to the right:

```
> (0b10 << 1).toString(2)
'100'
```
```
>>preserves highest bit,>>>doesn’t:
> b32(0b10000000000000000000000000000010 >> 1)
'11000000000000000000000000000001'
> b32(0b10000000000000000000000000000010 >>> 1)
'01000000000000000000000000000001'
```
## 16.10.5 b32(): displaying unsigned 32-bit integers in binary notation

We have now usedb32()a few times. The following code is an implementation of it:

```
/**
* Return a string representing n as a 32-bit unsigned integer,
* in binary notation.
*/
function b32(n) {
// >>> ensures highest bit isn’t interpreted as a sign
return (n>>> 0 ).toString( 2 ).padStart( 32 ,'0');
}
assert.equal(
b32( 6 ),
'00000000000000000000000000000110');
n >>> 0means that we are shiftingnzero bits to the right. Therefore, in principle, the
>>>operator does nothing, but it still coercesnto an unsigned 32-bit integer:
```
```
> 12 >>> 0
12
> -12 >>> 0
4294967284
> (2**32 + 1) >>> 0
1
```

```
142 16 Numbers
```
**16.11 Quick reference: numbers**

## 16.11.1 Global functions for numbers

JavaScript has the following four global functions for numbers:

- isFinite()
- isNaN()
- parseFloat()
- parseInt()
However, it is better to use the corresponding methods ofNumber(Number.isFinite(),
etc.),whichhavefewerpitfalls. TheywereintroducedwithES6andarediscussedbelow.

## 16.11.2 Static properties ofNumber

- .EPSILON: number[ES6]
    The difference between 1 and the next representable floating point number. In
    general,amachineepsilonprovidesanupperboundforroundingerrorsinfloating
    point arithmetic.
       **-** Approximately: 2.2204460492503130808472633361816 × 10-16
- .MAX_SAFE_INTEGER: number[ES6]
    The largest integer that JavaScript can represent unambiguously (2^53 −1).
- .MAX_VALUE: number[ES1]
    The largest positive finite JavaScript number.
       **-** Approximately: 1.7976931348623157 × 10^308
- .MIN_SAFE_INTEGER: number[ES6]
    The smallest integer that JavaScript can represent unambiguously (−2^53 +1).
- .MIN_VALUE: number[ES1]
    The smallest positive JavaScript number. Approximately 5 × 10−324.
- .NaN: number[ES1]
    The same as the global variableNaN.
- .NEGATIVE_INFINITY: number[ES1]
    The same as-Number.POSITIVE_INFINITY.
- .POSITIVE_INFINITY: number[ES1]
    The same as the global variableInfinity.

## 16.11.3 Static methods ofNumber

- .isFinite(num: number): boolean[ES6]
    Returnstrueifnumisanactualnumber(neitherInfinitynor-InfinitynorNaN).


_16.11 Quick reference: numbers_ 143

```
> Number.isFinite(Infinity)
false
> Number.isFinite(-Infinity)
false
> Number.isFinite(NaN)
false
> Number.isFinite(123)
true
```
- .isInteger(num: number): boolean[ES6]
    Returnstrueifnumis a number and does not have a decimal fraction.
       > Number.isInteger(-17)
       **true**
       > Number.isInteger(33)
       **true**
       > Number.isInteger(33.1)
       **false**
       > Number.isInteger('33')
       **false**
       > Number.isInteger(NaN)
       **false**
       > Number.isInteger(Infinity)
       **false**
- .isNaN(num: number): boolean[ES6]
    Returnstrueifnumis the valueNaN:
       > Number.isNaN(NaN)
       **true**
       > Number.isNaN(123)
       **false**
       > Number.isNaN('abc')
       **false**
- .isSafeInteger(num: number): boolean[ES6]
    Returnstrueifnumis a number and unambiguously represents an integer.
- .parseFloat(str: string): number[ES6]
    Coerces its parameter to string and parses it as a floating point number. For con-
verting strings to numbers,Number()(which ignores leading and trailing white-
space)isusuallyabetterchoicethanNumber.parseFloat()(whichignoresleading
whitespace and illegal trailing characters and can hide problems).

```
> Number.parseFloat(' 123.4#')
123.4
> Number(' 123.4#')
NaN
```
- .parseInt(str: string, radix=10): number[ES6]


```
144 16 Numbers
```
```
Coercesitsparametertostringandparsesitasaninteger,ignoringleadingwhite-
space and illegal trailing characters:
> Number.parseInt(' 123#')
123
```
```
The parameterradixspecifies the base of the number to be parsed:
```
```
> Number.parseInt('101', 2)
5
> Number.parseInt('FF', 16)
255
```
```
Donotusethismethodtoconvertnumberstointegers: coercingtostringisineffi-
cient. Andstoppingbeforethefirstnon-digitisnotagoodalgorithmforremoving
the fraction of a number. Here is an example where it goes wrong:
```
```
> Number.parseInt(1e21, 10) // wrong
1
It is better to use one of the rounding functions ofMathto convert a number to an
integer:
```
```
> Math.trunc(1e21) // correct
1e+21
```
## 16.11.4 Methods ofNumber.prototype

(Number.prototypeis where the methods of numbers are stored.)

- .toExponential(fractionDigits?: number): string[ES3]
    Returns a string that represents the number via exponential notation. Withfrac-
    tionDigits,wecanspecify,howmanydigitsshouldbeshownofthenumberthat
    ismultipliedwiththeexponent(thedefaultistoshowasmanydigitsasnecessary).

```
Example: number too small to get a positive exponent via.toString().
```
```
> 1234..toString()
'1234'
```
```
> 1234..toExponential() // 3 fraction digits
'1.234e+3'
> 1234..toExponential(5)
'1.23400e+3'
> 1234..toExponential(1)
'1.2e+3'
```
```
Example: fraction not small enough to get a negative exponent via.toString().
```
```
> 0.003.toString()
'0.003'
> 0.003.toExponential()
'3e-3'
```

_16.11 Quick reference: numbers_ 145

- .toFixed(fractionDigits=0): string[ES3]
    Returnsanexponent-freerepresentationofthenumber,roundedtofractionDig-
    itsdigits.

```
> 0.00000012.toString() // with exponent
'1.2e-7'
```
```
> 0.00000012.toFixed(10) // no exponent
'0.0000001200'
> 0.00000012.toFixed()
'0'
If the number is 10^21 or greater, even.toFixed()uses an exponent:
```
```
> (10 ** 21).toFixed()
'1e+21'
```
- .toPrecision(precision?: number): string[ES3]

```
Works like.toString(), butprecisionspecifies how many digits should be
shown. Ifprecisionis missing,.toString()is used.
```
```
> 1234..toPrecision(3) // requires exponential notation
'1.23e+3'
```
```
> 1234..toPrecision(4)
'1234'
```
```
> 1234..toPrecision(5)
'1234.0'
```
```
> 1.234.toPrecision(3)
'1.23'
```
- .toString(radix=10): string[ES1]

```
Returns a string representation of the number.
```
```
By default, we get a base 10 numeral as a result:
```
```
> 123.456.toString()
'123.456'
If we want the numeral to have a different base, we can specify it viaradix:
```
```
> 4..toString(2) // binary (base 2)
'100'
> 4.5.toString(2)
'100.1'
```
```
> 255..toString(16) // hexadecimal (base 16)
'ff'
> 255.66796875.toString(16)
```

146 _16 Numbers_

```
'ff.ab'
```
```
> 1234567890..toString(36)
'kf12oi'
Number.parseInt()provides the inverse operation: it converts a string that con-
tains an integer (no fraction!) numeral with a given base, to a number.
> Number.parseInt('kf12oi', 36)
1234567890
```
## 16.11.5 Sources

- Wikipedia
- TypeScript’s built-in typings
- MDN web docs for JavaScript
- ECMAScript language specification

```
Quiz: advanced
Seequiz app.
```

**Chapter 17**

**Math**

## Contents

```
17.1 Data properties.............................. 147
17.2 Exponents, roots, logarithms...................... 148
17.3 Rounding................................. 149
17.4 Trigonometric Functions......................... 150
17.5 Various other functions......................... 152
17.6 Sources.................................. 153
```
Mathisanobjectwithdatapropertiesandmethodsforprocessingnumbers. Youcansee
it as a poor man’s module: It was created long before JavaScript had modules.

**17.1 Data properties**

- Math.E: number[ES1]

```
Euler’snumber,baseofthenaturallogarithms,approximately2.7182818284590452354.
```
- Math.LN10: number[ES1]

```
The natural logarithm of 10, approximately 2.302585092994046.
```
- Math.LN2: number[ES1]

```
The natural logarithm of 2, approximately 0.6931471805599453.
```
- Math.LOG10E: number[ES1]

```
The logarithm of e to base 10, approximately 0.4342944819032518.
```
- Math.LOG2E: number[ES1]

```
The logarithm of e to base 2, approximately 1.4426950408889634.
```
- Math.PI: number[ES1]

```
147
```

148 _17 Math_

```
The mathematical constant π, ratio of a circle’s circumference to its diameter, ap-
proximately 3.1415926535897932.
```
- Math.SQRT1_2: number[ES1]

```
The square root of 1/2, approximately 0.7071067811865476.
```
- Math.SQRT2: number[ES1]
    The square root of 2, approximately 1.4142135623730951.

**17.2 Exponents, roots, logarithms**

- Math.cbrt(x: number): number[ES6]

```
Returns the cube root ofx.
```
```
> Math.cbrt(8)
2
```
- Math.exp(x: number): number[ES1]

```
Returns e x( e being Euler’s number). The inverse ofMath.log().
```
```
> Math.exp(0)
1
> Math.exp(1) === Math.E
true
```
- Math.expm1(x: number): number[ES6]

```
ReturnsMath.exp(x)-1. The inverse ofMath.log1p(). Very small numbers (frac-
tions close to 0) are represented with a higher precision. Therefore, this function
returns more precise values whenever.exp()returns values close to 1.
```
- Math.log(x: number): number[ES1]
    Returns the natural logarithm ofx(to base _e_ , Euler’s number). The inverse of
    Math.exp().

```
> Math.log(1)
0
> Math.log(Math.E)
1
> Math.log(Math.E ** 2)
2
```
- Math.log1p(x: number): number[ES6]

```
ReturnsMath.log(1 + x). The inverse ofMath.expm1(). Very small numbers
(fractions close to 0) are represented with a higher precision. Therefore, you can
provide this function with a more precise argument whenever the argument for
.log()is close to 1.
```
- Math.log10(x: number): number[ES6]


_17.3 Rounding_ 149

```
Returns the logarithm ofxto base 10. The inverse of10 ** x.
```
```
> Math.log10(1)
0
> Math.log10(10)
1
> Math.log10(100)
2
```
- Math.log2(x: number): number[ES6]

```
Returns the logarithm ofxto base 2. The inverse of2 ** x.
```
```
> Math.log2(1)
0
> Math.log2(2)
1
> Math.log2(4)
2
```
- Math.pow(x: number, y: number): number[ES1]

```
Returnsxy,xto the power ofy. The same asx ** y.
```
```
> Math.pow(2, 3)
8
> Math.pow(25, 0.5)
5
```
- Math.sqrt(x: number): number[ES1]

```
Returns the square root ofx. The inverse ofx ** 2.
```
```
> Math.sqrt(9)
3
```
**17.3 Rounding**

Roundingmeansconvertinganarbitrarynumbertoaninteger(anumberwithoutadec-
imal fraction). The following functions implement different approaches to rounding.

- Math.ceil(x: number): number[ES1]

```
Returns the smallest (closest to −∞) integeriwithx≤i.
```
```
> Math.ceil(2.1)
3
> Math.ceil(2.9)
3
```
- Math.floor(x: number): number[ES1]

```
Returns the largest (closest to +∞) integeriwithi≤x.
```

```
150 17 Math
```
```
> Math.floor(2.1)
2
> Math.floor(2.9)
2
```
- Math.round(x: number): number[ES1]
    Returns the integer that is closest tox. If the decimal fraction ofxis.5then
    .round()rounds up (to the integer closer to positive infinity):
       > Math.round(2.4)
       **2**
       > Math.round(2.5)
       **3**
- Math.trunc(x: number): number[ES6]
    Removes the decimal fraction ofxand returns the resulting integer.
       > Math.trunc(2.1)
       **2**
       > Math.trunc(2.9)
       **2**

Tbl.17.1shows the results of the rounding functions for a few representative inputs.

```
Table 17.1: Rounding functions ofMath. Note how things change with
negative numbersbecause “larger” alwaysmeans “closertopositive in-
finity”.
```
### -2.9 -2.5 -2.1 2.1 2.5 2.9

```
Math.floor -3 -3 -3 2 2 2
Math.ceil -2 -2 -2 3 3 3
Math.round -3 -2 -2 2 3 3
Math.trunc -2 -2 -2 2 2 2
```
**17.4 Trigonometric Functions**

All angles are specified in radians. Use the following two functions to convert between
degrees and radians.

```
function degreesToRadians(degrees) {
return degrees/ 180 * Math .PI;
}
assert.equal(degreesToRadians( 90 ), Math .PI/ 2 );
```
```
function radiansToDegrees(radians) {
return radians/ Math .PI* 180 ;
}
assert.equal(radiansToDegrees( Math .PI), 180 );
```

_17.4 Trigonometric Functions_ 151

- Math.acos(x: number): number[ES1]

```
Returns the arc cosine (inverse cosine) ofx.
```
```
> Math.acos(0)
1.5707963267948966
> Math.acos(1)
0
```
- Math.acosh(x: number): number[ES6]

```
Returns the inverse hyperbolic cosine ofx.
```
- Math.asin(x: number): number[ES1]

```
Returns the arc sine (inverse sine) ofx.
```
```
> Math.asin(0)
0
> Math.asin(1)
1.5707963267948966
```
- Math.asinh(x: number): number[ES6]

```
Returns the inverse hyperbolic sine ofx.
```
- Math.atan(x: number): number[ES1]

```
Returns the arc tangent (inverse tangent) ofx.
```
- Math.atanh(x: number): number[ES6]

```
Returns the inverse hyperbolic tangent ofx.
```
- Math.atan2(y: number, x: number): number[ES1]

```
Returns the arc tangent of the quotient y/x.
```
- Math.cos(x: number): number[ES1]

```
Returns the cosine ofx.
```
```
> Math.cos(0)
1
> Math.cos(Math.PI)
-1
```
- Math.cosh(x: number): number[ES6]

```
Returns the hyperbolic cosine ofx.
```
- Math.hypot(...values: number[]): number[ES6]

```
Returnsthesquarerootofthesumofthesquaresofvalues(Pythagoras’theorem):
```
```
> Math.hypot(3, 4)
5
```

152 _17 Math_

- Math.sin(x: number): number[ES1]
    Returns the sine ofx.
       > Math.sin(0)
       **0**
       > Math.sin(Math.PI / 2)
       **1**
- Math.sinh(x: number): number[ES6]
    Returns the hyperbolic sine ofx.
- Math.tan(x: number): number[ES1]
    Returns the tangent ofx.
       > Math.tan(0)
       **0**
       > Math.tan(1)
       **1.5574077246549023**
- Math.tanh(x: number): number;[ES6]
    Returns the hyperbolic tangent ofx.

**17.5 Various other functions**

- Math.abs(x: number): number[ES1]

```
Returns the absolute value ofx.
> Math.abs(3)
3
> Math.abs(-3)
3
> Math.abs(0)
0
```
- Math.clz32(x: number): number[ES6]

```
Counts the leading zero bits in the 32-bit integerx. Used in DSP algorithms.
> Math.clz32(0b01000000000000000000000000000000)
1
> Math.clz32(0b00100000000000000000000000000000)
2
> Math.clz32(2)
30
> Math.clz32(1)
31
```
- Math.max(...values: number[]): number[ES1]

```
Convertsvaluesto numbers and returns the largest one.
```

_17.6 Sources_ 153

```
> Math.max(3, -5, 24)
24
```
- Math.min(...values: number[]): number[ES1]
    Convertsvaluesto numbers and returns the smallest one.
       > Math.min(3, -5, 24)
       **-5**
- Math.random(): number[ES1]
    Returns a pseudo-random numbernwhere 0 ≤n< 1.
       /** Returns a random integer i with 0 <= i < max */
       **function** getRandomInteger(max) {
          **returnMath** .floor( **Math** .random()*max);
       }
- Math.sign(x: number): number[ES6]
    Returns the sign of a number:
       > Math.sign(-8)
       **-1**
       > Math.sign(0)
       **0**
       > Math.sign(3)
       **1**

**17.6 Sources**

- Wikipedia
- TypeScript’s built-in typings
- MDN web docs for JavaScript
- ECMAScript language specification


154 _17 Math_


**Chapter 18**

**Bigints – arbitrary-precision**

**integers [ES2020] (advanced)**

## Contents

```
18.1 Why bigints?............................... 156
18.2 Bigints................................... 156
18.2.1 Going beyond 53 bits for integers................ 157
18.2.2 Example: using bigints...................... 157
18.3 Bigint literals............................... 158
18.3.1 Underscores (_) as separators in bigint literals [ES2021].... 158
18.4 Reusing number operators for bigints (overloading)......... 158
18.4.1 Arithmetic operators....................... 159
18.4.2 Ordering operators........................ 159
18.4.3 Bitwise operators......................... 160
18.4.4 Loose equality (==) and inequality (!=)............. 161
18.4.5 Strict equality (===) and inequality (!==)............ 162
18.5 The wrapper constructorBigInt.................... 162
18.5.1BigIntas a constructor and as a function............ 162
18.5.2BigInt.prototype.*methods.................. 163
18.5.3BigInt.*methods........................ 163
18.5.4 Casting and 64-bit integers.................... 164
18.6 Coercing bigints to other primitive types............... 164
18.7 TypedArrays and DataView operations for 64-bit values....... 164
18.8 Bigints and JSON............................ 164
18.8.1 Stringifying bigints........................ 165
18.8.2 Parsing bigints.......................... 165
18.9 FAQ: Bigints............................... 165
18.9.1 How do I decide when to use numbers and when to use bigints? 165
18.9.2 Whynotjustincreasetheprecisionofnumbersinthesameman-
ner as is done for bigints?.................... 166
```
```
155
```

```
156 18 Bigints – arbitrary-precision integers [ES2020] (advanced)
```
```
Inthischapter,wetakealookat bigints ,JavaScript’sintegerswhosestoragespacegrows
and shrinks as needed.
```
**18.1 Why bigints?**

```
Before ECMAScript 2020, JavaScript handled integers as follows:
```
- There only was a single type for floating point numbers and integers: 64-bit float-
    ing point numbers (IEEE 754 double precision).
- Under the hood, most JavaScript engines transparently supported integers: If a
    number has no decimal digits and is within a certain range, it can internally be
    stored as a genuine integer. This representation is called _small integer_ and usually
    fits into 32 bits. For example, the range of small integers on the 64-bit version of
    the V8 engine is from −2^31 to 2^31 −1 (source).
- JavaScript numbers could also represent integers beyond the small integer range,
    as floating point numbers. Here, the safe range is plus/minus 53 bits. For more
    information on this topic, see§16.9.3 “Safe integers”.

```
Sometimes, we need more than signed 53 bits – for example:
```
- Twitteruses64-bitintegersasIDsfortweets(source). InJavaScript,theseIDshad
    to be stored in strings.
- Financial technology uses so-called _big integers_ (integers with arbitrary precision)
    to represent amounts of money. Internally, the amounts are multiplied so that the
    decimal numbers disappear. For example, USD amounts are multiplied by 100 so
    that the cents disappear.

**18.2 Bigints**

_Bigint_ isanewprimitivedatatypeforintegers. Bigintsdon’thaveafixedstoragesizein
bits; their sizes adapt to the integers they represent:

- Small integers are represented with fewer bits than large integers.
- Thereisnonegativelowerlimitorpositiveupperlimitfortheintegersthatcanbe
    represented.

A bigint literal is a sequence of one or more digits, suffixed with ann– for example:

```
123 n
```
Operators such as-and*are overloaded and work with bigints:

```
> 123n * 456n
56088n
```
```
Bigints are primitive values.typeofreturns a new result for them:
> typeof 123n
'bigint'
```

```
18.2 Bigints 157
```
## 18.2.1 Going beyond 53 bits for integers

JavaScript numbers are internally represented as a fraction multiplied by an exponent
(see§16.8“Background: floatingpointprecision”fordetails). Asaconsequence,ifwego
beyondthehighest _safe integer_ 253 −1,therearestill _some_ integersthatcanberepresented,
but with gaps between them:

```
> 2**53 - 2 // safe
9007199254740990
> 2**53 - 1 // safe
9007199254740991
```
```
> 2**53 // unsafe, same as next integer
9007199254740992
> 2**53 + 1
9007199254740992
> 2**53 + 2
9007199254740994
> 2**53 + 3
9007199254740996
> 2**53 + 4
9007199254740996
> 2**53 + 5
9007199254740996
```
```
Bigints enable us to go beyond 53 bits:
```
```
> 2n**53n
9007199254740992n
> 2n**53n + 1n
9007199254740993n
> 2n**53n + 2n
9007199254740994n
```
## 18.2.2 Example: using bigints

This is what using bigints looks like (code based on an example in the proposal):

```
/**
* Takes a bigint as an argument and returns a bigint
*/
function nthPrime(nth) {
if ( typeof nth!=='bigint') {
thrownewTypeError ();
}
function isPrime(p) {
for ( let i= 2 n;i<p;i++) {
if (p%i=== 0 n) returnfalse ;
}
returntrue ;
```

```
158 18 Bigints – arbitrary-precision integers [ES2020] (advanced)
```
### }

```
for ( let i= 2 n;;i++) {
if (isPrime(i)) {
if (--nth=== 0 n) return i;
}
}
}
```
```
assert.deepEqual(
[ 1 n, 2 n, 3 n, 4 n, 5 n].map(nth => nthPrime(nth)),
[ 2 n, 3 n, 5 n, 7 n, 11 n]
);
```
**18.3 Bigint literals**

```
Like number literals, bigint literals support several bases:
```
- Decimal:123n
- Hexadecimal:0xFFn
- Binary:0b1101n
- Octal:0o777n

```
Negative bigints are produced by prefixing the unary minus operator:-0123n
```
## 18.3.1 Underscores (_) as separators in bigint literals [ES2021]

```
Just like in number literals, we can use underscores (_) as separators in bigint literals:
```
```
const massOfEarthInKg=6_000_000_000_000_000_000_000_000n;
```
```
Bigintsareoftenusedtorepresentmoneyinthefinancialtechnicalsector. Separatorscan
help here, too:
```
```
const priceInCents=123_000_00n;// 123 thousand dollars
```
As with number literals, two restrictions apply:

- We can only put an underscore between two digits.
- We can use at most one underscore in a row.

**18.4 Reusing number operators for bigints (overloading)**

With most operators, we are not allowed to mix bigints and numbers. If we do, excep-
tions are thrown:

```
> 2n + 1
TypeError: Cannot mix BigInt and other types, use explicit conversions
```
Thereasonforthisruleisthatthereisnogeneralwayofcoercinganumberandabigintto
a common type: numbers can’t represent bigints beyond 53 bits, bigints can’t represent


_18.4 Reusing number operators for bigints (overloading)_ 159

fractions. Therefore, the exceptions warn us about typos that may lead to unexpected
results.

For example, should the result of the following expression be9007199254740993nor
9007199254740992?

```
2 ** 53 + 1 n
```
It is also not clear what the result of the following expression should be:

```
2 n** 53 n*3.3
```
## 18.4.1 Arithmetic operators

Binary+, binary-,*,**work as expected:

```
> 7n * 3n
21n
```
It is OK to mix bigints and strings:

```
> 6n + ' apples'
'6 apples'
```
/,%round towards zero (likeMath.trunc()):

```
> 1n / 2n
0n
```
Unary-works as expected:

```
> -(-64n)
64n
```
Unary+isnotsupportedforbigintsbecausemuchcodereliesonitcoercingitsoperand
to number:

```
> +23n
TypeError: Cannot convert a BigInt value to a number
```
## 18.4.2 Ordering operators

Ordering operators<,>,>=,<=work as expected:

```
> 17n <= 17n
true
> 3n > -1n
true
```
Comparingbigintsandnumbersdoesnotposeanyrisks. Therefore,wecanmixbigints
and numbers:

```
> 3n > -1
true
```

```
160 18 Bigints – arbitrary-precision integers [ES2020] (advanced)
```
## 18.4.3 Bitwise operators

```
18.4.3.1 Bitwise operators for numbers
```
```
Bitwiseoperatorsinterpretnumbersas32-bitintegers. Theseintegersareeitherunsigned
orsigned. Iftheyaresigned,thenegativeofanintegerisits two’s complement (addingan
integer to its two’s complement – while ignoring overflow – produces zero):
> 2**32-1 >> 0
-1
```
```
Due to these integers having a fixed size, their highest bits indicate their signs:
> 2**31 >> 0 // highest bit is 1
-2147483648
> 2**31 - 1 >> 0 // highest bit is 0
2147483647
```
```
18.4.3.2 Bitwise operators for bigints
For bigints, bitwise operators interpret a negative sign as an infinite two’s complement
```
- for example:
    - -1is···111111(ones extend infinitely to the left)
    - -2is···111110
    - -3is···111101
    - -4is···111100

That is, a negative sign is more of an external flag and not represented as an actual bit.

```
18.4.3.3 Bitwise Not (~)
```
```
Bitwise Not (~) inverts all bits:
> ~0b10n
-3n
> ~0n
-1n
> ~-2n
1n
```
```
18.4.3.4 Binary bitwise operators (&,|,^)
```
Applying binary bitwise operators to bigints works analogously to applying them to
numbers:
> (0b1010n | 0b0111n).toString(2)
**'1111'**
> (0b1010n & 0b0111n).toString(2)
**'10'**

```
> (0b1010n | -1n).toString(2)
'-1'
```

```
18.4 Reusing number operators for bigints (overloading) 161
```
```
> (0b1010n & -1n).toString(2)
'1010'
```
```
18.4.3.5 Bitwise signed shift operators (<<and>>)
```
The signed shift operators for bigints preserve the sign of a number:

```
> 2n << 1n
4n
> -2n << 1n
-4n
```
```
> 2n >> 1n
1n
> -2n >> 1n
-1n
Recallthat-1nisasequenceofonesthatextendsinfinitelytotheleft. That’swhyshifting
it left doesn’t change it:
> -1n >> 20n
-1n
```
```
18.4.3.6 Bitwise unsigned right shift operator (>>>)
```
There is no unsigned right shift operator for bigints:

```
> 2n >>> 1n
TypeError: BigInts have no unsigned right shift, use >> instead
```
Why? The idea behind unsigned right shifting is that a zero is shifted in “from the left”.
In other words, the assumption is that there is a finite amount of binary digits.
However, with bigints, there is no “left”, their binary digits extend infinitely. This is
especially important with negative numbers.
Signedrightshiftworksevenwithaninfinitenumberofdigitsbecausethehighestdigit
is preserved. Therefore, it can be adapted to bigints.

## 18.4.4 Loose equality (==) and inequality (!=)

```
Loose equality (==) and inequality (!=) coerce values:
> 0n == false
true
> 1n == true
true
```
```
> 123n == 123
true
```
```
> 123n == '123'
true
```

```
162 18 Bigints – arbitrary-precision integers [ES2020] (advanced)
```
## 18.4.5 Strict equality (===) and inequality (!==)

```
Strict equality (===) and inequality (!==) only consider values to be equal if they have
the same type:
> 123n === 123
false
> 123n === 123n
true
```
**18.5 The wrapper constructorBigInt**

Analogously to numbers, bigints have the associated wrapper constructorBigInt.

## 18.5.1 BigIntas a constructor and as a function

- new BigInt(): throws aTypeError.
- BigInt(x)convertsarbitraryvaluesxtobigint. ThisworkssimilarlytoNumber(),
    with several differences which are summarized in tbl.18.1and explained in more
    detail in the following subsections.

```
Table 18.1: Converting values to bigints.
```
```
x BigInt(x)
undefined ThrowsTypeError
null ThrowsTypeError
boolean false → 0n,true → 1n
number Example:123 → 123n
Non-integer→throwsRangeError
bigint x(no change)
string Example:'123' → 123n
Unparsable→throwsSyntaxError
symbol ThrowsTypeError
object Configurable (e.g. via.valueOf())
```
```
18.5.1.1 Convertingundefinedandnull
```
ATypeErroris thrown ifxis eitherundefinedornull:

```
> BigInt(undefined)
TypeError: Cannot convert undefined to a BigInt
> BigInt(null)
TypeError: Cannot convert null to a BigInt
```
```
18.5.1.2 Converting strings
```
```
If a string does not represent an integer,BigInt()throws aSyntaxError(whereasNum-
ber()returns the error valueNaN):
```

```
18.5 The wrapper constructorBigInt 163
```
```
> BigInt('abc')
SyntaxError: Cannot convert abc to a BigInt
```
The suffix'n'is not allowed:

```
> BigInt('123n')
SyntaxError: Cannot convert 123n to a BigInt
```
All bases of bigint literals are allowed:

```
> BigInt('123')
123n
> BigInt('0xFF')
255n
> BigInt('0b1101')
13n
> BigInt('0o777')
511n
```
```
18.5.1.3 Non-integer numbers produce exceptions
```
```
> BigInt(123.45)
RangeError: The number 123.45 cannot be converted to a BigInt because
it is not an integer
> BigInt(123)
123n
```
```
18.5.1.4 Converting objects
```
```
How objects are converted to bigints can be configured – for example, by overriding
.valueOf():
```
```
> BigInt({valueOf() {return 123n}})
123n
```
## 18.5.2 BigInt.prototype.*methods

```
BigInt.prototypeholds the methods “inherited” by primitive bigints:
```
- BigInt.prototype.toLocaleString(locales?, options?)
- BigInt.prototype.toString(radix?)
- BigInt.prototype.valueOf()

## 18.5.3 BigInt.*methods

- BigInt.asIntN(width, theInt)
    CaststheInttowidthbits (signed). This influences how the value is represented
    internally.
- BigInt.asUintN(width, theInt)
    CaststheInttowidthbits (unsigned).


```
164 18 Bigints – arbitrary-precision integers [ES2020] (advanced)
```
## 18.5.4 Casting and 64-bit integers

```
Casting allows us to create integer values with a specific number of bits. If we want to
restrict ourselves to just 64-bit integers, we have to always cast:
const uint64a= BigInt .asUintN( 64 , 12345 n);
const uint64b= BigInt .asUintN( 64 , 67890 n);
const result= BigInt .asUintN( 64 ,uint64a*uint64b);
```
**18.6 Coercing bigints to other primitive types**

This table show what happens if we convert bigints to other primitive types:

```
Convert to Explicit conversion Coercion (implicit conversion)
boolean Boolean(0n) → false !0n → true
Boolean(int) → true !int → false
number Number(7n) → 7(example) +int → TypeError(1)
string String(7n) → '7'(example) ''+7n → '7'(example)
```
```
Footnote:
```
- (1) Unary+is not supported for bigints, because much code relies on it coercing
    its operand to number.

```
18.7 TypedArraysandDataViewoperationsfor64-bitval-
ues
```
Thanks to bigints, Typed Arrays and DataViews can support 64-bit values:

- Typed Array constructors:
    **-** BigInt64Array
    **-** BigUint64Array
- DataView methods:
    **-** DataView.prototype.getBigInt64()
    **-** DataView.prototype.setBigInt64()
    **-** DataView.prototype.getBigUint64()
    **-** DataView.prototype.setBigUint64()

**18.8 Bigints and JSON**

TheJSONstandardisfixedandwon’tchange. TheupsideisthatoldJSONparsingcode
will never be outdated. The downside is that JSON can’t be extended to contain bigints.

```
Stringifying bigints throws exceptions:
```
```
> JSON.stringify(123n)
TypeError: Do not know how to serialize a BigInt
```

```
18.9 FAQ: Bigints 165
```
```
> JSON.stringify([123n])
TypeError: Do not know how to serialize a BigInt
```
## 18.8.1 Stringifying bigints

Therefore, our best option is to store bigints in strings:

```
const bigintPrefix='[[bigint]]';
```
```
function bigintReplacer(_key,value) {
if ( typeof value==='bigint') {
return bigintPrefix+value;
}
return value;
}
```
```
const data={value: 9007199254740993 n };
assert.equal(
JSON .stringify(data,bigintReplacer),
'{"value":"[[bigint]]9007199254740993"}'
);
```
## 18.8.2 Parsing bigints

The following code shows how to parse strings such as the one that we have produced
in the previous example.

```
function bigintReviver(_key,value) {
if ( typeof value==='string'&&value.startsWith(bigintPrefix)) {
returnBigInt (value.slice(bigintPrefix.length));
}
return value;
}
```
```
const str='{"value":"[[bigint]]9007199254740993"}';
assert.deepEqual(
JSON .parse(str,bigintReviver),
{value: 9007199254740993 n }
);
```
**18.9 FAQ: Bigints**

## 18.9.1 HowdoIdecidewhentousenumbersandwhentousebigints?

```
My recommendations:
```
- Use numbers for up to 53 bits and for Array indices. Rationale: They already
    appeareverywhereandarehandledefficientlybymostengines(especiallyifthey
    fit into 31 bits). Appearances include:


```
166 18 Bigints – arbitrary-precision integers [ES2020] (advanced)
```
**-** Array.prototype.forEach()
**-** Array.prototype.entries()
- Use bigints for large numeric values: If your fraction-less values don’t fit into 53
bits, you have no choice but to move to bigints.

All existing web APIs return and accept only numbers and will only upgrade to bigint
on a case-by-case basis.

## 18.9.2 Why not just increase the precision of numbers in the same

## manner as is done for bigints?

One could conceivably splitnumberintointegeranddouble, but that would add many
newcomplexitiestothelanguage(severalinteger-onlyoperatorsetc.). I’vesketchedthe
consequences ina Gist.

```
Acknowledgements:
```
- Thanks to Daniel Ehrenberg for reviewing an earlier version of this content.
- Thanks to Dan Callahan for reviewing an earlier version of this content.


**Chapter 19**

**Unicode – a brief introduction**

**(advanced)**

## Contents

```
19.1 Code points vs. code units........................ 167
19.1.1 Code points............................ 168
19.1.2 Encoding Unicode code points: UTF-32, UTF-16, UTF-8.... 168
19.2 Encodings used in web development: UTF-16 and UTF-8...... 170
19.2.1 Source code internally: UTF-16................. 170
19.2.2 Strings: UTF-16.......................... 170
19.2.3 Source code in files: UTF-8.................... 170
19.3 Grapheme clusters – the real characters................ 171
19.3.1 Grapheme clusters vs. glyphs.................. 171
```
```
Unicodeisastandardforrepresentingandmanagingtextinmostoftheworld’swriting
systems. Virtually all modern software that works with text, supports Unicode. The
standard is maintained by the Unicode Consortium. A new version of the standard is
published every year (with new emojis, etc.). Unicode version 1.0.0 was published in
October 1991.
```
**19.1 Code points vs. code units**

Two concepts are crucial for understanding Unicode:

- _Code points_ are numbers that represent the atomic parts of Unicode text. Most of
    them represent visible symbols but they can also have other meanings such as
    specifying an aspect of a symbol (the accent of a letter, the skin tone of an emoji,
    etc.).
- _Code units_ are numbers that encode code points, to store or transmit Unicode text.
    One or more code units encode a single code point. Each code unit has the same

```
167
```

```
168 19 Unicode – a brief introduction (advanced)
```
```
size, which depends on the encoding format that is used. The most popular format,
UTF-8, has 8-bit code units.
```
## 19.1.1 Code points

ThefirstversionofUnicodehad16-bitcodepoints. Sincethen,thenumberofcharacters
has grown considerably and the size of code points was extended to 21 bits. These 21
bits are partitioned in 17 planes, with 16 bits each:

- Plane 0: **Basic Multilingual Plane (BMP)** , 0x0000–0xFFFF
    **-** Containscharactersforalmostallmodernlanguages(Latincharacters,Asian
       characters, etc.) and many symbols.
- Plane 1: Supplementary Multilingual Plane (SMP), 0x10000–0x1FFFF
    **-** Supportshistoricwritingsystems(e.g.,Egyptianhieroglyphsandcuneiform)
       and additional modern writing systems.
    **-** Supports emojis and many other symbols.
- Plane 2: Supplementary Ideographic Plane (SIP), 0x20000–0x2FFFF
    **-** Contains additional CJK (Chinese, Japanese, Korean) ideographs.
- Plane 3–13: Unassigned
- Plane 14: Supplementary Special-Purpose Plane (SSP), 0xE0000–0xEFFFF
    **-** Containsnon-graphicalcharacterssuchastagcharactersandglyphvariation
       selectors.
- Plane 15–16: Supplementary Private Use Area (S PUA A/B), 0x0F0000–0x10FFFF
    **-** Available for character assignment by parties outside the ISO and the Uni-
       code Consortium. Not standardized.

```
Planes 1-16 are called supplementary planes or astral planes.
```
```
Let’s check the code points of a few characters:
```
```
> 'A'.codePointAt(0).toString(16)
'41'
> 'ü'.codePointAt(0).toString(16)
'fc'
> 'π'.codePointAt(0).toString(16)
'3c0'
> '☺'.codePointAt(0).toString(16)
'1f642'
```
The hexadecimal numbers of the code points tell us that the first three characters reside
in plane 0 (within 16 bits), while the emoji resides in plane 1.

## 19.1.2 Encoding Unicode code points: UTF-32, UTF-16, UTF-8

The main ways of encoding code points are three _Unicode Transformation Formats_ (UTFs):
UTF-32,UTF-16,UTF-8. Thenumberattheendofeachformatindicatesthesize(inbits)
of its code units.


```
19.1 Code points vs. code units 169
```
```
19.1.2.1 UTF-32 (Unicode Transformation Format 32)
UTF-32 uses 32 bits to store code units, resulting in one code unit per code point. This
formatistheonlyonewith fixed-length encoding ;allothersuseavaryingnumberofcode
units to encode a single code point.
```
```
19.1.2.2 UTF-16 (Unicode Transformation Format 16)
UTF-16 uses 16-bit code units. It encodes code points as follows:
```
- The BMP (first 16 bits of Unicode) is stored in single code units.
- Astral planes: The BMP comprises 0x10_000 code points. Given that Unicode has
    a total of 0x110_000 code points, we still need to encode the remaining 0x100_000
    code points (20 bits). The BMP has two ranges of unassigned code points that
    provide the necessary storage:
       **-** Most significant 10 bits ( _leading surrogate_ ): 0xD800-0xDBFF
       **-** Least significant 10 bits ( _trailing surrogate_ ): 0xDC00-0xDFFF
Inotherwords,thetwohexadecimaldigitsattheendcontribute8bits. Butwecanonly
use those 8 bits if a BMP starts with one of the following 2-digit pairs:
- D8, D9, DA, DB
- DC, DD, DE, DF
Per surrogate, we have a choice between 4 pairs, which is where the remaining 2 bits
come from.

As a consequence, each UTF-16 code unit is always either a leading surrogate, a trailing
surrogate, or encodes a BMP code point.

These are two examples of UTF-16-encoded code points:

- Code point 0x03C0 (π) is in the BMP and can therefore be represented by a single
    UTF-16 code unit: 0x03C0.
- Code point 0x1F642 (☺) is in an astral plane and represented by two code units:
    0xD83D and 0xDE42.

```
19.1.2.3 UTF-8 (Unicode Transformation Format 8)
UTF-8 has 8-bit code units. It uses 1–4 code units to encode a code point:
```
```
Code points Code units
0000–007F 0bbbbbbb (7 bits)
0080–07FF 110bbbbb, 10bbbbbb (5+6 bits)
0800–FFFF 1110bbbb, 10bbbbbb, 10bbbbbb (4+6+6 bits)
10000–1FFFFF 11110bbb, 10bbbbbb, 10bbbbbb, 10bbbbbb (3+6+6+6 bits)
```
```
Notes:
```
- The bit prefix of each code unit tells us:
    **-** Is it first in a series of code units? If yes, how many code units will follow?


```
170 19 Unicode – a brief introduction (advanced)
```
**-** Is it second or later in a series of code units?
- Thecharactermappingsinthe0000–007FrangearethesameasASCII,whichleads
to a degree of backward compatibility with older software.

Three examples:

```
Character Code point Code units
A 0x0041 01000001
π 0x03C0 11001111, 10000000
☺ 0x1F642 11110000, 10011111, 10011001, 10000010
```
```
19.2 Encodings used in web development: UTF-16 and
UTF-8
```
TheUnicodeencodingformatsthatareusedinwebdevelopmentare: UTF-16andUTF-
8.

## 19.2.1 Source code internally: UTF-16

The ECMAScript specification internally represents source code as UTF-16.

## 19.2.2 Strings: UTF-16

The characters in JavaScript strings are based on UTF-16 code units:

```
> const smiley = '☺';
> smiley.length
2
> smiley === '\uD83D\uDE42' // code units
true
```
FormoreinformationonUnicodeandstrings,consult§20.7“Atomsoftext: codepoints,
JavaScript characters, grapheme clusters”.

## 19.2.3 Source code in files: UTF-8

```
HTML and JavaScript are almost always encoded as UTF-8 these days.
```
```
For example, this is how HTML files usually start now:
```
```
<!doctypehtml>
<html>
<head>
<meta charset="UTF-8" >
···
```
```
For HTML modules loaded in web browsers, thestandard encodingis also UTF-8.
```

```
19.3 Grapheme clusters – the real characters 171
```
**19.3 Grapheme clusters – the real characters**

The concept of a character becomes remarkably complex once we consider the various
writing systems of the world. That’s why there are several different Unicode terms that
all mean “character” in some way: _code point_ , _grapheme cluster_ , _glyph_ , etc.
In Unicode, a _code point_ is an atomic part of text.
However, a _grapheme cluster_ corresponds most closely to a symbol displayed on screen
or paper. It is defined as “a horizontally segmentable unit of text”. Therefore,official
Unicode documentsalso call it a _user-perceived character_. One or more code points are
needed to encode a grapheme cluster.
For example, the Devanagari _kshi_ is encoded by 4 code points. We useArray.from()to
split a string into an Array with code points (for details, consult§20.7.1 “Working with
code points”):

```
Flag emojis are also grapheme clusters and composed of two code points – for example,
the flag of Japan:
```
## 19.3.1 Grapheme clusters vs. glyphs

A symbol is an abstract concept and part of written language:

- It is represented in computer memory by a _grapheme cluster_ – a sequence of one or
    more numbers (code points).
- It is drawn on screen via _glyphs_. A glyph is an image and usually stored in a font.
    More than one glyph may be used to draw a single symbol – for example, the
    symbol “é” may be drawn by combining the glyph “e” with the glyph “ ́”.

The distinction between a concept and its representation is subtle and can blur when
talking about Unicode.

```
More information on grapheme clusters
For more information, consult“Let’s Stop Ascribing Meaning to Code Points”by
Manish Goregaokar.
```
```
Quiz
```

172 _19 Unicode – a brief introduction (advanced)_

```
Seequiz app.
```

**Chapter 20**

**Strings**

## Contents

```
20.1 Cheat sheet: strings........................... 174
20.1.1 Working with strings....................... 174
20.1.2 JavaScript characters vs. code points vs. grapheme clusters.. 175
20.1.3 String methods.......................... 175
20.2 Plain string literals............................ 176
20.2.1 Escaping.............................. 177
20.3 Accessing JavaScript characters..................... 177
20.4 String concatenation via+........................ 178
20.5 Converting to string........................... 178
20.5.1 Stringifying objects........................ 179
20.5.2 Customizing the stringification of objects............ 179
20.5.3 An alternate way of stringifying values............. 180
20.6 Comparing strings............................ 180
20.7 Atoms of text: code points, JavaScript characters, grapheme clusters 180
20.7.1 Working with code points.................... 181
20.7.2 Working with code units (char codes).............. 182
20.7.3 ASCII escapes........................... 182
20.7.4 Caveat: grapheme clusters.................... 183
20.8 Quick reference: Strings......................... 183
20.8.1 Converting to string....................... 183
20.8.2 Numeric values of text atoms.................. 183
20.8.3String.prototype: finding and matching........... 184
20.8.4String.prototype: extracting.................. 186
20.8.5String.prototype: combining.................. 187
20.8.6String.prototype: transforming................ 187
20.8.7 Sources.............................. 190
```
```
173
```

174 _20 Strings_

**20.1 Cheat sheet: strings**

Strings are primitive values in JavaScript and immutable. That is, string-related opera-
tions always produce new strings and never change existing strings.

## 20.1.1 Working with strings

Literals for strings:

```
const str1='Don\'t say "goodbye"';// string literal
const str2="Don't say\"goodbye\"";// string literals
assert.equal(
`As easy as${ 123 }!`,// template literal
'As easy as 123!',
);
```
Backslashes are used to:

- Escape literal delimiters (first 2 lines of previous example)
- Represent special characters:
    **-** \\represents a backslash
    **-** \nrepresents a newline
    **-** \rrepresents a carriage return
    **-** \trepresents a tab

Inside aString.rawtagged template (line A), backslashes are treated as normal charac-
ters:

```
assert.equal(
String .raw`\ \n\t`,// (A)
'\\ \\n\\t',
);
```
Convertings values to strings:

```
> String(undefined)
'undefined'
> String(null)
'null'
> String(123.45)
'123.45'
> String(true)
'true'
```
Copying parts of a string

```
// There is no type for characters;
// reading characters produces strings:
const str3='abc';
assert.equal(
str3[ 2 ],'c'// no negative indices allowed
);
assert.equal(
```

```
20.1 Cheat sheet: strings 175
```
```
str3.at(- 1 ),'c'// negative indices allowed
);
```
```
// Copying more than one character:
assert.equal(
'abc'.slice( 0 , 2 ),'ab'
);
```
```
Concatenating strings:
```
```
assert.equal(
'I bought '+ 3 +' apples',
'I bought 3 apples',
);
```
```
let str='';
str+= 'I bought ';
str+= 3 ;
str+= ' apples';
assert.equal(
str,'I bought 3 apples',
);
```
## 20.1.2 JavaScript characters vs. code points vs. grapheme clusters

```
JavaScript characters are 16 bits in size. They are what is indexed in strings and what
.lengthcounts.
```
```
Code points are the atomic parts of Unicode text. Most of them fit into one JavaScript
character, some of them occupy two (especially emojis):
```
```
assert.equal(
'A'.length, 1
);
assert.equal(
'☺'.length, 2
);
```
```
Grapheme clusters ( user-perceived characters ) represent written symbols. Each one com-
prises one or more code points.
```
```
Due to these facts, we shouldn’t split text into JavaScript characters, we should split it
into graphemes. For more information on how to handle text, see§20.7 “Atoms of text:
code points, JavaScript characters, grapheme clusters”.
```
## 20.1.3 String methods

ThissubsectiongivesabriefoverviewofthestringAPI.Thereisamorecomprehensive
quick referenceat the end of this chapter.

```
Finding substrings:
```

176 _20 Strings_

```
> 'abca'.includes('a')
true
> 'abca'.startsWith('ab')
true
> 'abca'.endsWith('ca')
true
```
```
> 'abca'.indexOf('a')
0
> 'abca'.lastIndexOf('a')
3
```
Splitting and joining:

```
assert.deepEqual(
'a, b,c'.split(/,?/),
['a','b','c']
);
assert.equal(
['a','b','c'].join(', '),
'a, b, c'
);
```
Padding and trimming:

```
> '7'.padStart(3, '0')
'007'
> 'yes'.padEnd(6, '!')
'yes!!!'
```
```
> '\t abc\n '.trim()
'abc'
> '\t abc\n '.trimStart()
'abc\n '
> '\t abc\n '.trimEnd()
'\t abc'
```
Repeating and changing case:

```
> '*'.repeat(5)
'*****'
> '= b2b ='.toUpperCase()
'= B2B ='
> 'ΑΒΓ'.toLowerCase()
'αβγ'
```
**20.2 Plain string literals**

Plain string literals are delimited by either single quotes or double quotes:


```
20.3 Accessing JavaScript characters 177
```
```
const str1='abc';
const str2="abc";
assert.equal(str1,str2);
```
```
Single quotes are used more often because it makes it easier to mention HTML, where
double quotes are preferred.
```
```
The next chaptercovers template literals , which give us:
```
- String interpolation
- Multiple lines
- Raw string literals (backslash has no special meaning)

## 20.2.1 Escaping

The backslash lets us create special characters:

- Unix line break:'\n'
- Windows line break:'\r\n'
- Tab:'\t'
- Backslash:'\\'

The backslash also lets us use the delimiter of a string literal inside that literal:

```
assert.equal(
'She said: "Let\'s go!"',
"She said:\"Let's go!\"");
```
**20.3 Accessing JavaScript characters**

```
JavaScript has no extra data type for characters – characters are always represented as
strings.
```
```
const str='abc';
```
```
// Reading a JavaScript character at a given index
assert.equal(str[ 1 ],'b');
```
```
// Counting the JavaScript characters in a string:
assert.equal(str.length, 3 );
```
Thecharactersweseeonscreenarecalled _graphemeclusters_. Mostofthemarerepresented
by single JavaScript characters. However, there are also grapheme clusters (especially
emojis) that are represented by multiple JavaScript characters:

```
> '☺'.length
2
```
```
Howthatworksisexplainedin§20.7“Atomsoftext: codepoints,JavaScriptcharacters,
grapheme clusters”.
```

```
178 20 Strings
```
**20.4 String concatenation via+**

```
Ifatleastoneoperandisastring,theplusoperator(+)convertsanynon-stringstostrings
and concatenates the result:
```
```
assert.equal( 3 +' times '+ 4 ,'3 times 4');
```
The assignment operator+=is useful if we want to assemble a string, piece by piece:

```
let str='';// must be `let`!
str+='Say it';
str+=' one more';
str+=' time';
```
```
assert.equal(str,'Say it one more time');
```
```
Concatenating via+is efficient
Using+toassemblestringsisquiteefficientbecausemostJavaScriptenginesinter-
nally optimize it.
```
```
Exercise: Concatenating strings
exercises/strings/concat_string_array_test.mjs
```
**20.5 Converting to string**

These are three ways of converting a valuexto a string:

- String(x)
- ''+x
- x.toString()(does not work forundefinedandnull)
Recommendation: use the descriptive and safeString().
Examples:
assert.equal( **String** ( **undefined** ),'undefined');
assert.equal( **String** ( **null** ),'null');

```
assert.equal( String ( false ),'false');
assert.equal( String ( true ),'true');
```
```
assert.equal( String (123.45),'123.45');
Pitfall for booleans: If we convert a boolean to a string viaString(), we generally can’t
convert it back viaBoolean():
> String(false)
'false'
```

```
20.5 Converting to string 179
```
```
> Boolean('false')
true
```
The only string for whichBoolean()returnsfalse, is the empty string.

## 20.5.1 Stringifying objects

```
Plain objects have a default string representation that is not very useful:
```
```
> String({a: 1})
'[object Object]'
```
Arrays have a better string representation, but it still hides much information:

```
> String(['a', 'b'])
'a,b'
> String(['a', ['b']])
'a,b'
```
```
> String([1, 2])
'1,2'
> String(['1', '2'])
'1,2'
```
```
> String([true])
'true'
> String(['true'])
'true'
> String(true)
'true'
```
```
Stringifying functions, returns their source code:
```
```
> String(function f() {return 4})
'function f() {return 4}'
```
## 20.5.2 Customizing the stringification of objects

We can override the built-in way of stringifying objects by implementing the method
toString():

```
const obj={
toString() {
return 'hello';
}
};
```
```
assert.equal( String (obj),'hello');
```

```
180 20 Strings
```
## 20.5.3 An alternate way of stringifying values

The JSON data format is a text representation of JavaScript values. Therefore,JSON.
stringify()can also be used to convert values to strings:

```
> JSON.stringify({a: 1})
'{"a":1}'
> JSON.stringify(['a', ['b']])
'["a",["b"]]'
```
The caveat is that JSON only supportsnull, booleans, numbers, strings, Arrays, and
objects (which it always treats as if they were created by object literals).

Tip: The third parameter lets us switch on multiline output and specify how much to
indent – for example:

```
console .log( JSON .stringify({first:'Jane',last:'Doe'}, null , 2 ));
```
This statement produces the following output:

```
{
"first": "Jane",
"last": "Doe"
}
```
**20.6 Comparing strings**

```
Strings can be compared via the following operators:
```
```
< <= > >=
```
There is one important caveat to consider: These operators compare based on the nu-
meric values of JavaScriptcharacters. That means that the order thatJavaScriptuses for
strings is different from the one used in dictionaries and phone books:

```
> 'A' < 'B' // ok
true
> 'a' < 'B' // not ok
false
> 'ä' < 'b' // not ok
false
```
```
Properlycomparingtextisbeyondthescopeofthisbook. ItissupportedviatheECMA-
Script Internationalization API (Intl).
```
```
20.7 Atoms of text: code points, JavaScript characters,
grapheme clusters
```
```
Quick recap of§19 “Unicode – a brief introduction”:
```
- _Code points_ are the atomic parts of Unicode text. Each code point is 21 bits in size.


```
20.7 Atoms of text: code points, JavaScript characters, grapheme clusters 181
```
- JavaScriptstringsimplementUnicodeviatheencodingformatUTF-16. Itusesone
    or two 16-bit _code units_ to encode a single code point.
       **-** Each JavaScript character (as indexed in strings) is a code unit. In the
          JavaScript standard library, code units are also called _char codes_.
- _Graphemeclusters_ ( _user-perceivedcharacters_ )representwrittensymbols,asdisplayed
    on screen or paper. One or more code points are needed to encode a single
    grapheme cluster.

The following code demonstrates that a single code point comprises one or two
JavaScript characters. We count the latter via.length:
// 3 code points, 3 JavaScript characters:
assert.equal('abc'.length, 3 );

```
// 1 code point, 2 JavaScript characters:
assert.equal('☺'.length, 2 );
```
The following table summarizes the concepts we have just explored:

```
Entity Size Encoded via
JavaScript character (UTF-16 code unit) 16 bits –
Unicode code point 21 bits 1–2 code units
Unicode grapheme cluster 1+ code points
```
## 20.7.1 Working with code points

```
Let’s explore JavaScript’s tools for working with code points.
```
A _Unicode code point escape_ lets us specify a code point hexadecimally (1–5 digits). It pro-
duces one or two JavaScript characters.

```
> '\u{1F642}'
'☺'
```
```
Unicode escape sequences
In the ECMAScript language specification, Unicode code point escapes and Unicode
code unit escapes (which we’ll encounter later) are called Unicode escape sequences.
```
```
String.fromCodePoint()converts a single code point to 1–2 JavaScript characters:
```
```
> String.fromCodePoint(0x1F642)
'☺'
```
```
.codePointAt()converts 1–2 JavaScript characters to a single code point:
```
```
> '☺'.codePointAt(0).toString(16)
'1f642'
```

```
182 20 Strings
```
Wecan _iterate_ overastring,whichvisitscodepoints(notJavaScriptcharacters). Iteration
is describedlater in this book. One way of iterating is via afor-ofloop:

```
const str='☺a';
assert.equal(str.length, 3 );
```
```
for ( const codePointChar of str) {
console .log(codePointChar);
}
```
```
// Output:
// '☺'
// 'a'
```
```
Array.from()is also based on iteration and visits code points:
```
```
> Array.from('☺a')
[ '☺', 'a' ]
```
That makes it a good tool for counting code points:

```
> Array.from('☺a').length
2
> '☺a'.length
3
```
## 20.7.2 Working with code units (char codes)

IndicesandlengthsofstringsarebasedonJavaScriptcharacters(asrepresentedbyUTF-
16 code units).

To specify a code unit hexadecimally, we can use a _Unicode code unit escape_ with exactly
four hexadecimal digits:

```
> '\uD83D\uDE42'
'☺'
```
And we can useString.fromCharCode(). _Char code_ is the standard library’s name for
_code unit_ :

```
> String.fromCharCode(0xD83D) + String.fromCharCode(0xDE42)
'☺'
```
To get the char code of a character, use.charCodeAt():

```
> '☺'.charCodeAt(0).toString(16)
'd83d'
```
## 20.7.3 ASCII escapes

If the code point of a character is below 256, we can refer to it via a _ASCII escape_ with
exactly two hexadecimal digits:


```
20.8 Quick reference: Strings 183
```
```
> 'He\x6C\x6Co'
'Hello'
```
(TheofficialnameofASCIIescapesis _Hexadecimalescapesequences_ –itwasthefirstescape
that used hexadecimal numbers.)

## 20.7.4 Caveat: grapheme clusters

Whenworkingwithtextthatmaybewritteninanyhumanlanguage,it’sbesttosplitat
the boundaries of grapheme clusters, not at the boundaries of code points.

TC39 is working onIntl.Segmenter, a proposal for the ECMAScript Internationaliza-
tion API to support Unicode segmentation (along grapheme cluster boundaries, word
boundaries, sentence boundaries, etc.).
Untilthatproposalbecomesastandard,wecanuseoneofseverallibrariesthatareavail-
able (do a web search for “JavaScript grapheme”).

**20.8 Quick reference: Strings**

## 20.8.1 Converting to string

Tbl.20.2describes how various values are converted to strings.

```
Table 20.2: Converting values to strings.
```
```
x String(x)
undefined 'undefined'
null 'null'
boolean false → 'false',true → 'true'
number Example:123 → '123'
bigint Example:123n → '123'
string x(input, unchanged)
symbol Example:Symbol('abc') → 'Symbol(abc)'
object Configurable via, e.g.,toString()
```
## 20.8.2 Numeric values of text atoms

- **Charcode** : numberrepresentingaJavaScriptcharacter. JavaScript’snamefor _Uni-_
    _code code unit_.
       **-** Size: 16 bits, unsigned
       **-** Convert number to string:String.fromCharCode()[ES1]
       **-** Convert string to number: string method.charCodeAt()[ES1]
- **Code point** : number representing an atomic part of Unicode text.
    **-** Size: 21 bits, unsigned (17 planes, 16 bits each)
    **-** Convert number to string:String.fromCodePoint()[ES6]
    **-** Convert string to number: string method.codePointAt()[ES6]


```
184 20 Strings
```
## 20.8.3 String.prototype: finding and matching

(String.prototypeis where the methods of strings are stored.)

- .endsWith(searchString: string, endPos=this.length): boolean[ES6]
    ReturnstrueifthestringwouldendwithsearchStringifitslengthwereendPos.
    Returnsfalseotherwise.

```
> 'foo.txt'.endsWith('.txt')
true
> 'abcde'.endsWith('cd', 4)
true
```
- .includes(searchString: string, startPos=0): boolean[ES6]
    Returnstrueif the string contains thesearchStringandfalseotherwise. The
    search starts atstartPos.
       > 'abc'.includes('b')
       **true**
       > 'abc'.includes('b', 2)
       **false**
- .indexOf(searchString: string, minIndex=0): number[ES1]
    Returns the lowest index at whichsearchStringappears within the string or-1,
    otherwise. Any returned index will beminIndex‘ or higher.
       > 'abab'.indexOf('a')
       **0**
       > 'abab'.indexOf('a', 1)
       **2**
       > 'abab'.indexOf('c')
       **-1**
- .lastIndexOf(searchString: string, maxIndex=Infinity): number[ES1]
    ReturnsthehighestindexatwhichsearchStringappearswithinthestringor-1,
    otherwise. Any returned index will bemaxIndex‘ or lower.

```
> 'abab'.lastIndexOf('ab', 2)
2
> 'abab'.lastIndexOf('ab', 1)
0
> 'abab'.lastIndexOf('ab')
2
```
- [1 of 2].match(regExp: string | RegExp): RegExpMatchArray | null[ES3]

```
IfregExpis a regular expression with flag/gnot set, then.match()returns the
firstmatchforregExpwithinthestring. Ornullifthereisnomatch. IfregExpisa
string, it is used to create a regular expression (think parameter ofnew RegExp())
before performing the previously mentioned steps.
```
```
The result has the following type:
```

_20.8 Quick reference: Strings_ 185

```
interface RegExpMatchArray extendsArray <string>{
index:number;
input:string;
groups:undefined|{
[key:string]:string
};
}
```
```
NumberedcapturegroupsbecomeArrayindices(whichiswhythistypeextends
Array). Named capture groups(ES2018) become properties of.groups. In this
mode,.match()works likeRegExp.prototype.exec().
```
```
Examples:
```
```
> 'ababb'.match(/a(b+)/)
{ 0: 'ab', 1: 'b', index: 0, input: 'ababb', groups: undefined }
> 'ababb'.match(/a(?<foo>b+)/)
{ 0: 'ab', 1: 'b', index: 0, input: 'ababb', groups: { foo: 'b' } }
> 'abab'.match(/x/)
null
```
- [2 of 2].match(regExp: RegExp): string[] | null[ES3]

```
If flag/gofregExpis set,.match()returns either an Array with all matches or
nullif there was no match.
```
```
> 'ababb'.match(/a(b+)/g)
[ 'ab', 'abb' ]
> 'ababb'.match(/a(?<foo>b+)/g)
[ 'ab', 'abb' ]
> 'abab'.match(/x/g)
null
```
- .search(regExp: string | RegExp): number[ES3]

```
ReturnstheindexatwhichregExpoccurswithinthestring. IfregExpisastring,it
is used to create a regular expression (think parameter ofnew RegExp()).
```
```
> 'a2b'.search(/[0-9]/)
1
> 'a2b'.search('[0-9]')
1
```
- .startsWith(searchString: string, startPos=0): boolean[ES6]

```
ReturnstrueifsearchStringoccurs in the string at indexstartPos. Returns
falseotherwise.
```
```
> '.gitignore'.startsWith('.')
true
> 'abcde'.startsWith('bc', 1)
true
```

186 _20 Strings_

## 20.8.4 String.prototype: extracting

- .slice(start=0, end=this.length): string[ES3]

```
Returns the substring of the string that starts at (including) indexstartand ends
at(excluding)indexend. Ifanindexisnegative,itisaddedto.lengthbeforeitis
used (-1becomesthis.length-1, etc.).
> 'abc'.slice(1, 3)
'bc'
> 'abc'.slice(1)
'bc'
> 'abc'.slice(-2)
'bc'
```
- .at(index: number): string | undefined[ES2022]
    Returns the JavaScript character atindexas a string. Ifindexis negative, it is
    added to.lengthbefore it is used (-1becomesthis.length-1, etc.).

```
> 'abc'.at(0)
'a'
> 'abc'.at(-1)
'c'
```
- .split(separator: string | RegExp, limit?: number): string[][ES3]
    Splits the string into an Array of substrings – the strings that occur between the
    separators. The separator can be a string:

```
> 'a | b | c'.split('|')
[ 'a ', ' b ', ' c' ]
It can also be a regular expression:
```
```
> 'a : b : c'.split(/ *: */)
[ 'a', 'b', 'c' ]
> 'a : b : c'.split(/( *):( *)/)
[ 'a', ' ', ' ', 'b', ' ', ' ', 'c' ]
The last invocation demonstrates that captures made by groups in the regular ex-
pression become elements of the returned Array.
```
```
Warning:.split('')splitsastringintoJavaScriptcharacters. Thatdoesn’twork
well when dealing with astral code points (which are encoded as two JavaScript
characters). For example, emojis are astral:
> '☺X☺'.split('')
[ '\uD83D', '\uDE42', 'X', '\uD83D', '\uDE42' ]
```
```
Instead, it is better to useArray.from()(or spreading):
> Array.from('☺X☺')
[ '☺', 'X', '☺' ]
```
- .substring(start: number, end=this.length): string[ES1]


_20.8 Quick reference: Strings_ 187

```
Use.slice()instead of this method..substring()wasn’t implemented consis-
tently in older engines and doesn’t support negative indices.
```
## 20.8.5 String.prototype: combining

- .concat(...strings: string[]): string[ES3]
    Returns the concatenation of the string andstrings.'a'.concat('b')is equiva-
    lent to'a'+'b'. The latter is much more popular.

```
> 'ab'.concat('cd', 'ef', 'gh')
'abcdefgh'
```
- .padEnd(len: number, fillString=' '): string[ES2017]

```
Appends(fragmentsof)fillStringtothestringuntilithasthedesiredlengthlen.
If it already has or exceedslen, then it is returned without any changes.
> '#'.padEnd(2)
'# '
> 'abc'.padEnd(2)
'abc'
> '#'.padEnd(5, 'abc')
'#abca'
```
- .padStart(len: number, fillString=' '): string[ES2017]
    Prepends (fragments of)fillStringto the string until it has the desired length
    len. If it already has or exceedslen, then it is returned without any changes.

```
> '#'.padStart(2)
' #'
> 'abc'.padStart(2)
'abc'
> '#'.padStart(5, 'abc')
'abca#'
```
- .repeat(count=0): string[ES6]

```
Returns the string, concatenatedcounttimes.
> '*'.repeat()
''
> '*'.repeat(3)
'***'
```
## 20.8.6 String.prototype: transforming

- .normalize(form: 'NFC'|'NFD'|'NFKC'|'NFKD' = 'NFC'): string[ES6]
    Normalizes the string according tothe Unicode Normalization Forms.
- [1of2].replaceAll(searchValue: string | RegExp, replaceValue: string):
    string[ES2021]


188 _20 Strings_

```
What to do if you can’t use.replaceAll()
If.replaceAll()isn’tavailableonyourtargetedplatform,youcanuse.re-
place()instead. How is explained in[content not included].
```
```
Replaces all matches ofsearchValuewithreplaceValue. IfsearchValueis a reg-
ular expression without flag/g, aTypeErroris thrown.
> 'x.x.'.replaceAll('.', '#')
'x#x#'
> 'x.x.'.replaceAll(/./g, '#')
'####'
> 'x.x.'.replaceAll(/./, '#')
TypeError: String.prototype.replaceAll called with
a non-global RegExp argument
Special characters inreplaceValueare:
```
**-** $$: becomes$
**-** $n: becomes the capture of numbered groupn(alas,$0stands for the string
    '$0', it does not refer to the complete match)
**-** $&: becomes the complete match
**-** $`: becomes everything before the match
**-** $': becomes everything after the match
Examples:
> 'a 1995-12 b'.replaceAll(/([0-9]{4})-([0-9]{2})/g, '|$2|')
**'a |12| b'**
> 'a 1995-12 b'.replaceAll(/([0-9]{4})-([0-9]{2})/g, '|$&|')
**'a |1995-12| b'**
> 'a 1995-12 b'.replaceAll(/([0-9]{4})-([0-9]{2})/g, '|$`|')
**'a |a | b'**
Named capture groups(ES2018) are supported, too:
**-** $<name>becomes the capture of named groupname
Example:
assert.equal(
'a 1995-12 b'.replaceAll(
/(?<year>[0-9]{4})-(?<month>[0-9]{2})/g,'|$<month>|'),
'a |12| b');
- [2 of 2].replaceAll(searchValue: string | RegExp, replacer: (...args:
any[]) => string): string[ES2021]

```
If the second parameter is a function, occurrences are replaced with the strings it
returns. Its parametersargsare:
```
**-** matched: string. The complete match
**-** g1: string|undefined. The capture of numbered group 1


_20.8 Quick reference: Strings_ 189

**-** g2: string|undefined. The capture of numbered group 2
**-** (Etc.)
**-** offset: number. Where was the match found in the input string?
**-** input: string. The whole input string

```
const regexp=/([0-9]{4})-([0-9]{2})/g;
const replacer=(all,year,month) => '|'+all+'|';
assert.equal(
'a 1995-12 b'.replaceAll(regexp,replacer),
'a |1995-12| b');
```
```
Namedcapturegroups(ES2018)aresupported,too. Ifthereareany,anargument
is added at the end with an object whose properties contain the captures:
const regexp=/(?<year>[0-9]{4})-(?<month>[0-9]{2})/g;
const replacer=(...args) => {
const groups=args.pop();
return '|'+groups.month+'|';
};
assert.equal(
'a 1995-12 b'.replaceAll(regexp,replacer),
'a |12| b');
```
- .replace(searchValue: string | RegExp, replaceValue: string): string
    [ES3]
- .replace(searchValue: string | RegExp, replacer: (...args: any[]) =>
    string): string[ES3]

```
.replace()works like.replaceAll(), but only replaces the first occurrence if
searchValueis a string or a regular expression without/g:
```
```
> 'x.x.'.replace('.', '#')
'x#x.'
> 'x.x.'.replace(/./, '#')
'#.x.'
For more information on this method, see[content not included].
```
- .toUpperCase(): string[ES1]

```
Returns a copy of the string in which all lowercase alphabetic characters are con-
verted to uppercase. How well that works for various alphabets, depends on the
JavaScript engine.
> '-a2b-'.toUpperCase()
'-A2B-'
> 'αβγ'.toUpperCase()
'ΑΒΓ'
```
- .toLowerCase(): string[ES1]

```
Returns a copy of the string in which all uppercase alphabetic characters are con-
verted to lowercase. How well that works for various alphabets, depends on the
```

190 _20 Strings_

```
JavaScript engine.
> '-A2B-'.toLowerCase()
'-a2b-'
> 'ΑΒΓ'.toLowerCase()
'αβγ'
```
- .trim(): string[ES5]
    Returns a copy of the string in which all leading and trailing whitespace (spaces,
    tabs, line terminators, etc.) is gone.
       > '\r\n#\t '.trim()
       **'#'**
       > ' abc '.trim()
       **'abc'**
- .trimEnd(): string[ES2019]
    Similar to.trim()but only the end of the string is trimmed:
       > ' abc '.trimEnd()
       **' abc'**
- .trimStart(): string[ES2019]
    Similar to.trim()but only the beginning of the string is trimmed:
       > ' abc '.trimStart()
       **'abc '**

## 20.8.7 Sources

- TypeScript’s built-in typings
- MDN web docs for JavaScript
- ECMAScript language specification

```
Exercise: Using string methods
exercises/strings/remove_extension_test.mjs
```
```
Quiz
Seequiz app.
```

**Chapter 21**

**Using template literals and**

**tagged templates**

## Contents

```
21.1 Disambiguation: “template”...................... 191
21.2 Template literals............................. 192
21.3 Tagged templates............................. 193
21.3.1 Cooked vs. raw template strings (advanced).......... 193
21.4 Examples of tagged templates (as provided via libraries)....... 195
21.4.1 Tag function library: lit-html................... 195
21.4.2 Tag function library: re-template-tag.............. 195
21.4.3 Tag function library: graphql-tag................ 195
21.5 Raw string literals............................ 196
21.6 (Advanced)................................ 196
21.7 Multiline template literals and indentation.............. 196
21.7.1 Fix: template tag for dedenting................. 197
21.7.2 Fix:.trim()............................ 198
21.8 Simple templating via template literals................ 198
21.8.1 A more complex example.................... 198
21.8.2 Simple HTML-escaping..................... 199
```
```
Before we dig into the two features template literal and tagged template , let’s first examine
the multiple meanings of the term template.
```
**21.1 Disambiguation: “template”**

The following three things are significantly different despite all having _template_ in their
names and despite all of them looking similar:

```
191
```

```
192 21 Using template literals and tagged templates
```
- A _text template_ is a function from data to text. It is frequently used in web devel-
    opment and often defined via text files. For example, the following text defines a
    template for the libraryHandlebars:

```
<div class="entry" >
<h1> {{title}} </h1>
<div class="body" >
{{body}}
</div>
</div>
```
```
This template has two blanks to be filled in:titleandbody. It is used like this:
```
```
// First step: retrieve the template text, e.g. from a text file.
const tmplFunc=Handlebars.compile(TMPL_TEXT);// compile string
const data={title:'My page',body:'Welcome to my page!'};
const html=tmplFunc(data);
```
- A _templateliteral_ issimilartoastringliteral,buthasadditionalfeatures–forexam-
    ple, interpolation. It is delimited by backticks:

```
const num= 5 ;
assert.equal(`Count:${num}!`,'Count: 5!');
```
- Syntactically,a _taggedtemplate_ isatemplateliteralthatfollowsafunction(orrather,
    anexpressionthatevaluatestoafunction). Thatleadstothefunctionbeingcalled.
    Its arguments are derived from the contents of the template literal.

```
const getArgs=(...args) => args;
assert.deepEqual(
getArgs`Count:${ 5 }!`,
[['Count: ','!'], 5 ] );
```
```
Note thatgetArgs()receives both the text of the literal and the data interpolated
via${}.
```
**21.2 Template literals**

A template literal has two new features compared to a normal string literal.

```
First, it supports string interpolation : if we put a dynamically computed value inside a
${}, it is converted to a string and inserted into the string returned by the literal.
```
```
const MAX= 100 ;
function doSomeWork(x) {
if (x>MAX) {
thrownewError (`At most${MAX}allowed:${x}!`);
}
// ···
}
assert.throws(
```

```
21.3 Tagged templates 193
```
```
() => doSomeWork( 101 ),
{message:'At most 100 allowed: 101!'});
Second, template literals can span multiple lines:
const str=`this is
a text with
multiple lines`;
```
Template literals always produce strings.

**21.3 Tagged templates**

The expression in line A is a _tagged template_. It is equivalent to invokingtagFunc()with
the arguments listed in the Array in line B.
**function** tagFunc(...args) {
**return** args;
}

```
const setting='dark mode';
const value= true ;
```
```
assert.deepEqual(
tagFunc`Setting${setting}is${value}!`,// (A)
[['Setting ',' is ','!'],'dark mode', true ]// (B)
);
```
The functiontagFuncbefore the first backtick is called a _tag function_. Its arguments are:

- _Templatestrings_ (firstargument): anArraywiththetextfragmentssurroundingthe
    interpolations${}.
       **-** In the example:['Setting ', ' is ', '!']
- _Substitutions_ (remaining arguments): the interpolated values.
    **-** In the example:'dark mode'andtrue

The static (fixed) parts of the literal (the template strings) are kept separate from the
dynamic parts (the substitutions).

A tag function can return arbitrary values.

## 21.3.1 Cooked vs. raw template strings (advanced)

```
So far, we have only seen the cooked interpretation of template strings. But tag functions
actually get two interpretations:
```
- A _cooked interpretation_ where backslashes have special meaning. For example,\t
    producesatabcharacter. Thisinterpretationofthetemplatestringsisstoredasan
Array in the first argument.
- A _raw interpretation_ where backslashes do not have special meaning. For exam-
    ple,\tproduces two characters – a backslash and at. This interpretation of the
    template strings is stored in property.rawof the first argument (an Array).


```
194 21 Using template literals and tagged templates
```
The raw interpretation enables raw string literals viaString.raw(described later)and
similar applications.

The following tag functioncookedRawuses both interpretations:

```
function cookedRaw(templateStrings,...substitutions) {
return {
cooked: Array .from(templateStrings),// copy only Array elements
raw:templateStrings.raw,
substitutions,
};
}
assert.deepEqual(
cookedRaw`\tab${'subst'}\newline\\`,
{
cooked:['\tab','\newline\\'],
raw: ['\\tab','\\newline\\\\'],
substitutions:['subst'],
});
```
We can also use Unicode code point escapes (\u{1F642}), Unicode code unit escapes
(\u03A9), and ASCII escapes (\x52) in tagged templates:

```
assert.deepEqual(
cookedRaw`\u{54}\u0065\x78t`,
{
cooked:['Text'],
raw: ['\\u{54}\\u0065\\x78t'],
substitutions:[],
});
```
```
If the syntax of one of these escapes isn’t correct, the corresponding cooked template
string isundefined, while the raw version is still verbatim:
```
```
assert.deepEqual(
cookedRaw`\uu\xx${ 1 }after`,
{
cooked:[ undefined ,' after'],
raw: ['\\uu\\xx ',' after'],
substitutions:[ 1 ],
});
```
```
Incorrect escapes produce syntax errors in template literals and string literals. Before
ES2018,theyevenproducederrorsintaggedtemplates. Whywasthatchanged? Wecan
now use tagged templates for text that was previously illegal – for example:
```
```
windowsPath`C:\uuu\xxx\111`
latex`\unicode`
```

```
21.4 Examples of tagged templates (as provided via libraries) 195
```
```
21.4 Examples of tagged templates (as provided via li-
braries)
```
Taggedtemplatesaregreatforsupportingsmallembeddedlanguages(so-called _domain-
specific languages_ ). We’ll continue with a few examples.

## 21.4.1 Tag function library: lit-html

```
lit-htmlisatemplatinglibrarythatisbasedontaggedtemplatesandusedbythefrontend
framework Polymer:
import {html,render}from'lit-html';
```
```
const template=(items) => html`
<ul>
${
repeat(items,
(item) => item.id,
(item,index) => html`<li>${index}.${item.name}</li>`
)
}
</ul>
`;
repeat()is a custom function for looping. Its 2nd parameter produces unique keys for
thevaluesreturnedbythe3rdparameter. Notethenestedtaggedtemplateusedbythat
parameter.
```
## 21.4.2 Tag function library: re-template-tag

re-template-tagisasimplelibraryforcomposingregularexpressions. Templatestagged
withreproduceregularexpressions. Themainbenefitisthatwecaninterpolateregular
expressions and plain text via${}(line A):
**const** RE_YEAR=re`(?<year>[0-9]{4})`;
**const** RE_MONTH=re`(?<month>[0-9]{2})`;
**const** RE_DAY=re`(?<day>[0-9]{2})`;
**const** RE_DATE=re`/${RE_YEAR}-${RE_MONTH}-${RE_DAY}/u`;// (A)

```
const match=RE_DATE.exec('2017-01-27');
assert.equal(match.groups.year,'2017');
```
## 21.4.3 Tag function library: graphql-tag

```
The library graphql-taglets us create GraphQL queries via tagged templates:
```
```
import gqlfrom'graphql-tag';
```
```
const query=gql`
{
```

```
196 21 Using template literals and tagged templates
```
```
user(id: 5) {
firstName
lastName
}
}
`;
```
Additionally, there are plugins for pre-compiling such queries in Babel, TypeScript, etc.

**21.5 Raw string literals**

```
Raw string literals are implemented via the tag functionString.raw. They are string
literals where backslashes don’t do anything special (such as escaping characters, etc.):
assert.equal( String .raw`\back`,'\\back');
```
This helps whenever data contains backslashes – for example, strings with regular ex-
pressions:
**const** regex1=/^\./;
**const** regex2= **newRegExp** ('^\\.');
**const** regex3= **newRegExp** ( **String** .raw`^\.`);

All three regular expressions are equivalent. With a normal string literal, we have to
write the backslash twice, to escape it for that literal. With a raw string literal, we don’t
have to do that.
Raw string literals are also useful for specifying Windows filename paths:
**const** WIN_PATH= **String** .raw`C:\foo\bar`;
assert.equal(WIN_PATH,'C:\\foo\\bar');

**21.6 (Advanced)**

All remaining sections are advanced

**21.7 Multiline template literals and indentation**

```
If we put multiline text in template literals, two goals are in conflict: On one hand, the
template literal should be indented to fit inside the source code. On the other hand, the
lines of its content should start in the leftmost column.
For example:
function div(text) {
return `
<div>
${text}
</div>
`;
}
```

```
21.7 Multiline template literals and indentation 197
```
```
console .log('Output:');
console .log(
div('Hello!')
// Replace spaces with mid-dots:
.replace(/ /g,'·')
// Replace \n with #\n:
.replace(/\n/g,'#\n')
);
```
```
Duetotheindentation,thetemplateliteralfitswellintothesourcecode. Alas,theoutput
isalsoindented. Andwedon’twantthereturnatthebeginningandthereturnplustwo
spaces at the end.
```
```
Output:
#
···· <div> #
······Hello!#
···· </div> #
··
```
There are two ways to fix this: via a tagged template or by trimming the result of the
template literal.

## 21.7.1 Fix: template tag for dedenting

The first fix is to use a custom template tag that removes the unwanted whitespace. It
uses the first line after the initial line break to determine in which column the text starts
andshortenstheindentationeverywhere. Italsoremovesthelinebreakattheverybegin-
ning and the indentation at the very end. One such template tag isdedentby Desmond
Brand:

```
import dedentfrom'dedent';
function divDedented(text) {
return dedent`
<div>
${text}
</div>
`.replace(/\n/g,'#\n');
}
console .log('Output:');
console .log(divDedented('Hello!'));
```
This time, the output is not indented:

```
Output:
<div> #
Hello!#
</div>
```

```
198 21 Using template literals and tagged templates
```
## 21.7.2 Fix:.trim()

The second fix is quicker, but also dirtier:

```
function divDedented(text) {
return `
<div>
${text}
</div>
`.trim().replace(/\n/g,'#\n');
}
console .log('Output:');
console .log(divDedented('Hello!'));
```
Thestringmethod.trim()removesthesuperfluouswhitespaceatthebeginningandat
the end, but the content itself must start in the leftmost column. The advantage of this
solution is that we don’t need a custom tag function. The downside is that it looks ugly.

The output is the same as withdedent:

```
Output:
<div> #
Hello!#
</div>
```
**21.8 Simple templating via template literals**

Whiletemplateliteralslookliketexttemplates,itisnotimmediatelyobvioushowtouse
themfor(text)templating: Atexttemplategetsitsdatafromanobject,whileatemplate
literalgetsitsdatafromvariables. Thesolutionistouseatemplateliteralinthebodyof
a function whose parameter receives the templating data – for example:
**const** tmpl=(data) **=>** `Hello${data.name}!`;
assert.equal(tmpl({name:'Jane'}),'Hello Jane!');

## 21.8.1 A more complex example

As a more complex example, we’d like to take an Array of addresses and produce an
HTML table. This is the Array:
**const** addresses=[
{first:'<Jane>',last:'Bond'},
{first:'Lars',last:'<Croft>'},
];

The functiontmpl()that produces the HTML table looks as follows:

1 **const** tmpl=(addrs) **=>** `
2 <table>
3 ${addrs.map(
4 (addr) **=>** `
5 <tr>


```
21.8 Simple templating via template literals 199
```
6 <td>${escapeHtml(addr.first)}</td>
7 <td>${escapeHtml(addr.last)}</td>
8 </tr>
9 `.trim()
10 ).join('')}
11 </table>
12 `.trim();

```
This code contains two templating functions:
```
- The first one (line 1) takesaddrs, an Array with addresses, and returns a string
    with a table.
- The second one (line 4) takesaddr, an object containing an address, and returns a
    string with a table row. Note the.trim()at the end, which removes unnecessary
    whitespace.
Thefirsttemplatingfunctionproducesitsresultbywrappingatableelementaroundan
Arraythatitjoinsintoastring(line10). ThatArrayisproducedbymappingthesecond
templating function to each element ofaddrs(line 3). It therefore contains strings with
table rows.
ThehelperfunctionescapeHtml()isusedtoescapespecialHTMLcharacters(line6and
line 7). Its implementation is shown in the next subsection.
Let us calltmpl()with the addresses and log the result:
**console** .log(tmpl(addresses));
The output is:
**<table>
<tr>
<td>** &lt;Jane&gt; **</td>
<td>** Bond **</td>
</tr><tr>
<td>** Lars **</td>
<td>** &lt;Croft&gt; **</td>
</tr>
</table>**

## 21.8.2 Simple HTML-escaping

```
The following function escapes plain text so that it is displayed verbatim in HTML:
function escapeHtml(str) {
return str
.replace(/&/g,'&amp;')// first!
.replace(/>/g,'&gt;')
.replace(/</g,'&lt;')
.replace(/"/g,'&quot;')
.replace(/'/g,'&#39;')
.replace(/`/g,'&#96;')
;
```

200 _21 Using template literals and tagged templates_

### }

```
assert.equal(
escapeHtml('Rock & Roll'),'Rock &amp; Roll');
assert.equal(
escapeHtml('<blank>'),'&lt;blank&gt;');
```
```
Exercise: HTML templating
Exercise with bonus challenge: exercises/template-literals/templating_
test.mjs
```
```
Quiz
Seequiz app.
```

**Chapter 22**

**Symbols**

## Contents

```
22.1 Symbols are primitives that are also like objects........... 201
22.1.1 Symbols are primitive values.................. 201
22.1.2 Symbols are also like objects................... 202
22.2 The descriptions of symbols...................... 202
22.3 Use cases for symbols.......................... 202
22.3.1 Symbols as values for constants................. 203
22.3.2 Symbols as unique property keys................ 204
22.4 Publicly known symbols........................ 205
22.5 Converting symbols........................... 206
```
**22.1 Symbols are primitives that are also like objects**

```
Symbols are primitive values that are created via the factory functionSymbol():
```
```
const mySymbol= Symbol ('mySymbol');
```
Theparameterisoptionalandprovidesadescription,whichismainlyusefulfordebug-
ging.

## 22.1.1 Symbols are primitive values

```
Symbols are primitive values:
```
- They have to be categorized viatypeof:

```
const sym= Symbol ();
assert.equal( typeof sym,'symbol');
```
- They can be property keys in objects:

```
201
```

```
202 22 Symbols
```
```
const obj={
[sym]: 123 ,
};
```
## 22.1 Symbols are primitives that are also like objects

```
Eventhoughsymbolsareprimitives,theyarealsolikeobjectsinthateachvaluecreated
bySymbol()is unique and not compared by value:
> Symbol() === Symbol()
false
```
```
Priortosymbols,objectswerethebestchoiceifweneededvaluesthatwereunique(only
equal to themselves):
const string1='abc';
const string2='abc';
assert.equal(
string1===string2, true );// not unique
```
```
const object1={};
const object2={};
assert.equal(
object1===object2, false );// unique
```
```
const symbol1= Symbol ();
const symbol2= Symbol ();
assert.equal(
symbol1===symbol2, false );// unique
```
**22.2 The descriptions of symbols**

The parameter we pass to the symbol factory function provides a description for the
created symbol:
**const** mySymbol= **Symbol** ('mySymbol');

The description can be accessed in two ways.

```
First, it is part of the string returned by.toString():
assert.equal(mySymbol.toString(),'Symbol(mySymbol)');
Second, since ES2019, we can retrieve the description via the property.description:
assert.equal(mySymbol.description,'mySymbol');
```
**22.3 Use cases for symbols**

The main use cases for symbols, are:

- Values for constants


```
22.3 Use cases for symbols 203
```
- Unique property keys

## 22.3.1 Symbols as values for constants

```
Let’s assume you want to create constants representing the colors red, orange, yellow,
green, blue, and violet. One simple way of doing so would be to use strings:
const COLOR_BLUE='Blue';
```
```
Ontheplusside,loggingthatconstantproduceshelpfuloutput. Ontheminusside,there
is a risk of mistaking an unrelated value for a color because two strings with the same
content are considered equal:
```
```
const MOOD_BLUE='Blue';
assert.equal(COLOR_BLUE,MOOD_BLUE);
```
We can fix that problem via symbols:

```
const COLOR_BLUE= Symbol ('Blue');
const MOOD_BLUE= Symbol ('Blue');
```
```
assert.notEqual(COLOR_BLUE,MOOD_BLUE);
```
```
Let’s use symbol-valued constants to implement a function:
```
```
const COLOR_RED = Symbol ('Red');
const COLOR_ORANGE= Symbol ('Orange');
const COLOR_YELLOW= Symbol ('Yellow');
const COLOR_GREEN = Symbol ('Green');
const COLOR_BLUE = Symbol ('Blue');
const COLOR_VIOLET= Symbol ('Violet');
```
```
function getComplement(color) {
switch (color) {
case COLOR_RED:
return COLOR_GREEN;
case COLOR_ORANGE:
return COLOR_BLUE;
case COLOR_YELLOW:
return COLOR_VIOLET;
case COLOR_GREEN:
return COLOR_RED;
case COLOR_BLUE:
return COLOR_ORANGE;
case COLOR_VIOLET:
return COLOR_YELLOW;
default :
thrownew Exception('Unknown color: '+color);
}
}
assert.equal(getComplement(COLOR_YELLOW),COLOR_VIOLET);
```

```
204 22 Symbols
```
## 22.3.2 Symbols as unique property keys

The keys of properties (fields) in objects are used at two levels:

- Theprogramoperatesata _baselevel_. Thekeysatthatlevelreflectthe _problemdomain_
    - the area in which a program solves a problem – for example:
       **-** If a program manages employees, the property keys may be about job titles,
          salary categories, department IDs, etc.
       **-** If the program is a chess app, the property keys may be about chess pieces,
          chess boards, player colors, etc.
- ECMAScript and many libraries operate at a _meta-level_. They manage data and
    provide services that are not part of the problem domain – for example:
       **-** The standard method.toString()is used by ECMAScript when creating a
          string representation of an object (line A):

```
const point={
x: 7 ,
y: 4 ,
toString() {
return `(${ this .x},${ this .y})`;
},
};
assert.equal(
String (point),'(7, 4)');// (A)
```
```
.xand.yare base-level properties – they are used to solve the problem of
computing with points. .toString()is a meta-level property – it doesn’t
have anything to do with the problem domain.
```
**-** The standard ECMAScript method.toJSON()
    **const** point={
       x: 7 ,
       y: 4 ,
       toJSON() {
          **return** [ **this** .x, **this** .y];
       },
    };
    assert.equal(
       **JSON** .stringify(point),'[7,4]');

```
.xand.yare base-level properties,.toJSON()is a meta-level property.
```
Thebaselevelandthemeta-levelofaprogrammustbeindependent: Base-levelproperty
keys should not be in conflict with meta-level property keys.

```
If we use names (strings) as property keys, we are facing two challenges:
```
- When a language is first created, it can use any meta-level names it wants. Base-
    level code is forced to avoid those names. Later, however, when much base-level
    code already exists, meta-level names can’t be chosen freely, anymore.


## 22.4 Publicly known symbols

- Wecouldintroducenamingrulestoseparatebaselevelandmeta-level. Forexam-
    ple,Pythonbracketsmeta-levelnameswithtwounderscores:__init__,__iter_-
    _,__hash__, etc. However, the meta-level names of the language and the meta-
    level names of libraries would still exist in the same namespace and can clash.

These are two examples of where the latter was an issue for JavaScript:

- InMay2018,theArraymethod.flatten()hadtoberenamedto.flat()because
    the former name was already used by libraries (source).
- InNovember2020,theArraymethod.item()hadtoberenamedto.at()because
    the former name was already used by library (source).

```
Symbols, used as property keys, help us here: Each symbol is unique and a symbol key
never clashes with any other string or symbol key.
```
```
22.3.2.1 Example: a library with a meta-level method
```
Asanexample,let’sassumewearewritingalibrarythattreatsobjectsdifferentlyifthey
implement a special method. This is what defining a property key for such a method
and implementing it for an object would look like:
**const** specialMethod= **Symbol** ('specialMethod');
**const** obj={
_id:'kf12oi',
[specialMethod]() {// (A)
**returnthis** ._id;
}
};
assert.equal(obj[specialMethod](),'kf12oi');

The square brackets in line A enable us to specify that the method must have the key
specialMethod. Moredetailsareexplainedin§28.7.2“Computedkeysinobjectliterals”.

**22.4 Publicly known symbols**

```
SymbolsthatplayspecialroleswithinECMAScriptarecalled publiclyknownsymbols. Ex-
amples include:
```
- Symbol.iterator: makesanobject _iterable_. It’sthekeyofamethodthatreturnsan
    iterator. For more information on this topic, see[content not included].
- Symbol.hasInstance: customizeshowinstanceofworks. Ifanobjectimplements
    a method with that key, it can be used at the right-hand side of that operator. For
    example:
       **const** PrimitiveNull={
          [ **Symbol** .hasInstance](x) {
             **return** x=== **null** ;
          }
       };
       assert.equal( **nullinstanceof** PrimitiveNull, **true** );


```
206 22 Symbols
```
- Symbol.toStringTag: influences the default.toString()method.
    > String({})
    **'[object Object]'**
    > String({ [Symbol.toStringTag]: 'is no money' })
    **'[object is no money]'**
Note: It’s usually better to override.toString().

```
Exercises: Publicly known symbols
```
- Symbol.toStringTag:exercises/symbols/to_string_tag_test.mjs
- Symbol.hasInstance:exercises/symbols/has_instance_test.mjs

**22.5 Converting symbols**

What happens if we convert a symbolsymto another primitive type? Tbl.22.1has the
answers.

```
Table 22.1: The results of converting symbols to other primitive types.
```
```
Convert to Explicit conversion Coercion (implicit conv.)
boolean Boolean(sym) →OK !sym →OK
number Number(sym) → TypeError sym*2 → TypeError
string String(sym) →OK ''+sym → TypeError
sym.toString() →OK `${sym}` → TypeError
```
Onekeypitfallwithsymbolsishowoftenexceptionsarethrownwhenconvertingthem
to something else. What is the thinking behind that? First, conversion to number never
makes sense and should be warned about. Second, converting a symbol to a string is
indeed useful for diagnostic output. But it also makes sense to warn about accidentally
turning a symbol into a string (which is a different kind of property key):

```
const obj={};
const sym= Symbol ();
assert.throws(
() => { obj['__'+sym+'__']= true },
{message:'Cannot convert a Symbol value to a string'});
```
Thedownsideisthattheexceptionsmakeworkingwithsymbolsmorecomplicated. You
have to explicitly convert symbols when assembling strings via the plus operator:

```
> const mySymbol = Symbol('mySymbol');
> 'Symbol I used: ' + mySymbol
TypeError: Cannot convert a Symbol value to a string
> 'Symbol I used: ' + String(mySymbol)
'Symbol I used: Symbol(mySymbol)'
```

## 22.5 Converting symbols

```
Quiz
```
Seequiz app.


208 _22 Symbols_


**Part V**

**Control flow and data flow**

```
209
```


**Chapter 23**

**Control flow statements**

## Contents

```
23.1 Controlling loops:breakandcontinue................. 212
23.1.1break............................... 212
23.1.2breakplus label: leaving any labeled statement........ 212
23.1.3continue............................. 213
23.2 Conditions of control flow statements................. 213
23.3ifstatements [ES1]............................ 214
23.3.1 The syntax ofifstatements................... 214
23.4switchstatements [ES3]......................... 215
23.4.1 A first example of aswitchstatement.............. 215
23.4.2 Don’t forget toreturnorbreak!................. 216
23.4.3 Empty case clauses........................ 216
23.4.4 Checking for illegal values via adefaultclause........ 217
23.5whileloops [ES1]............................. 217
23.5.1 Examples ofwhileloops..................... 218
23.6do-whileloops [ES3]........................... 218
23.7forloops [ES1].............................. 218
23.7.1 Examples offorloops...................... 219
23.8for-ofloops [ES6]............................ 220
23.8.1const:for-ofvs.for....................... 220
23.8.2 Iterating over iterables...................... 220
23.8.3 Iterating over [index, element] pairs of Arrays......... 220
23.9for-await-ofloops [ES2018]...................... 221
23.10for-inloops (avoid) [ES1]........................ 221
23.11Recomendations for looping...................... 222
```
This chapter covers the following control flow statements:

- ifstatement [ES1]
- switchstatement [ES3]

```
211
```

```
212 23 Control flow statements
```
- whileloop [ES1]
- do-whileloop [ES3]
- forloop [ES1]
- for-ofloop [ES6]
- for-await-ofloop [ES2018]
- for-inloop [ES1]

**23.1 Controlling loops:breakandcontinue**

Thetwooperatorsbreakandcontinuecanbeusedtocontrolloopsandotherstatements
while we are inside them.

## 23.1.1 break

Therearetwoversionsofbreak: onewithanoperandandonewithoutanoperand. The
latterversionworksinsidethefollowingstatements:while,do-while,for,for-of,for-
await-of,for-inandswitch. It immediately leaves the current statement:

```
for ( const x of ['a','b','c']) {
console .log(x);
if (x==='b') break ;
console .log('---')
}
```
```
// Output:
// 'a'
// '---'
// 'b'
```
## 23.1.2 breakplus label: leaving any labeled statement

```
breakwith an operand works everywhere. Its operand is a label. Labels can be put in
front of any statement, including blocks.break my_labelleaves the statement whose
label ismy_label:
```
```
my_label:{// label
if (condition) break my_label;// labeled break
// ···
}
In the following example, the search can either:
```
- Fail: Theloopfinisheswithoutfindingaresult. Thatishandleddirectlyafterthe
    loop (line B).
- Succeed: While looping, we find aresult. Then we usebreakplus label (line A)
    to skip the code that handles failure.

```
function findSuffix(stringArray,suffix) {
let result;
search_block:{
```

## 23.2 Conditions of control flow statements.

```
for ( const str of stringArray) {
if (str.endsWith(suffix)) {
// Success:
result=str;
break search_block;// (A)
}
}// for
// Failure:
result='(Untitled)';// (B)
}// search_block
```
```
return { suffix,result };
// Same as: {suffix: suffix, result: result}
}
assert.deepEqual(
findSuffix(['notes.txt','index.html'],'.html'),
{suffix:'.html',result:'index.html'}
);
assert.deepEqual(
findSuffix(['notes.txt','index.html'],'.mjs'),
{suffix:'.mjs',result:'(Untitled)'}
);
```
## 23.1.3 continue

continueonly works insidewhile,do-while,for,for-of,for-await-of, andfor-in.
It immediately leaves the current loop iteration and continues with the next one – for
example:

```
const lines=[
'Normal line',
'# Comment',
'Another normal line',
];
for ( const line of lines) {
if (line.startsWith('#')) continue ;
console .log(line);
}
// Output:
// 'Normal line'
// 'Another normal line'
```
**23.2 Conditions of control flow statements**

if,while, anddo-whilehave conditions that are, in principle, boolean. However, a
condition only has to be _truthy_ (trueif coerced to boolean) in order to be accepted. In
other words, the following two control flow statements are equivalent:


```
214 23 Control flow statements
```
```
if (value) {}
if ( Boolean (value)=== true ) {}
This is a list of all falsy values:
```
- undefined,null
- false
- 0 ,NaN
- 0n
- ''
All other values are truthy. For more information, see§15.2 “Falsy and truthy values”.

**23.3 ifstatements [ES1]**

These are two simpleifstatements: one with just a “then” branch and one with both a
“then” branch and an “else” branch:

```
if (cond) {
// then branch
}
```
```
if (cond) {
// then branch
} else {
// else branch
}
Instead of the block,elsecan also be followed by anotherifstatement:
if (cond1) {
// ···
} elseif (cond2) {
// ···
}
```
```
if (cond1) {
// ···
} elseif (cond2) {
// ···
} else {
// ···
}
You can continue this chain with moreelse ifs.
```
## 23.3.1 The syntax ofifstatements

```
The general syntax ofifstatements is:
if (cond) «then_statement»
else «else_statement»
```

## 23.4switchstatements [ES3]

```
Sofar,thethen_statementhasalwaysbeenablock,butwecanuseanystatement. That
statement must be terminated with a semicolon:
if ( true ) console .log('Yes'); elseconsole .log('No');
```
That means thatelse ifis not its own construct; it’s simply anifstatement whose
else_statementis anotherifstatement.

**23.4 switchstatements [ES3]**

Aswitchstatement looks as follows:

```
switch («switch_expression») {
«switch_body»
}
```
The body ofswitchconsists of zero or more case clauses:

```
case «case_expression»:
«statements»
```
And, optionally, a default clause:

```
default:
«statements»
```
Aswitchis executed as follows:

- It evaluates the switch expression.
- Itjumpstothefirstcaseclausewhoseexpressionhasthesameresultastheswitch
    expression.
- Otherwise, if there is no such clause, it jumps to the default clause.
- Otherwise, if there is no default clause, it does nothing.

## 23.4.1 A first example of aswitchstatement

```
Let’slookatanexample: Thefollowingfunctionconvertsanumberfrom1–7tothename
of a weekday.
function dayOfTheWeek(num) {
switch (num) {
case 1 :
return 'Monday';
case 2 :
return 'Tuesday';
case 3 :
return 'Wednesday';
case 4 :
return 'Thursday';
case 5 :
return 'Friday';
case 6 :
```

```
216 23 Control flow statements
```
```
return 'Saturday';
case 7 :
return 'Sunday';
}
}
assert.equal(dayOfTheWeek( 5 ),'Friday');
```
## 23.4.2 Don’t forget toreturnorbreak!

At the end of a case clause, execution continues with the next case clause, unless we
returnorbreak– for example:
**function** englishToFrench(english) {
**let** french;
**switch** (english) {
**case** 'hello':
french='bonjour';
**case** 'goodbye':
french='au revoir';
}
**return** french;
}
// The result should be 'bonjour'!
assert.equal(englishToFrench('hello'),'au revoir');

That is, our implementation ofdayOfTheWeek()only worked because we usedreturn.
We can fixenglishToFrench()by usingbreak:

```
function englishToFrench(english) {
let french;
switch (english) {
case 'hello':
french='bonjour';
break ;
case 'goodbye':
french='au revoir';
break ;
}
return french;
}
assert.equal(englishToFrench('hello'),'bonjour');// ok
```
## 23.4.3 Empty case clauses

The statements of a case clause can be omitted, which effectively gives us multiple case
expressions per case clause:

```
function isWeekDay(name) {
switch (name) {
case 'Monday':
```

## 23.5whileloops [ES1]

```
case 'Tuesday':
case 'Wednesday':
case 'Thursday':
case 'Friday':
returntrue ;
case 'Saturday':
case 'Sunday':
returnfalse ;
}
}
assert.equal(isWeekDay('Wednesday'), true );
assert.equal(isWeekDay('Sunday'), false );
```
## 23.4.4 Checking for illegal values via adefaultclause

Adefaultclause is jumped to if theswitchexpression has no other match. That makes
it useful for error checking:

```
function isWeekDay(name) {
switch (name) {
case 'Monday':
case 'Tuesday':
case 'Wednesday':
case 'Thursday':
case 'Friday':
returntrue ;
case 'Saturday':
case 'Sunday':
returnfalse ;
default :
thrownewError ('Illegal value: '+name);
}
}
assert.throws(
() => isWeekDay('January'),
{message:'Illegal value: January'});
```
```
Exercises:switch
```
- exercises/control-flow/number_to_month_test.mjs
- Bonus:exercises/control-flow/is_object_via_switch_test.mjs

**23.5 whileloops [ES1]**

Awhileloop has the following syntax:


```
218 23 Control flow statements
```
```
while («condition») {
«statements»
}
```
```
Before each loop iteration,whileevaluatescondition:
```
- If the result is falsy, the loop is finished.
- If the result is truthy, thewhilebody is executed one more time.

## 23.5.1 Examples ofwhileloops

Thefollowingcodeusesawhileloop. Ineachloopiteration,itremovesthefirstelement
ofarrvia.shift()and logs it.

```
const arr=['a','b','c'];
while (arr.length> 0 ) {
const elem=arr.shift();// remove first element
console .log(elem);
}
// Output:
// 'a'
// 'b'
// 'c'
```
```
If the condition always evaluates totrue, thenwhileis an infinite loop:
```
```
while ( true ) {
if ( Math .random()=== 0 ) break ;
}
```
**23.6 do-whileloops [ES3]**

Thedo-whileloop works much likewhile, but it checks its condition _after_ each loop
iteration, not before.

```
let input;
do {
input=prompt('Enter text:');
console .log(input);
} while (input!==':q');
```
```
do-whilecan also be viewed as awhileloop that runs at least once.
```
```
prompt()is a global function that is available in web browsers. It prompts the user to
input text and returns it.
```
**23.7 forloops [ES1]**

Aforloop has the following syntax:


## 23.7forloops [ES1]

```
for («initialization»; «condition»; «post_iteration») {
«statements»
}
```
Thefirstlineisthe _head_ oftheloopandcontrolshowoftenthe _body_ (theremainderofthe
loop) is executed. It has three parts and each of them is optional:

- initialization: sets up variables, etc. for the loop. Variables declared here via
    letorconstonly exist inside the loop.
- condition: This condition is checked before each loop iteration. If it is falsy, the
    loop stops.
- post_iteration: This code is executed after each loop iteration.

Aforloop is therefore roughly equivalent to the followingwhileloop:

```
«initialization»
while («condition») {
«statements»
«post_iteration»
}
```
## 23.7.1 Examples offorloops

As an example, this is how to count from zero to two via aforloop:

```
for ( let i= 0 ;i< 3 ;i++) {
console .log(i);
}
```
```
// Output:
// 0
// 1
// 2
```
This is how to log the contents of an Array via aforloop:

```
const arr=['a','b','c'];
for ( let i= 0 ;i<arr.length;i++) {
console .log(arr[i]);
}
```
```
// Output:
// 'a'
// 'b'
// 'c'
```
```
If we omit all three parts of the head, we get an infinite loop:
```
```
for (;;) {
if ( Math .random()=== 0 ) break ;
}
```

```
220 23 Control flow statements
```
**23.8 for-ofloops [ES6]**

Afor-ofloop iterates over any _iterable_ – a data container that supportsthe _iteration pro-
tocol_. Each iterated value is stored in a variable, as specified in the head:
for («iteration_variable» of «iterable») {
«statements»
}

The iteration variable is usually created via a variable declaration:

```
const iterable=['hello','world'];
for ( const elem of iterable) {
console .log(elem);
}
// Output:
// 'hello'
// 'world'
```
```
But we can also use a (mutable) variable that already exists:
const iterable=['hello','world'];
let elem;
for (elem of iterable) {
console .log(elem);
}
```
## 23.8.1 const:for-ofvs.for

Note that infor-ofloops we can useconst. The iteration variable can still be different
for each iteration (it just can’t change during the iteration). Think of it as a newconst
declaration being executed each time in a fresh scope.

```
In contrast, inforloops we must declare variables vialetorvarif their values change.
```
## 23.8.2 Iterating over iterables

As mentioned before,for-ofworks with any iterable object, not just with Arrays – for
example, with Sets:
**const** set= **newSet** (['hello','world']);
**for** ( **const** elem **of** set) {
**console** .log(elem);
}

## 23.8.3 Iterating over [index, element] pairs of Arrays

```
Lastly, we can also usefor-ofto iterate over the [index, element] entries of Arrays:
```
```
const arr=['a','b','c'];
for ( const [index,elem] of arr.entries()) {
console .log(`${index}->${elem}`);
```

## 23.9for-await-ofloops [ES2018]

### }

```
// Output:
// '0 -> a'
// '1 -> b'
// '2 -> c'
```
With[index, element], we are using _destructuring_ to access Array elements.

```
Exercise:for-of
exercises/control-flow/array_to_string_test.mjs
```
**23.9 for-await-ofloops [ES2018]**

```
for-await-ofis likefor-of, but it works with asynchronous iterables instead of syn-
chronous ones. And it can only be used inside async functions and async generators.
```
```
forawait ( const item of asyncIterable) {
// ···
}
```
```
for-await-ofis described in detailin the chapter on asynchronous iteration.
```
**23.10 for-inloops (avoid) [ES1]**

Thefor-inloop visits all (own and inherited) enumerable property keys of an object.
When looping over an Array, it is rarely a good choice:

- It visits property keys, not values.
- As property keys, the indices of Array elements are strings, not numbers (more
    information on how Array elements work).
- Itvisitsallenumerablepropertykeys(bothownandinheritedones),notjustthose
    of Array elements.

The following code demonstrates these points:

```
const arr=['a','b','c'];
arr.propKey='property value';
```
```
for ( const key in arr) {
console .log(key);
}
```
```
// Output:
// '0'
// '1'
// '2'
// 'propKey'
```

222 _23 Control flow statements_

**23.11 Recomendations for looping**

- Ifyouwanttoloopoveranasynchronousiterable(inES2018+),youmustusefor-
    await-of.
- Forloopingoverasynchronousiterable(inES6+),youmustusefor-of. Notethat
    Arrays are iterables.
- For looping over an Array in ES5+, you can usethe Array method.forEach().
- Before ES5, you can use a plainforloop to loop over an Array.
- Don’t usefor-into loop over an Array.

```
Quiz
Seequiz app.
```

**Chapter 24**

**Exception handling**

## Contents

```
24.1 Motivation: throwing and catching exceptions............ 223
24.2throw................................... 224
24.2.1 What values should we throw?................. 225
24.3 Thetrystatement............................ 225
24.3.1 Thetryblock........................... 225
24.3.2 Thecatchclause......................... 226
24.3.3 Thefinallyclause........................ 227
24.4Errorand its subclasses......................... 227
24.4.1 ClassError............................ 228
24.4.2 The built-in subclasses ofError................. 229
24.4.3 SubclassingError......................... 229
24.5 Chaining errors.............................. 230
24.5.1 Why would we want to chain errors?.............. 230
24.5.2 Chaining errors viaerror.cause[ES2022]........... 230
24.5.3 An alternative to.cause: a custom error class......... 231
```
This chapter covers how JavaScript handles exceptions.

```
Why doesn’t JavaScript throw exceptions more often?
JavaScript didn’t support exceptions until ES3. That explains why they are used
sparingly by the language and its standard library.
```
**24.1 Motivation: throwing and catching exceptions**

```
Considerthefollowingcode. ItreadsprofilesstoredinfilesintoanArraywithinstances
of classProfile:
```
```
223
```

```
224 24 Exception handling
```
```
function readProfiles(filePaths) {
const profiles=[];
for ( const filePath of filePaths) {
try {
const profile=readOneProfile(filePath);
profiles.push(profile);
} catch (err) {// (A)
console .log('Error in: '+filePath,err);
}
}
}
function readOneProfile(filePath) {
const profile= new Profile();
const file=openFile(filePath);
// ··· (Read the data in `file` into `profile`)
return profile;
}
function openFile(filePath) {
if (!fs.existsSync(filePath)) {
thrownewError ('Could not find file '+filePath);// (B)
}
// ··· (Open the file whose path is `filePath`)
}
Let’s examine what happens in line B: An error occurred, but the best place to handle
theproblemisnotthecurrentlocation,it’slineA.There,wecanskipthecurrentfileand
move on to the next one.
```
Therefore:

- In line B, we use athrowstatement to indicate that there was a problem.
- In line A, we use atry-catchstatement to handle the problem.

When we throw, the following constructs are active:

```
readProfiles(···)
for (const filePath of filePaths)
try
readOneProfile(···)
openFile(···)
if (!fs.existsSync(filePath))
throw
```
One by one,throwexits the nested constructs, until it encounters atrystatement. Exe-
cution continues in thecatchclause of thattrystatement.

**24.2 throw**

This is the syntax of thethrowstatement:

```
throw «value»;
```

```
24.3 Thetrystatement 225
```
## 24.2.1 What values should we throw?

Any value can be thrown in JavaScript. However, it’s best to use instances ofErroror a
subclassbecausetheysupportadditionalfeaturessuchasstacktracesanderrorchaining
(see§24.4 “Errorand its subclasses”).

That leaves us with the following options:

- Using classErrordirectly. That is less limiting in JavaScript than in a more static
    language because we can add our own properties to instances:

```
const err= newError ('Could not find the file');
err.filePath=filePath;
throw err;
```
- Using one ofthe subclasses ofError.
- SubclassingError(more details are explainedlater):

```
class MyError extendsError {
}
function func() {
thrownew MyError('Problem!');
}
assert.throws(
() => func(),
MyError);
```
**24.3 Thetrystatement**

The maximal version of thetrystatement looks as follows:

```
try {
«try_statements»
} catch (error) {
«catch_statements»
} finally {
«finally_statements»
}
```
We can combine these clauses as follows:

- try-catch
- try-finally
- try-catch-finally

## 24.3.1 Thetryblock

Thetryblockcanbeconsideredthebodyofthestatement. Thisiswhereweexecutethe
regular code.


```
226 24 Exception handling
```
## 24.3.2 Thecatchclause

```
If an exception reaches thetryblock, then it is assigned to the parameter of thecatch
clause and the code in that clause is executed. Next, execution normally continues after
thetrystatement. That may change if:
```
- There is areturn,break, orthrowinside thecatchblock.
- Thereisafinallyclause(whichisalwaysexecutedbeforethetrystatementends).

ThefollowingcodedemonstratesthatthevaluethatisthrowninlineAisindeedcaught
in line B.

```
const errorObject= newError ();
function func() {
throw errorObject;// (A)
}
```
```
try {
func();
} catch (err) {// (B)
assert.equal(err,errorObject);
}
```
```
24.3.2.1 Omitting thecatchbinding [ES2019]
```
We can omit thecatchparameter if we are not interested in the value that was thrown:

```
try {
// ···
} catch {
// ···
}
```
That may occasionally be useful. For example, Node.js has the API functionas-
sert.throws(func)that checks whether an error is thrown insidefunc. It could be
implemented as follows.

```
function throws(func) {
try {
func();
} catch {
return ;// everything OK
}
thrownewError ('Function didn’t throw an exception!');
}
```
```
However, a more complete implementation of this function would have acatchparam-
eter and would, for example, check that its type is as expected.
```

## 24.4Errorand its subclasses

## 24.3.3 Thefinallyclause

Thecodeinsidethefinallyclauseisalwaysexecutedattheendofatrystatement–no
matter what happens in thetryblock or thecatchclause.

```
Let’s look at a common use case forfinally: We have created a resource and want to
alwaysdestroyitwhenwearedonewithit,nomatterwhathappenswhileworkingwith
it. We would implement that as follows:
```
```
const resource=createResource();
try {
// Work with `resource`. Errors may be thrown.
} finally {
resource.destroy();
}
```
```
24.3.3.1 finallyis always executed
```
Thefinallyclause is always executed, even if an error is thrown (line A):

```
let finallyWasExecuted= false ;
assert.throws(
() => {
try {
thrownewError ();// (A)
} finally {
finallyWasExecuted= true ;
}
},
Error
);
assert.equal(finallyWasExecuted, true );
```
And even if there is areturnstatement (line A):

```
let finallyWasExecuted= false ;
function func() {
try {
return ;// (A)
} finally {
finallyWasExecuted= true ;
}
}
func();
assert.equal(finallyWasExecuted, true );
```
**24.4 Errorand its subclasses**

```
Erroris the common superclass of all built-in error classes.
```

```
228 24 Exception handling
```
## 24.4.1 ClassError

This is whatError’s instance properties and constructor look like:

```
classError {
// Instance properties
message:string;
cause?:any;// ES2022
stack:string;// non-standard but widely supported
```
```
constructor (
message:string='',
options?:ErrorOptions// ES2022
);
}
interface ErrorOptions {
cause?:any;// ES2022
}
```
The constructor has two parameters:

- messagespecifies an error message.
- optionswasintroducedinECMAScript2022. Itcontainsanobjectwhereoneprop-
    erty is currently supported:
       **-** .causespecifies which exception (if any) caused the current error.

Thesubsectionsafterthenextoneexplaintheinstanceproperties.message,.causeand
.stackin more detail.

```
24.4.1.1 Error.prototype.name
```
```
Each built-in error classEhas a propertyE.prototype.name:
```
```
> Error.prototype.name
'Error'
> RangeError.prototype.name
'RangeError'
```
Therefore, there are two ways to get the name of the class of a built-in error object:

```
> new RangeError().name
'RangeError'
> new RangeError().constructor.name
'RangeError'
```
```
24.4.1.2 Error instance property.message
```
```
.messagecontains just the error message:
```
```
const err= newError ('Hello!');
assert.equal( String (err),'Error: Hello!');
assert.equal(err.message,'Hello!');
```

```
24.4Errorand its subclasses 229
```
```
If we omit the message then the empty string is used as a default value (inherited from
Error.prototype.message):
If we omit the message, it is the empty string:
assert.equal( newError ().message,'');
```
```
24.4.1.3 Error instance property.stack
```
The instance property.stackis not an ECMAScript feature, but it is widely supported
by JavaScript engines. It is usually a string, but its exact structure is not standardized
and varies between engines.

This is what it looks like on the JavaScript engine V8:

```
const err= newError ('Hello!');
assert.equal(
err.stack,
`
Error: Hello!
at file://ch_exception-handling.mjs:1:13
`.trim());
```
```
24.4.1.4 Error instance property.cause[ES2022]
```
The instance property.causeis created via the options object in the second parameter
ofnew Error(). It specifies which other error caused the current one.
**const** err= **newError** ('msg',{cause:'the cause'});
assert.equal(err.cause,'the cause');

```
For information on how to use this property see§24.5 “Chaining errors”.
```
## 24.4.2 The built-in subclasses ofError

```
Errorhas the following subclasses – quotingthe ECMAScript specification:
```
- AggregateError[ES2021] represents multiple errors at once. In the standard li-
    brary, onlyPromise.any()uses it.
- RangeErrorindicates a value that is not in the set or range of allowable values.
- ReferenceErrorindicates that an invalid reference value has been detected.
- SyntaxErrorindicates that a parsing error has occurred.
- TypeErroris used to indicate an unsuccessful operation when none of the other
    _NativeError_ objects are an appropriate indication of the failure cause.
- URIErrorindicates that one of the global URI handling functions was used in a
    way that is incompatible with its definition.

## 24.4.3 SubclassingError

```
SinceECMAScript2022,theErrorconstructoracceptstwoparameters(seeprevioussub-
section). Therefore, we have two choices when subclassing it: We can either omit the
constructor in our subclass or we can invokesuper()like this:
```

```
230 24 Exception handling
```
```
class MyCustomError extendsError {
constructor(message,options) {
super (message,options);
// ···
}
}
```
**24.5 Chaining errors**

## 24.5.1 Why would we want to chain errors?

```
Sometimes, we catch errors that are thrown during a more deeply nested function call
and would like to attach more information to it:
```
```
function readFiles(filePaths) {
return filePaths.map(
(filePath) => {
try {
const text=readText(filePath);
const json= JSON .parse(text);
return processJson(json);
} catch (error) {
// (A)
}
});
}
```
The statements inside thetryclause may throw all kinds of errors. In most cases, an
error won’t be aware of the path of the file that caused it. That‘s why we would like to
attach that information in line A.

## 24.5 Chaining errors

```
Since ECMAScript 2022,new Error()lets us specify what caused it:
```
```
function readFiles(filePaths) {
return filePaths.map(
(filePath) => {
try {
// ···
} catch (error) {
thrownewError (
`While processing ${filePath}`,
{cause:error}
);
}
});
}
```

```
24.5 Chaining errors 231
```
## 24.5.3 An alternative to.cause: a custom error class

The following custom error class supports chaining. It is forward compatible with
.cause.
/**
* An error class that supports error chaining.
* If there is built-in support for .cause, it uses it.
* Otherwise, it creates this property itself.
*
*@seehttps://github.com/tc39/proposal-error-cause
*/
**class** CausedError **extendsError** {
constructor(message,options) {
**super** (message,options);
**if** (
(isObject(options)&&'cause' **in** options)
&&!('cause' **inthis** )
) {
// .cause was specified but the superconstructor
// did not create an instance property.
**const** cause=options.cause;
**this** .cause=cause;
**if** ('stack' **in** cause) {
**this** .stack= **this** .stack+'\nCAUSE: '+cause.stack;
}
}
}
}

```
function isObject(value) {
return value!== null && typeof value==='object';
}
```
```
Exercise: Exception handling
exercises/exception-handling/call_function_test.mjs
```
```
Quiz
Seequiz app.
```

232 _24 Exception handling_


**Chapter 25**

**Callable values**

## Contents

```
25.1 Kinds of functions............................ 234
25.2 Ordinary functions............................ 234
25.2.1 Named function expressions (advanced)............ 234
25.2.2 Terminology: function definitions and function expressions.. 235
25.2.3 Parts of a function declaration.................. 236
25.2.4 Roles played by ordinary functions............... 236
25.2.5 Terminology: entity vs. syntax vs. role (advanced)....... 237
25.3 Specialized functions.......................... 237
25.3.1 Specialized functions are still functions............. 238
25.3.2 Arrow functions......................... 239
25.3.3 The special variablethisin methods, ordinary functions and
arrow functions.......................... 240
25.3.4 Recommendation: prefer specialized functions over ordinary
functions............................. 241
25.4 Summary: kinds of callable values................... 242
25.5 Returning values from functions and methods............ 243
25.6 Parameter handling........................... 244
25.6.1 Terminology: parameters vs. arguments............ 244
25.6.2 Terminology: callback...................... 244
25.6.3 Too many or not enough arguments............... 244
25.6.4 Parameter default values..................... 245
25.6.5 Rest parameters.......................... 245
25.6.6 Named parameters........................ 246
25.6.7 Simulating named parameters.................. 246
25.6.8 Spreading (...) into function calls................ 247
25.7 Methods of functions:.call(),.apply(),.bind().......... 248
25.7.1 The function method.call().................. 248
25.7.2 The function method.apply()................. 249
25.7.3 The function method.bind().................. 249
```
```
233
```

## 25 Callable values

```
In this chapter, we look at JavaScript values that can be invoked: functions, methods,
and classes.
```
**25.1 Kinds of functions**

JavaScript has two categories of functions:

- An _ordinary function_ can play several roles:
    **-** Real function
    **-** Method
    **-** Constructor function
- A _specialized function_ can only play one of those roles – for example:
    **-** An _arrow function_ can only be a real function.
    **-** A _method_ can only be a method.
    **-** A _class_ can only be a constructor function.
Specialized functions were added to the language in ECMAScript 6.

```
Read on to find out what all of those things mean.
```
**25.2 Ordinary functions**

The following code shows two ways of doing (roughly) the same thing: creating an or-
dinary function.

```
// Function declaration (a statement)
function ordinary1(a,b,c) {
// ···
}
```
```
// const plus anonymous (nameless) function expression
const ordinary2= function (a,b,c) {
// ···
};
Inside a scope, function declarations are activated early (see§11.8 “Declarations: scope
and activation”) and can be called before they are declared. That is occasionally useful.
```
Variable declarations, such as the one forordinary2, are not activated early.

## 25.2.1 Named function expressions (advanced)

```
So far, we have only seen anonymous function expressions – which don’t have names:
const anonFuncExpr= function (a,b,c) {
// ···
};
```

## 25.2 Ordinary functions

```
But there are also named function expressions :
const namedFuncExpr= function myName(a,b,c) {
// `myName` is only accessible in here
};
myNameisonlyaccessibleinsidethebodyofthefunction. Thefunctioncanuseittorefer
to itself (for self-recursion, etc.) – independently of which variable it is assigned to:
const func= function funcExpr() { return funcExpr };
assert.equal(func(),func);
```
// The name `funcExpr` only exists inside the function body:
assert.throws(() **=>** funcExpr(), **ReferenceError** );
Eveniftheyarenotassignedtovariables,namedfunctionexpressionshavenames(line
A):

```
function getNameOfCallback(callback) {
return callback.name;
}
```
```
assert.equal(
getNameOfCallback( function () {}),'');// anonymous
```
```
assert.equal(
getNameOfCallback( function named() {}),'named');// (A)
Note that functions created via function declarations or variable declarations always
have names:
function funcDecl() {}
assert.equal(
getNameOfCallback(funcDecl),'funcDecl');
```
```
const funcExpr= function () {};
assert.equal(
getNameOfCallback(funcExpr),'funcExpr');
Onebenefitoffunctionshavingnamesisthatthosenamesshowupinerrorstacktraces.
```
## 25.2.2 Terminology: function definitions and function expressions

A _function definition_ is syntax that creates functions:

- A function declaration (a statement)
- A function expression
Functiondeclarationsalwaysproduceordinaryfunctions. Functionexpressionsproduce
either ordinary functions or specialized functions:
- Ordinary function expressions (which we have already encountered):
**-** Anonymous function expressions
**-** Named function expressions


```
236 25 Callable values
```
- Specialized function expressions (which we’ll look at later):
    **-** Arrow functions (which are always expressions)

While function declarations are still popular in JavaScript, function expressions are al-
most always arrow functions in modern code.

## 25.2.3 Parts of a function declaration

```
Let’sexaminethepartsofafunctiondeclarationviathefollowingexample. Mostofthe
terms also apply to function expressions.
function add(x,y) {
return x+y;
}
```
- addis the _name_ of the function declaration.
- add(x, y)is the _head_ of the function declaration.
- xandyare the _parameters_.
- Thecurlybraces({and})andeverythingbetweenthemarethe _body_ ofthefunction
    declaration.
- Thereturnstatement explicitly returns a value from the function.

```
25.2.3.1 Trailing commas in parameter lists
```
JavaScript has always allowed and ignored trailing commas in Array literals. Since ES5,
they are also allowed in object literals. Since ES2017, we can add trailing commas to
parameter lists (declarations and invocations):
// Declaration
**function** retrieveData(
contentText,
keyword,
{unique,ignoreCase,pageSize},// trailing comma
) {
// ···
}

```
// Invocation
retrieveData(
'',
null ,
{ignoreCase: true ,pageSize: 10 },// trailing comma
);
```
## 25.2.4 Roles played by ordinary functions

```
Consider the following function declaration from the previous section:
function add(x,y) {
return x+y;
}
```

## 25.3 Specialized functions

Thisfunctiondeclarationcreatesanordinaryfunctionwhosenameisadd. Asanordinary
function,add()can play three roles:

- Real function: invoked via a function call.

```
assert.equal(add( 2 , 1 ), 3 );
```
- Method: stored in a property, invoked via a method call.

```
const obj={addAsMethod:add };
assert.equal(obj.addAsMethod( 2 , 4 ), 6 );// (A)
In line A,objis called the receiver of the method call.
```
- Constructor function: invoked vianew.
    **const** inst= **new** add();
    assert.equal(inst **instanceof** add, **true** );

```
As an aside, the names of constructor functions (incl. classes) normally start with
capital letters.
```
## 25.2.5 Terminology: entity vs. syntax vs. role (advanced)

The distinction between the concepts _syntax_ , _entity_ , and _role_ is subtle and often doesn’t
matter. But I’d like to sharpen your eye for it:

- An _entity_ is a JavaScript feature as it “lives” in RAM. An ordinary function is an
    entity.
       **-** Entities include: ordinary functions, arrow functions, methods, and classes.
- _Syntax_ is the code that we use to create entities. Function declarations and anony-
    mous function expressions are syntax. They both create entities that are called
    ordinary functions.
       **-** Syntaxincludes: functiondeclarationsandanonymousfunctionexpressions.
          The syntax that produces arrow functions is also called _arrow functions_. The
             same is true for methods and classes.
- A _role_ describes how we use entities. The entity _ordinary function_ can play the role
    _real function_ , or the role _method_ , or the role _class_. The entity _arrow function_ can also
    play the role _real function_.
       **-** The roles of functions are: real function, method, and constructor function.
Many other programming languages only have a single entity that plays the role _real
function_. Then they can use the name _function_ for both role and entity.

**25.3 Specialized functions**

```
Specialized functions are single-purpose versions of ordinary functions. Each one of
them specializes in a single role:
```
- The purpose of an _arrow function_ is to be a real function:

```
const arrow=() => {
return 123 ;
```

```
238 25 Callable values
```
### };

```
assert.equal(arrow(), 123 );
```
- The purpose of a _method_ is to be a method:
    **const** obj={
       myMethod() {
          **return** 'abc';
       }
    };
    assert.equal(obj.myMethod(),'abc');
- The purpose of a _class_ is to be a constructor function:
    **class** MyClass {
       /* ··· */
    }
    **const** inst= **new** MyClass();

Apart from nicer syntax, each kind of specialized function also supports new features,
making them better at their jobs than ordinary functions.

- Arrow functions are explained soon.
- Methods are explainedin the chapter on single objects.
- Classes are explainedin the chapter on classes.

Tbl.25.1lists the capabilities of ordinary and specialized functions.

```
Table 25.1: Capabilities of four kinds of functions. If a cell value is in
parentheses, that implies some kind of limitation. The special variable
thisisexplainedin§25.3.3“Thespecialvariablethisinmethods,ordi-
nary functions and arrow functions”.
```
```
Function call Method call Constructor call
Ordinary function (this === undefined) ✔ ✔
Arrow function ✔ (lexicalthis) ✘
Method (this === undefined) ✔ ✘
Class ✘ ✘ ✔
```
## 25.3.1 Specialized functions are still functions

```
It’s important to note that arrow functions, methods, and classes are still categorized as
functions:
```
```
> (() => {}) instanceof Function
true
> ({ method() {} }.method) instanceof Function
true
> (class SomeClass {}) instanceof Function
true
```

```
25.3 Specialized functions 239
```
## 25.3.2 Arrow functions

Arrow functions were added to JavaScript for two reasons:

```
1.To provide a more concise way for creating functions.
2.Theyworkbetterasrealfunctionsinsidemethods: Methodscanrefertotheobject
that received a method call via the special variablethis. Arrow functions can
access thethisof a surrounding method, ordinary functions can’t (because they
have their ownthis).
```
We’ll first examine the syntax of arrow functions and then howthisworks in various
functions.

```
25.3.2.1 The syntax of arrow functions
Let’s review the syntax of an anonymous function expression:
```
```
const f= function (x,y,z) { return 123 };
```
The (roughly) equivalent arrow function looks as follows. Arrow functions are expres-
sions.

```
const f=(x,y,z) => { return 123 };
```
```
Here, the body of the arrow function is a block. But it can also be an expression. The
following arrow function works exactly like the previous one.
```
```
const f=(x,y,z) => 123 ;
```
```
Ifanarrow functionhasonlyasingleparameterandthatparameterisanidentifier(not
a destructuring pattern) then you can omit the parentheses around the parameter:
```
```
const id=x => x;
```
That is convenient when passing arrow functions as parameters to other functions or
methods:

```
> [1,2,3].map(x => x+1)
[ 2, 3, 4 ]
```
Thispreviousexampledemonstratesonebenefitofarrowfunctions–conciseness. Ifwe
perform the same task with a function expression, our code is more verbose:

```
[ 1 , 2 , 3 ].map( function (x) { return x+ 1 });
```
```
25.3.2.2 Syntax pitfall: returning an object literal from an arrow function
```
```
If you want the expression body of an arrow function to be an object literal, you must
put the literal in parentheses:
```
```
const func1=() => ({a: 1 });
assert.deepEqual(func1(),{a: 1 });
```
```
If you don’t, JavaScript thinks, the arrow function has a block body (that doesn’t return
anything):
```

```
240 25 Callable values
```
**const** func2=() **=>** {a: 1 };
assert.deepEqual(func2(), **undefined** );
{a: 1}isinterpretedasablockwiththelabela:andtheexpressionstatement 1. Without
an explicitreturnstatement, the block body returnsundefined.

This pitfall is caused bysyntactic ambiguity: object literals and code blocks have the
samesyntax. WeusetheparenthesestotellJavaScriptthatthebodyisanexpression(an
object literal) and not a statement (a block).

## 25.3.3 The special variablethisin methods, ordinary functions and

## arrow functions

```
The special variablethisis an object-oriented feature
Wearetakingaquicklookatthespecialvariablethishere,inordertounderstand
why arrow functions are better real functions than ordinary functions.
But this feature only matters in object-oriented programming and is covered in
more depth in§28.5 “Methods and the special variablethis”. Therefore, don’t
worry if you don’t fully understand it yet.
```
```
Inside methods, the special variablethislets us access the receiver – the object which
received the method call:
const obj={
myMethod() {
assert.equal( this ,obj);
}
};
obj.myMethod();
```
Ordinaryfunctionscanbemethodsandthereforealsohavetheimplicitparameterthis:

```
const obj={
myMethod: function () {
assert.equal( this ,obj);
}
};
obj.myMethod();
```
thisis even an implicit parameter when we use an ordinary function as a real function.
Then its value isundefined(ifstrict modeis active, which it almost always is):

```
function ordinaryFunc() {
assert.equal( this , undefined );
}
ordinaryFunc();
```
That means that an ordinary function, used as a real function, can’t access thethisof a
surroundingmethod(lineA).Incontrast,arrowfunctionsdon’thavethisasanimplicit


```
25.3 Specialized functions 241
```
```
parameter. They treat it like any other variable and can therefore access thethisof a
surrounding method (line B):
const jill={
name:'Jill',
someMethod() {
function ordinaryFunc() {
assert.throws(
() => this .name,// (A)
/^TypeError: Cannot read properties of undefined\(reading 'name'\)$/);
}
ordinaryFunc();
```
```
const arrowFunc=() => {
assert.equal( this .name,'Jill');// (B)
};
arrowFunc();
},
};
jill.someMethod();
In this code, we can observe two ways of handlingthis:
```
- Dynamicthis: InlineA,wetrytoaccessthethisof.someMethod()fromanordi-
    naryfunction. There,itis _shadowed_ bythefunction’sownthis,whichisundefined
(as filled in by the function call). Given that ordinary functions receive theirthis
via (dynamic) function or method calls, theirthisis called _dynamic_.
- Lexicalthis: In line B, we again try to access thethisof.someMethod(). This
    time, we succeed because the arrow function does not have its ownthis. this
    is resolved _lexically_ , just like any other variable. That’s why thethisof arrow
    functions is called _lexical_.

## 25.3.4 Recommendation: prefer specialized functions over ordinary

## functions

```
Normally, you should prefer specialized functions over ordinary functions, especially
classes and methods.
```
When it comes to real functions, the choice between an arrow function and an ordinary
function is less clear-cut, though:

- Foranonymousinlinefunctionexpressions,arrowfunctionsareclearwinners,due
    to their compact syntax and them not havingthisas an implicit parameter:

```
const twiceOrdinary=[ 1 , 2 , 3 ].map( function (x) { return x* 2 });
const twiceArrow=[ 1 , 2 , 3 ].map(x => x* 2 );
```
- For stand-alone named function declarations, arrow functions still benefit from
    lexicalthis. But function declarations (which produce ordinary functions) have
    nicesyntaxandearlyactivationisalsooccasionallyuseful(see§11.8“Declarations:
    scopeandactivation”). Ifthisdoesn’tappearinthebodyofanordinaryfunction,


```
242 25 Callable values
```
```
there is no downside to using it as a real function. The static checking tool ESLint
can warn us during development when we do this wrong viaa built-in rule.
function timesOrdinary(x,y) {
return x*y;
}
const timesArrow=(x,y) => {
return x*y;
};
```
**25.4 Summary: kinds of callable values**

```
This section refers to upcoming content
This section mainly serves as a reference for the current and upcoming chapters.
Don’t worry if you don’t understand everything.
```
```
So far, all (real) functions and methods, that we have seen, were:
```
- Single-result
- Synchronous
Later chapters will cover other modes of programming:
- _Iteration_ treatsobjectsascontainersofdata(so-called _iterables_ )andprovidesastan-
dardizedwayforretrievingwhatisinsidethem. Ifafunctionoramethodreturns
an iterable, it returns multiple values.
- _Asynchronous programming_ deals with handling a long-running computation. You
are notified when the computation is finished and can do something else in be-
tween. Thestandardpatternforasynchronouslydeliveringsingleresultsiscalled
_Promise_.

These modes can be combined – for example, there are synchronous iterables and asyn-
chronous iterables.
Several new kinds of functions and methods help with some of the mode combinations:

- _Async functions_ help implement functions that return Promises. There are also
    _async methods_.
- _Synchronous generator functions_ help implement functions that return synchronous
    iterables. There are also _synchronous generator methods_.
- _Asynchronous generator functions_ help implement functions that return asyn-
    chronous iterables. There are also _asynchronous generator methods_.

That leaves us with 4 kinds (2 × 2) of functions and methods:

- Synchronous vs. asynchronous
- Generator vs. single-result

Tbl.25.2givesanoverviewofthesyntaxforcreatingthese4kindsoffunctionsandmeth-
ods.


## 25.5 Returning values from functions and methods

```
Table 25.2: Syntax for creating functions and methods. The last column
specifies how many values are produced by an entity.
```
```
Result #
Sync function Sync method
function f() {} { m() {} } value 1
f = function () {}
f = () => {}
Sync generator function Sync gen. method
function* f() {} { * m() {} } iterable 0+
f = function* () {}
Async function Async method
async function f() {} { async m() {} } Promise 1
f = async function () {}
f = async () => {}
Async generator function Async gen. method
async function* f() {} { async * m() {} } async iterable 0+
f = async function* () {}
```
**25.5 Returning values from functions and methods**

(Everything mentioned in this section applies to both functions and methods.)

Thereturnstatement explicitly returns a value from a function:

```
function func() {
return 123 ;
}
assert.equal(func(), 123 );
```
Another example:

```
function boolToYesNo(bool) {
if (bool) {
return 'Yes';
} else {
return 'No';
}
}
assert.equal(boolToYesNo( true ),'Yes');
assert.equal(boolToYesNo( false ),'No');
```
```
If, at the end of a function, you haven’t returned anything explicitly, JavaScript returns
undefinedfor you:
function noReturn() {
// No explicit return
}
assert.equal(noReturn(), undefined );
```

```
244 25 Callable values
```
**25.6 Parameter handling**

Once again, I am only mentioning functions in this section, but everything also applies
to methods.

## 25.6.1 Terminology: parameters vs. arguments

Theterm _parameter_ andtheterm _argument_ basicallymeanthesamething. Ifyouwantto,
you can make the following distinction:

- _Parameters_ are part of a function definition. They are also called _formal parameters_
    and _formal arguments_.
- _Arguments_ are part of a function call. They are also called _actual parameters_ and
    _actual arguments_.

## 25.6.2 Terminology: callback

A _callback_ or _callback function_ is a function that is an argument of a function or method
call.

The following is an example of a callback:

```
const myArray=['a','b'];
const callback=(x) => console .log(x);
myArray.forEach(callback);
```
```
// Output:
// 'a'
// 'b'
```
## 25.6.3 Too many or not enough arguments

JavaScriptdoesnotcomplainifafunctioncallprovidesadifferentnumberofarguments
than expected by the function definition:

- Extra arguments are ignored.
- Missing parameters are set toundefined.

```
For example:
```
```
function foo(x,y) {
return [x,y];
}
```
```
// Too many arguments:
assert.deepEqual(foo('a','b','c'),['a','b']);
```
```
// The expected number of arguments:
assert.deepEqual(foo('a','b'),['a','b']);
```

## 25.6 Parameter handling.

```
// Not enough arguments:
assert.deepEqual(foo('a'),['a', undefined ]);
```
## 25.6.4 Parameter default values

```
Parameterdefaultvaluesspecifythevaluetouseifaparameterhasnotbeenprovided–
for example:
function f(x,y= 0 ) {
return [x,y];
}
```
```
assert.deepEqual(f( 1 ),[ 1 , 0 ]);
assert.deepEqual(f(),[ undefined , 0 ]);
undefinedalso triggers the default value:
assert.deepEqual(
f( undefined , undefined ),
[ undefined , 0 ]);
```
## 25.6.5 Rest parameters

A rest parameter is declared by prefixing an identifier with three dots (...). During a
function or method call, it receives an Array with all remaining arguments. If there are
no extra arguments at the end, it is an empty Array – for example:
**function** f(x,...y) {
**return** [x,y];
}
assert.deepEqual(
f('a','b','c'),['a',['b','c']]
);
assert.deepEqual(
f(),[ **undefined** ,[]]
);

There are two restrictions related to how we can use rest parameters:

- We cannot use more than one rest parameter per function definition.
    assert.throws(
       () **=>** eval('function f(...x, ...y) {}'),
       /^SyntaxError: Rest parameter must be last formal parameter$/
    );
- A rest parameter must always come last. As a consequence, we can’t access the
    last parameter like this:
       assert.throws(
          () **=>** eval('function f(...restParams, lastParam) {}'),
          /^SyntaxError: Rest parameter must be last formal parameter$/
       );


```
246 25 Callable values
```
```
25.6.5.1 Enforcing a certain number of arguments via a rest parameter
```
Youcanusearestparametertoenforceacertainnumberofarguments. Take,forexample,
the following function:
**function** createPoint(x,y) {
**return** {x,y};
// same as {x: x, y: y}
}

This is how we force callers to always provide two arguments:

```
function createPoint(...args) {
if (args.length!== 2 ) {
thrownewError ('Please provide exactly 2 arguments!');
}
const [x,y]=args;// (A)
return {x,y};
}
In line A, we access the elements ofargsvia destructuring.
```
## 25.6.6 Named parameters

Whensomeonecallsafunction,theargumentsprovidedbythecallerareassignedtothe
parameters received by the callee. Two common ways of performing the mapping are:
1.Positional parameters: An argument is assigned to a parameter if they have the
same position. A function call with only positional arguments looks as follows.
selectEntries( 3 , 20 , 2 )
2.Namedparameters: Anargumentisassignedtoaparameteriftheyhavethesame
name. JavaScriptdoesn’thavenamedparameters,butyoucansimulatethem. For
example, this is a function call with only (simulated) named arguments:
selectEntries({start: 3 ,end: 20 ,step: 2 })
Named parameters have several benefits:

- Theyleadtomoreself-explanatorycodebecauseeachargumenthasadescriptive
    label. Just compare the two versions ofselectEntries(): with the second one, it
    is much easier to see what happens.
- The order of the arguments doesn’t matter (as long as the names are correct).
- Handlingmorethanoneoptionalparameterismoreconvenient: callerscaneasily
    provide any subset of all optional parameters and don’t have to be aware of the
    onesthey omit(with positionalparameters,you have to fillin preceding optional
    parameters, withundefined).

## 25.6.7 Simulating named parameters

JavaScript doesn’t have real named parameters. The official way of simulating them is
via object literals:


```
25.6 Parameter handling 247
```
```
function selectEntries({start= 0 ,end=- 1 ,step= 1 }) {
return {start,end,step};
}
```
This function uses _destructuring_ to access the properties of its single parameter. The pat-
tern it uses is an abbreviation for the following pattern:
{start:start= 0 ,end:end=- 1 ,step:step= 1 }

This destructuring pattern works for empty object literals:

```
> selectEntries({})
{ start: 0, end: -1, step: 1 }
But it does not work if you call the function without any parameters:
> selectEntries()
TypeError: Cannot read properties of undefined (reading 'start')
```
You can fix this by providing a default value for the whole pattern. This default value
works the same as default values for simpler parameter definitions: if the parameter is
missing, the default is used.
**function** selectEntries({start= 0 ,end=- 1 ,step= 1 }={}) {
**return** {start,end,step};
}
assert.deepEqual(
selectEntries(),
{start: 0 ,end:- 1 ,step: 1 });

## 25.6.8 Spreading (...) into function calls

If you put three dots (...) in front of the argument of a function call, then you _spread_ it.
Thatmeansthattheargumentmustbean _iterable_ objectandtheiteratedvaluesallbecome
arguments. Inotherwords,asingleargumentisexpandedintomultiplearguments–for
example:
**function** func(x,y) {
**console** .log(x);
**console** .log(y);
}
**const** someIterable=['a','b'];
func(...someIterable);
// same as func('a', 'b')

```
// Output:
// 'a'
// 'b'
Spreading and rest parameters use the same syntax (...), but they serve opposite pur-
poses:
```
- Rest parameters are used when defining functions or methods. They collect argu-
    ments into Arrays.


```
248 25 Callable values
```
- Spreadargumentsareusedwhencallingfunctionsormethods. Theyturniterable
    objects into arguments.

```
25.6.8.1 Example: spreading intoMath.max()
```
```
Math.max()returns the largest one of its zero or more arguments. Alas, it can’t be used
for Arrays, but spreading gives us a way out:
> Math.max(-1, 5, 11, 3)
11
> Math.max(...[-1, 5, 11, 3])
11
> Math.max(-1, ...[-5, 11], 3)
11
```
```
25.6.8.2 Example: spreading intoArray.prototype.push()
```
```
Similarly, the Array method.push()destructively adds its zero or more parameters to
the end of its Array. JavaScript has no method for destructively appending an Array to
another one. Once again, we are saved by spreading:
const arr1=['a','b'];
const arr2=['c','d'];
```
```
arr1.push(...arr2);
assert.deepEqual(arr1,['a','b','c','d']);
```
```
Exercises: Parameter handling
```
- Positional parameters: exercises/callables/positional_parameters_
    test.mjs
- Named parameters:exercises/callables/named_parameters_test.mjs

**25.7 Methods of functions:.call(),.apply(),.bind()**

```
Functions are objects and have methods. In this section, we look at three of those meth-
ods:.call(),.apply(), and.bind().
```
## 25.7.1 The function method.call()

```
Each functionsomeFunchas the following method:
```
```
someFunc.call(thisValue,arg1,arg2,arg3);
```
This method invocation is loosely equivalent to the following function call:

```
someFunc(arg1,arg2,arg3);
```
```
However, with.call(), we can also specify a value forthe implicit parameterthis. In
other words:.call()makes the implicit parameterthisexplicit.
```

```
25.7 Methods of functions:.call(),.apply(),.bind() 249
```
The following code demonstrates the use of.call():

```
function func(x,y) {
return [ this ,x,y];
}
```
```
assert.deepEqual(
func.call('hello','a','b'),
['hello','a','b']);
```
As we have seen before, if we function-call an ordinary function, itsthisisundefined:

```
assert.deepEqual(
func('a','b'),
[ undefined ,'a','b']);
```
Therefore, the previous function call is equivalent to:

```
assert.deepEqual(
func.call( undefined ,'a','b'),
[ undefined ,'a','b']);
```
```
Inarrowfunctions,thevalueforthisprovidedvia.call()(orothermeans)isignored.
```
## 25.7.2 The function method.apply()

```
Each functionsomeFunchas the following method:
```
```
someFunc.apply(thisValue,[arg1,arg2,arg3]);
```
This method invocation is loosely equivalent to the following function call (which uses
spreading):

```
someFunc(...[arg1,arg2,arg3]);
```
```
However, with.apply(), we can also specify a value forthe implicit parameterthis.
```
The following code demonstrates the use of.apply():

```
function func(x,y) {
return [ this ,x,y];
}
```
```
const args=['a','b'];
assert.deepEqual(
func.apply('hello',args),
['hello','a','b']);
```
## 25.7.3 The function method.bind()

```
.bind()is another method of function objects. This method is invoked as follows:
```
```
const boundFunc=someFunc.bind(thisValue,arg1,arg2);
```

```
250 25 Callable values
```
.bind()returnsanewfunctionboundFunc(). CallingthatfunctioninvokessomeFunc()
withthissettothisValueandtheseparameters:arg1,arg2,followedbytheparameters
ofboundFunc().

That is, the following two function calls are equivalent:

```
boundFunc('a','b')
someFunc.call(thisValue,arg1,arg2,'a','b')
```
```
25.7.3.1 An alternative to.bind()
```
Another way of pre-fillingthisand parameters is via an arrow function:

```
const boundFunc2=(...args) =>
someFunc.call(thisValue,arg1,arg2,...args);
```
```
25.7.3.2 An implementation of.bind()
```
```
Considering the previous section,.bind()can be implemented as a real function as fol-
lows:
function bind(func,thisValue,...boundArgs) {
return (...args) =>
func.call(thisValue,...boundArgs,...args);
}
```
```
25.7.3.3 Example: binding a real function
Using.bind()for real functions is somewhat unintuitive because we have to provide
a value forthis. Given that it isundefinedduring function calls, it is usually set to
undefinedornull.
Inthefollowingexample,wecreateadd8(),afunctionthathasoneparameter,bybinding
the first parameter ofadd()to 8.
function add(x,y) {
return x+y;
}
```
```
const add8=add.bind( undefined , 8 );
assert.equal(add8( 1 ), 9 );
```
```
Quiz
Seequiz app.
```

**Chapter 26**

**Evaluating code dynamically:**

**eval(), new Function()**

**(advanced)**

## Contents

```
26.1eval()................................... 251
26.2new Function().............................. 252
26.3 Recommendations............................ 252
```
```
In this chapter, we’ll look at two ways of evaluating code dynamically:eval()andnew
```
## 26.2new Function().

**26.1 eval()**

```
Given a stringstrwith JavaScript code,eval(str)evaluates that code and returns the
result:
> eval('2 ** 4')
16
There are two ways of invokingeval():
```
- _Directly_ , via a function call. Then the code in its argument is evaluated inside the
    current scope.
- _Indirectly_ , not via a function call. Then it evaluates its code in global scope.

“Not via a function call” means “anything that looks different thaneval(···)”:

- eval.call(undefined, '···')(usesmethod.call()of functions)
- eval?.()() (usesoptional chaining)
- (0, eval)('···')(usesthe comma operator)
- globalThis.eval('···')

```
251
```

## 26 Evaluating code dynamically:eval(),new Function()(advanced)

- const e = eval; e('···')
- Etc.

The following code illustrates the difference:

```
globalThis.myVariable='global';
function func() {
const myVariable='local';
```
```
// Direct eval
assert.equal(eval('myVariable'),'local');
```
```
// Indirect eval
assert.equal(eval.call( undefined ,'myVariable'),'global');
}
```
```
Evaluating code in global context is safer because the code has access to fewer internals.
```
**26.2 new Function()**

```
new Function()creates a function object and is invoked as follows:
```
```
const func= newFunction ('«param_1»',···,'«param_n»','«func_body»');
```
The previous statement is equivalent to the next statement. Note that«param_1», etc.,
are not inside string literals, anymore.

```
const func= function («param_1»,···,«param_n») {
«func_body»
};
```
In the next example, we create the same function twice, first vianew Function(), then
via a function expression:

```
const times1= newFunction ('a','b','return a * b');
const times2= function (a,b) { return a*b };
```
```
new Function()creates non-strict mode functions
By default, functions created vianew Function()aresloppy. If we want the func-
tion body to be in strict mode, we have toswitch it on manually.
```
**26.3 Recommendations**

Avoid dynamic evaluation of code as much as you can:

- It’sasecurityriskbecauseitmayenableanattackertoexecutearbitrarycodewith
    the privileges of your code.
- It may be switched off – for example, in browsers, viaa Content Security Policy.


## 26.3 Recommendations

Very often, JavaScript is dynamic enough so that you don’t needeval()or similar. In
the following example, what we are doing witheval()(line A) can be achieved just as
well without it (line B).

```
const obj={a: 1 ,b: 2 };
const propKey='b';
```
```
assert.equal(eval('obj.'+propKey), 2 );// (A)
assert.equal(obj[propKey], 2 );// (B)
If you have to dynamically evaluate code:
```
- Prefernew Function()overeval(): it always executes its code in global context
    and a function provides a clean interface to the evaluated code.
- Prefer indirectevalover directeval: evaluating code in global context is safer.


254 _26 Evaluating code dynamically:eval(),new Function()(advanced)_


**Part VI**

**Modularity**

```
255
```


**Chapter 27**

**Modules**

## Contents

```
27.1 Cheat sheet: modules.......................... 258
27.1.1 Exporting............................. 258
27.1.2 Importing............................. 258
27.2 JavaScript source code formats..................... 259
27.2.1 Code before built-in modules was written in ECMAScript 5.. 259
27.3 Before we had modules, we had scripts................ 259
27.4 Module systems created prior to ES6.................. 261
27.4.1 Server side: CommonJS modules................ 261
27.4.2 Client side: AMD (Asynchronous Module Definition) modules 261
27.4.3 Characteristics of JavaScript modules.............. 262
27.5 ECMAScript modules.......................... 263
27.5.1 ES modules: syntax, semantics, loader API........... 263
27.6 Named exports and imports....................... 263
27.6.1 Named exports.......................... 263
27.6.2 Named imports.......................... 264
27.6.3 Namespace imports........................ 265
27.6.4 Named exporting styles: inline versus clause (advanced)... 265
27.7 Default exports and imports....................... 266
27.7.1 The two styles of default-exporting............... 266
27.7.2 The default export as a named export (advanced)....... 267
27.8 More details on exporting and importing............... 268
27.8.1 Imports are read-only views on exports............. 268
27.8.2 ESM’s transparent support for cyclic imports (advanced)... 269
27.9 npm packages............................... 269
27.9.1 Packages are installed inside a directorynode_modules/.... 270
27.9.2 Why can npm be used to install frontend libraries?....... 271
27.10Naming modules............................. 271
27.11Module specifiers............................ 272
```
```
257
```

258 _27 Modules_

```
27.11.1 Categories of module specifiers................. 272
27.11.2 ES module specifiers in browsers................ 272
27.11.3 ES module specifiers on Node.js................. 273
27.12import.meta– metadata for the current module [ES2020]....... 274
27.12.1import.meta.url......................... 274
27.12.2import.meta.urland classURL................. 274
27.12.3import.meta.urlon Node.js................... 274
27.13Loading modules dynamically viaimport()[ES2020] (advanced).. 275
27.13.1The limitations of staticimportstatements........... 276
27.13.2Dynamic imports via theimport()operator.......... 276
27.13.3Use cases forimport()...................... 278
27.14Top-levelawaitin modules [ES2022] (advanced)........... 278
27.14.1Use cases for top-levelawait................... 279
27.14.2How does top-levelawaitwork under the hood?....... 279
27.14.3The pros and cons of top-levelawait.............. 280
27.15Polyfills: emulating native web platform features (advanced).... 280
27.15.1Sources of this section...................... 281
```
**27.1 Cheat sheet: modules**

## 27.1.1 Exporting

```
// Named exports
export function f() {}
export const one= 1 ;
export{foo,basbar};
```
```
// Default exports
exportdefault function f() {}// declaration with optional name
// Replacement for `const` (there must be exactly one value)
exportdefault 123 ;
```
```
// Re-exporting from another module
export{foo,basbar}from'./some-module.mjs';
export*from'./some-module.mjs';
export*asnsfrom'./some-module.mjs';// ES2020
```
## 27.1.2 Importing

```
// Named imports
import{foo,barasb}from'./some-module.mjs';
// Namespace import
import*assomeModulefrom'./some-module.mjs';
// Default import
importsomeModulefrom'./some-module.mjs';
```

## 27.3 Before we had modules, we had scripts.

```
// Combinations:
import someModule,*assomeModulefrom'./some-module.mjs';
import someModule,{foo,barasb}from'./some-module.mjs';
```
```
// Empty import (for modules with side effects)
import './some-module.mjs';
```
**27.2 JavaScript source code formats**

ThecurrentlandscapeofJavaScriptmodulesisquitediverse: ES6broughtbuilt-inmod-
ules, but the source code formats that came before them, are still around, too. Under-
standing the latter helps understand the former, so let’s investigate. The next sections
describe the following ways of delivering JavaScript source code:

- _Scripts_ are code fragments that browsers run in global scope. They are precursors
    of modules.
- _CommonJS modules_ are a module format that is mainly used on servers (e.g., via
    Node.js).
- _AMD modules_ are a module format that is mainly used in browsers.
- _ECMAScript modules_ areJavaScript’sbuilt-inmoduleformat. Itsupersedesallpre-
    vious formats.

Tbl.27.1gives an overview of these code formats. Note that for CommonJS modules
and ECMAScript modules, two filename extensions are commonly used. Which one is
appropriatedependsonhowwewanttouseafile. Detailsaregivenlaterinthischapter.

```
Table 27.1: Ways of delivering JavaScript source code.
```
```
Runs on Loaded Filename ext.
Script browsers async .js
CommonJS module servers sync .js .cjs
AMD module browsers async .js
ECMAScript module browsers and servers async .js .mjs
```
## 27.2.1 Code before built-in modules was written in ECMAScript 5

```
Before we get to built-in modules (which were introduced with ES6), all code that we’ll
see, will be written in ES5. Among other things:
```
- ES5 did not haveconstandlet, onlyvar.
- ES5 did not have arrow functions, only function expressions.

**27.3 Before we had modules, we had scripts**

Initially, browsers only had _scripts_ – pieces of code that were executed in global scope.
As an example, consider an HTML file that loads script files via the following HTML:


```
260 27 Modules
```
```
<script src="other-module1.js" ></script>
<script src="other-module2.js" ></script>
<script src="my-module.js" ></script>
```
The main file ismy-module.js, where we simulate a module:

```
var myModule=( function () {// Open IIFE
// Imports (via global variables)
var importedFunc1=otherModule1.importedFunc1;
var importedFunc2=otherModule2.importedFunc2;
```
```
// Body
function internalFunc() {
// ···
}
function exportedFunc() {
importedFunc1();
importedFunc2();
internalFunc();
}
```
```
// Exports (assigned to global variable `myModule`)
return {
exportedFunc:exportedFunc,
};
})();// Close IIFE
```
```
myModuleis a global variable that is assigned the result of immediately invoking a func-
tion expression. The function expression starts in the first line. It is invoked in the last
line.
```
This way of wrapping a code fragment is called _immediately invoked function expression_
(IIFE, coined by Ben Alman). What do we gain from an IIFE?varis not block-scoped
(likeconstandlet), it is function-scoped: the only way to create new scopes forvar-
declared variables is via functions or methods (withconstandlet, we can use either
functions, methods, or blocks{}). Therefore, the IIFE in the example hides all of the
followingvariablesfromglobalscopeandminimizesnameclashes:importedFunc1,im-
portedFunc2,internalFunc,exportedFunc.

Note that we are using an IIFE in a particular manner: at the end, we pick what we
wanttoexportandreturnitviaanobjectliteral. Thatiscalledthe _revealingmodulepattern_
(coined by Christian Heilmann).

This way of simulating modules, has several issues:

- Librariesinscriptfilesexportandimportfunctionalityviaglobalvariables,which
    risks name clashes.
- Dependencies are not stated explicitly, and there is no built-in way for a script to
    load the scripts it depends on. Therefore, the web page has to load not just the
    scripts that are needed by the page but also the dependencies of those scripts, the
    dependencies’ dependencies, etc. And it has to do so in the right order!


## 27.4 Module systems created prior to ES6 8 CONTENTS

**27.4 Module systems created prior to ES6**

```
Prior to ECMAScript 6, JavaScript did not have built-in modules. Therefore, the flexi-
ble syntax of the language was used to implement custom module systems within the
language. Two popular ones are:
```
- CommonJS (targeting the server side)
- AMD (Asynchronous Module Definition, targeting the client side)

## 27.4.1 Server side: CommonJS modules

The original CommonJS standard for modules was created for server and desktop plat-
forms. It was the foundation of the original Node.js module system, where it achieved
enormous popularity. Contributing to that popularity were the npm package manager
forNodeandtoolsthatenabledusingNodemodulesontheclientside(browserify,web-
pack, and others).
From now on, _CommonJS module_ means the Node.js version of this standard (which has
a few additional features). This is an example of a CommonJS module:
// Imports
**var** importedFunc1 =require('./other-module1.js').importedFunc1;
**var** importedFunc2 =require('./other-module2.js').importedFunc2;

```
// Body
function internalFunc() {
// ···
}
function exportedFunc() {
importedFunc1();
importedFunc2();
internalFunc();
}
```
```
// Exports
module.exports={
exportedFunc:exportedFunc,
};
```
```
CommonJS can be characterized as follows:
```
- Designed for servers.
- Modules are meant to be loaded _synchronously_ (the importer waits while the im-
    ported module is loaded and executed).
- Compact syntax.

## 27.4.2 Clientside: AMD(AsynchronousModuleDefinition)modules

TheAMDmoduleformatwascreatedtobeeasiertouseinbrowsersthantheCommonJS
format. Its most popular implementation isRequireJS. The following is an example of
an AMD module.


```
262 27 Modules
```
```
define(['./other-module1.js','./other-module2.js'],
function (otherModule1,otherModule2) {
var importedFunc1=otherModule1.importedFunc1;
var importedFunc2=otherModule2.importedFunc2;
```
```
function internalFunc() {
// ···
}
function exportedFunc() {
importedFunc1();
importedFunc2();
internalFunc();
}
```
```
return {
exportedFunc:exportedFunc,
};
});
```
AMD can be characterized as follows:

- Designed for browsers.
- Modules are meant to be loaded _asynchronously_. That’s a crucial requirement for
    browsers, where code can’t wait until a module has finished downloading. It has
    to be notified once the module is available.
- The syntax is slightly more complicated.

On the plus side, AMD modules can be executed directly. In contrast, CommonJS mod-
ules must either be compiled before deployment or custom source code must be gen-
erated and evaluated dynamically(thinkeval()). That isn’t always permitted on the
web.

## 27.4.3 Characteristics of JavaScript modules

```
Looking at CommonJS and AMD, similarities between JavaScript module systems
emerge:
```
- There is one module per file.
- Such a file is basically a piece of code that is executed:
    **-** Local scope: The code is executed in a local “module scope”. Therefore, by
       default, all of the variables, functions, and classes declared in it are internal
       and not global.
    **-** Exports: If we want any declared entity to be exported, we must explicitly
       mark it as an export.
    **-** Imports: Each module can import exported entities from other modules.
       Those other modules are identified via _module specifiers_ (usually paths,
       occasionally full URLs).
- Modulesare _singletons_ : Evenifamoduleisimportedmultipletimes,onlyasingle
    “instance” of it exists.
- No global variables are used. Instead, module specifiers serve as global IDs.


## 27.5 ECMAScript modules

**27.5 ECMAScript modules**

_ECMAScript modules_ ( _ES modules_ or _ESM_ ) were introduced with ES6. They continue the
traditionofJavaScriptmodulesandhavealloftheiraforementionedcharacteristics. Ad-
ditionally:

- WithCommonJS,ESmodulessharethecompactsyntaxandsupportforcyclicde-
    pendencies.
- With AMD, ES modules share being designed for asynchronous loading.
ES modules also have new benefits:
- The syntax is even more compact than CommonJS’s.
- Modules have _static_ structures (which can’t be changed at runtime). That helps
with static checking, optimized access of imports, dead code elimination, and
more.
- Support for cyclic imports is completely transparent.

This is an example of ES module syntax:

```
import {importedFunc1}from'./other-module1.mjs';
import {importedFunc2}from'./other-module2.mjs';
```
```
function internalFunc() {
···
}
```
```
export function exportedFunc() {
importedFunc1();
importedFunc2();
internalFunc();
}
From now on, “module” means “ECMAScript module”.
```
## 27.5.1 ES modules: syntax, semantics, loader API

The full standard of ES modules comprises the following parts:

```
1.Syntax (how code is written): What is a module? How are imports and exports
declared? Etc.
2.Semantics(howcodeisexecuted): Howarevariablebindingsexported? Howare
imports connected with exports? Etc.
3.A programmatic loader API for configuring module loading.
```
```
Parts 1 and 2 were introduced with ES6. Work on part 3 is ongoing.
```
**27.6 Named exports and imports**

## 27.6.1 Named exports

```
Each module can have zero or more named exports.
```

```
264 27 Modules
```
As an example, consider the following two files:

```
lib/my-math.mjs
main.mjs
Modulemy-math.mjshas two named exports:squareandLIGHTSPEED.
// Not exported, private to module
function times(a,b) {
return a*b;
}
export function square(x) {
return times(x,x);
}
export const LIGHTSPEED= 299792458 ;
```
To export something, we put the keywordexportin front of a declaration. Entities that
are not exported are private to a module and can’t be accessed from outside.

## 27.6.2 Named imports

```
Modulemain.mjshas a single named import,square:
import{square}from'./lib/my-math.mjs';
assert.equal(square( 3 ), 9 );
It can also rename its import:
import{squareassq}from'./lib/my-math.mjs';
assert.equal(sq( 3 ), 9 );
```
```
27.6.2.1 Syntactic pitfall: named importing is not destructuring
Both named importing and destructuring look similar:
import{foo}from'./bar.mjs';// import
const {foo}=require('./bar.mjs');// destructuring
But they are quite different:
```
- Imports remain connected with their exports.
- We can destructure again inside a destructuring pattern, but the{}in an import
    statement can’t be nested.
- The syntax for renaming is different:
    import{fooasf}from'./bar.mjs';// importing
    **const** {foo:f}=require('./bar.mjs');// destructuring
    Rationale: Destructuring is reminiscent of an object literal (including nesting),
    while importing evokes the idea of renaming.


## 27.6 Named exports and imports

```
Exercise: Named exports
exercises/modules/export_named_test.mjs
```
## 27.6.3 Namespace imports

```
Namespace imports are an alternative to named imports. If we namespace-import a mod-
ule,itbecomesanobjectwhosepropertiesarethenamedexports. Thisiswhatmain.mjs
looks like if we use a namespace import:
```
```
import *asmyMathfrom'./lib/my-math.mjs';
assert.equal(myMath.square( 3 ), 9 );
```
```
assert.deepEqual(
Object .keys(myMath),['LIGHTSPEED','square']);
```
## 27.6.4 Named exporting styles: inline versus clause (advanced)

Thenamedexportstylewehaveseensofarwas _inline_ : Weexportedentitiesbyprefixing
them with the keywordexport.

```
But we can also use separate export clauses. For example, this is whatlib/my-math.mjs
looks like with an export clause:
```
```
function times(a,b) {
return a*b;
}
function square(x) {
return times(x,x);
}
const LIGHTSPEED= 299792458 ;
```
```
export { square,LIGHTSPEED };// semicolon!
```
With an export clause, we can rename before exporting and use different names inter-
nally:

```
function times(a,b) {
return a*b;
}
function sq(x) {
return times(x,x);
}
const LS= 299792458 ;
```
```
export {
sqassquare,
LSasLIGHTSPEED,// trailing comma is optional
};
```

```
266 27 Modules
```
**27.7 Default exports and imports**

```
Eachmodulecanhaveatmostone defaultexport. Theideaisthatthemodule is thedefault-
exported value.
```
## 27.7 Default exports and imports

```
Amodulecanhavebothnamedexportsandadefaultexport,butit’susuallybetter
to stick to one export style per module.
```
As an example for default exports, consider the following two files:

```
my-func.mjs
main.mjs
```
```
Modulemy-func.mjshas a default export:
```
```
const GREETING='Hello!';
exportdefault function () {
return GREETING;
}
```
```
Modulemain.mjsdefault-imports the exported function:
```
```
importmyFuncfrom'./my-func.mjs';
assert.equal(myFunc(),'Hello!');
```
```
Note the syntactic difference: the curly braces around named imports indicate that we
are reaching into the module, while a default import is the module.
```
```
What are use cases for default exports?
The most common use case for a default export is a module that contains a single
function or a single class.
```
## 27.7.1 The two styles of default-exporting

There are two styles of doing default exports.

```
First, we can label existing declarations withexport default:
```
```
exportdefault function myFunc() {}// no semicolon!
exportdefault class MyClass {}// no semicolon!
```
```
Second,wecandirectlydefault-exportvalues. Thisstyleofexport defaultismuchlike
a declaration.
```
```
exportdefaultmyFunc;// defined elsewhere
exportdefaultMyClass;// defined previously
exportdefault Math .sqrt( 2 );// result of invocation is default-exported
```

```
27.7 Default exports and imports 267
```
```
export default'abc'+'def';
export default{no: false ,yes: true };
```
```
27.7.1.1 Why are there two default export styles?
```
Thereasonisthatexport defaultcan’tbeusedtolabelconst:constmaydefinemulti-
ple values, butexport defaultneeds exactly one value. Consider the following hypo-
thetical code:
// Not legal JavaScript!
export default **const** foo= 1 ,bar= 2 ,baz= 3 ;

With this code, we don’t know which one of the three values is the default export.

```
Exercise: Default exports
exercises/modules/export_default_test.mjs
```
## 27.7.2 The default export as a named export (advanced)

```
Internally, a default export is simply a named export whose name isdefault. As an
example, consider the previous modulemy-func.mjswith a default export:
const GREETING='Hello!';
export default function () {
return GREETING;
}
```
The following modulemy-func2.mjsis equivalent to that module:

```
const GREETING='Hello!';
function greet() {
return GREETING;
}
```
```
export {
greetasdefault,
};
For importing, we can use a normal default import:
import myFuncfrom'./my-func2.mjs';
assert.equal(myFunc(),'Hello!');
Or we can use a named import:
```
```
import {defaultasmyFunc}from'./my-func2.mjs';
assert.equal(myFunc(),'Hello!');
```
The default export is also available via property.defaultof namespace imports:

```
import *asmffrom'./my-func2.mjs';
assert.equal(mf.default(),'Hello!');
```

```
268 27 Modules
```
```
Isn’tdefaultillegal as a variable name?
defaultcan’t be a variable name, but it can be an export name and it can be a
property name:
const obj={
default : 123 ,
};
assert.equal(obj.default, 123 );
```
**27.8 More details on exporting and importing**

## 27.8.1 Imports are read-only views on exports

So far, we have used imports and exports intuitively, and everything seems to have
worked as expected. But now itis time to take a closerlook athow imports and exports
are really related.

```
Consider the following two modules:
```
```
counter.mjs
main.mjs
```
```
counter.mjsexports a (mutable!) variable and a function:
```
```
export let counter= 3 ;
export function incCounter() {
counter++;
}
```
```
main.mjsname-importsbothexports. WhenweuseincCounter(),wediscoverthatthe
connection tocounteris live – we can always access the live state of that variable:
```
```
import{ counter,incCounter }from'./counter.mjs';
```
```
// The imported value `counter` is live
assert.equal(counter, 3 );
incCounter();
assert.equal(counter, 4 );
```
Note that while the connection is live and we can readcounter, we cannot change this
variable (e.g., viacounter++).

There are two benefits to handling imports this way:

- It is easier to split modules because previously shared variables can become ex-
    ports.
- This behavior is crucial for supporting transparent cyclic imports. Read on for
    more information.


## 27.9 npm packages.

## 27.8.2 ESM’s transparent support for cyclic imports (advanced)

```
ESMsupportscyclicimportstransparently. Tounderstandhowthatisachieved,consider
the following example: fig.27.1shows a directed graph of modules importing other
modules. P importing M is the cycle in this case.
```
M

N O

P Q R S

```
Figure 27.1:A directed graph of modules importing modules: M imports N and O, N
imports P and Q, etc.
```
After parsing, these modules are set up in two phases:

- Instantiation: Everymoduleisvisitedanditsimportsareconnectedtoitsexports.
    Before a parent can be instantiated, all of its children must be instantiated.
- Evaluation: The bodies of the modules are executed. Once again, children are
    evaluated before parents.

This approach handles cyclic imports correctly, due to two features of ES modules:

- Due to the static structure of ES modules, the exports are already known after
    parsing. That makes it possible to instantiate P before its child M: P can already
    look up M’s exports.
- When P is evaluated, M hasn’t been evaluated, yet. However, entities in P can
    already mention imports from M. They just can’t use them, yet, because the im-
    ported values are filled in later. For example, a function in P can access an import
    from M. The only limitation is that we must wait until after the evaluation of M,
    before calling that function.

```
Imports being filled in later is enabled by them being “live immutable views” on
exports.
```
**27.9 npm packages**

The _npm software registry_ is the dominant way of distributing JavaScript libraries and
apps for Node.js and web browsers. It is managed via the _npm package manager_ (short:
_npm_ ). Software is distributed as so-called _packages_. A package is a directory containing
arbitrary files and a filepackage.jsonat the top level that describes the package. For
example, when npm creates an empty package inside a directorymy-package/, we get
thispackage.json:

```
{
"name":"my-package",
```

```
270 27 Modules
```
```
"version":"1.0.0",
"description":"",
"main":"index.js",
"scripts":{
"test":"echo\"Error: no test specified\"&& exit 1"
},
"keywords":[],
"author":"",
"license":"ISC"
}
Some of these properties contain simple metadata:
```
- namespecifiesthenameofthispackage. Onceitisuploadedtothenpmregistry,it
    can be installed vianpm install my-package.
- versionis used for version management and followssemantic versioning, with
    three numbers:
       **-** Major version: is incremented when incompatible API changes are made.
       **-** Minor version: is incremented when functionality is added in a backward
          compatible manner.
       **-** Patchversion: isincrementedwhenbackwardcompatiblechangesaremade.
- description,keywords,authormake it easier to find packages.
- licenseclarifies how we can use this package.

Other properties enable advanced configuration:

- main: specifies the module that “is” the package (explained later in this chapter).
- scripts: are commands that we can execute vianpm run. For example, the script
    testcan be executed vianpm run test.
For more information onpackage.json, consultthe npm documentation.

## 27.9.1 Packages are installed inside a directorynode_modules/

```
npm always installs packages inside a directorynode_modules. There are usually many
ofthesedirectories. Whichonenpmuses,dependsonthedirectorywhereonecurrently
is. Forexample,ifweareinsideadirectory/tmp/a/b/,npmtriestofindanode_modules
in the current directory, its parent directory, the parent directory of the parent, etc. In
other words, it searches the following chain of locations:
```
- /tmp/a/b/node_modules
- /tmp/a/node_modules
- /tmp/node_modules

Wheninstallingapackagesome-pkg,npmusestheclosestnode_modules. If,forexample,
weareinside/tmp/a/b/andthereisanode_modulesinthatdirectory,thennpmputsthe
package inside the directory:

```
/tmp/a/b/node_modules/some-pkg/
```
Whenimportingamodule,wecanuseaspecialmodulespecifiertotellNode.jsthatwe
want to import it from an installed package. How exactly that works, is explained later.
For now, consider the following example:


```
27.10 Naming modules 271
```
```
// /home/jane/proj/main.mjs
import *astheModulefrom'the-package/the-module.mjs';
```
To findthe-module.mjs(Node.js prefers the filename extension.mjsfor ES modules),
Node.js walks up thenode_modulechain and searches the following locations:

- /home/jane/proj/node_modules/the-package/the-module.mjs
- /home/jane/node_modules/the-package/the-module.mjs
- /home/node_modules/the-package/the-module.mjs

## 27.9.2 Why can npm be used to install frontend libraries?

Findinginstalledmodulesinnode_modulesdirectoriesisonlysupportedonNode.js. So
why can we also use npm to install libraries for browsers?

That is enabled viabundling tools, such as webpack, that compile and optimize code
beforeitisdeployedonline. Duringthiscompilationprocess,thecodeinnpmpackages
is adapted so that it works in browsers.

**27.10 Naming modules**

There are no established best practices for naming module files and the variables they
are imported into.
In this chapter, I’m using the following naming style:

- The names of module files are dash-cased and start with lowercase letters:

```
./my-module.mjs
./some-func.mjs
```
- The names of namespace imports are lowercased and camel-cased:
    import*asmyModulefrom'./my-module.mjs';
- The names of default imports are lowercased and camel-cased:
    importsomeFuncfrom'./some-func.mjs';

What are the rationales behind this style?

- npm doesn’t allow uppercase letters in package names (source). Thus, we avoid
    camel case, so that “local” files have names that are consistent with those of npm
    packages. Using only lowercase letters also minimizes conflicts between file sys-
    temsthatarecase-sensitiveandfilesystemsthataren’t: theformerdistinguishfiles
whose names have the same letters, but with different cases; the latter don’t.
- There are clear rules for translating dash-cased file names to camel-cased
    JavaScript variable names. Due to how we name namespace imports, these rules
    work for both namespace imports and default imports.
Ialsolikeunderscore-casedmodulefilenamesbecausewecandirectlyusethesenames
for namespace imports (without any translation):
import *asmy_modulefrom'./my_module.mjs';


```
272 27 Modules
```
```
Butthatstyledoesnotworkfordefaultimports: Ilikeunderscore-casingfornamespace
objects, but it is not a good choice for functions, etc.
```
**27.11 Module specifiers**

_Module specifiers_ are the strings that identify modules. They work slightly differently in
browsers and Node.js. Before we can look at the differences, we need to learn about the
different categories of module specifiers.

## 27.11.1 Categories of module specifiers

```
In ES modules, we distinguish the following categories of specifiers. These categories
originated with CommonJS modules.
```
- Relative path: starts with a dot. Examples:

```
'./some/other/module.mjs'
'../../lib/counter.mjs'
```
- Absolute path: starts with a slash. Example:

```
'/home/jane/file-tools.mjs'
```
- URL: includes a protocol (technically, paths are URLs, too). Examples:

```
'https://example.com/some-module.mjs'
'file:///home/john/tmp/main.mjs'
```
- Bare path: does not start with a dot, a slash or a protocol, and consists of a single
    filename without an extension. Examples:

```
'lodash'
'the-package'
```
- Deep import path: starts with a bare path and has at least one slash. Example:

```
'the-package/dist/the-module.mjs'
```
## 27.11.2 ES module specifiers in browsers

```
Browsers handle module specifiers as follows:
```
- Relative paths, absolute paths, and URLs work as expected. They all must point
    torealfiles(incontrasttoCommonJS,whichletsusomitfilenameextensionsand
    more).
- Thefilename extensionsofmodulesdon’tmatter,aslong asthey areserved with
    the content typetext/javascript.
- Howbarepathswillendupbeinghandledisnotyetclear. Wewillprobablyeven-
    tually be able to map them to other specifiers via lookup tables.

```
Note thatbundling toolssuch as webpack, which combine modules into fewer files, are
often less strict with specifiers than browsers. That’s because they operate at build/-
compile time (not at runtime) and can search for files by traversing the file system.
```

```
27.11 Module specifiers 273
```
## 27.11.3 ES module specifiers on Node.js

```
Node.js handles module specifiers as follows:
```
- Relativepathsareresolvedastheyareinwebbrowsers–relativetothepathofthe
    current module.
- Absolute paths are currently not supported. As a workaround, we can use URLs
    that start withfile:///. We can create such URLs viaurl.pathToFileURL().
- Onlyfile:is supported as a protocol for URL specifiers.
- A bare path is interpreted as a package name and resolved relative to the closest
    node_modulesdirectory. Whatmoduleshouldbeloaded,isdeterminedbylooking
    at property"main"of the package’spackage.json(similarly to CommonJS).
- Deep import paths are also resolved relatively to the closestnode_modulesdirec-
    tory. They contain file names, so it is always clear which module is meant.

Allspecifiers,exceptbarepaths,mustrefertoactualfiles. Thatis,ESMdoesnotsupport
the following CommonJS features:

- CommonJS automatically adds missing filename extensions.
- CommonJScanimportadirectorydirifthereisadir/package.jsonwitha"main"
    property.
- CommonJS can import a directorydirif there is a moduledir/index.js.

All built-in Node.js modules are available via bare paths and have named ESM exports

- for example:

```
import *asassertfrom'assert/strict';
import *aspathfrom'path';
```
```
assert.equal(
path.join('a/b/c','../d'),'a/b/d');
```
```
27.11.3.1 Filename extensions on Node.js
```
```
Node.js supports the following default filename extensions:
```
- .mjsfor ES modules
- .cjsfor CommonJS modules

Thefilenameextension.jsstandsforeitherESMorCommonJS.Whichoneitisisconfig-
ured via the “closest”package.json(in the current directory, the parent directory, etc.).
Usingpackage.jsonin this manner is independent of packages.
In thatpackage.json, there is a property"type", which has two settings:

- "commonjs"(the default): files with the extension.jsor without an extension are
    interpreted as CommonJS modules.
- "module": files with the extension.jsor without an extension are interpreted as
    ESM modules.


```
274 27 Modules
```
```
27.11.3.2 Interpreting non-file source code as either CommonJS or ESM
```
```
Not all source code executed by Node.js comes from files. We can also send it code via
stdin,--eval,and--print. Thecommandlineoption--input-typeletsusspecifyhow
such code is interpreted:
```
- As CommonJS (the default):--input-type=commonjs
- As ESM:--input-type=module

```
27.12 import.meta – metadata for the current module
[ES2020]
```
## 27.12import.meta– metadata for the current module [ES2020]

## 27.12.1 import.meta.url

The most important property ofimport.metais.urlwhich contains a string with the
URL of the current module’s file – for example:

```
'https://example.com/code/main.mjs'
```
## 27.12.2 import.meta.urland classURL

```
ClassURLisavailableviaaglobalvariableinbrowsersandonNode.js. Wecanlookupits
full functionality inthe Node.js documentation. When working withimport.meta.url,
its constructor is especially useful:
```
```
new URL(input:string,base?:string|URL)
```
```
ParameterinputcontainstheURLtobeparsed. Itcanberelativeifthesecondparameter,
base, is provided.
```
```
In other words, this constructor lets us resolve a relative path against a base URL:
```
```
> new URL('other.mjs', 'https://example.com/code/main.mjs').href
'https://example.com/code/other.mjs'
> new URL('../other.mjs', 'https://example.com/code/main.mjs').href
'https://example.com/other.mjs'
```
ThisishowwegetaURLinstancethatpointstoafiledata.txtthatsitsnexttothecurrent
module:

```
const urlOfData= new URL('data.txt',import.meta.url);
```
## 27.12.3 import.meta.urlon Node.js

On Node.js,import.meta.urlis always a string with afile:URL – for example:

```
'file:///Users/rauschma/my-module.mjs'
```

## 27.13Loading modules dynamically viaimport()[ES2020] (advanced)

**27.12.3.1 Example: reading a sibling file of a module**
ManyNode.jsfilesystemoperationsaccepteitherstringswithpathsorinstancesofURL.
That enables us to read a sibling filedata.txtof the current module:

```
import *asfsfrom'fs';
function readData() {
// data.txt sits next to current module
const urlOfData= new URL('data.txt',import.meta.url);
return fs.readFileSync(urlOfData,{encoding:'UTF-8'});
}
```
```
27.12.3.2 Modulefsand URLs
For most functions of the modulefs, we can refer to files via:
```
- Paths – in strings or instances ofBuffer.
- URLs – in instances ofURL(with the protocolfile:)
For more information on this topic, seethe Node.js API documentation.

```
27.12.3.3 Converting betweenfile:URLs and paths
The Node.js moduleurlhas two functions for converting betweenfile:URLs and
paths:
```
- fileURLToPath(url: URL|string): string
    Converts afile:URL to a path.
- pathToFileURL(path: string): URL
    Converts a path to afile:URL.
If we need a path that can be used in the local file system, then property.pathnameof
URLinstances does not always work:
assert.equal(
**new** URL('file:///tmp/with%20space.txt').pathname,
'/tmp/with%20space.txt');

Therefore, it is better to usefileURLToPath():

```
import *asurlfrom'url';
assert.equal(
url.fileURLToPath('file:///tmp/with%20space.txt'),
'/tmp/with space.txt');// result on Unix
Similarly,pathToFileURL()doesmorethanjustprepend'file://'toanabsolutepath.
```
```
27.13 Loadingmodulesdynamicallyviaimport()[ES2020]
(advanced)
```
```
Theimport()operator uses Promises
```

```
276 27 Modules
```
```
Promises are a technique for handling results that are computed asynchronously
(i.e., not immediately). They are explained in[content not included]. It may make
sense to postpone reading this section until you understand them.
```
## 27.13.1 The limitations of staticimportstatements

```
Sofar,theonlywaytoimportamodulehasbeenviaanimportstatement. Thatstatement
has several limitations:
```
- Wemust use itatthe top levelof a module. Thatis,wecan’t, for example, import
    something when we are inside a function or inside anifstatement.
- The module specifier is always fixed. That is, we can’t change what we import
    depending on a condition. And we can’t assemble a specifier dynamically.

## 27.13.2 Dynamic imports via theimport()operator

Theimport()operator doesn’t have the limitations ofimportstatements. It looks like
this:

```
import(moduleSpecifierStr)
.then((namespaceObject) => {
console .log(namespaceObject.namedExport);
});
```
This operator is used like a function, receives a string with a module specifier and re-
turnsaPromisethatresolvestoanamespaceobject. Thepropertiesofthatobjectarethe
exports of the imported module.
import()is even more convenient to use viaawait:

```
const namespaceObject= await import(moduleSpecifierStr);
console .log(namespaceObject.namedExport);
Note thatawaitcan be used at the top levels of modules (seenext section).
Let’s look at an example of usingimport().
```
```
27.13.2.1 Example: loading a module dynamically
```
```
Consider the following files:
lib/my-math.mjs
main1.mjs
main2.mjs
```
We have already seen modulemy-math.mjs:

```
// Not exported, private to module
function times(a,b) {
return a*b;
}
export function square(x) {
return times(x,x);
```

```
27.13 Loading modules dynamically viaimport()[ES2020] (advanced) 277
```
### }

```
export const LIGHTSPEED= 299792458 ;
```
We can useimport()to load this module on demand:

```
// main1.mjs
const moduleSpecifier='./lib/my-math.mjs';
```
```
function mathOnDemand() {
return import(moduleSpecifier)
.then(myMath => {
const result=myMath.LIGHTSPEED;
assert.equal(result, 299792458 );
return result;
});
}
```
```
mathOnDemand()
.then((result) => {
assert.equal(result, 299792458 );
});
```
Two things in this code can’t be done withimportstatements:

- We are importing inside a function (not at the top level).
- The module specifier comes from a variable.

```
Next, we’ll implement the same functionality as inmain1.mjsbut via a feature called
async function or async/await which provides nicer syntax for Promises.
```
```
// main2.mjs
const moduleSpecifier='./lib/my-math.mjs';
```
```
asyncfunction mathOnDemand() {
const myMath= await import(moduleSpecifier);
const result=myMath.LIGHTSPEED;
assert.equal(result, 299792458 );
return result;
}
```
```
Why isimport()an operator and not a function?
import()looks like a function but couldn’t be implemented as a function:
```
- It needs to know the URL of the current module in order to resolve relative

## 27.11Module specifiers.

- Ifimport()were a function, we’d have to explicitly pass this information to
    it (e.g. via an parameter).
- In contrast, an operator is a core language construct and has implicit access
    to more data, including the URL of the current module.


```
278 27 Modules
```
## 27.13.3 Use cases forimport()

```
27.13.3.1 Loading code on demand
```
```
Some functionality of web apps doesn’t have to be present when they start, it can be
loaded on demand. Thenimport()helps because we can put such functionality into
modules – for example:
```
```
button.addEventListener('click', event=> {
import('./dialogBox.mjs')
.then(dialogBox => {
dialogBox.open();
})
.catch(error => {
/* Error handling */
})
});
```
```
27.13.3.2 Conditional loading of modules
```
We may want to load a module depending on whether a condition is true. For example,
a module witha polyfillthat makes a new feature available on legacy platforms:

```
if (isLegacyPlatform()) {
import('./my-polyfill.mjs')
.then(···);
}
```
```
27.13.3.3 Computed module specifiers
```
```
For applications such as internationalization, it helps if we can dynamically compute
module specifiers:
```
```
import(`messages_${getLocale()}.mjs`)
.then(···);
```
**27.14 Top-levelawaitin modules [ES2022] (advanced)**

```
awaitis a feature of async functions
awaitisexplainedin[contentnotincluded]. Itmaymakesensetopostponereading
this section until you understand async functions.
```
We can use theawaitoperator at the top level of a module. If we do that, the module
becomes asynchronous and works differently. Thankfully, we don’t usually see that as
programmers because it is handled transparently by the language.


```
27.14 Top-levelawaitin modules [ES2022] (advanced) 279
```
## 27.14.1 Use cases for top-levelawait

Why would we want to use theawaitoperator at the top level of a module? It lets us
initialize a module with asynchronously loaded data. The next three subsections show
three examples of where that is useful.

```
27.14.1.1 Loading modules dynamically
```
```
const params= new URLSearchParams(location.search);
const language=params.get('lang');
const messages= await import(`./messages-${language}.mjs`);// (A)
```
```
console .log(messages.welcome);
InlineA,wedynamicallyimportamodule. Thankstotop-levelawait,thatisalmostas
convenient as using a normal, static import.
```
```
27.14.1.2 Using a fallback if module loading fails
let lodash;
try {
lodash= await import('https://primary.example.com/lodash');
} catch {
lodash= await import('https://secondary.example.com/lodash');
}
```
```
27.14.1.3 Using whichever resource loads fastest
```
```
const resource= awaitPromise .any([
fetch('http://example.com/first.txt')
.then(response => response.text()),
fetch('http://example.com/second.txt')
.then(response => response.text()),
]);
DuetoPromise.any(),variableresourceisinitializedviawhicheverdownloadfinishes
first.
```
## 27.14.2 How does top-levelawaitwork under the hood?

```
Consider the following two files.
first.mjs:
const response= await fetch('http://example.com/first.txt');
export const first= await response.text();
main.mjs:
import {first}from'./first.mjs';
import {second}from'./second.mjs';
assert.equal(first,'First!');
assert.equal(second,'Second!');
```

```
280 27 Modules
```
```
Both are roughly equivalent to the following code:
first.mjs:
```
```
export let first;
export const promise=( async () => {// (A)
const response= await fetch('http://example.com/first.txt');
first= await response.text();
})();
```
```
main.mjs:
import{promiseasfirstPromise,first}from'./first.mjs';
import{promiseassecondPromise,second}from'./second.mjs';
export const promise=( async () => {// (B)
awaitPromise .all([firstPromise,secondPromise]);// (C)
assert.equal(first,'First content!');
assert.equal(second,'Second content!');
})();
```
A module becomes asynchronous if:

```
1.It directly uses top-levelawait(first.mjs).
2.It imports one or more asynchronous modules (main.mjs).
```
```
EachasynchronousmoduleexportsaPromise(lineAandlineB)thatisfulfilledafterits
body was executed. At that point, it is safe to access the exports of that module.
Incase(2),theimportingmodulewaitsuntilthePromisesofallimportedasynchronous
modulesarefulfilled,beforeitentersitsbody(lineC).Synchronousmodulesarehandled
as usually.
```
Awaited rejections and synchronous exceptions are managed as in async functions.

## 27.14.3 The pros and cons of top-levelawait

The two most important benefits of top-levelawaitare:

- It ensures that modules don’t access asynchronous imports before they are fully
    initialized.
- It handles asynchronicity transparently: Importers do not need to know if an im-
    ported module is asynchronous or not.

Onthedownside,top-levelawaitdelaystheinitializationofimportingmodules. There-
fore, it‘s best used sparingly. Asynchronous tasks that take longer are better performed
later, on demand.

```
However,evenmoduleswithouttop-levelawaitcanblockimporters(e.g.viaaninfinite
loop at the top level), so blocking per se is not an argument against it.
```
```
27.15 Polyfills: emulating native web platform features
(advanced)
```

## 27.15Polyfills: emulating native web platform features (advanced).

```
Backends have polyfills, too
This section is about frontend development and web browsers, but similar ideas
apply to backend development.
```
_Polyfills_ help with a conflict that we are facing when developing a web application in
JavaScript:

- On one hand, we want to use modern web platform features that make the app
    better and/or development easier.
- On the other hand, the app should run on as many browsers as possible.
Given a web platform feature X:
- A _polyfill_ forXisapieceofcode. Ifitisexecutedonaplatformthatalreadyhasbuilt-
in support for X, it does nothing. Otherwise, it makes the feature available on the
platform. Inthelattercase,thepolyfilledfeatureis(mostly)indistinguishablefrom
anativeimplementation. Inordertoachievethat,thepolyfillusuallymakesglobal
changes. For example, it may modify global data or configure a global module
loader. Polyfills are often packaged as modules.
**-** The term _polyfill_ was coined by Remy Sharp.
- A _speculative polyfill_ is a polyfill for a proposed web platform feature (that is not
standardized, yet).
**-** Alternative term: _prollyfill_
- A _replica_ of X is a library that reproduces the API and functionality of X locally.
Such a library exists independently of a native (and global) implementation of X.
**-** _Replica_ is a new term introduced in this section. Alternative term: _ponyfill_
- Thereisalsotheterm _shim_ ,butitdoesn’thaveauniversallyagreedupondefinition.
It often means roughly the same as _polyfill_.
Everytimeourwebapplicationsstarts,itmustfirstexecuteallpolyfillsforfeaturesthat
may not be available everywhere. Afterwards, we can be sure that those features are
available natively.

## 27.15.1 Sources of this section

- “What is a Polyfill?”by Remy Sharp
- Inspiration for the term _replica_ :The Eiffel Tower in Las Vegas
- Useful clarification of “polyfill” and related terms:“Polyfills and the evolution of
    the Web”. Edited by Andrew Betts.

```
Quiz
Seequiz app.
```

282 _27 Modules_


**Chapter 28**

**Objects**

## Contents

```
28.1 Cheat sheet: objects........................... 284
28.1.1 Single objects........................... 284
28.1.2 Prototype chains......................... 286
28.2 What is an object?............................ 287
28.2.1 The two ways of using objects.................. 287
28.3 Fixed-layout objects........................... 288
28.3.1 Object literals: properties..................... 288
28.3.2 Object literals: property value shorthands........... 289
28.3.3 Getting properties......................... 289
28.3.4 Setting properties......................... 289
28.3.5 Object literals: methods..................... 290
28.3.6 Object literals: accessors..................... 290
28.4 Spreading into object literals (...) [ES2018].............. 291
28.4.1 Use case for spreading: copying objects............. 292
28.4.2 Use case for spreading: default values for missing properties. 293
28.4.3 Use case for spreading: non-destructively changing properties 293
28.4.4 “Destructive spreading”:Object.assign()[ES6]....... 294
28.5 Methods and the special variablethis................. 294
28.5.1 Methods are properties whose values are functions...... 294
28.5.2 The special variablethis..................... 295
28.5.3 Methods and.call()...................... 295
28.5.4 Methods and.bind()...................... 296
28.5.5thispitfall: extracting methods................. 296
28.5.6thispitfall: accidentally shadowingthis............ 298
28.5.7 The value ofthisin various contexts (advanced)....... 299
28.6 Optional chaining for property getting and method calls [ES2020]
(advanced)................................ 300
28.6.1 Example: optional fixed property getting............ 300
```
```
283
```

284 _28 Objects_

```
28.6.2 The operators in more detail (advanced)............ 301
28.6.3 Short-circuiting with optional property getting......... 302
28.6.4 Optional chaining: downsides and alternatives......... 303
28.6.5 Frequently asked questions................... 303
28.7 Dictionary objects (advanced)...................... 304
28.7.1 Quoted keys in object literals................... 304
28.7.2 Computed keys in object literals................. 305
28.7.3 Theinoperator: is there a property with a given key?..... 306
28.7.4 Deleting properties........................ 307
28.7.5 Enumerability........................... 307
28.7.6 Listing property keys viaObject.keys()etc........... 308
28.7.7 Listing property values viaObject.values().......... 309
28.7.8 Listing property entries viaObject.entries()[ES2017].... 309
28.7.9 Properties are listed deterministically.............. 310
28.7.10Assembling objects viaObject.fromEntries()[ES2019].... 310
28.7.11 The pitfalls of using an object as a dictionary.......... 312
28.8 Property attributes and freezing objects (advanced)......... 313
28.8.1 Property attributes and property descriptors [ES5]....... 313
28.8.2 Freezing objects [ES5]....................... 314
28.9 Prototype chains............................. 314
28.9.1 JavaScript’s operations: all properties vs. own properties... 315
28.9.2 Pitfall: only the first member of a prototype chain is mutated. 315
28.9.3 Tips for working with prototypes (advanced).......... 317
28.9.4Object.hasOwn(): Is a given property own (non-inherited)?
[ES2022].............................. 318
28.9.5 Sharing data via prototypes................... 319
28.10FAQ: objects............................... 320
28.10.1Why do objects preserve the insertion order of properties?.. 320
```
In this book, JavaScript’s style of object-oriented programming (OOP) is introduced in
four steps. This chapter covers step 1 and 2;the next chaptercovers step 3 and 4. The
steps are (fig.28.1):

1. **Single objects (this chapter):** How do _objects_ , JavaScript’s basic OOP building
    blocks, work in isolation?
2. **Prototype chains (this chapter):** Each object has a chain of zero or more _prototype_
    _objects_. Prototypes are JavaScript’s core inheritance mechanism.
3. **Classes (next chapter):** JavaScript’s _classes_ are factories for objects. The relation-
    ship between a class and its instances is based on prototypal inheritance (step 2).
4. **Subclassing (next chapter):** The relationship between a _subclass_ and its _superclass_
    is also based on prototypal inheritance.

**28.1 Cheat sheet: objects**

## 28.1.1 Single objects

Creating an object via an _object literal_ (starts and ends with a curly brace):


## 28.1 Cheat sheet: objects.

```
mthd ƒ
```
```
data
```
```
__proto__
4
```
```
ƒ
data
```
```
mthd
4
```
```
MyClass
data
mthd
```
```
SubClass
subData
subMthd
```
```
SuperClass
superData
superMthd
```
**1. Single objects2. Prototype chains** 3. Classes 4. Subclassing

Figure 28.1:This book introduces object-oriented programming in JavaScript in four
steps.

```
const myObject={// object literal
myProperty: 1 ,
myMethod() {
return 2 ;
},// comma!
getmyAccessor() {
returnthis .myProperty;
},// comma!
setmyAccessor(value) {
this .myProperty=value;
},// last comma is optional
};
```
```
assert.equal(
myObject.myProperty, 1
);
assert.equal(
myObject.myMethod(), 2
);
assert.equal(
myObject.myAccessor, 1
);
myObject.myAccessor= 3 ;
assert.equal(
myObject.myProperty, 3
);
```
Beingabletocreateobjectsdirectly(withoutclasses)isoneofthehighlightsofJavaScript.

Spreading into objects:

```
const original={
a: 1 ,
b:{
```

```
286 28 Objects
```
```
c: 3 ,
},
};
```
```
// Spreading (...) copies one object “into” another one:
const modifiedCopy={
...original,// spreading
d: 4 ,
};
```
```
assert.deepEqual(
modifiedCopy,
{
a: 1 ,
b:{
c: 3 ,
},
d: 4 ,
}
);
```
```
// Caveat: spreading copies shallowly (property values are shared)
modifiedCopy.a= 5 ;// does not affect `original`
modifiedCopy.b.c= 6 ;// affects `original`
assert.deepEqual(
original,
{
a: 1 ,// unchanged
b:{
c: 6 ,// changed
},
},
);
```
We can also use spreading to make an unmodified (shallow) copy of an object:

```
const exactCopy={...obj};
```
## 28.9 Prototype chains

PrototypesareJavaScript’sfundamentalinheritancemechanism. Evenclassesarebased
on it. Each objecthasnulloran objectasitsprototype. The latter objectcan also have a
prototype, etc. In general, we get _chains_ of prototypes.

Prototypes are managed like this:

```
// `obj1` has no prototype (its prototype is `null`)
const obj1= Object .create( null );// (A)
assert.equal(
Object .getPrototypeOf(obj1), null // (B)
```

## 28.2 What is an object?.

### );

```
// `obj2` has the prototype `proto`
const proto={
protoProp:'protoProp',
};
const obj2={
__proto__:proto,// (C)
objProp:'objProp',
}
assert.equal(
Object .getPrototypeOf(obj2),proto
);
Notes:
```
- Setting an object’s prototype while creating the object: line A, line C
- Retrieving the prototype of an object: line B
Each object inherits all the properties of its prototype:
// `obj2` inherits .protoProp from `proto`
assert.equal(
obj2.protoProp,'protoProp'
);
assert.deepEqual(
**Reflect** .ownKeys(obj2),
['objProp']// own properties of `obj2`
);

The non-inherited properties of an object are called its _own_ properties.

The most important use case for prototypes is that several objects can share methods by
inheriting them from a common prototype.

**28.2 What is an object?**

```
Objects in JavaScript:
```
- An object is a set of slots (key-value entries).
- Public slots are called _properties_ :
    **-** A property key can only be a string or a symbol.
- Private slots can only be created via classes and are explained in§29.2.4 “Public
    slots (properties) vs. private slots”.

## 28.2.1 The two ways of using objects

There are two ways of using objects in JavaScript:

- Fixed-layout objects: Used this way, objects work like records in databases. They
    have a fixed number of properties, whose keys are known at development time.
Their values generally have different types.


```
288 28 Objects
```
```
const fixedLayoutObject ={
product:'carrot',
quantity: 4 ,
};
```
- Dictionary objects: Used this way, objects work like lookup tables or maps. They
    have a variable number of properties, whose keys are not known at development
    time. All of their values have the same type.

```
const dictionaryObject={
['one']: 1 ,
['two']: 2 ,
};
```
```
Note that the two ways can also be mixed: Some objects are both fixed-layout objects
and dictionary objects.
```
The ways of using objects influence how they are explained in this chapter:

- First, we’ll explore fixed-layout objects. Even though property keys are strings or
    symbols under the hood, they will appear as fixed identifiers to us.
- Later, we’ll explore dictionary objects. Note thatMapsare usually better dictio-
    nariesthanobjects. However,someoftheoperationsthatwe’llencounterarealso

## 28.3 Fixed-layout objects.

**28.3 Fixed-layout objects**

```
Let’s first explore fixed-layout objects.
```
## 28.3.1 Object literals: properties

_Object literals_ are one way of creating fixed-layout objects. They are a stand-out feature
of JavaScript: we can directly create objects – no need for classes! This is an example:

```
const jane={
first:'Jane',
last:'Doe',// optional trailing comma
};
```
```
Intheexample,wecreatedanobjectviaanobjectliteral,whichstartsandendswithcurly
braces{}. Inside it, we defined two properties (key-value entries):
```
- The first property has the keyfirstand the value'Jane'.
- The second property has the keylastand the value'Doe'.

```
Since ES5, trailing commas are allowed in object literals.
```
Wewilllaterseeotherwaysofspecifyingpropertykeys,butwiththiswayofspecifying
them, they must follow the rules of JavaScript variable names. For example, we can
usefirst_nameas a property key, but notfirst-name). However, reserved words are
allowed:


```
28.3 Fixed-layout objects 289
```
```
const obj={
if: true ,
const : true ,
};
```
```
In order to check the effects of various operations on objects, we’ll occasionally useOb-
ject.keys()in this part of the chapter. It lists property keys:
```
```
> Object.keys({a:1, b:2})
[ 'a', 'b' ]
```
## 28.3.2 Object literals: property value shorthands

Wheneverthevalueofapropertyisdefinedviaavariablethathasthesamenameasthe
key, we can omit the key.

```
function createPoint(x,y) {
return {x,y};// Same as: {x: x, y: y}
}
assert.deepEqual(
createPoint( 9 , 2 ),
{x: 9 ,y: 2 }
);
```
## 28.3.3 Getting properties

This is how we _get_ (read) a property (line A):

```
const jane={
first:'Jane',
last:'Doe',
};
```
```
// Get property .first
assert.equal(jane.first,'Jane');// (A)
```
```
Getting an unknown property producesundefined:
```
```
assert.equal(jane.unknownProperty, undefined );
```
## 28.3.4 Setting properties

This is how we _set_ (write to) a property (line A):

```
const obj={
prop: 1 ,
};
assert.equal(obj.prop, 1 );
obj.prop= 2 ;// (A)
assert.equal(obj.prop, 2 );
```

```
290 28 Objects
```
We just changed an existing property via setting. If we set an unknown property, we
create a new entry:
**const** obj={};// empty object
assert.deepEqual(
**Object** .keys(obj),[]);

```
obj.unknownProperty='abc';
assert.deepEqual(
Object .keys(obj),['unknownProperty']);
```
## 28.3.5 Object literals: methods

The following code shows how to create the method.says()via an object literal:

**const** jane={
first:'Jane',// value property
says(text) { // method
**return** `${ **this** .first}says “${text}”`;// (A)
},// comma as separator (optional at end)
};
assert.equal(jane.says('hello'),'Jane says “hello”');
Duringthemethodcalljane.says('hello'),janeiscalledthe _receiver_ ofthemethodcall
andassignedtothespecialvariablethis(moreonthisin§28.5“Methodsandthespecial
variablethis”). That enables method.says()to access the sibling property.firstin
line A.

## 28.3.6 Object literals: accessors

An _accessor_ is defined via syntax inside an object literal that looks like methods: a _getter_
and/or a _setter_ (i.e., each accessor has one or both of them).
Invoking an accessor looks like accessing a value property:

- Reading the property invokes the getter.
- Writing to the property invokes the setter.

```
28.3.6.1 Getters
```
A getter is created by prefixing a method definition with the modifierget:

```
const jane={
first:'Jane',
last:'Doe',
getfull() {
return `${ this .first}${ this .last}`;
},
};
```
```
assert.equal(jane.full,'Jane Doe');
```

## 28.4 Spreading into object literals (...) [ES2018].

```
jane.first='John';
assert.equal(jane.full,'John Doe');
```
```
28.3.6.2 Setters
```
A setter is created by prefixing a method definition with the modifierset:

```
const jane={
first:'Jane',
last:'Doe',
setfull(fullName) {
const parts=fullName.split(' ');
this .first=parts[ 0 ];
this .last=parts[ 1 ];
},
};
```
```
jane.full='Richard Roe';
assert.equal(jane.first,'Richard');
assert.equal(jane.last,'Roe');
```
```
Exercise: Creating an object via an object literal
exercises/objects/color_point_object_test.mjs
```
**28.4 Spreading into object literals (...) [ES2018]**

```
Insideanobjectliteral,a spreadproperty addsthepropertiesofanotherobjecttothecurrent
one:
> const obj = {one: 1, two: 2};
> {...obj, three: 3}
{ one: 1, two: 2, three: 3 }
```
```
const obj1={one: 1 ,two: 2 };
const obj2={three: 3 };
assert.deepEqual(
{...obj1,...obj2,four: 4 },
{one: 1 ,two: 2 ,three: 3 , four: 4 }
);
```
```
If property keys clash, the property that is mentioned last “wins”:
> const obj = {one: 1, two: 2, three: 3};
> {...obj, one: true}
{ one: true, two: 2, three: 3 }
> {one: true, ...obj}
{ one: 1, two: 2, three: 3 }
```
All values are spreadable, evenundefinedandnull:


```
292 28 Objects
```
```
> {...undefined}
{}
> {...null}
{}
> {...123}
{}
> {...'abc'}
{ '0': 'a', '1': 'b', '2': 'c' }
> {...['a', 'b']}
{ '0': 'a', '1': 'b' }
```
```
Property.lengthof strings and Arrays is hidden from this kind of operation (it is not
enumerable ; see§28.8.1 “Property attributes and property descriptors [ES5]”for more in-
formation).
```
```
Spreading includes properties whose keys are symbols (which are ignored byOb-
ject.keys(),Object.values()andObject.entries()):
```
```
const symbolKey= Symbol ('symbolKey');
const obj={
stringKey: 1 ,
[symbolKey]: 2 ,
};
assert.deepEqual(
{...obj,anotherStringKey: 3 },
{
stringKey: 1 ,
[symbolKey]: 2 ,
anotherStringKey: 3 ,
}
);
```
## 28.4.1 Use case for spreading: copying objects

We can use spreading to create a copy of an objectoriginal:

```
const copy={...original};
```
Caveat – copying is _shallow_ :copyis a fresh object with duplicates of all properties (key-
value entries) oforiginal. But if property values are objects, then those are not copied
themselves; they are shared betweenoriginalandcopy. Let’s look at an example:

```
const original={a: 1 ,b:{prop: true } };
const copy={...original};
```
The first level ofcopyis really a copy: If we change any properties at that level, it does
not affect the original:

```
copy.a= 2 ;
assert.deepEqual(
original,{a: 1 ,b:{prop: true } });// no change
```

```
28.4 Spreading into object literals (...) [ES2018] 293
```
```
However, deeper levels are not copied. For example, the value of.bis shared between
original and copy. Changing.bin the copy also changes it in the original.
copy.b.prop= false ;
assert.deepEqual(
original,{a: 1 ,b:{prop: false } });
```
```
JavaScript doesn’t have built-in support for deep copying
Deep copies of objects (where all levels are copied) are notoriously difficult to do
generically. Therefore, JavaScript does not have a built-in operation for them (for
now). If we need such an operation, we have to implement it ourselves.
```
## 28.4.2 Use case for spreading: default values for missing properties

```
If one of the inputs of our code is an object with data, we can make properties optional
byspecifyingdefaultvaluesthatareusedifthosepropertiesaremissing. Onetechnique
fordoingsoisviaanobjectwhosepropertiescontainthedefaultvalues. Inthefollowing
example, that object isDEFAULTS:
```
```
const DEFAULTS={alpha:'a',beta:'b'};
const providedData={alpha: 1 };
```
```
const allData={...DEFAULTS,...providedData};
assert.deepEqual(allData,{alpha: 1 ,beta:'b'});
```
Theresult,theobjectallData,iscreatedbycopyingDEFAULTSandoverridingitsproper-
ties with those ofprovidedData.

```
Butwedon’tneedanobjecttospecifythedefaultvalues;wecanalsospecifytheminside
the object literal, individually:
```
```
const providedData={alpha: 1 };
```
```
const allData={alpha:'a',beta:'b',...providedData};
assert.deepEqual(allData,{alpha: 1 ,beta:'b'});
```
## 28.4.3 Use case for spreading: non-destructively changing properties

```
Sofar,wehaveencounteredonewayofchangingaproperty.alphaofanobject: We set
it (line A) and mutate the object. That is, this way of changing a property is destructive.
const obj={alpha:'a',beta:'b'};
obj.alpha= 1 ;// (A)
assert.deepEqual(obj,{alpha: 1 ,beta:'b'});
```
Withspreading,wecanchange.alphanon-destructively–wemakeacopyofobjwhere
.alphahas a different value:

```
const obj={alpha:'a',beta:'b'};
const updatedObj={...obj,alpha: 1 };
```

```
294 28 Objects
```
```
assert.deepEqual(updatedObj,{alpha: 1 ,beta:'b'});
```
```
Exercise: Non-destructively updating a property via spreading (fixed key)
exercises/objects/update_name_test.mjs
```
## 28.4.4 “Destructive spreading”:Object.assign()[ES6]

```
Object.assign()is a tool method:
```
```
Object .assign(target,source_1,source_2,···)
```
This expression assigns all properties ofsource_1totarget, then all properties of
source_2, etc. At the end, it returnstarget– for example:

```
const target={a: 1 };
```
```
const result= Object .assign(
target,
{b: 2 },
{c: 3 ,b: true });
```
```
assert.deepEqual(
result,{a: 1 ,b: true ,c: 3 });
// target was modified and returned:
assert.equal(result,target);
```
The use cases forObject.assign()are similar to those for spread properties. In a way,
it spreads destructively.

**28.5 Methods and the special variablethis**

## 28.5.1 Methods are properties whose values are functions

```
Let’s revisit the example that was used to introduce methods:
```
```
const jane={
first:'Jane',
says(text) {
return `${ this .first}says “${text}”`;
},
};
```
```
Somewhat surprisingly, methods are functions:
```
```
assert.equal( typeof jane.says,'function');
```
Why is that? We learnedin the chapter on callable valuesthat ordinary functions play
several roles. _Method_ is one of those roles. Therefore, internally,janeroughly looks as
follows.


## 28.5 Methods and the special variablethis

```
const jane={
first:'Jane',
says: function (text) {
return `${ this .first}says “${text}”`;
},
};
```
## 28.5.2 The special variablethis

```
Consider the following code:
```
```
const obj={
someMethod(x,y) {
assert.equal( this ,obj);// (A)
assert.equal(x,'a');
assert.equal(y,'b');
}
};
obj.someMethod('a','b');// (B)
```
```
In line B,objis the receiver of a method call. It is passed to the function stored in
obj.someMethodvia an implicit (hidden) parameter whose name isthis(line A).
```
```
How to understandthis
The best way to understandthisis as an implicit parameter of ordinary functions
(and therefore methods, too).
```
## 28.5.3 Methods and.call()

```
Methods are functions and functions have methods themselves. One of those methods
is.call(). Let’s look at an example to understand how this method works.
In the previous section, there was this method invocation:
obj.someMethod('a','b')
```
This invocation is equivalent to:

```
obj.someMethod.call(obj,'a','b');
```
Which is also equivalent to:

```
const func=obj.someMethod;
func.call(obj,'a','b');
.call()makes the normally implicit parameterthisexplicit: When invoking a func-
tion via.call(), the first parameter isthis, followed by the regular (explicit) function
parameters.
```
As an aside, this means that there are actually two different dot operators:

```
1.One for accessing properties:obj.prop
```

```
296 28 Objects
```
```
2.Another one for calling methods:obj.prop()
```
They are different in that (2) is not just (1) followed by the function call operator().
Instead, (2) additionally provides a value forthis.

## 28.5.4 Methods and.bind()

```
.bind()isanothermethodoffunctionobjects. Inthefollowingcode,weuse.bind()to
turn method.says()into the stand-alone functionfunc():
const jane={
first:'Jane',
says(text) {
return `${ this .first}says “${text}”`;// (A)
},
};
```
```
const func=jane.says.bind(jane,'hello');
assert.equal(func(),'Jane says “hello”');
Settingthistojanevia.bind()iscrucialhere. Otherwise,func()wouldn’tworkprop-
erly becausethisis used in line A. In the next section, we’ll explore why that is.
```
## 28.5.5 thispitfall: extracting methods

Wenowknowquiteabitaboutfunctionsandmethodsandarereadytotakealookatthe
biggestpitfallinvolvingmethodsandthis: function-callingamethodextractedfroman
object can fail if we are not careful.
In the following example, we fail when we extract methodjane.says(), store it in the
variablefunc, and function-callfunc.

```
const jane={
first:'Jane',
says(text) {
return `${ this .first}says “${text}”`;
},
};
const func=jane.says;// extract the method
assert.throws(
() => func('hello'),// (A)
{
name:'TypeError',
message:"Cannot read properties of undefined (reading 'first')",
});
In line A, we are making a normal function call. And in normal function calls,this
isundefined(ifstrict modeis active, which it almost always is). Line A is therefore
equivalent to:
assert.throws(
() => jane.says.call( undefined ,'hello'),// `this` is undefined!
```

```
28.5 Methods and the special variablethis 297
```
### {

```
name:'TypeError',
message:"Cannot read properties of undefined (reading 'first')",
}
);
```
```
How do we fix this? We need to use.bind()to extract method.says():
```
```
const func2=jane.says.bind(jane);
assert.equal(func2('hello'),'Jane says “hello”');
```
The.bind()ensures thatthisis alwaysjanewhen we callfunc().

We can also use arrow functions to extract methods:

```
const func3=text => jane.says(text);
assert.equal(func3('hello'),'Jane says “hello”');
```
```
28.5.5.1 Example: extracting a method
```
Thefollowingisasimplifiedversionofcodethatwemayseeinactualwebdevelopment:

```
class ClickHandler {
constructor(id,elem) {
this .id=id;
elem.addEventListener('click', this .handleClick);// (A)
}
handleClick( event ) {
alert('Clicked '+ this .id);
}
}
```
```
InlineA,wedon’textractthemethod.handleClick()properly. Instead,weshoulddo:
const listener= this .handleClick.bind( this );
elem.addEventListener('click',listener);
```
```
// Later, possibly:
elem.removeEventListener('click',listener);
```
```
Eachinvocationof.bind()createsanewfunction. That’swhyweneedtostoretheresult
somewhere if we want to remove it later on.
```
```
28.5.5.2 How to avoid the pitfall of extracting methods
```
Alas, there is no simple way around the pitfall of extracting methods: Whenever we
extract a method, we have to be careful and do it properly – for example, by binding
thisor by using an arrow function.

```
Exercise: Extracting a method
exercises/objects/method_extraction_exrc.mjs
```

```
298 28 Objects
```
## 28.5.6 thispitfall: accidentally shadowingthis

```
Accidentally shadowingthisis only an issue with ordinary functions
Arrow functions don’t shadowthis.
```
Consider the following problem: when we are inside an ordinary function, we can’t ac-
cess thethisof the surrounding scope because the ordinary function has its ownthis.
In other words, a variable in an inner scope hides a variable in an outer scope. That is
called _shadowing_. The following code is an example:

**const** prefixer={
prefix:'==> ',
prefixStringArray(stringArray) {
**return** stringArray.map(
**function** (x) {
**returnthis** .prefix+x;// (A)
});
},
};
assert.throws(
() **=>** prefixer.prefixStringArray(['a','b']),
{
name:'TypeError',
message:"Cannot read properties of undefined (reading 'prefix')",
}
);
In line A, we want to access thethisof.prefixStringArray(). But we can’t since the
surrounding ordinary function has its ownthisthat _shadows_ (and blocks access to) the
thisofthemethod. Thevalueoftheformerthisisundefinedduetothecallbackbeing
function-called. That explains the error message.

Thesimplestwaytofixthisproblemisviaanarrowfunction,whichdoesn’thaveitsown
thisand therefore doesn’t shadow anything:
**const** prefixer={
prefix:'==> ',
prefixStringArray(stringArray) {
**return** stringArray.map(
(x) **=>** {
**returnthis** .prefix+x;
});
},
};
assert.deepEqual(
prefixer.prefixStringArray(['a','b']),
['==> a','==> b']);

We can also storethisin a different variable (line A), so that it doesn’t get shadowed:


```
28.5 Methods and the special variablethis 299
```
```
prefixStringArray(stringArray) {
const that= this ;// (A)
return stringArray.map(
function (x) {
return that.prefix+x;
});
},
```
Another option is to specify a fixedthisfor the callback via.bind()(line A):

```
prefixStringArray(stringArray) {
return stringArray.map(
function (x) {
returnthis .prefix+x;
}.bind( this ));// (A)
},
```
```
Lastly,.map()lets us specify a value forthis(line A) that it uses when invoking the
callback:
```
```
prefixStringArray(stringArray) {
return stringArray.map(
function (x) {
returnthis .prefix+x;
},
this );// (A)
},
```
```
28.5.6.1 Avoiding the pitfall of accidentally shadowingthis
If we follow the advice in§25.3.4 “Recommendation: prefer specialized functions over
ordinary functions”, we can avoid the pitfall of accidentally shadowingthis. This is a
summary:
```
- Use arrow functions as anonymous inline functions. They don’t havethisas an
    implicit parameter and don’t shadow it.
- Fornamedstand-alonefunctiondeclarationswecaneitherusearrowfunctionsor
    function declarations. If we do the latter, we have to make surethisisn’t men-
    tioned in their bodies.

## 28.5.7 The value ofthisin various contexts (advanced)

What is the value ofthisin various contexts?

```
Inside a callable entity, the value ofthisdepends on how the callable entity is invoked
and what kind of callable entity it is:
```
- Function call:
    **-** Ordinary functions:this === undefined(instrict mode)
    **-** Arrow functions:thisis same as in surrounding scope (lexicalthis)
- Method call:thisis receiver of call


```
300 28 Objects
```
- new:thisrefers to the newly created instance

We can also accessthisin all common top-level scopes:

- <script>element:this === globalThis
- ECMAScript modules:this === undefined
- CommonJS modules:this === module.exports

```
Tip: pretend thatthisdoesn’t exist in top-level scopes
Iliketodothatbecausetop-levelthisisconfusingandtherearebetteralternatives
for its (few) use cases.
```
```
28.6 Optional chaining for property getting and method
calls [ES2020] (advanced)
```
The following kinds of optional chaining operations exist:

```
obj?.prop // optional fixed property getting
obj?.[«expr»]// optional dynamic property getting
func?.(«arg0»,«arg1»)// optional function or method call
```
The rough idea is:

- Ifthevaluebeforethequestionmarkisneitherundefinednornull,thenperform
    the operation after the question mark.
- Otherwise, returnundefined.
Eachofthethreesyntaxesiscoveredinmoredetaillater. Theseareafewfirstexamples:

```
> null?.prop
undefined
> {prop: 1}?.prop
1
```
```
> null?.(123)
undefined
> String?.(123)
'123'
```
## 28.6.1 Example: optional fixed property getting

```
Consider the following data:
```
```
const persons=[
{
surname:'Zoe',
address:{
street:{
name:'Sesame Street',
```

## (advanced). 28.6 Optional chaining for property getting and method calls [ES2020]

```
number:'123',
},
},
},
{
surname:'Mariner',
},
{
surname:'Carmen',
address:{
},
},
];
```
We can use optional chaining to safely extract street names:

```
const streetNames=persons.map(
p => p.address?.street?.name);
assert.deepEqual(
streetNames,['Sesame Street', undefined , undefined ]
);
```
```
28.6.1.1 Handling defaults via nullish coalescing
```
Thenullish coalescing operatorallows us to use the default value'(no name)'instead
ofundefined:

```
const streetNames=persons.map(
p => p.address?.street?.name??'(no name)');
assert.deepEqual(
streetNames,['Sesame Street','(no name)','(no name)']
);
```
## 28.6.2 The operators in more detail (advanced)

```
28.6.2.1 Optional fixed property getting
```
The following two expressions are equivalent:

```
o?.prop
(o !== undefined &&o!== null )?o.prop: undefined
```
```
Examples:
```
```
assert.equal( undefined ?.prop, undefined );
assert.equal( null ?.prop, undefined );
assert.equal({prop: 1 }?.prop, 1 );
```
```
28.6.2.2 Optional dynamic property getting
```
The following two expressions are equivalent:


```
302 28 Objects
```
```
o?.[«expr»]
(o!== undefined &&o!== null )?o[«expr»]: undefined
Examples:
const key='prop';
assert.equal( undefined ?.[key], undefined );
assert.equal( null ?.[key], undefined );
assert.equal({prop: 1 }?.[key], 1 );
```
```
28.6.2.3 Optional function or method call
```
The following two expressions are equivalent:

```
f?.(arg0,arg1)
(f!== undefined &&f!== null )?f(arg0,arg1): undefined
Examples:
assert.equal( undefined ?.( 123 ), undefined );
assert.equal( null ?.( 123 ), undefined );
assert.equal( String ?.( 123 ),'123');
Note that this operator produces an error if its left-hand side is not callable:
assert.throws(
() =>true ?.( 123 ),
TypeError );
```
Why? The idea is that the operator only tolerates deliberate omissions. An uncallable
value (other thanundefinedandnull) is probably an error and should be reported,
rather than worked around.

## 28.6.3 Short-circuiting with optional property getting

```
In a chain of property gettings and method invocations, evaluation stops once the first
optional operator encountersundefinedornullat its left-hand side:
function invokeM(value) {
return value?.a.b.m();// (A)
}
```
```
const obj={
a:{
b:{
m() { return 'result'}
}
}
};
assert.equal(
invokeM(obj),'result'
);
assert.equal(
```

```
28.6 Optional chaining for property getting and method calls [ES2020] (advanced) 303
```
```
invokeM( undefined ), undefined // (B)
);
ConsiderinvokeM(undefined)in line B:undefined?.aisundefined. Therefore we’d
expect.btofailinlineA.Butitdoesn’t: The?.operatorencountersthevalueundefined
and the evaluation of the whole expression immediately returnsundefined.
```
This behavior differs from a normal operator where JavaScript always evaluates all
operands before evaluating the operator. It is called _short-circuiting_. Other short-
circuiting operators are:

- (a && b):bis only evaluated ifais truthy.
- (a || b):bis only evaluated ifais falsy.
- (c? t : e): Ifcis truthy,tis evaluated. Otherwise,eis evaluated.

## 28.6.4 Optional chaining: downsides and alternatives

```
Optional chaining also has downsides:
```
- Deeply nested structures are more difficult to manage. For example, refactoring
    is harder if there are many sequences of property names: Each one enforces the
    structure of multiple objects.
- Beingsoforgivingwhenaccessingdatahidesproblemsthatwillsurfacemuchlater
    andarethenhardertodebug. Forexample,atypoearlyinasequenceofoptional
    property names has more negative effects than a normal typo.

Analternativetooptionalchainingistoextracttheinformationonce,inasinglelocation:

- We can either write a helper function that extracts the data.
- Or we can write a function whose input is deeply nested data and whose output
    is simpler, normalized data.

With either approach, it is possible to perform checks and to fail early if there are prob-
lems.

```
Further reading:
```
- “Overly defensive programming” byCarl Vitullo
- Thread on TwitterbyCory House

## 28.6.5 Frequently asked questions

```
28.6.5.1 What is a good mnemonic for the optional chaining operator (?.)?
```
Are you occasionally unsure if the optional chaining operator starts with a dot (.?) or a
question mark (?.)? Then this mnemonic may help you:

- IF (?) the left-hand side is not nullish
- THEN (.) access a property.

```
28.6.5.2 Why are there dots ino?.[x]andf?.()?
```
The syntaxes of the following two optional operator are not ideal:


```
304 28 Objects
```
```
obj?.[«expr»] // better: obj?[«expr»]
func?.(«arg0»,«arg1»)// better: func?(«arg0», «arg1»)
```
Alas, the less elegant syntax is necessary because distinguishing the ideal syntax (first
expression) from the conditional operator (second expression) is too complicated:

```
obj?['a','b','c'].map(x => x+x)
obj?['a','b','c'].map(x => x+x):[]
```
```
28.6.5.3 Why doesnull?.propevaluate toundefinedand notnull?
```
The operator?.is mainly about its right-hand side: Does property.propexist? If not,
stopearly. Therefore,keepinginformationaboutitsleft-handsideisrarelyuseful. How-
ever, only having a single “early termination” value does simplify things.

**28.7 Dictionary objects (advanced)**

Objectsworkbestasfixed-layoutobjects. ButbeforeES6,JavaScriptdidnothaveadata
structurefordictionaries(ES6broughtMaps). Therefore,objectshadtobeusedasdictio-
naries,whichimposedasignficantconstraint: Dictionarykeyshadtobestrings(symbols
were also introduced with ES6).

Wefirstlookatfeaturesofobjectsthatarerelatedtodictionariesbutalsousefulforfixed-
layoutobjects. Thissectionconcludeswithtipsforactuallyusingobjectsasdictionaries.
(Spoiler: If possible, it’s better to use Maps.)

## 28.7.1 Quoted keys in object literals

```
So far, we have always used fixed-layout objects. Property keys were fixed tokens that
had to be valid identifiers and internally became strings:
```
```
const obj={
mustBeAnIdentifier: 123 ,
};
```
```
// Get property
assert.equal(obj.mustBeAnIdentifier, 123 );
```
```
// Set property
obj.mustBeAnIdentifier='abc';
assert.equal(obj.mustBeAnIdentifier,'abc');
```
Asanextstep,we’llgobeyondthislimitationforpropertykeys: Inthissubsection,we’ll
use arbitrary fixed strings as keys. In the next subsection, we’ll dynamically compute
keys.

Two syntaxes enable us to use arbitrary strings as property keys.

```
First, when creating property keys via object literals, we can quote property keys (with
single or double quotes):
```

## 28.7 Dictionary objects (advanced)

```
const obj={
'Can be any string!': 123 ,
};
```
```
Second, when getting or setting properties, we can use square brackets with strings in-
side them:
```
```
// Get property
assert.equal(obj['Can be any string!'], 123 );
```
```
// Set property
obj['Can be any string!']='abc';
assert.equal(obj['Can be any string!'],'abc');
```
We can also use these syntaxes for methods:

```
const obj={
'A nice method'() {
return 'Yes!';
},
};
```
```
assert.equal(obj['A nice method'](),'Yes!');
```
## 28.7.2 Computed keys in object literals

```
Intheprevioussubsection,propertykeyswerespecifiedviafixedstringsinsideobjectlit-
erals. Inthissectionwelearnhowtodynamicallycomputepropertykeys. Thatenables
us to use either arbitrary strings or symbols.
```
The syntax of dynamically computed property keys in object literals is inspired by dy-
namicallyaccessingproperties. Thatis,wecanusesquarebracketstowrapexpressions:

```
const obj={
['Hello world!']: true ,
['p'+'r'+'o'+'p']: 123 ,
[ Symbol .toStringTag]:'Goodbye',// (A)
};
```
```
assert.equal(obj['Hello world!'], true );
assert.equal(obj.prop, 123 );
assert.equal(obj[ Symbol .toStringTag],'Goodbye');
```
The main use case for computed keys is having symbols as property keys (line A).

```
Note that the square brackets operator for getting and setting properties works with
arbitrary expressions:
```
```
assert.equal(obj['p'+'r'+'o'+'p'], 123 );
assert.equal(obj['==> prop'.slice( 4 )], 123 );
```
```
Methods can have computed property keys, too:
```

```
306 28 Objects
```
```
const methodKey= Symbol ();
const obj={
[methodKey]() {
return 'Yes!';
},
};
```
```
assert.equal(obj[methodKey](),'Yes!');
For the remainder of this chapter, we’ll mostly use fixed property keys again (because
they are syntactically more convenient). But all features are also available for arbitrary
strings and symbols.
```
```
Exercise: Non-destructivelyupdatingapropertyviaspreading(computed
key)
exercises/objects/update_property_test.mjs
```
## 28.7.3 Theinoperator: is there a property with a given key?

Theinoperator checks if an object has a property with a given key:

```
const obj={
alpha:'abc',
beta: false ,
};
```
```
assert.equal('alpha' in obj, true );
assert.equal('beta' in obj, true );
assert.equal('unknownKey' in obj, false );
```
```
28.7.3.1 Checking if a property exists via truthiness
```
We can also use a truthiness check to determine if a property exists:

```
assert.equal(
obj.alpha?'exists':'does not exist',
'exists');
assert.equal(
obj.unknownKey?'exists':'does not exist',
'does not exist');
```
The previous checks work becauseobj.alphais truthy and because reading a missing
property returnsundefined(which is falsy).

Thereis,however,oneimportantcaveat: truthinesschecksfailifthepropertyexists,but
has a falsy value (undefined,null,false, 0 ,"", etc.):
assert.equal(
obj.beta?'exists':'does not exist',
'does not exist');// should be: 'exists'


```
28.7 Dictionary objects (advanced) 307
```
## 28.7.4 Deleting properties

We can delete properties via thedeleteoperator:

```
const obj={
myProp: 123 ,
};
```
```
assert.deepEqual( Object .keys(obj),['myProp']);
delete obj.myProp;
assert.deepEqual( Object .keys(obj),[]);
```
## 28.7.5 Enumerability

_Enumerability_ is an _attribute_ of a property. Non-enumerable properties are ignored by
some operations – for example, byObject.keys()and when spreading properties. By
default, most properties are enumerable. The next example shows how to change that
and how it affects spreading.

```
const enumerableSymbolKey= Symbol ('enumerableSymbolKey');
const nonEnumSymbolKey= Symbol ('nonEnumSymbolKey');
```
```
// We create enumerable properties via an object literal
const obj={
enumerableStringKey: 1 ,
[enumerableSymbolKey]: 2 ,
}
```
```
// For non-enumerable properties, we need a more powerful tool
Object .defineProperties(obj,{
nonEnumStringKey:{
value: 3 ,
enumerable: false ,
},
[nonEnumSymbolKey]:{
value: 4 ,
enumerable: false ,
},
});
```
```
// Non-enumerable properties are ignored by spreading:
assert.deepEqual(
{...obj},
{
enumerableStringKey: 1 ,
[enumerableSymbolKey]: 2 ,
}
);
```
```
Object.defineProperties()is explainedlater in this chapter. The next subsection
```

```
308 28 Objects
```
```
shows how these operations are affected by enumerability:
```
## 28.7.6 Listing property keys viaObject.keys()etc.

```
Table 28.1: Standard library methods for listing own (non-inherited)
property keys. All of them return Arrays with strings and/or symbols.
```
```
enumerable non-e. string symbol
Object.keys() ✔ ✔
Object.getOwnPropertyNames() ✔ ✔ ✔
Object.getOwnPropertySymbols() ✔ ✔ ✔
Reflect.ownKeys() ✔ ✔ ✔ ✔
```
```
Each of the methods in tbl.28.1returns an Array with the own property keys of the
parameter. In the names of the methods, we can see that the following distinction is
made:
```
- A _property key_ can be either a string or a symbol.
- A _property name_ is a property key whose value is a string.
- A _property symbol_ is a property key whose value is a symbol.

Todemonstratethefouroperations,werevisittheexamplefromtheprevioussubsection:

```
const enumerableSymbolKey= Symbol ('enumerableSymbolKey');
const nonEnumSymbolKey= Symbol ('nonEnumSymbolKey');
```
```
const obj={
enumerableStringKey: 1 ,
[enumerableSymbolKey]: 2 ,
}
Object .defineProperties(obj,{
nonEnumStringKey:{
value: 3 ,
enumerable: false ,
},
[nonEnumSymbolKey]:{
value: 4 ,
enumerable: false ,
},
});
```
```
assert.deepEqual(
Object .keys(obj),
['enumerableStringKey']
);
assert.deepEqual(
Object .getOwnPropertyNames(obj),
['enumerableStringKey','nonEnumStringKey']
```

```
28.7 Dictionary objects (advanced) 309
```
### );

```
assert.deepEqual(
Object .getOwnPropertySymbols(obj),
[enumerableSymbolKey,nonEnumSymbolKey]
);
assert.deepEqual(
Reflect .ownKeys(obj),
[
'enumerableStringKey','nonEnumStringKey',
enumerableSymbolKey,nonEnumSymbolKey,
]
);
```
## 28.7.7 Listing property values viaObject.values()

```
Object.values()lists the values of all enumerable string-keyed properties of an object:
```
```
const firstName= Symbol ('firstName');
const obj={
[firstName]:'Jane',
lastName:'Doe',
};
assert.deepEqual(
Object .values(obj),
['Doe']);
```
## 28.7.8 Listing property entries viaObject.entries()[ES2017]

```
Object.entries()listsallenumerablestring-keyedpropertiesaskey-valuepairs. Each
pair is encoded as a two-element Array:
```
```
const firstName= Symbol ('firstName');
const obj={
[firstName]:'Jane',
lastName:'Doe',
};
assert.deepEqual(
Object .entries(obj),
[
['lastName','Doe'],
]);
```
```
28.7.8.1 A simple implementation ofObject.entries()
```
The following function is a simplified version ofObject.entries():

```
function entries(obj) {
returnObject .keys(obj)
.map(key => [key,obj[key]]);
}
```

```
310 28 Objects
```
```
Exercise:Object.entries()
exercises/objects/find_key_test.mjs
```
## 28.7.9 Properties are listed deterministically

Own (non-inherited) properties of objects are always listed in the following order:

```
1.Properties with string keys that contain integer indices (that includesArray in-
dices):
In ascending numeric order
2.Remaining properties with string keys:
In the order in which they were added
3.Properties with symbol keys:
In the order in which they were added
```
The following example demonstrates how property keys are sorted according to these
rules:
> Object.keys({b:0,a:0, 10:0,2:0})
**[ '2', '10', 'b', 'a' ]**

```
The order of properties
TheECMAScriptspecificationdescribesinmoredetailhowpropertiesareordered.
```
## 28.7.10 Assembling objects viaObject.fromEntries()[ES2019]

Given an iterable over [key, value] pairs,Object.fromEntries()creates an object:
**const** symbolKey= **Symbol** ('symbolKey');
assert.deepEqual(
**Object** .fromEntries(
[
['stringKey', 1 ],
[symbolKey, 2 ],
]
),
{
stringKey: 1 ,
[symbolKey]: 2 ,
}
);
Object.fromEntries()does the opposite ofObject.entries(). However, whileOb-
ject.entries()ignores symbol-keyed properties,Object.fromEntries()doesn’t (see
previous example).

To demonstrate both, we’ll use them to implement two tool functions from the library
Underscorein the next subsubsections.


```
28.7 Dictionary objects (advanced) 311
```
```
28.7.10.1 Example:pick()
```
```
The Underscore functionpick()has the following signature:
```
```
pick(object,...keys)
```
```
It returns a copy ofobjectthat has only those properties whose keys are mentioned in
the trailing arguments:
```
```
const address={
street:'Evergreen Terrace',
number:'742',
city:'Springfield',
state:'NT',
zip:'49007',
};
assert.deepEqual(
pick(address,'street','number'),
{
street:'Evergreen Terrace',
number:'742',
}
);
```
We can implementpick()as follows:

```
function pick(object,...keys) {
const filteredEntries= Object .entries(object)
.filter(([key,_value]) => keys.includes(key));
returnObject .fromEntries(filteredEntries);
}
```
```
28.7.10.2 Example:invert()
```
```
The Underscore functioninvert()has the following signature:
```
```
invert(object)
```
```
It returns a copy ofobjectwhere the keys and values of all properties are swapped:
```
```
assert.deepEqual(
invert({a: 1 ,b: 2 ,c: 3 }),
{ 1 :'a', 2 :'b', 3 :'c'}
);
```
We can implementinvert()like this:

```
function invert(object) {
const reversedEntries= Object .entries(object)
.map(([key,value]) => [value,key]);
returnObject .fromEntries(reversedEntries);
}
```

```
312 28 Objects
```
```
28.7.10.3 A simple implementation ofObject.fromEntries()
```
The following function is a simplified version ofObject.fromEntries():

```
function fromEntries(iterable) {
const result={};
for ( const [key,value] of iterable) {
let coercedKey;
if ( typeof key==='string'|| typeof key==='symbol') {
coercedKey=key;
} else {
coercedKey= String (key);
}
result[coercedKey]=value;
}
return result;
}
```
```
Exercise: UsingObject.entries()andObject.fromEntries()
exercises/objects/omit_properties_test.mjs
```
## 28.7.11 The pitfalls of using an object as a dictionary

```
Ifweuseplainobjects(createdviaobjectliterals)asdictionaries,wehavetolookoutfor
two pitfalls.
```
The first pitfall is that theinoperator also finds inherited properties:

```
const dict={};
assert.equal('toString' in dict, true );
```
Wewantdicttobetreatedasempty,buttheinoperatordetectsthepropertiesitinherits
from its prototype,Object.prototype.

Thesecondpitfallisthatwecan’tusethepropertykey__proto__becauseithasspecial
powers (it sets the prototype of the object):
**const** dict={};

```
dict['__proto__']= 123 ;
// No property was added to dict:
assert.deepEqual( Object .keys(dict),[]);
```
```
28.7.11.1 Safely using objects as dictionaries
```
```
So how do we avoid the two pitfalls?
```
- If we can, we use Maps. They are the best solution for dictionaries.
- Ifwecan’t,weusealibraryforobjects-as-dictionariesthatprotectsusfrommaking
    mistakes.
- If that’s not possible or desired, we use an object without a prototype.


## 28.8 Property attributes and freezing objects (advanced)

The following code demonstrates using prototype-less objects as dictionaries:

```
const dict= Object .create( null );// prototype is `null`
```
```
assert.equal('toString' in dict, false );// (A)
```
```
dict['__proto__']= 123 ;
assert.deepEqual( Object .keys(dict),['__proto__']);
```
We avoided both pitfalls:

- First, a property without a prototype does not inherit any properties (line A).
- Second, in modern JavaScript,__proto__is implemented viaObject.prototype.
    ThatmeansthatitisswitchedoffifObject.prototypeisnotintheprototypechain.

```
Exercise: Using an object as a dictionary
exercises/objects/simple_dict_test.mjs
```
**28.8 Property attributes and freezing objects (advanced)**

## 28.8.1 Property attributes and property descriptors [ES5]

Just as objects are composed of properties, properties are composed of _attributes_. The
value of a property is only one of several attributes. Others include:

- writable: Is it possible to change the value of the property?
- enumerable: Is the property considered byObject.keys(), spreading, etc.?

Whenweareusingoneoftheoperationsforhandlingpropertyattributes,attributesare
specified via _property descriptors_ : objects where each property represents one attribute.
For example, this is how we read the attributes of a propertyobj.myProp:
**const** obj={myProp: 123 };
assert.deepEqual(
**Object** .getOwnPropertyDescriptor(obj,'myProp'),
{
value: 123 ,
writable: **true** ,
enumerable: **true** ,
configurable: **true** ,
});

And this is how we change the attributes ofobj.myProp:

```
assert.deepEqual( Object .keys(obj),['myProp']);
```
```
// Hide property `myProp` from Object.keys()
// by making it non-enumerable
Object .defineProperty(obj,'myProp',{
enumerable: false ,
```

```
314 28 Objects
```
### });

```
assert.deepEqual( Object .keys(obj),[]);
Further reading:
```
- Enumerability is covered in greater detailearlier in this chapter.
- For more information on property attributes and property descriptors, see _Deep_
    _JavaScript_.

## 28.8.2 Freezing objects [ES5]

```
Object.freeze(obj)makesobjcompletelyimmutable: Wecan’tchangeproperties,add
properties, or change its prototype – for example:
const frozen= Object .freeze({x: 2 ,y: 5 });
assert.throws(
() => { frozen.x= 7 },
{
name:'TypeError',
message:/^Cannot assign to read only property 'x'/,
});
```
```
Under the hood,Object.freeze()changes the attributes of properties (e.g., it makes
themnon-writable)andobjects(e.g.,itmakesthem non-extensible ,meaningthatnoprop-
erties can be added anymore).
```
There is one caveat:Object.freeze(obj)freezes shallowly. That is, only the properties
ofobjare frozen but not objects stored in properties.

```
More information
Formoreinformationonfreezingandotherwaysoflockingdownobjects,see Deep
JavaScript.
```
**28.9 Prototype chains**

```
Prototypes are JavaScript’s only inheritance mechanism: Each object has a prototype
thatiseithernulloranobject. Inthelattercase,theobjectinheritsalloftheprototype’s
properties.
In an object literal, we can set the prototype via the special property__proto__:
```
```
const proto={
protoProp:'a',
};
const obj={
__proto__:proto,
objProp:'b',
};
```

_28.9 Prototype chains_ 315

```
// obj inherits .protoProp:
assert.equal(obj.protoProp,'a');
assert.equal('protoProp' in obj, true );
```
Given that a prototype object can have a prototype itself, we get a chain of objects – the
so-called _prototype chain_. Inheritance gives us the impression that we are dealing with
single objects, but we are actually dealing with chains of objects.

Fig.28.2shows what the prototype chain ofobjlooks like.

```
__proto__
protoProp 'a'
```
```
proto
```
## 

```
objProp
```
```
__proto__
'b'
```
```
obj
```
```
Figure 28.2:objstarts a chain of objects that continues withprotoand other objects.
```
Non-inherited properties are called _own properties_ .objhas one own property,.objProp.

## 28.9.1 JavaScript’s operations: all properties vs. own properties

Someoperationsconsiderallproperties(ownandinherited)–forexample,gettingprop-
erties:

```
> const obj = { one: 1 };
> typeof obj.one // own
'number'
> typeof obj.toString // inherited
'function'
```
Other operations only consider own properties – for example,Object.keys():

```
> Object.keys(obj)
[ 'one' ]
```
Read on for another operation that also only considers own properties: setting proper-
ties.

## 28.9.2 Pitfall: only the first member of a prototype chain is mutated

Given an objectobjwith a chain of prototype objects, it makes sense that setting an
own property ofobjonly changesobj. However, setting an inherited property viaobj


```
316 28 Objects
```
```
also only changesobj. Itcreates anew own property inobjthatoverridestheinherited
property. Let’s explore how that works with the following object:
```
```
const proto={
protoProp:'a',
};
const obj={
__proto__:proto,
objProp:'b',
};
```
In the next code snippet, we set the inherited propertyobj.protoProp(line A). That
“changes”itby creatingan own property: When readingobj.protoProp,the own prop-
erty is found first and its value _overrides_ the value of the inherited property.

```
// In the beginning, obj has one own property
assert.deepEqual( Object .keys(obj),['objProp']);
```
```
obj.protoProp='x';// (A)
```
```
// We created a new own property:
assert.deepEqual( Object .keys(obj),['objProp','protoProp']);
```
```
// The inherited property itself is unchanged:
assert.equal(proto.protoProp,'a');
```
```
// The own property overrides the inherited property:
assert.equal(obj.protoProp,'x');
```
```
The prototype chain ofobjis depicted in fig.28.3.
```
```
protoProp 'a'
```
```
__proto__
```
```
proto
```
## 

```
'b'
```
```
__proto__
objProp
protoProp 'x'
```
```
obj
```
```
Figure28.3:Theownproperty.protoPropofobjoverridesthepropertyinheritedfrom
proto.
```

```
28.9 Prototype chains 317
```
## 28.9.3 Tips for working with prototypes (advanced)

```
28.9.3.1 Getting and setting prototypes
```
```
Recommendations for__proto__:
```
- Don’t use__proto__as a pseudo-property (a setter of all instances ofObject):
    **-** It can’t be used with all objects (e.g. objects that are not instances ofObject).
    **-** The language specification has deprecated it.
For more information on this feature see§29.8.7 “Object.prototype.__proto__-
(accessor)”.
- Using__proto__in object literals to set prototypes is different: It’s a feature of
    object literals that has no pitfalls.

The recommended ways of getting and setting prototypes are:

- Getting the prototype of an object:
    **Object** .getPrototypeOf(obj: **Object** ): **Object**
- The best time to set the prototype of an object is when we are creating it. We can
    do so via__proto__in an object literal or via:
       **Object** .create(proto: **Object** ): **Object**
If we have to, we can useObject.setPrototypeOf()to change the prototype of
an existing object. But that may affect performance negatively.

This is how these features are used:

```
const proto1={};
const proto2a={};
const proto2b={};
```
```
const obj1={
__proto__:proto1,
a: 1 ,
b: 2 ,
};
assert.equal( Object .getPrototypeOf(obj1),proto1);
```
```
const obj2= Object .create(
proto2a,
{
a:{
value: 1 ,
writable: true ,
enumerable: true ,
configurable: true ,
},
b:{
value: 2 ,
```

```
318 28 Objects
```
```
writable: true ,
enumerable: true ,
configurable: true ,
},
}
);
assert.equal( Object .getPrototypeOf(obj2),proto2a);
```
```
Object .setPrototypeOf(obj2,proto2b);
assert.equal( Object .getPrototypeOf(obj2),proto2b);
```
```
28.9.3.2 Checking if an object is in the prototype chain of another object
```
So far, “protois a prototype ofobj” always meant “protois a _direct_ prototype ofobj”.
Butitcanalsobeusedmorelooselyandmeanthatprotoisintheprototypechainofobj.
That looser relationship can be checked via.isPrototypeOf():

```
For example:
const a={};
const b={__proto__:a};
const c={__proto__:b};
```
```
assert.equal(a.isPrototypeOf(b), true );
assert.equal(a.isPrototypeOf(c), true );
```
```
assert.equal(c.isPrototypeOf(a), false );
assert.equal(a.isPrototypeOf(a), false );
Formoreinformationonthismethodsee§29.8.5“Object.prototype.isPrototypeOf()”.
```
## 28.9.4 Object.hasOwn(): Is a given property own (non-inherited)?

## [ES2022]

Theinoperator (line A) checks if an object has a given property. In contrast,Ob-
ject.hasOwn()(lines B and C) checks if a property is own.

```
const proto={
protoProp:'protoProp',
};
const obj={
__proto__:proto,
objProp:'objProp',
}
assert.equal('protoProp' in obj, true );// (A)
assert.equal( Object .hasOwn(obj,'protoProp'), false );// (B)
assert.equal( Object .hasOwn(proto,'protoProp'), true );// (C)
```

```
28.9 Prototype chains 319
```
```
Alternative before ES2022:.hasOwnProperty()
BeforeES2022,wecanuseanotherfeature:§29.8.8“Object.prototype.hasOwnProperty()”.
This feature has pitfalls, but the referenced section explains how to work around
them.
```
## 28.9.5 Sharing data via prototypes

```
Consider the following code:
```
```
const jane={
firstName:'Jane',
describe() {
return 'Person named '+ this .firstName;
},
};
const tarzan={
firstName:'Tarzan',
describe() {
return 'Person named '+ this .firstName;
},
};
```
```
assert.equal(jane.describe(),'Person named Jane');
assert.equal(tarzan.describe(),'Person named Tarzan');
```
We have two objects that are very similar. Both have two properties whose names are
.firstNameand.describe. Additionally, method.describe()is the same. How can
we avoid duplicating that method?

We can move it to an objectPersonProtoand make that object a prototype of bothjane
andtarzan:

```
const PersonProto={
describe() {
return 'Person named '+ this .firstName;
},
};
const jane={
__proto__:PersonProto,
firstName:'Jane',
};
const tarzan={
__proto__:PersonProto,
firstName:'Tarzan',
};
```
The name of the prototype reflects that bothjaneandtarzanare persons.

```
Fig.28.4illustrates how the three objects are connected: The objects at the bottom now
```

```
320 28 Objects
```
```
__proto__
firstName 'Jane' firstName
```
```
__proto__
'Tarzan'
```
```
describe function() {···}
```
```
jane tarzan
```
```
PersonProto
```
```
Figure28.4:Objectsjaneandtarzansharemethod.describe(),viatheircommonpro-
totypePersonProto.
```
```
containthepropertiesthatarespecifictojaneandtarzan. Theobjectatthetopcontains
the properties that are shared between them.
```
When we make the method calljane.describe(),thispoints to the receiver of that
methodcall,jane(inthebottom-leftcornerofthediagram). That’swhythemethodstill
works.tarzan.describe()works similarly.

```
assert.equal(jane.describe(),'Person named Jane');
assert.equal(tarzan.describe(),'Person named Tarzan');
Looking ahead to the next chapter on classes – this is how classes are organized inter-
nally:
```
- All instances share a common prototype with methods.
- Instance-specific data is stored in own properties in each instance.
§29.3 “The internals of classes”explains this in more detail.

**28.10 FAQ: objects**

## 28.10.1 Why do objects preserve the insertion order of properties?

```
In principle, objects are unordered. The main reason for ordering properties is so that
operationsthatlistentries,keys,orvaluesaredeterministic. Thathelps,e.g.,withtesting.
```
```
Quiz
Seequiz app.
```

**Chapter 29**

**Classes [ES6]**

## CONTENTS

```
29.1 Cheat sheet: classes........................... 322
29.2 The essentials of classes......................... 324
29.2.1 A class for persons........................ 324
29.2.2 Class expressions......................... 326
29.2.3 Theinstanceofoperator..................... 326
29.2.4 Public slots (properties) vs. private slots............ 326
29.2.5 Private slots in more detail [ES2022] (advanced)........ 327
29.2.6 The pros and cons of classes in JavaScript............ 332
29.2.7 Tips for using classes....................... 333
29.3 The internals of classes......................... 333
29.3.1 A class is actually two connected objects............ 333
29.3.2 Classes set up the prototype chains of their instances..... 334
29.3.3.__proto__vs..prototype................... 334
29.3.4Person.prototype.constructor(advanced).......... 335
29.3.5 Dispatched vs. direct method calls (advanced)......... 335
29.3.6 Classes evolved from ordinary functions (advanced)...... 337
29.4 Prototype members of classes...................... 339
29.4.1 Public prototype methods and accessors............ 339
29.4.2 Private methods and accessors [ES2022]............. 341
29.5 Instance members of classes [ES2022]................. 342
29.5.1 Instance public fields....................... 342
29.5.2 Instance private fields...................... 344
29.5.3 Private instance data before ES2022 (advanced)........ 345
29.5.4 Simulating protected visibility and friend visibility via
WeakMaps (advanced)...................... 347
29.6 Static members of classes........................ 348
29.6.1 Static public methods and accessors............... 348
29.6.2 Static public fields [ES2022]................... 349
```
```
321
```

## 29 Classes [ES6]

```
29.6.3 Static private methods, accessors, and fields [ES2022]..... 350
29.6.4 Static initialization blocks in classes [ES2022].......... 351
29.6.5 Pitfall: Usingthisto access static private fields........ 353
29.6.6 All members (static, prototype, instance) can access all private
members.............................. 354
29.6.7 Static private methods and data before ES2022......... 355
29.6.8 Static factory methods...................... 356
29.7 Subclassing................................ 357
29.7.1 The internals of subclassing (advanced)............. 358
29.7.2instanceofand subclassing (advanced)............ 359
29.7.3 Not all objects are instances ofObject(advanced)....... 360
29.7.4 Prototype chains of built-in objects (advanced)......... 361
29.7.5 Mixin classes (advanced)..................... 363
29.8 The methods and accessors ofObject.prototype(advanced).... 364
29.8.1 UsingObject.prototypemethods safely............ 365
29.8.2Object.prototype.toString()................. 367
29.8.3Object.prototype.toLocaleString()............. 367
29.8.4Object.prototype.valueOf().................. 367
29.8.5Object.prototype.isPrototypeOf().............. 368
29.8.6Object.prototype.propertyIsEnumerable()......... 368
29.8.7Object.prototype.__proto__(accessor)............ 370
29.8.8Object.prototype.hasOwnProperty()............. 370
29.9 FAQ: classes................................ 371
29.9.1 Why are they called “instance private fields” in this book and
not “private instance fields”?................... 371
29.9.2 Why the identifier prefix#? Why not declare private fields via
private?.............................. 371
```
In this book, JavaScript’s style of object-oriented programming (OOP) is introduced in
four steps. This chapter covers step 3 and 4,the previous chaptercovers step 1 and 2.
The steps are (fig.29.1):

1. **Single objects (previous chapter):** How do _objects_ , JavaScript’s basic OOP build-
    ing blocks, work in isolation?
2. **Prototype chains (previous chapter):** Each object has a chain of zero or more _pro-_
    _totype objects_. Prototypes are JavaScript’s core inheritance mechanism.
3. **Classes(thischapter):** JavaScript’s _classes_ arefactoriesforobjects. Therelationship
    between a class and its instances is based on prototypal inheritance (step 2).
4. **Subclassing (this chapter):** The relationship between a _subclass_ and its _superclass_
    is also based on prototypal inheritance.

**29.1 Cheat sheet: classes**

```
Superclass:
```

## 29.1 Cheat sheet: classes.

```
mthd ƒ
```
```
data
```
```
__proto__
4
```
```
ƒ
data
```
```
mthd
4
```
```
MyClass
data
mthd
```
```
SubClass
subData
subMthd
```
```
SuperClass
superData
superMthd
```
1. Single objects 2. Prototype chains **3. Classes 4. Subclassing**

Figure 29.1:This book introduces object-oriented programming in JavaScript in four
steps.

```
class Person {
#firstName;// (A)
constructor(firstName) {
this .#firstName=firstName;// (B)
}
describe() {
return `Person named ${ this .#firstName}`;
}
static extractNames(persons) {
return persons.map(person => person.#firstName);
}
}
const tarzan= new Person('Tarzan');
assert.equal(
tarzan.describe(),
'Person named Tarzan'
);
assert.deepEqual(
Person.extractNames([tarzan, new Person('Cheeta')]),
['Tarzan','Cheeta']
);
```
Subclass:

```
class Employee extends Person {
constructor(firstName,title) {
super (firstName);
this .title=title;// (C)
}
describe() {
returnsuper .describe()+
` (${ this .title})`;
}
}
```

```
324 29 Classes [ES6]
```
```
const jane= new Employee('Jane','CTO');
assert.equal(
jane.title,
'CTO'
);
assert.equal(
jane.describe(),
'Person named Jane (CTO)'
);
Notes:
```
- .#firstNameis a _private field_ and must be declared (line A) before it can be initial-
    ized (line B).
       **-** Aprivatefieldcanonlybeaccessedinsideitssurroundingclass. Itcan’teven
          be accessed by subclasses.
- .titleis a property and can be initialized without a prior declaration (line C).
    JavaScriptrelativelyoftenmakesinstancedatapublic(incontrastto,e.g.,Javathat
    prefers to hide it).

**29.2 The essentials of classes**

Classes are basically a compact syntax for setting up prototype chains (which are ex-
plained inthe previous chapter). Under the hood, JavaScript’s classes are unconven-
tional. But that is something we rarely see when working with them. They should
normally feel familiar to people who have used other object-oriented programming lan-
guages.
Note that we don’t need classes to create objects. We can also do so viaobject literals.
That’swhythesingletonpatternisn’tneededinJavaScriptandclassesareusedlessthan
in many other languages that have them.

## 29.2.1 A class for persons

```
We have previously worked withjaneandtarzan, single objects representing persons.
Let’s use a class declaration to implement a factory for such objects:
class Person {
#firstName;// (A)
constructor(firstName) {
this .#firstName=firstName;// (B)
}
describe() {
return `Person named${ this .#firstName}`;
}
static extractNames(persons) {
return persons.map(person => person.#firstName);
}
}
```

## 29.2 The essentials of classes

```
janeandtarzancan now be created vianew Person():
```
```
const jane= new Person('Jane');
const tarzan= new Person('Tarzan');
```
```
Let’s examine what’s inside the body of classPerson.
```
- .constructor()is a special method that is called after the creation of a new in-
    stance. Inside it,thisrefers to that instance.
- [ES2022].#firstNameisan _instanceprivatefield_ : Suchfieldsarestoredininstances.
    They are accessed similarly to properties, but their names are separate – they al-
    ways start with hash symbols (#). And they are invisible to the world outside the
       class:

```
assert.deepEqual(
Reflect .ownKeys(jane),
[]
);
```
```
Beforewecaninitialize.#firstNameintheconstructor(lineB),weneedtodeclare
it by mentioning it in the class body (line A).
```
- .describe()is a method. If we invoke it viaobj.describe()thenthisrefers to
    objinside the body of.describe().

```
assert.equal(
jane.describe(),'Person named Jane'
);
assert.equal(
tarzan.describe(),'Person named Tarzan'
);
```
- .extractName()is a _static_ method. “Static” means that it belongs to the class, not
    to instances:

```
assert.deepEqual(
Person.extractNames([jane,tarzan]),
['Jane','Tarzan']
);
```
We can also create instance properties (public fields) in constructors:

```
class Container {
constructor(value) {
this .value=value;
}
}
const abcContainer= new Container('abc');
assert.equal(
abcContainer.value,'abc'
);
```

```
326 29 Classes [ES6]
```
```
In contrast to instance private fields, instance properties don’t have to be declared in
class bodies.
```
## 29.2.2 Class expressions

There are two kinds of _class definitions_ (ways of defining classes):

- _Class declarations_ , which we have seen in the previous section.
- _Class expressions_ , which we’ll see next.
Class expressions can be anonymous and named:

```
// Anonymous class expression
const Person= class { ··· };
```
```
// Named class expression
const Person= class MyClass { ··· };
```
The name of a named class expression works similarly tothe name of a named function
expression: Itcanonlybeaccessedinsidethebodyofaclassandstaysthesame,regard-
less of what the class is assigned to.

## 29.2.3 Theinstanceofoperator

Theinstanceofoperator tells us if a value is an instance of a given class:

```
> new Person('Jane') instanceof Person
true
> {} instanceof Person
false
> {} instanceof Object
true
> [] instanceof Array
true
```
We’ll explore theinstanceofoperator in more detaillater, after we have looked at sub-
classing.

## 29.2.4 Public slots (properties) vs. private slots

```
In the JavaScript language, objects can have two kinds of “slots”.
```
- _Public slots_ (which are are also called _properties_ ). For example, methods are public
    slots.
- _Private slots_ [ES2022]. For example, private fields are private slots.

These are the most important rules we need to know about properties and private slots:

- In classes, we can use public and private versions of fields, methods, getters and
    setters. All of them are slots in objects. Which objects they are placed in depends
    on whether the keywordstaticis used and other factors.
- Agetterandasetterthathavethesamekeycreateasingle _accessor_ slot. AnAcces-
    sor can also have only a getter or only a setter.


## 29.3 The internals of classes

- Properties and private slots are very different – for example:
    **-** They are stored separately.
    **-** Their keys are different. The keys of private slots can’t even be accessed di-
       rectly(see§29.2.5.2“Eachprivateslothasauniquekey(a _privatename_ )”later
       in this chapter).
    **-** Properties are inherited from prototypes, private slots aren’t.
    **-** Private slots can only be created via classes.

```
More information on properties and private slots
Thischapterdoesn’tcoveralldetailsofpropertiesandprivateslots(justtheessen-
tials). If you want to dig deeper, you can do so here:
```
- §28.8.1 “Property attributes and property descriptors [ES5]”
- Section“Object Internal Methods and Internal Slots”in the ECMAScript
    language specification explains how private slots work. Search for
“[[PrivateElements]]”.

The following class demonstrates the two kinds of slots. Each of its instances has one
private field and one property:

```
class MyClass {
#instancePrivateField= 1 ;
instanceProperty= 2 ;
getInstanceValues() {
return [
this .#instancePrivateField,
this .instanceProperty,
];
}
}
const inst= new MyClass();
assert.deepEqual(
inst.getInstanceValues(),[ 1 , 2 ]
);
```
As expected, outsideMyClass, we can only see the property:

```
assert.deepEqual(
Reflect .ownKeys(inst),
['instanceProperty']
);
```
```
Next, we’ll look at some of the details of private slots.
```
## 29.2.5 Private slots in more detail [ES2022] (advanced)


```
328 29 Classes [ES6]
```
```
29.2.5.1 Private slots can’t be accessed in subclasses
```
Aprivateslotreallycanonlybeaccessedinsidethebodyofitsclass. Wecan’tevenaccess
it from a subclass:

```
class SuperClass {
#superProp='superProp';
}
class SubClass extends SuperClass {
getSuperProp() {
returnthis .#superProp;
}
}
// SyntaxError: Private field '#superProp'
// must be declared in an enclosing class
```
Subclassing viaextendsis explained later in this chapter. How to work around this
limitation is explained in§29.5.4 “Simulating protected visibility and friend visibility
via WeakMaps”.

```
29.2.5.2 Each private slot has a unique key (a private name )
```
```
Private slots have unique keys that are similar tosymbols. Consider the following class
from earlier:
```
```
class MyClass {
#instancePrivateField= 1 ;
instanceProperty= 2 ;
getInstanceValues() {
return [
this .#instancePrivateField,
this .instanceProperty,
];
}
}
Internally, the private field ofMyClassis handled roughly like this:
```
```
let MyClass;
{// Scope of the body of the class
const instancePrivateFieldKey= Symbol ();
MyClass= class {
// Very loose approximation of how this
// works in the language specification
__PrivateElements__= newMap ([
[instancePrivateFieldKey, 1 ],
]);
instanceProperty= 2 ;
getInstanceValues() {
return [
this .__PrivateElements__.get(instancePrivateFieldKey),
```

```
29.2 The essentials of classes 329
```
```
this .instanceProperty,
];
}
}
}
```
The value ofinstancePrivateFieldKeyis called a _private name_. We can’t use private
names directly in JavaScript, we can only use them indirectly, via the fixed identifiers
of private fields, private methods, and private accessors. Where the fixed identifiers of
publicslots(suchasgetInstanceValues)areinterpretedasstringkeys,thefixedidenti-
fiers of private slots (such as#instancePrivateField) refer to private names (similarly
to how variable names refer to values).

```
29.2.5.3 The same private identifier refers to different private names in different
classes
```
```
Because the identifiers of private slots aren’t used as keys, using the same identifier in
different classes produces different slots (line A and line C):
```
```
class Color {
#name;// (A)
constructor(name) {
this .#name=name;// (B)
}
static getName(obj) {
return obj.#name;
}
}
class Person {
#name;// (C)
constructor(name) {
this .#name=name;
}
}
```
```
assert.equal(
Color.getName( new Color('green')),'green'
);
```
```
// We can’t access the private slot #name of a Person in line B:
assert.throws(
() => Color.getName( new Person('Jane')),
{
name:'TypeError',
message:'Cannot read private member #name from'
+' an object whose class did not declare it',
}
);
```

```
330 29 Classes [ES6]
```
```
29.2.5.4 The names of private fields never clash
Even if a subclass uses the same name for a private field, the two names never clash
becausetheyrefertoprivatenames(whicharealwaysunique). Inthefollowingexample,
.#privateFieldinSuperClassdoes not clash with.#privateFieldinSubClass, even
though both slots are stored directly ininst:
class SuperClass {
#privateField='super';
getSuperPrivateField() {
returnthis .#privateField;
}
}
class SubClass extends SuperClass {
#privateField='sub';
getSubPrivateField() {
returnthis .#privateField;
}
}
const inst= new SubClass();
assert.equal(
inst.getSuperPrivateField(),'super'
);
assert.equal(
inst.getSubPrivateField(),'sub'
);
Subclassing viaextendsis explained later in this chapter.
```
```
29.2.5.5 Usinginto check if an object has a given private slot
```
Theinoperator can be used to check if a private slot exists (line A):

```
class Color {
#name;
constructor(name) {
this .#name=name;
}
static check(obj) {
return #name in obj;// (A)
}
}
Let’s look at more examples ofinapplied to private slots.
Privatemethods. Thefollowingcodeshowsthatprivatemethodscreateprivateslotsin
instances:
class C1 {
#priv() {}
static check(obj) {
return #priv in obj;
```

_29.2 The essentials of classes_ 331

### }

### }

```
assert.equal(C1.check( new C1()), true );
```
**Static private fields.** We can also useinfor a static private field:

```
class C2 {
static #priv= 1 ;
static check(obj) {
return #priv in obj;
}
}
assert.equal(C2.check(C2), true );
assert.equal(C2.check( new C2()), false );
```
**Static private methods.** And we can check for the slot of a static private method:

```
class C3 {
static #priv() {}
static check(obj) {
return #priv in obj;
}
}
assert.equal(C3.check(C3), true );
```
**Using the same private identifier in different classes.** In the next example, the two
classesColorandPersonboth have a slot whose identifier is#name. Theinoperator
distinguishes them correctly:

```
class Color {
#name;
constructor(name) {
this .#name=name;
}
static check(obj) {
return #name in obj;
}
}
class Person {
#name;
constructor(name) {
this .#name=name;
}
static check(obj) {
return #name in obj;
}
}
```
```
// Detecting Color’s #name
assert.equal(
Color.check( new Color()), true
```

```
332 29 Classes [ES6]
```
### );

```
assert.equal(
Color.check( new Person()), false
);
```
```
// Detecting Person’s #name
assert.equal(
Person.check( new Person()), true
);
assert.equal(
Person.check( new Color()), false
);
```
## 29.2.6 The pros and cons of classes in JavaScript

```
I recommend using classes for the following reasons:
```
- Classes are a common standard for object creation and inheritance that is now
    widely supported across libraries and frameworks. This is an improvement com-
    pared to how things were before, when almost every framework had its own in-
    heritance library.
- They help tools such as IDEs and type checkers with their work and enable new
    features there.
- IfyoucomefromanotherlanguagetoJavaScriptandareusedtoclasses,thenyou
    can get started more quickly.
- JavaScriptenginesoptimizethem. Thatis,codethatusesclassesisalmostalways
    faster than code that uses a custom inheritance library.
- We can subclass built-in constructor functions such asError.

That doesn’t mean that classes are perfect:

- There is a risk of overdoing inheritance.
- Thereisariskofputtingtoomuchfunctionalityinclasses(whensomeofitisoften
    better put in functions).
- Classeslookfamiliartoprogrammerscomingfromotherlanguages,buttheywork
    differentlyandareuseddifferently(seenextsubsection). Therefore,thereisarisk
    of those programmers writing code that doesn’t feel like JavaScript.
- How classes seem to work superficially is quite different from how they actually
    work. In other words, there is a disconnect between syntax and semantics. Two
    examples are:
       **-** A method definition inside a class Ccreates a method in the object
          C.prototype.
       **-** Classes are functions.

```
The motivation for the disconnect is backward compatibility. Thankfully, the dis-
connect causes few problems in practice; we are usually OK if we go along with
```

```
29.3 The internals of classes 333
```
```
what classes pretend to be.
```
This was a first look at classes. We’ll explore more features soon.

```
Exercise: Writing a class
exercises/classes/point_class_test.mjs
```
## 29.2.7 Tips for using classes

- Use inheritance sparingly – it tends to make code more complicated and spread
    out related functionality across multiple locations.
- Insteadofstaticmembers,itisoftenbettertouseexternalfunctionsandvariables.
    We can even make those private to a module, simply by not exporting them. Two
       important exceptions to this rule are:
          **-** Operations that need access to private slots
          **-** Static factory methods
- Onlyputcorefunctionalityinprototypemethods. Otherfunctionalityisbetterim-
    plementedviafunctions–especiallyalgorithmsthatinvolveinstancesofmultiple
    classes.

**29.3 The internals of classes**

## 29.3.1 A class is actually two connected objects

```
Under the hood, a class becomes two connected objects. Let’s revisit classPersonto see
how that works:
class Person {
#firstName;
constructor(firstName) {
this .#firstName=firstName;
}
describe() {
return `Person named ${ this .#firstName}`;
}
static extractNames(persons) {
return persons.map(person => person.#firstName);
}
}
```
The first object created by the class is stored inPerson. It has four properties:

```
assert.deepEqual(
Reflect .ownKeys(Person),
['length','name','prototype','extractNames']
);
```
```
// The number of parameters of the constructor
```

```
334 29 Classes [ES6]
```
```
assert.equal(
Person.length, 1
);
```
```
// The name of the class
assert.equal(
Person.name,'Person'
);
```
The two remaining properties are:

- Person.extractNamesis the static method that we have already seen in action.
- Person.prototypepoints to the second object that is created by a class definition.

These are the contents ofPerson.prototype:

```
assert.deepEqual(
Reflect .ownKeys(Person.prototype),
['constructor','describe']
);
```
There are two properties:

- Person.prototype.constructorpoints to the constructor.
- Person.prototype.describeis the method that we have already used.

## 29.3.2 Classes set up the prototype chains of their instances

The objectPerson.prototypeis the prototype of all instances:

```
const jane= new Person('Jane');
assert.equal(
Object .getPrototypeOf(jane),Person.prototype
);
```
```
const tarzan= new Person('Tarzan');
assert.equal(
Object .getPrototypeOf(tarzan),Person.prototype
);
```
That explains how the instances get their methods: They inherit them from the object
Person.prototype.

```
Fig.29.2visualizes how everything is connected.
```
## 29.3.3 .__proto__vs..prototype

```
Itiseasytoconfuse.__proto__and.prototype. Hopefully,fig.29.2makesitclearhow
they differ:
```
- .__proto__isanaccessorofclassObjectthatletsusgetandsettheprototypesof
    its instances.


```
29.3 The internals of classes 335
```
```
__proto__
#firstName 'Tarzan'
```
```
describe function() {···}
```
```
constructor
```
```
tarzan
```
```
Person.prototype
```
```
extractNames function() {···}
```
```
prototype
```
```
Person
```
```
__proto__
#firstName 'Jane'
```
```
jane
```
```
Figure 29.2:The classPersonhas the property.prototypethat points to an object that
is the prototype of all instances ofPerson. The objectsjaneandtarzanare two such
instances.
```
- .prototypeis a normal property like any other. It is only special because thenew
    operator uses its value as the prototype of instances. Its name is not ideal. A dif-
    ferent name such as.instancePrototypewould be more fitting.

## 29.3.4 Person.prototype.constructor(advanced)

Thereisonedetailinfig.29.2thatwehaven’tlookedat,yet:Person.prototype.constructor
points back toPerson:
> Person.prototype.constructor === Person
**true**

This setup exists due to backward compatibility. But it has two additional benefits.

```
First, each instance of a class inherits property.constructor. Therefore, given an in-
stance, we can make “similar” objects via it:
const jane= new Person('Jane');
```
```
const cheeta= new jane.constructor('Cheeta');
// cheeta is also an instance of Person
assert.equal(cheeta instanceof Person, true );
Second, we can get the name of the class that created a given instance:
const tarzan= new Person('Tarzan');
assert.equal(tarzan.constructor.name,'Person');
```
## 29.3.5 Dispatched vs. direct method calls (advanced)

```
In this subsection, we learn about two different ways of invoking methods:
```
- Dispatched method calls


```
336 29 Classes [ES6]
```
- Direct method calls
Understanding both of them will give us important insights into how methods work.

We’ll also need the second waylaterin this chapter: It will allow us to borrow useful
methods fromObject.prototype.

```
29.3.5.1 Dispatched method calls
Let’s examine how method calls work with classes. We are revisitingjanefrom earlier:
class Person {
#firstName;
constructor(firstName) {
this .#firstName=firstName;
}
describe() {
return 'Person named '+ this .#firstName;
}
}
const jane= new Person('Jane');
Fig.29.3has a diagram withjane’s prototype chain.
```
```
__proto__
describe function() {···}
```
```
Person.prototype
```
...

```
#firstName
```
```
__proto__
'Jane'
```
```
jane
```
```
Figure 29.3: The prototype chain ofjanestarts withjaneand continues withPer-
son.prototype.
```
```
Normal method calls are dispatched – the method call
jane.describe()
happens in two steps:
```
- Dispatch: JavaScript traverses the prototype chain starting withjaneto find the
    firstobjectthathasanownpropertywiththekey'describe': Itfirstlooksatjane
    and doesn’t find an own property.describe. It continues withjane’s prototype,
    Person.prototypeand finds an own propertydescribewhose value it returns.
       **const** func=jane.describe;


```
29.3 The internals of classes 337
```
- Invocation: Method-invoking a value is different from function-invoking a value
    in that it not only calls what comes before the parentheses with the arguments
    inside the parentheses but also setsthisto the receiver of the method call (in this
    case,jane):

```
func.call(jane);
```
Thiswayofdynamicallylookingforamethodandinvokingitiscalled _dynamic dispatch_.

```
29.3.5.2 Direct method calls
```
We can also make method calls _directly_ , without dispatching:

```
Person.prototype.describe.call(jane)
```
This time, we directly point to the method viaPerson.prototype.describeand don’t
search for it in the prototype chain. We also specifythisdifferently – via.call().

```
thisalways points to the instance
No matter where in the prototype chain of an instance a method is located,this
always points to the instance (the beginning of the prototype chain). That enables
.describe()to access.#firstNamein the example.
```
Whenaredirectmethodcallsuseful? Wheneverwewanttoborrowamethodfromelse-
where that a given object doesn’t have – for example:

```
const obj= Object .create( null );
```
```
// `obj` is not an instance of Object and doesn’t inherit
// its prototype method .toString()
assert.throws(
() => obj.toString(),
/^TypeError: obj.toString is not a function$/
);
assert.equal(
Object .prototype.toString.call(obj),
'[object Object]'
);
```
## 29.3.6 Classes evolved from ordinary functions (advanced)

```
Before ECMAScript 6, JavaScript didn’t have classes. Instead,ordinary functionswere
used as constructor functions :
```
```
function StringBuilderConstr(initialString) {
this .string=initialString;
}
StringBuilderConstr.prototype.add= function (str) {
this .string+=str;
```

```
338 29 Classes [ES6]
```
```
returnthis ;
};
```
```
const sb= new StringBuilderConstr('¡');
sb.add('Hola').add('!');
assert.equal(
sb.string,'¡Hola!'
);
```
```
Classes provide better syntax for this approach:
```
```
class StringBuilderClass {
constructor(initialString) {
this .string=initialString;
}
add(str) {
this .string+=str;
returnthis ;
}
}
const sb= new StringBuilderClass('¡');
sb.add('Hola').add('!');
assert.equal(
sb.string,'¡Hola!'
);
```
```
Subclassing is especially tricky with constructor functions. Classes also offer benefits
that go beyond more convenient syntax:
```
- Built-in constructor functions such asErrorcan be subclassed.
- We can access overridden properties viasuper.
- Classes can’t be function-called.
- Methods can’t benew-called and don’t have the property.prototype.
- Support for private instance data.
- And more.

```
Classes are so compatible with constructor functions that they can even extend them:
```
```
function SuperConstructor() {}
class SubClass extends SuperConstructor {}
```
```
assert.equal(
new SubClass() instanceof SuperConstructor, true
);
```
```
extendsand subclassing are explainedlater in this chapter.
```
```
29.3.6.1 A class is the constructor
```
This brings us to an interesting insight. On one hand,StringBuilderClassrefers to its
constructor viaStringBuilderClass.prototype.constructor.


## 29.4 Prototype members of classes

```
On the other hand, the class is the constructor (a function):
```
```
> StringBuilderClass.prototype.constructor === StringBuilderClass
true
> typeof StringBuilderClass
'function'
```
```
Constructor (functions) vs. classes
Due to how similar they are, I use the terms constructor (function) and class inter-
changeably.
```
**29.4 Prototype members of classes**

## 29.4.1 Public prototype methods and accessors

All members in the body of the following class declaration create properties ofPub-
licProtoClass.prototype.

```
class PublicProtoClass {
constructor(args) {
// (Do something with `args` here.)
}
publicProtoMethod() {
return 'publicProtoMethod';
}
getpublicProtoAccessor() {
return 'publicProtoGetter';
}
setpublicProtoAccessor(value) {
assert.equal(value,'publicProtoSetter');
}
}
```
```
assert.deepEqual(
Reflect .ownKeys(PublicProtoClass.prototype),
['constructor','publicProtoMethod','publicProtoAccessor']
);
```
```
const inst= new PublicProtoClass('arg1','arg2');
assert.equal(
inst.publicProtoMethod(),'publicProtoMethod'
);
assert.equal(
inst.publicProtoAccessor,'publicProtoGetter'
);
inst.publicProtoAccessor='publicProtoSetter';
```

340 _29 Classes [ES6]_

**29.4.1.1 All kinds of public prototype methods and accessors (advanced)**

```
const accessorKey= Symbol ('accessorKey');
const syncMethodKey= Symbol ('syncMethodKey');
const syncGenMethodKey= Symbol ('syncGenMethodKey');
const asyncMethodKey= Symbol ('asyncMethodKey');
const asyncGenMethodKey= Symbol ('asyncGenMethodKey');
```
```
class PublicProtoClass2 {
// Identifier keys
getaccessor() {}
setaccessor(value) {}
syncMethod() {}
*syncGeneratorMethod() {}
async asyncMethod() {}
async *asyncGeneratorMethod() {}
```
```
// Quoted keys
get'an accessor'() {}
set'an accessor'(value) {}
'sync method'() {}
*'sync generator method'() {}
async 'async method'() {}
async *'async generator method'() {}
```
```
// Computed keys
get [accessorKey]() {}
set [accessorKey](value) {}
[syncMethodKey]() {}
*[syncGenMethodKey]() {}
async [asyncMethodKey]() {}
async *[asyncGenMethodKey]() {}
}
```
```
// Quoted and computed keys are accessed via square brackets:
const inst= new PublicProtoClass2();
inst['sync method']();
inst[syncMethodKey]();
```
Quoted and computed keys can also be used in object literals:

- §28.7.1 “Quoted keys in object literals”
- §28.7.2 “Computed keys in object literals”

More information on accessors (defined via getters and/or setters), generators, async
methods, and async generator methods:

- §28.3.6 “Object literals: accessors”
- [Content not included]
- [Content not included]


## 29.5 Instance members of classes [ES2022]

- [Content not included]

## 29.4.2 Private methods and accessors [ES2022]

```
Private methods (and accessors) are an interesting mix of prototype members and in-
stance members.
```
```
On one hand, private methods are stored in slots in instances (line A):
class MyClass {
#privateMethod() {}
static check() {
const inst= new MyClass();
assert.equal(
#privateMethod in inst, true // (A)
);
assert.equal(
#privateMethod in MyClass.prototype, false
);
assert.equal(
#privateMethod in MyClass, false
);
}
}
MyClass.check();
```
Whyaretheynotstoredin.prototypeobjects? Privateslotsarenotinherited,onlyprop-
erties are.
Ontheotherhand,privatemethodsaresharedbetweeninstances–likeprototypepublic
methods:

```
class MyClass {
#privateMethod() {}
static check() {
const inst1= new MyClass();
const inst2= new MyClass();
assert.equal(
inst1.#privateMethod,
inst2.#privateMethod
);
}
}
```
```
Due to that and due to their syntax being similar to prototype public methods, they are
covered here.
```
The following code demonstrates how private methods and accessors work:

```
class PrivateMethodClass {
#privateMethod() {
return 'privateMethod';
```

```
342 29 Classes [ES6]
```
### }

```
get #privateAccessor() {
return 'privateGetter';
}
set #privateAccessor(value) {
assert.equal(value,'privateSetter');
}
callPrivateMembers() {
assert.equal( this .#privateMethod(),'privateMethod');
assert.equal( this .#privateAccessor,'privateGetter');
this .#privateAccessor='privateSetter';
}
}
assert.deepEqual(
Reflect .ownKeys( new PrivateMethodClass()),[]
);
```
```
29.4.2.1 All kinds of private methods and accessors (advanced)
```
With private slots, the keys are always identifiers:

```
class PrivateMethodClass2 {
get #accessor() {}
set #accessor(value) {}
#syncMethod() {}
*#syncGeneratorMethod() {}
async #asyncMethod() {}
async *#asyncGeneratorMethod() {}
}
```
```
More information on accessors (defined via getters and/or setters), generators, async
methods, and async generator methods:
```
- §28.3.6 “Object literals: accessors”
- [Content not included]
- [Content not included]
- [Content not included]

**29.5 Instance members of classes [ES2022]**

## 29.5.1 Instance public fields

```
Instances of the following class have two instance properties (created in line A and line
B):
```
```
class InstPublicClass {
// Instance public field
instancePublicField= 0 ;// (A)
```
```
constructor(value) {
```

```
29.5 Instance members of classes [ES2022] 343
```
```
// We don’t need to mention .property elsewhere!
this .property=value;// (B)
}
}
```
```
const inst= new InstPublicClass('constrArg');
assert.deepEqual(
Reflect .ownKeys(inst),
['instancePublicField','property']
);
assert.equal(
inst.instancePublicField, 0
);
assert.equal(
inst.property,'constrArg'
);
```
```
If we create an instance property inside the constructor (line B), we don’t need to “de-
clare” it elsewhere. As we have already seen, that is different for instance private fields.
```
```
NotethatinstancepropertiesarerelativelycommoninJavaScript;muchmoresothanin,
e.g., Java, where most instance state is private.
```
```
29.5.1.1 Instance public fields with quoted and computed keys (advanced)
```
```
const computedFieldKey= Symbol ('computedFieldKey');
class InstPublicClass2 {
'quoted field key'= 1 ;
[computedFieldKey]= 2 ;
}
const inst= new InstPublicClass2();
assert.equal(inst['quoted field key'], 1 );
assert.equal(inst[computedFieldKey], 2 );
```
```
29.5.1.2 What is the value ofthisin instance public fields? (advanced)
```
```
In the initializer of a instance public field,thisrefers to the newly created instance:
```
```
class MyClass {
instancePublicField= this ;
}
const inst= new MyClass();
assert.equal(
inst.instancePublicField,inst
);
```
```
29.5.1.3 When are instance public fields executed? (advanced)
```
The execution of instance public fields roughly follows these two rules:


```
344 29 Classes [ES6]
```
- In base classes (classes without superclasses), instance public fields are executed
    immediately before the constructor.
- In derived classes (classes with superclasses):
    **-** The superclass sets up its instance slots whensuper()is called.
    **-** Instance public fields are executed immediately aftersuper().

The following example demonstrates these rules:

```
class SuperClass {
superProp= console .log('superProp');
constructor() {
console .log('super-constructor');
}
}
class SubClass extends SuperClass {
subProp= console .log('subProp');
constructor() {
console .log('BEFORE super()');
super ();
console .log('AFTER super()');
}
}
new SubClass();
```
```
// Output:
// 'BEFORE super()'
// 'superProp'
// 'super-constructor'
// 'subProp'
// 'AFTER super()'
```
```
extendsand subclassing are explainedlater in this chapter.
```
## 29.5.2 Instance private fields

The following class contains two instance private fields (line A and line B):

```
class InstPrivateClass {
#privateField1='private field 1';// (A)
#privateField2;// (B) required!
constructor(value) {
this .#privateField2=value;// (C)
}
/**
* Private fields are not accessible outside the class body.
*/
checkPrivateValues() {
assert.equal(
this .#privateField1,'private field 1'
);
```

```
29.5 Instance members of classes [ES2022] 345
```
```
assert.equal(
this .#privateField2,'constructor argument'
);
}
}
```
```
const inst= new InstPrivateClass('constructor argument');
inst.checkPrivateValues();
```
```
// No instance properties were created
assert.deepEqual(
Reflect .ownKeys(inst),
[]
);
```
```
Note that we can only use.#privateField2in line C if we declare it in the class body.
```
## 29.5.3 Private instance data before ES2022 (advanced)

```
Inthissection,welookattwotechniquesforkeepinginstancedataprivate. Becausethey
don’t rely on classes, we can also use them for objects that were created in other ways –
e.g., via object literals.
```
```
29.5.3.1 Before ES6: private members via naming conventions
```
The first technique makes a property private by prefixing its name with an underscore.
Thisdoesn’tprotectthepropertyinanyway;itmerelysignalstotheoutside: “Youdon’t
need to know about this property.”

```
In the following code, the properties._counterand._actionare private.
class Countdown {
constructor(counter,action) {
this ._counter=counter;
this ._action=action;
}
dec() {
this ._counter--;
if ( this ._counter=== 0 ) {
this ._action();
}
}
}
```
```
// The two properties aren’t really private:
assert.deepEqual(
Object .keys( new Countdown()),
['_counter','_action']);
```
With this technique, we don’t get any protection and private names can clash. On the


```
346 29 Classes [ES6]
```
```
plus side, it is easy to use.
```
Private methods work similarly: They are normal methods whose names start with un-
derscores.

```
29.5.3.2 ES6 and later: private instance data via WeakMaps
```
We can also manage private instance data via WeakMaps:

```
const _counter= newWeakMap ();
const _action= newWeakMap ();
```
```
class Countdown {
constructor(counter,action) {
_counter.set( this ,counter);
_action.set( this ,action);
}
dec() {
let counter=_counter.get( this );
counter--;
_counter.set( this ,counter);
if (counter=== 0 ) {
_action.get( this )();
}
}
}
```
```
// The two pseudo-properties are truly private:
assert.deepEqual(
Object .keys( new Countdown()),
[]);
```
```
How exactly that works is explainedin the chapter on WeakMaps.
```
This technique offers us considerable protection from outside access and there can’t be
any name clashes. But it is also more complicated to use.

We control the visibility of the pseudo-property_superPropby controlling who has ac-
cess to it – for example: If the variable exists inside a module and isn’t exported, every-
oneinsidethemoduleandnooneoutsidethemodulecanaccessit. Inotherwords: The
scope of privacy isn’t the class in this case, it’s the module. We could narrow the scope,
though:

```
let Countdown;
{// class scope
const _counter= newWeakMap ();
const _action= newWeakMap ();
```
```
Countdown= class {
// ···
```

```
29.5 Instance members of classes [ES2022] 347
```
### }

### }

This technique doesn’t really support private methods. But module-local functions that
have access to_superPropare the next best thing:
**const** _counter= **newWeakMap** ();
**const** _action= **newWeakMap** ();

```
class Countdown {
constructor(counter,action) {
_counter.set( this ,counter);
_action.set( this ,action);
}
dec() {
privateDec( this );
}
}
```
```
function privateDec(_this) {// (A)
let counter=_counter.get(_this);
counter--;
_counter.set(_this,counter);
if (counter=== 0 ) {
_action.get(_this)();
}
}
Note thatthisbecomes the explicit function parameter_this(line A).
```
## 29.5.4 Simulating protected visibility and friend visibility via

## WeakMaps (advanced)

As previously discussed, instance private fields are only visible inside their classes and
not even in subclasses. Thus, there is no built-in way to get:

- Protected visibility: A class and all of its subclasses can access a piece instance
    data.
- Friendvisibility: Aclassandits“friends”(designatedfunctions,objects,orclasses)
    can access a piece of instance data.
Intheprevioussubsection,wesimulated“modulevisibility”(everyoneinsideamodule
has access to a piece of instance data) via WeakMaps. Therefore:
- Ifweputaclassanditssubclassesintothesamemodule,wegetprotectedvisibil-
ity.
- If we put a class and its friends into the same module, we get friend visibility.

The next example demonstrates protected visibility:

```
const _superProp= newWeakMap ();
class SuperClass {
```

```
348 29 Classes [ES6]
```
```
constructor() {
_superProp.set( this ,'superProp');
}
}
class SubClass extends SuperClass {
getSuperProp() {
return _superProp.get( this );
}
}
assert.equal(
new SubClass().getSuperProp(),
'superProp'
);
```
```
Subclassing viaextendsis explained later in this chapter.
```
**29.6 Static members of classes**

## 29.6.1 Static public methods and accessors

All members in thebody ofthefollowing classdeclaration create so-called _static_ proper-
ties – properties ofStaticClassitself.

```
class StaticPublicMethodsClass {
static staticMethod() {
return 'staticMethod';
}
static getstaticAccessor() {
return 'staticGetter';
}
static setstaticAccessor(value) {
assert.equal(value,'staticSetter');
}
}
assert.equal(
StaticPublicMethodsClass.staticMethod(),'staticMethod'
);
assert.equal(
StaticPublicMethodsClass.staticAccessor,'staticGetter'
);
StaticPublicMethodsClass.staticAccessor='staticSetter';
```
```
29.6.1.1 All kinds of static public methods and accessors (advanced)
```
```
const accessorKey= Symbol ('accessorKey');
const syncMethodKey= Symbol ('syncMethodKey');
const syncGenMethodKey= Symbol ('syncGenMethodKey');
const asyncMethodKey= Symbol ('asyncMethodKey');
const asyncGenMethodKey= Symbol ('asyncGenMethodKey');
```

## 29.6 Static members of classes.

```
class StaticPublicMethodsClass2 {
// Identifier keys
static getaccessor() {}
static setaccessor(value) {}
static syncMethod() {}
static *syncGeneratorMethod() {}
staticasync asyncMethod() {}
staticasync *asyncGeneratorMethod() {}
```
```
// Quoted keys
static get'an accessor'() {}
static set'an accessor'(value) {}
static 'sync method'() {}
static *'sync generator method'() {}
staticasync 'async method'() {}
staticasync *'async generator method'() {}
```
```
// Computed keys
static get [accessorKey]() {}
static set [accessorKey](value) {}
static [syncMethodKey]() {}
static *[syncGenMethodKey]() {}
staticasync [asyncMethodKey]() {}
staticasync *[asyncGenMethodKey]() {}
}
```
```
// Quoted and computed keys are accessed via square brackets:
StaticPublicMethodsClass2['sync method']();
StaticPublicMethodsClass2[syncMethodKey]();
Quoted and computed keys can also be used in object literals:
```
- §28.7.1 “Quoted keys in object literals”
- §28.7.2 “Computed keys in object literals”
More information on accessors (defined via getters and/or setters), generators, async
methods, and async generator methods:
- §28.3.6 “Object literals: accessors”
- [Content not included]
- [Content not included]
- [Content not included]

## 29.6.2 Static public fields [ES2022]

Thefollowingcodedemonstratesstaticpublicfields.StaticPublicFieldClasshasthree
of them:
**const** computedFieldKey= **Symbol** ('computedFieldKey');
**class** StaticPublicFieldClass {


```
350 29 Classes [ES6]
```
```
static identifierFieldKey= 1 ;
static 'quoted field key'= 2 ;
static [computedFieldKey]= 3 ;
}
```
```
assert.deepEqual(
Reflect .ownKeys(StaticPublicFieldClass),
[
'length',// number of constructor parameters
'name',// 'StaticPublicFieldClass'
'prototype',
'identifierFieldKey',
'quoted field key',
computedFieldKey,
],
);
```
```
assert.equal(StaticPublicFieldClass.identifierFieldKey, 1 );
assert.equal(StaticPublicFieldClass['quoted field key'], 2 );
assert.equal(StaticPublicFieldClass[computedFieldKey], 3 );
```
## 29.6.3 Static private methods, accessors, and fields [ES2022]

The following class has two static private slots (line A and line B):

```
class StaticPrivateClass {
// Declare and initialize
static #staticPrivateField='hello';// (A)
static #twice() {// (B)
const str=StaticPrivateClass.#staticPrivateField;
return str+' '+str;
}
static getResultOfTwice() {
return StaticPrivateClass.#twice();
}
}
```
```
assert.deepEqual(
Reflect .ownKeys(StaticPrivateClass),
[
'length',// number of constructor parameters
'name',// 'StaticPublicFieldClass'
'prototype',
'getResultOfTwice',
],
);
```
```
assert.equal(
StaticPrivateClass.getResultOfTwice(),
```

```
29.6 Static members of classes 351
```
```
'hello hello'
);
```
This is a complete list of all kinds of static private slots:

```
class MyClass {
static #staticPrivateMethod() {}
static *#staticPrivateGeneratorMethod() {}
```
```
staticasync #staticPrivateAsyncMethod() {}
staticasync *#staticPrivateAsyncGeneratorMethod() {}
```
```
static get #staticPrivateAccessor() {}
static set #staticPrivateAccessor(value) {}
}
```
## 29.6.4 Static initialization blocks in classes [ES2022]

To set up instance data via classes, we have two constructs:

- _Fields_ , to create and optionally initialize instance data
- _Constructors_ ,blocksofcodethatareexecutedeverytimeanewinstanceiscreated

```
For static data, we have:
```
- _Static fields_
- _Static blocks_ that are executed when a class is created

The following code demonstrates static blocks (line A):

```
class Translator {
static translations={
yes:'ja',
no:'nein',
maybe:'vielleicht',
};
static englishWords=[];
static germanWords=[];
static {// (A)
for ( const [english,german] of Object .entries( this .translations)) {
this .englishWords.push(english);
this .germanWords.push(german);
}
}
}
```
We could also execute the code inside the static block after the class (at the top level).
However, using a static block has two benefits:

- All class-related code is inside the class.
- The code in a static block has access to private slots.


```
352 29 Classes [ES6]
```
```
29.6.4.1 Rules for static initialization blocks
```
The rules for how static initialization blocks work, are relatively simple:

- There can be more than one static block per class.
- The execution of static blocks is interleaved with the execution of static field ini-
    tializers.
- The static members of a superclass are executed before the static members of a
    subclass.

The following code demonstrates these rules:

```
class SuperClass {
static superField1= console .log('superField1');
static {
assert.equal( this ,SuperClass);
console .log('static block 1 SuperClass');
}
static superField2= console .log('superField2');
static {
console .log('static block 2 SuperClass');
}
}
```
```
class SubClass extends SuperClass {
static subField1= console .log('subField1');
static {
assert.equal( this ,SubClass);
console .log('static block 1 SubClass');
}
static subField2= console .log('subField2');
static {
console .log('static block 2 SubClass');
}
}
```
```
// Output:
// 'superField1'
// 'static block 1 SuperClass'
// 'superField2'
// 'static block 2 SuperClass'
// 'subField1'
// 'static block 1 SubClass'
// 'subField2'
// 'static block 2 SubClass'
```
```
Subclassing viaextendsis explained later in this chapter.
```

```
29.6 Static members of classes 353
```
## 29.6.5 Pitfall: Usingthisto access static private fields

```
In static public members, we can access static public slots viathis. Alas, we should not
use it to access static private slots.
```
```
29.6.5.1 thisand static public fields
Consider the following code:
```
```
class SuperClass {
static publicData= 1 ;
```
```
static getPublicViaThis() {
returnthis .publicData;
}
}
class SubClass extends SuperClass {
}
```
```
Subclassing viaextendsis explained later in this chapter.
```
```
Static public fields are properties. If we make the method call
assert.equal(SuperClass.getPublicViaThis(), 1 );
```
```
thenthispoints toSuperClassand everything works as expected. We can also invoke
.getPublicViaThis()via the subclass:
assert.equal(SubClass.getPublicViaThis(), 1 );
```
```
SubClassinherits.getPublicViaThis()from its prototypeSuperClass.thispoints to
SubClassandthingscontinuetowork,becauseSubClassalsoinheritstheproperty.pub-
licData.
```
As an aside, if we assigned tothis.publicDataingetPublicViaThis()and invoked it
viaSubClass.getPublicViaThis(), then we would create a new own poperty ofSub-
Classthat (non-destructively) overrides the property inherited fromSuperClass.

```
29.6.5.2 thisand static private fields
Consider the following code:
```
```
class SuperClass {
static #privateData= 2 ;
static getPrivateDataViaThis() {
returnthis .#privateData;
}
static getPrivateDataViaClassName() {
return SuperClass.#privateData;
}
}
class SubClass extends SuperClass {
}
```

```
354 29 Classes [ES6]
```
Invoking.getPrivateDataViaThis()viaSuperClassworks,becausethispointstoSu-
perClass:

```
assert.equal(SuperClass.getPrivateDataViaThis(), 2 );
```
However, invoking.getPrivateDataViaThis()viaSubClassdoes not work, because
thisnow points toSubClassandSubClasshas no static private field.#privateData
(private slots in prototype chains are not inherited):

```
assert.throws(
() => SubClass.getPrivateDataViaThis(),
{
name:'TypeError',
message:'Cannot read private member #privateData from'
+' an object whose class did not declare it',
}
);
```
The workaround is to accesss.#privateDatadirectly, viaSuperClass:

```
assert.equal(SubClass.getPrivateDataViaClassName(), 2 );
```
With static private methods, we are facing the same issue.

## 29.6.6 All members (static, prototype, instance) can access all private

## members

```
Everymemberinsideaclasscanaccessallothermembersinsidethatclass–bothpublic
and private ones:
```
```
class DemoClass {
static #staticPrivateField= 1 ;
#instPrivField= 2 ;
```
```
static staticMethod(inst) {
// A static method can access static private fields
// and instance private fields
assert.equal(DemoClass.#staticPrivateField, 1 );
assert.equal(inst.#instPrivField, 2 );
}
```
```
protoMethod() {
// A prototype method can access instance private fields
// and static private fields
assert.equal( this .#instPrivField, 2 );
assert.equal(DemoClass.#staticPrivateField, 1 );
}
}
```
```
In contrast, no one outside can access the private members:
```
```
// Accessing private fields outside their classes triggers
```

```
29.6 Static members of classes 355
```
```
// syntax errors (before the code is even executed).
assert.throws(
() => eval('DemoClass.#staticPrivateField'),
{
name:'SyntaxError',
message:"Private field '#staticPrivateField' must"
+" be declared in an enclosing class",
}
);
// Accessing private fields outside their classes triggers
// syntax errors (before the code is even executed).
assert.throws(
() => eval('new DemoClass().#instPrivField'),
{
name:'SyntaxError',
message:"Private field '#instPrivField' must"
+" be declared in an enclosing class",
}
);
```
## 29.6.7 Static private methods and data before ES2022

The following code only works in ES2022 – due to every line that has a hash symbol (#)
in it:
**class** StaticClass {
**static** #secret='Rumpelstiltskin';
**static** #getSecretInParens() {
**return** `(${StaticClass.#secret})`;
}
**static** callStaticPrivateMethod() {
**return** StaticClass.#getSecretInParens();
}
}
Since private slots only exist once per class, we can move#secretand#getSecret-
InParensto the scope surrounding the class and use a module to hide them from the
world outside the module.

```
const secret='Rumpelstiltskin';
function getSecretInParens() {
return `(${secret})`;
}
```
```
// Only the class is accessible outside the module
export class StaticClass {
static callStaticPrivateMethod() {
return getSecretInParens();
}
}
```

```
356 29 Classes [ES6]
```
## 29.6.8 Static factory methods

```
Sometimes there are multiple ways in which a class can be instantiated. Then we can
implement static factory methods such asPoint.fromPolar():
```
```
classPoint {
static fromPolar(radius,angle) {
const x=radius* Math .cos(angle);
const y=radius* Math .sin(angle);
returnnewPoint (x,y);
}
constructor(x= 0 ,y= 0 ) {
this .x=x;
this .y=y;
}
}
```
assert.deepEqual(
**Point** .fromPolar( 13 ,0.39479111969976155),
**newPoint** ( 12 , 5 )
);
I like how descriptive static factory methods are:fromPolardescribes how an instance
is created. JavaScript’s standard library also has such factory methods – for example:

- Array.from()
- Object.create()
Iprefertoeitherhavenostaticfactorymethodsor _only_ staticfactorymethods. Thingsto
consider in the latter case:
- Onefactorymethodwillprobablydirectlycalltheconstructor(buthaveadescrip-
tive name).
- We need to find a way to prevent the constructor being called from outside.

```
In the following code, we use a secret token (line A) to prevent the constructor being
called from outside the current module.
// Only accessible inside the current module
const secretToken= Symbol ('secretToken');// (A)
```
```
export classPoint {
static create(x= 0 ,y= 0 ) {
returnnewPoint (secretToken,x,y);
}
static fromPolar(radius,angle) {
const x=radius* Math .cos(angle);
const y=radius* Math .sin(angle);
returnnewPoint (secretToken,x,y);
}
constructor(token,x,y) {
if (token!==secretToken) {
```

## 29.7 Subclassing

```
thrownewTypeError ('Must use static factory method');
}
this .x=x;
this .y=y;
}
}
Point .create( 3 , 4 );// OK
assert.throws(
() =>newPoint ( 3 , 4 ),
TypeError
);
```
**29.7 Subclassing**

Classes can also extend existing classes. For example, the following classEmployeeex-
tendsPerson:

```
class Person {
#firstName;
constructor(firstName) {
this .#firstName=firstName;
}
describe() {
return `Person named ${ this .#firstName}`;
}
static extractNames(persons) {
return persons.map(person => person.#firstName);
}
}
```
```
class Employee extends Person {
constructor(firstName,title) {
super (firstName);
this .title=title;
}
describe() {
returnsuper .describe()+
` (${ this .title})`;
}
}
```
```
const jane= new Employee('Jane','CTO');
assert.equal(
jane.title,
'CTO'
);
assert.equal(
jane.describe(),
```

```
358 29 Classes [ES6]
```
```
'Person named Jane (CTO)'
);
```
Terminology related to extending:

- Another word for _extending_ is _subclassing_.
- Personis the superclass ofEmployee.
- Employeeis the subclass ofPerson.
- A _base class_ is a class that has no superclasses.
- A _derived class_ is a class that has a superclass.

Inside the.constructor()of a derived class, we must call the super-constructor via
super()before we can accessthis. Why is that?

Let’s consider a chain of classes:

- Base classA
- ClassBextendsA.
- ClassCextendsB.
If we invokenew C(),C’s constructor super-callsB’s constructor which super-callsA’s
constructor. Instances are always created in base classes, before the constructors of sub-
classes add their slots. Therefore, the instance doesn’t exist before we callsuper()and
we can’t access it viathis, yet.

```
Note that static public slots are inherited. For example,Employeeinherits the static
method.extractNames():
> 'extractNames' in Employee
true
```
```
Exercise: Subclassing
exercises/classes/color_point_class_test.mjs
```
## 29.7.1 The internals of subclassing (advanced)

TheclassesPersonandEmployeefromtheprevioussectionaremadeupofseveralobjects
(fig.29.4). One key insight for understanding how these objects are related is that there
are two prototype chains:

- The instance prototype chain, on the right.
- The class prototype chain, on the left.

```
29.7.1.1 The instance prototype chain (right column)
```
The instance prototype chain starts withjaneand continues withEmployee.prototype
andPerson.prototype. In principle, the prototype chain ends at this point, but we get
one more object:Object.prototype. This prototype provides services to virtually all
objects, which is why it is included here, too:
> Object.getPrototypeOf(Person.prototype) === Object.prototype
**true**


```
29.7 Subclassing 359
```
```
Person Person.prototype
```
```
Employee Employee.prototype
```
```
jane
```
```
__proto__
```
```
__proto__
```
```
prototype
```
```
prototype
```
```
Object.prototype
```
```
__proto__
```
```
__proto__
```
```
Function.prototype
```
```
__proto__
```
Figure 29.4:These are the objects that make up classPersonand its subclass,Employee.
The left column is about classes. The right column is about theEmployeeinstancejane
and its prototype chain.

```
29.7.1.2 The class prototype chain (left column)
```
```
In the class prototype chain,Employeecomes first,Personnext. Afterward, the chain
continues withFunction.prototype, which is only there becausePersonis a function
and functions need the services ofFunction.prototype.
```
```
> Object.getPrototypeOf(Person) === Function.prototype
true
```
## 29.7.2 instanceofand subclassing (advanced)

Wehavenotyetlearnedhowinstanceofreallyworks. Howdoesinstanceofdetermine
if a valuexis an instance of a classC(it can be a direct instance ofCor a direct instance
of a subclass ofC)? It checks ifC.prototypeis in the prototype chain ofx. That is, the
following two expressions are equivalent:

```
x instanceof C
C.prototype.isPrototypeOf(x)
```
```
If we go back to fig.29.4, we can confirm that the prototype chain does lead us to the
following correct answers:
```
```
> jane instanceof Employee
true
> jane instanceof Person
true
> jane instanceof Object
true
```
```
Note thatinstanceofalways returnsfalseif its self-hand side is a primitive value:
```

```
360 29 Classes [ES6]
```
```
> 'abc' instanceof String
false
> 123 instanceof Number
false
```
## 29.7.3 Not all objects are instances ofObject(advanced)

Anobject(anon-primitivevalue)isonlyaninstanceofObjectifObject.prototypeisin
itsprototypechain(seeprevioussubsection). VirtuallyallobjectsareinstancesofObject

- for example:

```
assert.equal(
{a: 1 } instanceofObject , true
);
assert.equal(
['a'] instanceofObject , true
);
assert.equal(
/abc/g instanceofObject , true
);
assert.equal(
newMap () instanceofObject , true
);
```
```
class C {}
assert.equal(
new C() instanceofObject , true
);
```
In the next example,obj1andobj2are both objects (line A and line C), but they are not
instancesofObject(lineBandlineD):Object.prototypeisnotintheirprototypechains
because they don’t have any prototypes.

```
const obj1={__proto__: null };
assert.equal(
typeof obj1,'object'// (A)
);
assert.equal(
obj1 instanceofObject , false // (B)
);
```
```
const obj2= Object .create( null );
assert.equal(
typeof obj2,'object'// (C)
);
assert.equal(
obj2 instanceofObject , false // (D)
);
```
```
Object.prototypeis the object that ends most prototype chains. Its prototype isnull,
```

```
29.7 Subclassing 361
```
which means it isn’t an instance ofObjecteither:

```
> typeof Object.prototype
'object'
> Object.getPrototypeOf(Object.prototype)
null
> Object.prototype instanceof Object
false
```
## 29.7.4 Prototype chains of built-in objects (advanced)

```
Next, we’ll use our knowledge of subclassing to understand the prototype chains of a
few built-in objects. The following tool functionp()helps us with our explorations.
```
```
const p= Object .getPrototypeOf.bind( Object );
```
We extracted method.getPrototypeOf()ofObjectand assigned it top.

```
29.7.4.1 The prototype chain of{}
```
```
Let’s start by examining plain objects:
> p({}) === Object.prototype
true
> p(p({})) === null
true
```
```
Object.prototype
```
```
{}
```
```
__proto__
```
```
null
```
```
__proto__
```
```
Figure29.5:Theprototypechainofanobjectcreatedviaanobjectliteralstartswiththat
object, continues withObject.prototype, and ends withnull.
```
```
Fig.29.5showsadiagramforthisprototypechain. Wecanseethat{}reallyisaninstance
ofObject–Object.prototypeis in its prototype chain.
```
```
29.7.4.2 The prototype chain of[]
```
What does the prototype chain of an Array look like?

```
> p([]) === Array.prototype
true
> p(p([])) === Object.prototype
```

```
362 29 Classes [ES6]
```
```
true
> p(p(p([]))) === null
true
```
```
Object.prototype
```
```
Array.prototype
```
```
[]
```
```
__proto__
```
```
__proto__
```
```
null
```
```
__proto__
```
```
Figure 29.6:The prototype chain of an Array has these members: the Array instance,
Array.prototype,Object.prototype,null.
```
Thisprototypechain(visualizedinfig.29.6)tellsusthatanArrayobjectisaninstanceof
Arrayand ofObject.

```
29.7.4.3 The prototype chain offunction () {}
Lastly, the prototype chain of an ordinary function tells us that all functions are objects:
```
```
> p(function () {}) === Function.prototype
true
> p(p(function () {})) === Object.prototype
true
```
```
29.7.4.4 The prototype chains of built-in classes
```
The prototype of a base class isFunction.prototypewhich means that it is a function
(an instance ofFunction):

```
class A {}
assert.equal(
Object .getPrototypeOf(A),
Function .prototype
);
```
```
assert.equal(
Object .getPrototypeOf( class {}),
Function .prototype
);
```

```
29.7 Subclassing 363
```
The prototype of a derived class is its superclass:

```
class B extends A {}
assert.equal(
Object .getPrototypeOf(B),
A
);
```
```
assert.equal(
Object .getPrototypeOf( classextendsObject {}),
Object
);
```
```
Interestingly,Object,Array, andFunctionare all base classes:
```
```
> Object.getPrototypeOf(Object) === Function.prototype
true
> Object.getPrototypeOf(Array) === Function.prototype
true
> Object.getPrototypeOf(Function) === Function.prototype
true
```
```
However,aswehaveseen,eventheinstancesofbaseclasseshaveObject.prototypein
their prototype chains because it provides services that all objects need.
```
```
Why areArrayandFunctionbase classes?
Base classes are where instances are actually created. BothArrayandFunction
need to create their own instances because they have so-called “internal slots”
which can’t be added later to instances created byObject.
```
## 29.7.5 Mixin classes (advanced)

```
JavaScript’s class system only supports single inheritance. That is, each class can have
at most one superclass. One way around this limitation is via a technique called mixin
classes (short: mixins ).
```
The idea is as follows: Let’s say we want a classCto inherit from two superclassesS1
andS2. That would be _multiple inheritance_ , which JavaScript doesn’t support.

```
Our workaround is to turnS1andS2into mixins , factories for subclasses:
```
```
const S1=(Sup) =>classextends Sup {/*···*/};
const S2=(Sup) =>classextends Sup {/*···*/};
```
```
EachofthesetwofunctionsreturnsaclassthatextendsagivensuperclassSup. Wecreate
classCas follows:
```
```
class C extends S2(S1( Object )) {
/*···*/
}
```

```
364 29 Classes [ES6]
```
We now have a classCthat extends the class returned byS2()which extends the class
returned byS1()which extendsObject.

```
29.7.5.1 Example: a mixin for brand management
```
WeimplementamixinBrandedthathashelpermethodsforsettingandgettingthebrand
of an object:

```
const Named=(Sup) =>classextends Sup {
name='(Unnamed)';
toString() {
const className= this .constructor.name;
return `${className}named${ this .name}`;
}
};
```
We use this mixin to implement a classCitythat has a name:

```
class City extends Named( Object ) {
constructor(name) {
super ();
this .name=name;
}
}
```
The following code confirms that the mixin works:

```
const paris= new City('Paris');
assert.equal(
paris.name,'Paris'
);
assert.equal(
paris.toString(),'City named Paris'
);
```
```
29.7.5.2 The benefits of mixins
```
```
Mixins free us from the constraints of single inheritance:
```
- The same class can extend a single superclass and zero or more mixins.
- The same mixin can be used by multiple classes.

```
29.8 ThemethodsandaccessorsofObject.prototype(ad-
vanced)
```
As we have seen in§29.7.3 “Not all objects are instances ofObject”, almost all objects
are instances ofObject. This class provides several useful methods and an accessor to
its instances:


```
29.8 The methods and accessors ofObject.prototype(advanced) 365
```
- Configuringhowobjectsareconvertedtoprimitivevalues(e.g.bythe+operator):
    Thefollowingmethodshavedefaultimplementationsbutareoftenoverriddenin
       subclasses or instances.
          **-** .toString(): Configures how an object is converted to a string.
          **-** .toLocaleString(): Aversionof.toString()thatcanbeconfiguredinvar-
             ious ways via arguments (language, region, etc.).
          **-** .valueOf(): Configureshowanobjectisconvertedtoanon-stringprimitive
             value (often a number).
- Useful methods (with pitfalls – see next subsection):
    **-** .isPrototypeOf(): Is the receiver in the prototype chain of a given object?
    **-** .propertyIsEnumerable(): Doesthereceiverhaveanenumerableownprop-
       erty with the given key?
- Avoid these features (there are better alternatives):
    **-** .__proto__: Get and set the prototype of the receiver.

## *Using this accessor is not recommended. Alternatives:

```
·Object.getPrototypeOf()
·Object.setPrototypeOf()
```
**-** .hasOwnProperty(): Does the receiver have an own property with a given
    key?

## *Usingthismethodisnotrecommended. AlternativeinES2022andlater:

```
Object.hasOwn().
Before we take a closer look at each of these features, we’ll learn about an important
pitfall(andhowtoworkaroundit): Wecan’tusethefeaturesofObject.prototypewith
```
## 28.10FAQ: objects.

## 29.8.1 UsingObject.prototypemethods safely

InvokingoneofthemethodsofObject.prototypeonanarbitraryobjectdoesn’talways
work. To illustrate why, we use methodObject.prototype.hasOwnProperty, which re-
turnstrueif an object has an own property with a given key:

```
> {ownProp: true}.hasOwnProperty('ownProp')
true
> {ownProp: true}.hasOwnProperty('abc')
false
Invoking.hasOwnProperty()on an arbitrary object can fail in two ways. On one hand,
this method isn’t available if an object is not an instance ofObject(see§29.7.3 “Not all
objects are instances ofObject”):
```
```
const obj= Object .create( null );
assert.equal(obj instanceofObject , false );
assert.throws(
() => obj.hasOwnProperty('prop'),
{
name:'TypeError',
message:'obj.hasOwnProperty is not a function',
}
);
```

```
366 29 Classes [ES6]
```
Ontheotherhand,wecan’tuse.hasOwnProperty()ifanobjectoverridesitwithanown
property (line A):

```
const obj={
hasOwnProperty:'yes'// (A)
};
assert.throws(
() => obj.hasOwnProperty('prop'),
{
name:'TypeError',
message:'obj.hasOwnProperty is not a function',
}
);
```
There is, however, a safe way to use.hasOwnProperty():

```
function hasOwnProp(obj,propName) {
returnObject .prototype.hasOwnProperty.call(obj,propName);// (A)
}
assert.equal(
hasOwnProp( Object .create( null ),'prop'), false
);
assert.equal(
hasOwnProp({hasOwnProperty:'yes'},'prop'), false
);
assert.equal(
hasOwnProp({hasOwnProperty:'yes'},'hasOwnProperty'), true
);
```
The method invocation in line A is explained in§29.3.5 “Dispatched vs. direct method
calls”.

We can also use.bind()to implementhasOwnProp():

```
const hasOwnProp= Object .prototype.hasOwnProperty.call
.bind( Object .prototype.hasOwnProperty);
```
Howdoesthiswork? Whenweinvoke.call()likeinlineAinthepreviousexample,it
doesexactlywhathasOwnProp()shoulddo,includingavoidingthepitfalls. However,if
we want to function-call it, we can’t simply extract it, we must also ensure that itsthis
always has the right value. That’s what.bind()does.

```
Is it never OK to useObject.prototypemethods via dynamic dispatch?
InsomecaseswecanbelazyandcallObject.prototypemethodslikenormalmeth-
ods (without.call()or.bind()): If we know the receivers and they are fixed-
layout objects.
If, on the other hand, we don’t know their receivers and/or they are dictionary
objects, then we need to take precautions.
```

```
29.8 The methods and accessors ofObject.prototype(advanced) 367
```
## 29.8.2 Object.prototype.toString()

```
By overriding.toString()(in a subclass or an instance), we can configure how objects
are converted to strings:
```
```
> String({toString() { return 'Hello!' }})
'Hello!'
> String({})
'[object Object]'
```
```
Forconvertingobjectstostringsit’sbettertouseString()becausethatalsoworkswith
undefinedandnull:
```
```
> undefined.toString()
TypeError: Cannot read properties of undefined (reading 'toString')
> null.toString()
TypeError: Cannot read properties of null (reading 'toString')
> String(undefined)
'undefined'
> String(null)
'null'
```
## 29.8.3 Object.prototype.toLocaleString()

```
.toLocaleString()is a version of.toString()that can be configured via a locale and
often additional options. Any class or instance can implement this method. In the stan-
dard library, the following classes do:
```
- Array.prototype.toLocaleString()
- Number.prototype.toLocaleString()
- Date.prototype.toLocaleString()
- TypedArray.prototype.toLocaleString()
- BigInt.prototype.toLocaleString()

As an example, this is how numbers with decimal fractions are converted to string dif-
ferently, depending on locale ('fr'is French,'en'is English):

```
> 123.45.toLocaleString('fr')
'123,45'
> 123.45.toLocaleString('en')
'123.45'
```
## 29.8.4 Object.prototype.valueOf()

```
By overriding.valueOf()(in a subclass or an instance), we can configure how objects
are converted to non-string values (often numbers):
```
```
> Number({valueOf() { return 123 }})
123
> Number({})
NaN
```

```
368 29 Classes [ES6]
```
## 29.8.5 Object.prototype.isPrototypeOf()

```
proto.isPrototypeOf(obj)returnstrueifprotois in the prototype chain ofobjand
falseotherwise.
```
```
const a={};
const b={__proto__:a};
const c={__proto__:b};
```
```
assert.equal(a.isPrototypeOf(b), true );
assert.equal(a.isPrototypeOf(c), true );
```
```
assert.equal(a.isPrototypeOf(a), false );
assert.equal(c.isPrototypeOf(a), false );
```
This is how to use this method safely (for details see§29.8.1 “UsingObject.prototype
methods safely”):

```
const obj={
// Overrides Object.prototype.isPrototypeOf
isPrototypeOf: true ,
};
// Doesn’t work in this case:
assert.throws(
() => obj.isPrototypeOf( Object .prototype),
{
name:'TypeError',
message:'obj.isPrototypeOf is not a function',
}
);
// Safe way of using .isPrototypeOf():
assert.equal(
Object .prototype.isPrototypeOf.call(obj, Object .prototype), false
);
```
## 29.8.6 Object.prototype.propertyIsEnumerable()

```
obj.propertyIsEnumerable(propKey)returnstrueifobjhasanownenumerableprop-
erty whose key ispropKeyandfalseotherwise.
```
```
const proto={
enumerableProtoProp: true ,
};
const obj={
__proto__:proto,
enumerableObjProp: true ,
nonEnumObjProp: true ,
};
Object .defineProperty(
obj,'nonEnumObjProp',
```

```
29.8 The methods and accessors ofObject.prototype(advanced) 369
```
### {

```
enumerable: false ,
}
);
```
```
assert.equal(
obj.propertyIsEnumerable('enumerableProtoProp'),
false // not an own property
);
assert.equal(
obj.propertyIsEnumerable('enumerableObjProp'),
true
);
assert.equal(
obj.propertyIsEnumerable('nonEnumObjProp'),
false // not enumerable
);
assert.equal(
obj.propertyIsEnumerable('unknownProp'),
false // not a property
);
```
This is how to use this method safely (for details see§29.8.1 “UsingObject.prototype
methods safely”):

```
const obj={
// Overrides Object.prototype.propertyIsEnumerable
propertyIsEnumerable: true ,
enumerableProp:'yes',
};
// Doesn’t work in this case:
assert.throws(
() => obj.propertyIsEnumerable('enumerableProp'),
{
name:'TypeError',
message:'obj.propertyIsEnumerable is not a function',
}
);
// Safe way of using .propertyIsEnumerable():
assert.equal(
Object .prototype.propertyIsEnumerable.call(obj,'enumerableProp'),
true
);
```
Another safe alternative is to useproperty descriptors:

```
assert.deepEqual(
Object .getOwnPropertyDescriptor(obj,'enumerableProp'),
{
value:'yes',
```

```
370 29 Classes [ES6]
```
```
writable: true ,
enumerable: true ,
configurable: true ,
}
);
```
## 29.8.7 Object.prototype.__proto__(accessor)

```
Property__proto__exists in two versions:
```
- An accessor that all instances ofObjecthave.
- Apropertyofobjectliteralsthatsetstheprototypesoftheobjectscreatedbythem.

```
I recommend to avoid the former feature:
```
- As explained in§29.8.1 “UsingObject.prototypemethods safely”, it doesn’t
    work with all objects.
- The ECMAScript specification has deprecated it and calls it“optional” and
    “legacy”.

```
In contrast,__proto__in object literals always works and is not deprecated.
```
```
Read on if you are interested in how the accessor__proto__works.
```
```
__proto__isanaccessorofObject.prototypethatisinheritedbyallinstancesofObject.
Implementing it via a class would look like this:
```
```
classObject {
get__proto__() {
returnObject .getPrototypeOf( this );
}
set__proto__(other) {
Object .setPrototypeOf( this ,other);
}
// ···
}
```
Since__proto__isinheritedfromObject.prototype,wecanremovethisfeaturebycre-
ating an object that doesn’t haveObject.prototypein its prototype chain (see§29.7.3
“Not all objects are instances ofObject”):

```
> '__proto__' in {}
true
> '__proto__' in Object.create(null)
false
```
## 29.8.8 Object.prototype.hasOwnProperty()

```
Better alternative to.hasOwnProperty():Object.hasOwn()[ES2022]
See§28.9.4“Object.hasOwn(): Isagivenpropertyown(non-inherited)? [ES2022]”.
```

## 29.9 FAQ: classes.

```
obj.hasOwnProperty(propKey)returnstrueifobjhasanown(non-inherited)property
whose key ispropKeyandfalseotherwise.
```
```
const obj={ownProp: true };
assert.equal(
obj.hasOwnProperty('ownProp'), true // own
);
assert.equal(
'toString' in obj, true // inherited
);
assert.equal(
obj.hasOwnProperty('toString'), false
);
```
```
This is how to use this method safely (for details see§29.8.1 “UsingObject.prototype
methods safely”):
```
```
const obj={
// Overrides Object.prototype.hasOwnProperty
hasOwnProperty: true ,
};
// Doesn’t work in this case:
assert.throws(
() => obj.hasOwnProperty('anyPropKey'),
{
name:'TypeError',
message:'obj.hasOwnProperty is not a function',
}
);
// Safe way of using .hasOwnProperty():
assert.equal(
Object .prototype.hasOwnProperty.call(obj,'anyPropKey'), false
);
```
**29.9 FAQ: classes**

## 29.9.1 Why are they called “instance private fields” in this book and

## not “private instance fields”?

That is done to highlight how different properties (public slots) and private slots are:
By changing the order of the adjectives, the words “public” and “field” and the words
“private” and “field” are always mentioned together.

## 29.9.2 Why the identifier prefix#? Why not declare private fields via

## private?

```
Could private fields be declared viaprivateand use normal identifiers? Let’s examine
what would happen if that were possible:
```

```
372 29 Classes [ES6]
```
```
class MyClass {
private value;// (A)
compare(other) {
returnthis .value===other.value;
}
}
```
Wheneveranexpressionsuchasother.valueappearsinthebodyofMyClass,JavaScript
has to decide:

- Is.valuea property?
- Is.valuea private field?

At compile time, JavaScript doesn’t know if the declaration in line A applies toother
(due to it being an instance ofMyClass) or not. That leaves two options for making the
decision:

```
1..valueis always interpreted as a private field.
2.JavaScript decides at runtime:
```
- Ifotheris an instance ofMyClass, then.valueis interpreted as a private
    field.
- Otherwise.valueis interpreted as a property.
Both options have downsides:
- With option (1), we can’t use.valueas a property, anymore – for any object.
- With option (2), performance is affected negatively.

That’swhythenameprefix#wasintroduced. Thedecisionisnoweasy: Ifweuse#,we
want to access a private field. If we don’t, we want to access a property.

privateworksforstaticallytypedlanguages(suchasTypeScript)becausetheyknowat
compile time ifotheris an instance ofMyClassand can then treat.valueas private or
public.

```
Quiz
Seequiz app.
```

**Chapter 30**

**Where are the remaining**

**chapters?**

Youarereadingapreviewversionofthisbook. Youcaneitherreadallessentialchapters
onlineor you canbuy the full version.

You can take a look atthe full table of contents, which is also linked to from the book’s
homepage.

```
373
```

