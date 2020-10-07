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
