#!/usr/bin/python3
"""
This module defines the FileStorage class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass

    def _serialize(self, obj):
        """
        Serialize an object to a dictionary
        """
        obj_dict = obj.to_dict()
        # Add class name to the dictionary
        obj_dict['__class__'] = type(obj).__name__
        return obj_dict

    def _deserialize(self, obj_dict):
        """
        Deserialize a dictionary to an object
        """
        if '__class__' in obj_dict:
            class_name = obj_dict.pop('__class__')
            if class_name == 'BaseModel':
                return BaseModel(**obj_dict)
            elif class_name == 'User':
                return User(**obj_dict)
            else:
                raise ValueError("Unknown class: {}".format(class_name))
        else:
            raise ValueError("Invalid dictionary format")

