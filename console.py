#!/usr/bin/python3


"""
This module implements a command interpreter for the project.
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = [
        "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"
    ]

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program in non-interactive mode."""
        return True

    def do_create(self, args):
        """Create a new instance, save it (to the JSON file) and print its id."""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(args_list[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args_list[0], args_list[1])
        if obj_key in storage.all():
            print(storage.all()[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args_list[0], args_list[1])
        if obj_key in storage.all():
            del storage.all()[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representations of instances."""
        args_list = args.split()
        if args_list and args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        obj_list = [str(obj) for obj in storage.all().values()]
        print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args_list[0], args_list[1])
        if obj_key not in storage.all():
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        if len(args_list) < 4:
            print("** value missing **")
            return

        instance = storage.all()[obj_key]
        attr_name = args_list[2]
        attr_value = args_list[3]

        if hasattr(instance, attr_name):
            try:
                attr_value = eval(attr_value)
            except (NameError, SyntaxError):
                pass
            setattr(instance, attr_name, attr_value)
            instance.updated_at = datetime.utcnow()
            storage.save()
        else:
            print("** attribute doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
