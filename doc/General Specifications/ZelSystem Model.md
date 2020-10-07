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


1.      Function Namespace  --   Variable Namespace
                   \                  /
2.                   Input Processing
		       	   |
3.                   Output Collection

