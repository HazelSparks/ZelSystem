# ZelSystem 
## Document 2a: Language Specifications

The language of the ZelSystem, ZLang, will be used inside the REPL, Interpreter,
API, and environment subsystems. As such, it must be precisely and carefully
defined before work can begin on the other subsystems. Considerations need to be
made with regard to syntax and format, variable structure and runtime style. This
document will serve as an implementation guide for ZLang, and model precisely how
the language will operate with the other components of ZelSystem.

### Feature List
Below is a list of features that must be included for a minimum viable product of
ZLang:
- Scheme-like syntax
- Global environment variables
- On-the-fly execution adjustment
- Malleable execution model
- Modular environment

#### Scheme-like Syntax
ZLang will have a look-and-feel similar to MIT Scheme, with parenthesis being
used for evaluation, and a quote operator to return the quoted object with no
evaluation. Keywords like **defun**, **lambda**, and the convention of
conditionals being denoted with **condition?** will make a return. This choice is
almost purely inspired by the head developer's love of 'The Little Schemer'.

#### Global Environment Variables
It is to be required that the environment variables which are common among the
ZLang runtime be made global and have an accessible method of modification to
each user-case, REPL, interpreter, or plug-in.

#### Execution Adjustment
Tying into the above requirement, the full execution model of ZLang must be made
global and public to allow for programs which change the mode of execution. This
is also inspired by 'The Little Schemer', as an expansion of the impressive
level of modification allowed by Scheme. This will put even the language itself
into the hands of user customization.

#### Malleable Execution Model
As for the method to provide the above specifications, it is required that the
execution model of ZLang be global and able to be modified in real time by the
program under execution. In addition, a level of safety must be established so
a program isn't able to cause a hang or halt. Furthermore, a level of modularity
should be provided so saved execution models can be loaded with a single function
call.

#### Modular Environment
As specified in the execution model table, the ambient environment of ZLang must
be able to be modified with single function calls, exported, imported, and
otherwise changed. This includes variable namespaces, function tables, and syntax
trees during interpretation.

### Language Design
#### Structures
There are two types of variables in ZLang, atoms and lists. A list contains
variables, and can include other lists. The way this will be represented in
Python is with a dictionary **var_table**, whose entries will all have the
structure "(var_name, var_type) : var_value". The function to define new
variables is **define**, and it is used with the syntax
**(define var_name var_value)** which will have its type inferred by the
structure of the value. ZLang will have built-in two special constants, **T** and
**F**, which are atoms representing boolean values. Furthermore, additional lists
can be constructed using the **cons** function, to which reference will be made
to MIT Scheme.

#### Exhaustive List of Functions and Primitives (subject to change)
- (), the empty list								IMPLEMENTED
- **T**, the boolean truth value						IMPLEMENTED
- **F**, the boolean false value						IMPLEMENTED
- atomq, returns true if the value is an atom					IMPLEMENTED
- car, returns the first element of a non-empty list				IMPLEMENTED
- cdr, returns the remaining elements of a decapitated non-empty list		IMPLEMENTED
- cons, places a value at the front of a list	       		 		IMPLEMENTED
- nullq, returns true if the value is the empty list				IMPLEMENTED
- ver, short for verbatim, returns whatever it is passed without evaluation	IMPLEMENTED
- lambda, substitutes arbitrary values into specific places	 		
- list, creates a list containing the arguments it's passed			IMPLEMENTED
- cond, branches execution based on a boolean value  				
- define, defines a variable with a list or an atom				
- eqq, returns true if the two values are equal					IMPLEMENTED
- warning, returned in the case of a non-critical error				IMPLEMENTED
- error, returned in the case of a critical error 				IMPLEMENTED
- zleval, evaluates the specified function on the following arguments		
- envi, the environment, which is a list of pairs, name and definition		

#### Function Execution Syntax
The evaluation syntax for ZLang is as follows

(func val1 val2 val3 ... valn)

for a function of n variables. Do note that functions can be passed as values.

#### Example Program
(define lat?
       (lambda (l)
       	       (cond
		((null? l) **T**)
		((atom? (car l)) (lat? (cdr l)))
		(else **F**))))

(define contains?
       (lambda (lat a)
       	       (cond
		((null? lat) **F**)
		((eq? (car lat) a) **T**)
		(else (contains? (cdr lat) a)))))

(define testlist '(a b c d e f))

(lat? testlist)
(contains? testlist a)
(contains? testlist z)

This program should output
**T**
**T**
**F**

by consultation with the primitives used.

#### Theory and Syntax
The most important thing to take away from the construction of ZLang is that
functions are lists. The second is that lambda is nothing more than a search and
replace for variables. The third is that ZLang's execution model simply repeats
evaluation until the **car** of the list is **ver** or is not in the namespace.
This is one of the things that has enamoured Scheme and Lisp programmers since
the inception of the language. Likewise, our head developer has Lisp fever, so
she opted for a simple primitive environment that would be easy to code, "that
the Lisp-gifted among us might flourish with this drop in the ever-expanding 
basin." She has lost her mind entirely. Given this stance, we are only going to
implement the above primitives in Python, and implement the remainder of the
language in this primitive ZLang.

##### Implementation Model
To implement ZLang in a language like Python, it is useful to first implement a
smaller version of the language, then write the language's standard library in
that reduced environment. In our case, we will label the reduced language
micro-ZLang, or mZL for short. mZL consists of the above set of primitives and is
implemented directly in Python. The most critical piece of mZL is the eval
operator. It's the lynchpin that allows us to continue with exection in each
iteration. The flow of control is as follows:

- The input string is converted into a list of ZLang statements
- The runtime reads in the first ZLang statement of the input
- eval is applied recursively until the statement has a car of ver, define, or
  a value which isn't in the namespace
- The remainder of the statement is returned to the output
- The next ZLang statement is read in 

More information can be found in the Implementation Guide.