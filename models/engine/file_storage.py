#!/usr/bin/python3
"""
Defines the FileStorage class.
"""


import json
import models


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
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
