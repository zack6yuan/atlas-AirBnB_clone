#!/usr/bin/python3
"""
Base model that provides common attributes and methods
for other models to inherit.
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """
    Defines the BaseModel class with attributes and methods
    that provide structure for other classes.
    """

    def __init__(self, *args, **kwargs):
        """ Initializes a new instance of BaseModel.
d, initializes a new instance with
        unique ID and current timestamp. If kwargs are provided,
        initializes from the kwargs."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' timestamp and saves the instance
        to storage via models.storage.save().
        """
        self.updated_at = datetime.now()
        models.storage.save()
        return self.id

    def to_dict(self):
        """ Converts the instance to a dictionary,
        including the class name and timestamp fields."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        formatTime = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict["created_at"] = self.created_at.strftime(formatTime)
        new_dict["updated_at"] = self.updated_at.strftime(formatTime)
        return new_dict
