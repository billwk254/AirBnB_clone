#!/usr/bin/python3

"""
This module defines the BaseModel class.
"""


import uuid
import datetime
import models


class BaseModel:
    """
    Defines the BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel attributes.
        """
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing BaseModel attributes.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return new_dict

    def __str__(self):
        """
        Return the string representation of BaseModel.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """
        Return the string representation of BaseModel.
        """
        return self.__str__()
