#!/usr/bin/env python3
"""entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the cmd for 'quit' as an arg to cmd
        """
        return True

    def do_EOF(self, line):
        """Exits the program cleanly
        """
        return True

    def emptyline(self):
        """Ignores empty commands
        """
        pass

    def do_show(self, argv):
        """Prints the string representation of an instance
        """
        args = argv.split()

        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            if class_name not in globals() or not issubclass(
                    globals()[class_name], BaseModel):
                print("** class doesn't exist **")
            else:
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"
                obj_dict = storage.all()
                if key in obj_dict:
                    print(obj_dict[key])
                else:
                    print("** no instance found **")

    def do_create(self, argv):
        """Creates a new instance of BaseModel, saves it, and prints the id.
        """
        args = argv.split()

        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]

            print(class_name)
            try:
                instance_new = eval(f'{class_name}()')
                instance_new.save()
                print(instance_new.id)
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the
class name."""
        obj_dict = storage.all()

        if not arg:
            print([str(obj) for obj in obj_dict.values()])
        else:
            class_name = arg
            if class_name not in globals() or not issubclass(
                    globals()[class_name], BaseModel):
                print("** class doesn't exist **")
            else:
                filtered_obj = [str(obj) for key, obj in obj_dict.items()
                                if key.startswith(class_name + ".")]
                print(filtered_obj)

    def do_update(self, argv):
        """Updates an instance based on the class name and id by adding
or updating attribute."""

        args = argv.split()
        obj_dict = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in globals() or not issubclass(globals()[args[0]],
                                                        BaseModel):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            inst_id = args[1]
            inst_key = f"{class_name}.{inst_id}"

            if inst_key not in obj_dict:
                print("** no instance found **")
                return
            obj_inst = obj_dict[inst_key]
            attribute_name = args[2]
            attribute_value = ' '.join(args[3:])
            if attribute_value.startswith('"') and attribute_value.endswith(
                    '"'):
                attribute_value = attribute_value[1:-1]

            setattr(obj_inst, attribute_name, attribute_value)
            obj_inst.save()

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id (save the
changes into the JSON file).
        """

        args = argv.split()

        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            if class_name not in globals() or not issubclass(
                    globals()[class_name], BaseModel):
                print("** class doesn't exist **")
            else:
                inst_id = args[1]
                key = "{}.{}".format(class_name, inst_id)
                obj_dict = storage.all()

                if key in obj_dict:
                    del obj_dict[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def help_show(self):
        """Documentation for the help show method"""
        print("Prints the string representation of an instance based on "
              "the class name and id.\nUsage: show <Class name> <instance id>"
              "\nRequirements:""\n\tAtleast 2 arguements:"
              "\n\t\tClass must already exit."
              "\n\t\tAn existing instance id.")
    def help_update(self):
        """Documentation for the help update method"""
        print("Updates an instance based on the class name and id by adding\n"
              "or updating attribute, then saves the change into the\n"
              "JSON file\nUsage: update <class name> <instance id> <key>"
              " <value>.\nRequirements:\n\tAtleast 4 arguments:"
              "\n\t* Class name must exist\n\t* Instance id must be existing"
              "\n\t* Key attribute name to be updated. (It is added on the"
              "\n\t  condition it did not exist prior)"
              "\n\t* An attribute value.")

    def help_create(self):
        """Documentation for the help create method"""
        print("Creates a new instance of BaseModel, saves"
              "it\nto the JSON file and prints the id."
              "\nUsage: create <class name>/BaseModel"
              "\nRequirements: \n\t* An existing class name.")

    def help_destroy(self):
        """Documentation for the help create method"""
        print("Deletes an instance based on the class name"
              "\nand id (saves the change into the JSON file)"
              "\nUsage: destroy <class name> <instance id>"
              "\nRequirements:"
              "\n\t* An existing class name."
              "\n\t* An existing instance id.")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
