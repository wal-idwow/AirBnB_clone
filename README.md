# AirBnB clone - The console


## Description

This package is meant to emulate the back-end of the AirBnB workflow.
From user creation to database storage to modifying the user's details.
We put in place a parent class (called BaseModel) to take care of the initialization, seria\
lization and deserialization Instance <-> Dictionary <-> JSON string <-> file.
We included abstracted storage engine of the project: File storage.


## The console

A simple shell using python's cmd module to emulate a shellThis shell like module can be used to easily access the main functionality of the project.


## Usage

The console is run by executing the console.py file

```
./console.py
```

The user will be greeted by a csutom prompt. Thereafter, be allowed to run any command from the list of commands.

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
**Syntanx: \<help\> \<command\>**
e.g
```
help count
```

### quit
The quit command is used to exit the command line interface (stopping the console.py progra\
m).
**Syntax: \<quit\>**
```
quit
```

### EOF
The EOF command also exits the command line interface. It does this by mimmicking the cntrl\
-D command. Since these are essantial the same, cntrl-D can be used instead.
**Syntax: \<EOF\>**
```
EOF
```

### count

The count command counts instances of a class saved in the file.json.
The number of instances is printed as output.

**Syntanx: \<count\> \<class name\>**
**2. Syntanx: \<class name\>.\<count\>()**
```
count BaseModel
```
```
Amenity.count()
```

### create

The create command creates an instance and saves it to the file.json file.
It takes in a class name as an argument to make a new instance of that class and prints out the instance's automat\
ically created id
after successful creation.
**Syntax: \<create\> \<class name\>**
**2. Syntax: \<class name\>.\<create\>()**
```
create City
```
```
BaseModel.create()
```

### destroy

Remove an an instance from the saved instances in file.json. The instance is deleted, once created again, its prop\
erties will differ, making it a new instance.
**Syntanx: \<destroy\> \<class name\> \<instance id\>**
⋅⋅2. **Syntax: \<class name\>.\<destroy\>(instance id)**
```destroy Amenity 345vsd-vsd-vsd```
```Amenity.destroy(345vsd-vsd-vsd)```

### all
View all instances and intances of a particular class.
This command can be used by itself and with an optional argument of a particular class.

**Syntanx: all [\<class name\>]** with [] representing an optional argument.

**Syntanx: \<class name\>.all()**
```
all User
```
```
User.all()
```
```
all
```

### show

View an instance of a class based on the class name as well as the instance ID.
**Syntanx: \<show\> \<class name\> \<instance id\>**
**Syntax: \<class name\>.\<show\>(instance id)**
```
show User 123fda-3czdsf4-sfd34
```
```
User.show(123fda-3czdsf4-sfd34)
```

### update

Update an instance of a class based on the instance class name and instance id by adding or updating attribute.
Two more arguemnts are required for this command:
* \<attribute name\>
* \<attribute value\>

**Syntax: <update> <class name> <instance id> <attribute name> <attribute value>**
```
update Basemodel fvs3-c3ccz54-acd34 first_name "Megan"
```
**Syntax: User.update(\<insatnce id\>, \<attribute name\>, \<attribute value\>)**
```
User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
```