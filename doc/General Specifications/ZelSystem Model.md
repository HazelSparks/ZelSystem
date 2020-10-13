# ZelSystem
## Document 1b: ZelSystem Model

### Purpose
The purpose of this document is to elucidate the general model of ZelSystem.
This document is written from the perspective of implementation, and a user
guide should be found elsewhere. The sub-systems of ZelSystem are arranged with
the following dependency structure


1.  	        ZLang      --          API
                  |                     |
2.		REPL	   --	   Interpreter

That is to say, ZLang and its API must function together before either the REPL
or Interpreter can function. In addition, the REPL and Interpreter will be
interdependent, given how similar their functionality is. Now, we will break
down the structure of each component in more detail

### ZLang Model
The ZLang model is roughly arranged with the following structure


1.                   Input Processing
                       /         \     
2.                Namespace --- Compute
		       \         /
3.                   Output Collection

Python will manage the Input Processing and Output Collection sections, and the
minimal set of primitives for ZLang will be implemented likewise. After that,
language features will be implemented in ZLang. This follows the implementation
pattern of C, Scheme, and many other developed languages. Compute will be
managed by both Python and ZLang. The main process of Compute will be to consult
the namespace, and hand Python the name of the function to be executed. Python
will perform the function, or hand execution back to ZLang for certain
operations. Certain ZLang functions modify the namespace, and as such Compute
results can change as execution continues. Safety features will be discussed
later on and in the Language Specification document.

### TODO: API Model

### TODO: REPL Model

### TODO: Interpreter Model

### TODO: Big Picture