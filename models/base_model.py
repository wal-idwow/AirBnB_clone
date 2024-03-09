#!/usr/bin/python3
"""define BaseModel class"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """class BaseModel wich all other classes will inherite"""

    def __init__(self, *args, **kwargs):
        """initialize instance attributes
        
        Args:
            *args : list of argument
            **kwargs (dict): Key/Value of the attributes
        """
        default_value = True
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    if not isinstance(value, datetime):
                        try:
                            self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                            default_value = False
                        except ValueError:
                            pass
                    else:
                        self.__dict__[key] = value
                        default_value = False
                else:
                    self.__dict__[key] = value
                    default_value = False

        if default_value:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return official string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return the dictionary of BaseModel instance
        """

        dict_object = self.__dict__.copy()
        dict_object['created_at'] = self.created_at.isoformat()
        dict_object['updated_at'] = self.updated_at.isoformat()
        dict_object['__class__'] = self.__class__.__name__

        return dict_object
