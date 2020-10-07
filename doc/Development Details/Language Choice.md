# ZelSystem
## Document 3a: Language Choice

### ZelSystem Development Language
The language selected for the development of ZelSystem is Python. However, the
contenders are important to examine for a possible change of language while it
is still early in development.

#### C
C has the advantage of developer experience, and a relatively uncomplicated
structure. However, a critical piece of the ZelShell structure is the modifying
of the environment, which is represented as an array of function pointers. As
well, the lead developer dislikes the look-and-feel of C code.

#### Haskell
Haskell is a favorite language of the (geek) lead developer. However, Haskell
would be difficult for the other developer to use, as she is more experienced
with procedural language. Haskell's functional syntax might be a bit cumbersome
for a project of this scale.

#### Python
Python is loved by both developers, and practiced widely likewise. Python has a
very mature community, and there is a massive library of references on the
canonical forms for certain structures. Python is also agreed upon as the
natural choice for this type of project, especially with the ability to
reference functions as dictionary values.

#### Rust
Rust boasts effortless memory control, security, and a young active community of
support. However, it is like C in the lead developer's dislike of its syntax.
Her distaste could be overlooked provided that Rust was the top option of the
languages.

### Choice and Methods of Change
Upon review of this list, the obvious winner is Python. Although it may not be
optimal for a system developed closer to the metal, it is highly preferable to
even Rust for a system developed 'on top of' an existing shell. Python also has
plug-ins and libraries specifically designed for terminal applications. The only
way for the language to change is within the first week of code writing, if it
is discovered that switching to the new target language could cut the remaining
code writing by 50% or more. While the odds of such a switch are small, it is
worth having a numerical criterion for.