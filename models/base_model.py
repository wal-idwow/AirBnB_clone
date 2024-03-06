#!/usr/bin/python3
"""define BaseModel class"""
#import models
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class representation"""

    def __init__(self, *args, **kwargs):
        """initialize BaseModel
        
        Args:
            *args : Unused
            **kwargs (dict): Key/Value of the attributes
        """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        # unique id and conversion to str
        self.id = str(uuid.uuid4())
        # set created_at and updated_at to the current datetime
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len (kwargs) != 0:
            for ky, val in kwargs.items():
                if ky == "created_at" or ky == "updated_at":
                    self.__dict__[ky] = datetime.strptime(val, time_form)
                else:
                    self.__dict__[ky] = val
        #else:
            #models.storage.new(self)

    def __str__(self):
        """return the print string representation"""
        #represent string with format
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update update_at with the current time"""
        self.updated_at = datetime.now()
        #models.storage.save()

    def to_dict(self):
        """return the dictionary of BaseModel instance
        """
        #represent dictionary of the object
        dict_object = self.__dict__.copy()
        #add '__class__' key to class name
        dict_object['__class__'] = self.__class__.__name__
        #convert created_at and updated_at to ISO format string
        dict_object['created_at'] = self.created_at.isoformat()
        dict_object['updated_at'] = self.updated_at.isoformat()

        return dict_object


if __name__ == "__main__":
    base = BaseModel()
    inst_dict = base.to_dict()
    base_new = BaseModel(**inst_dict)
    print(base)
    print("========")
    print("========")
    print(base_new)
