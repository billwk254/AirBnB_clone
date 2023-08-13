#!/usr/bin/python3
import uuid
from datetime import datetime
import models


"""Defines the BaseModel class."""


class BaseModel:
    """
    Defines the BaseModel class.
    Attributes:
        id (str): The ID of the instance.
        created_at (datetime): The creation date and time.
        updated_at (datetime): The last update date and time.
    """    
    def __init__(self):
        """Initialize BaseModel attributes."""
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
            self.created_at = datetime.now()
            self.updated_at = self.
            models.storage.new(self)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing BaseModel attributes."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    
    def __str__(self):
        """Return the string representation of BaseModel."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def __repr__(self):
        """
        Return the string representation of BaseModel.
        """
        return self.__str__()
