#!/usr/bin/python3

"""
Module for the command interpreter.
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    
    prompt = "(hbnb) "
    
    def emptyline(self):
        """Does nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program gracefully with EOF"""
        print()
        return True
    
    def do_create(self, arg):
        """Create a new instance of the specified class, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg
            new_obj = eval(class_name)()
            new_obj.save()
            print(new_obj.id)
        except NameError:
            print("** class doesn't exist **")
    
    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj_key = class_name + "." + obj_id
        if obj_key in storage.all():
            print(storage.all()[obj_key])
        else:
            print("** no instance found **")
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj_key = class_name + "." + obj_id
        if obj_key in storage.all():
            del storage.all()[obj_key]
            storage.save()
        else:
            print("** no instance found **")
    
    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        objs = storage.all()
        if not args or args[0] == "BaseModel":
            print([str(obj) for obj in objs.values() if isinstance(obj, BaseModel)])
        elif args[0] == "User":
            print([str(obj) for obj in objs.values() if isinstance(obj, User)])
        else:
            print("** class doesn't exist **")
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj_key = class_name + "." + obj_id
        objs = storage.all()
        if obj_key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        setattr(objs[obj_key], attr_name, attr_value)
        objs[obj_key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
