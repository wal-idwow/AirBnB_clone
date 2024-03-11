# AirBnB clone - The console

# AirBnB clone - The console

## Description

This package is meant to emulate the back-end of the AirBnB workflow.
From user creation to database storage to modifying the user's details.
We put in place a parent class (called BaseModel) to take care of the initialization, seria\
lization and deserialization Instance <-> Dictionary <-> JSON string <-> file.
We included abstracted storage engine of the project: File storage.


## The console

A simple shell using python's cmd module to emulate a shellThis shell like module can be us\
ed to easily access the main functionality of the project.


## Usage

The console is run by executing the console.py file

`./console.py`

The user will be greeted by a csutom prompt.

Thereafter, be allowed to run any command from the list of commands.

## Commands
* quit
* EOF
* help
* count
* create
* destroy
* show
* update
* all

### Help

The help command by itself lists all documented commands. These are commands that can be us\
ed with
the help command to print out the documentation for the rest of the commands
ultimately getting a better understanding.
**Syntanx: <help> <command>**
e.g `help count`

### quit
The quit command is used to exit the command line interface (stopping the console.py progra\
m)
**Syntax: <quit>**
`quit`

### EOF
The EOF command also exits the command line interface. It does this by mimmicking the cntrl\
-D command. Since these are essantial the same, cntrl-D can be used instead.
**Syntax: <EOF>**
`EOF`

### count

The count command counts instances of a class saved in the file.json.
The number of instances is printed as output.
**Syntanx: <count> <class name>**
⋅⋅2. **Syntanx: <class name>.<count>()**
`count BaseModel`
`Amenity.count()`
