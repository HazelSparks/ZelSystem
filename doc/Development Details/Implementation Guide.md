# ZelSystem
## Document 3b: Implementation Guide

### ZLang Module Structure
The Python package for ZLang will be structured as follows:

- main.py
- zl_environment.py
- zl_runtime.py
- zl_primitives.py
- zl_standard_library.zl

Where the responsibilities of the files are as follows:

#### main.py
To initialize each of zl_modules, and process command-line inputs.

#### zl_environment.py
Handle the basic execution process, error handling, input processing, and output
collection.

#### zl_runtime.py
Pulls together the ZLang resources and actually schedules the computations and
makes the references to libraries.

#### zl_primitives.py
Defines the minimal set of functions needed to write a standard library for
ZLang. This is the implementation of mZL.

#### zl_standard_library.zl
This is the true language ZLang, and it's written in ZLang. This implementation
pattern allows for a cleaner syntax that's more focused on the language itself
rather than the quirks of translation.

What is most critical to the mZL execution is a "string-to-list" function, which
turns a string of parenthesis into a list of mZL statements. The full details
of this function are to be placed

## TODO
# HERE 
## TODO

### Complete list of mZL primitives, and their suggested implementation
#### (), the empty list
The empty list is to be implemented as a single table in the namespace,
"()" : "()"

#### **T**, Boolean truth
The truth boolean is to be implemented in the namespace as "T" : True

#### **F**, Boolean false
The false boolean follows the above pattern

