#!/usr/bin/python3
"""
Module for the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class.
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program with EOF (Ctrl-D).
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass

    def do_create(self, line):
        """
        Create a new instance of BaseModel, saves it, and prints the id.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances.
        """
        args = line.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if args[0] == key.split('.')[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    obj = storage.all()[key]
                    setattr(obj, args[2], args[3])
                    obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
