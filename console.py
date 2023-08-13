#!/usr/bin/python3
"""
Module for the command interpreter.
"""


import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
