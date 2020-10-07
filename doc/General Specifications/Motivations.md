# ZelSystem
## Document 1a: Motivations

### Main Desire
ZelSystem exists to serve as an extensible, tailored shell system with a usable
scripting language for environment customization, and an API for the development
of larger plugins.

### Feature Requirements
- Custom scripting language
- REPL capability 
- Interpreter capability
- API structure for plugin intergration
- User-customizable environment
- Graceful error-handling
- Environment transparency

### Estimations
This is a hobby project being developed by a single lead programmer, although she
will likely receive assistance at some point by a fellow amateur developer. The
assistance of this programmer will not be factored into estimations until it
occurs. That makes this a 1-person project, and the lead developer can put about
1 hour a day focused on this project. The lead needs 2 days a week off to focus
on other projects, so that leaves 5 person-hours a week of development time.

#### Scripting Language
To plan out a simple language for scripting in a shell should take no less than
5 hours and no more than 20 hours. This does not include the actual coding time,
strictly the time to plan out each detail before implementation. This time should
include documenting environment specifications, syntax details, and execution
models.

#### REPL capability
Designing a REPL for a well-defined scripting language takes no less than 1 hour
and no more than 6 hours. Of the considerations to be looked at is the REPL
environment, the execution model, and the evaluation style. Furthermore, the
design of the 'look-and-feel' of the shell is to be planned and implemented here.

#### Interpreter capability
Designing an interpreter system for a langauge and REPL takes no less than 3
hours and no more than 10 hours. Among the concerns of this subsystem are file
handling, program translation, and linting and error handling. Intermediary
language selection is the critical choice, and should be considered carefully.

#### API structure
Given the lead programmers inexperience with API systems, implementing one for a
new language will take no less than 15 hours and no more 30 hours. The vast
majority of this time will be spent consulting other developers and researching
existing API systems for both inspiration and guidance.

#### Tweakable environment
To allow for a predetermined environment to be meaningfully changed by user
interaction will take no less 5 hours and no more than 15 hours. The key choices
to be made in this phase of development are the degree of flexibility, and the
method of customization, if it will be live, the structure of the environment
itself needs to be determined for an accurate estimate.

#### Graceful Error-handling
To introduce and extend error handling in a way that interrupts the user as
little as possible will take no less than 3 hours and no more than 7 hours. Key
choices to be made in this phase are when it is appropriate to interrupt the user
and when an error is critical enough to require terminating execution.

#### Environmental transparency
To develop an environment that is presented in a concise and understandable way
will take no less than 10 hours and no more than 20 hours. The method of
presenting environmental information is critcal here, as well as the level of
simplicity the method of modifying this environmental data has.

#### Total Estimates
We have a best and worst case total time estimate of 42 to 108 hours, or 9 to 22
weeks for project development time. This estimation will be given weekly updates,
beginning next Monday. 
