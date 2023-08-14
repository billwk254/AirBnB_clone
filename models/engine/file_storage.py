#!/usr/bin/python3
"""
This module defines the FileStorage class
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        if cls is None:
            return self.__objects
        else:
            cls_name = cls.__name__
            cls_objects = {}
            for obj_id, obj in self.__objects.items():
                if obj.__class__.__name__ == cls_name:
                    cls_objects[obj_id] = obj
            return cls_objects

    def new(self, obj):
        """Adds a new object to the dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    class_ = eval(class_name)
                    self.__objects[key] = class_(**value)
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

