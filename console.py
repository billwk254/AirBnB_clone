#!/usr/bin/python3
"""
Module for the command interpreter.
"""


from models import storage
from models.base_model import BaseModel
from cmd import Cmd

model_classes = storage.models


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
        """Creates a new instance of a model"""
        parsed_args, arg_count = parse(args)

        if not arg_count:
            print("** class name missing **")
        elif parsed_args[0] not in custom_classes:
            print("** class doesn't exist **")
        elif arg_count == 1:
            new_instance = eval(parsed_args[0])()
            print(new_instance.id)
            new_instance.save()
        else:
            print("** Too many arguments for create **")

    def do_show(self, line):
        """Shows an instance based on its class name and id"""
        parsed_args, arg_count = parse(arg)

        if not arg_count:
            print("** class name missing **")
        elif arg_count == 1:
            print("** instance id missing **")
        elif arg_count == 2:
            try:
                instance = storage.find_by_id(*parsed_args)
                print(instance)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many arguments for show **")

    def do_destroy(self, line):
        """Destroys an instance based on its class name and id"""
        parsed_args, arg_count = parse(arg)

        if not arg_count:
            print("** class name missing **")
        elif arg_count == 1:
            print("** instance id missing **")
        elif arg_count == 2:
            try:
                storage.delete_by_id(*parsed_args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many arguments for destroy **")

    def do_all(self, line):
        """Prints all instances of a specific class"""
        parsed_args, arg_count = parse(args)

        if arg_count < 2:
            try:
                print(storage.find_all(*parsed_args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many arguments for all **")

    def do_update(self, line):
        """Updates an instance based on its class name, id, attribute name, and value"""
        parsed_args, arg_count = parse(arg)
        if not arg_count:
            print("** class name missing **")
        elif arg_count == 1:
            print("** instance id missing **")
        elif arg_count == 2:
            print("** attribute name missing **")
        elif arg_count == 3:
            print("** value missing **")
        else:
            try:
                storage.update_one(*parsed_args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
