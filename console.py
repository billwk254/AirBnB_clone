#!/usr/bin/python3

"""
Module for the command interpreter.
"""


import cmd
import re
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
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False
    
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
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in globals():
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
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in globals():
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
        if not args:
            objs = storage.all()
            print([str(obj) for obj in objs.values()])
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            objs = storage.all()
            print([str(obj) for obj in objs.values() if type(obj).__name__ == class_name])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attributes"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in globals():
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

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arg_list = arg.split()
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """Count the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        count = len([obj for obj in storage.all().values() if type(obj).__name__ == class_name])
        print(count)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj_key = class_name + "." + obj_id
        objs = storage.all()
        if obj_key in objs:
            print(objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj_key = class_name + "." + obj_id
        objs = storage.all()
        if obj_key in objs:
            del objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
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

    def do_update_dict(self, arg):
        """Updates an instance based on the class name and id using a dictionary"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
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
            print("** dictionary missing **")
            return
        update_dict = eval(args[2])
        for key, value in update_dict.items():
            setattr(objs[obj_key], key, value)
        objs[obj_key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
