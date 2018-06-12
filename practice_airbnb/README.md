# AirBnb Clone Command Interpreter
The goal for this project was to build a command line interpreter that can :
- Put in place a parent class to take care of the initialization, serialization and deserialization of future instances
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON strin <-> file
- Create all classes used for AirBnb (User, State, City, Place..) 
- Create the first abstracted storage engine of the project: File Storage
- Create all unittests to validate all our classes and storage engine

## Command Interpreter
The command interpreter should be capable of:
- Creating a new object
- Retrieving an object from a file, a database, etc...
- Doing operations on objects
- Updating attributes of an object
- Destroying an object

## Project Goals
- Create a Python package
- Create a command interpreter in Python using the cmd module
- Implement unit testing at a large scale
- Serialize and deserialize a Class
- Write and read a JSON file
- Manage datetime
- Define a UUID
- Know how to use \*args and \*\*kwargs
- Know how to handle named arguments in a function

## Directory Descriptions
| Directory | Description |
| ------------- |:-------------:|
| models | contains all models |
| engine | contains file_storage module to interact with data |
| tests | contains all unit tests |

## File Descriptions
| File | Description |
| ------------- |:-------------:|
| console.py | entry point of the command interpreter |
| base_model.py | contains class BaseModel that defines all common attributes/methods for other classes |
| file_storage.py | contains class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances|
| init.py | within models, links BaseModel to FileStorage through the variable storage |

### Command Line Commands
| Command | Description |
| ------------- |:-------------:|
| help | lists all documented commands |
| exit | exits the console |
| EOF | exits the console |
| all | Prints all string representations of all instances based or not on the class name |
| create | Creates a new instance of BaseModel and saves it to the JSON file |
| destroy | Deletes an instance based on the class name and id |
| show | Prints the string represenation of an instance based on the class name and id |
| update | Updates an instance based on the class name and id by adding or updating attribute |

### Examples
``` ./hsh  
(hbnb) create BaseModel

(hbnb) show BaseModel 111111

(hbnb) destroy BaseModel 111111

(hbnb) update BaseModel 11111 
```

#### Authors
Mikaela Gurney, Lisa Olson
