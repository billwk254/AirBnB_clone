#!/usr/bin/python3


import cmd
from models import storage
from models.base_model import BaseModel


"""
Module for the command interpreter.
"""


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class.
    """

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing if line is empty"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, save it, and print the id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        new_instance = storage.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all instances or instances of a specific class"""
        args = line.split()
        all_objs = storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in all_objs.values() if type(obj).__name__ == class_name])
    
    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        obj = storage.all()[key]
        if hasattr(obj, attribute_name):
            attr_type = type(getattr(obj, attribute_name))
            setattr(obj, attribute_name, attr_type(attribute_value))
            obj.save()
        else:
            print("** attribute doesn't exist **")
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()