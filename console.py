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
         args, n = parse(args)

        if not n:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif n == 1:
            temp = eval(args[0])()
            print(temp.id)
            temp.save()
        else:
            print("** Too many arguments for create **")

    def do_show(self, line):
        """
        Prints the string representation of an instance.
        """
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                inst = storage.find_by_id(*args)
                print(inst)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many arguments for show **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                storage.delete_by_id(*args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many arguments for destroy **")

    def do_all(self, line):
        """
        Prints all string representation of all instances.
        """
        args, n = parse(args)

        if n < 2:
            try:
                print(storage.find_all(*args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many arguments for all **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id.
        """
         args, n = parse(arg)
        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            print("** value missing **")
        else:
            try:
                storage.update_one(*args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
