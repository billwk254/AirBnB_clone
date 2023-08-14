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
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for class_key, class_data in data.items():
                    class_name = class_key.split('.')[0]
                    class_dict = {"BaseModel": BaseModel, "User": User,
                                  "State": State, "City": City,
                                  "Amenity": Amenity, "Place": Place,
                                  "Review": Review}
                    if class_name in class_dict:
                        new_instance = class_dict[class_name](**class_data)
                        self.__objects[class_key] = new_instance
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

