#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    """
    BaseModel class for other classes to inherit common attributes and methods.

    Attributes:
        id (str): Unique identifier generated using uuid.uuid4().
        created_at (datetime): Date and time when the instance is created.
        updated_at (datetime): Date and time when the instance is last updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            kwargs: Dictionary containing attributes to initialize the instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                        self.__dict__[value] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                     self.__dict__[key] = value
        
        else:
             models.storage.new(self)
            
    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict