#!/usr/bin/python3
"""File storage module"""


import json


class FileStorage():
    """File storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to __objects"""
        name_obj = obj.__class__.__name__
        id_obj = obj.id
        FileStorage.__objects[name_obj + '.' + id_obj] = obj

    def save(self):
        """serializes __objects to the json file (path: __file_path)"""
        way = FileStorage.__file_path

        #convert objects to dictionary of dictionaries
        obj_new = {ke: FileStorage.__objects[ke].to_dict(
        ) for ke in FileStorage.__objects.keys()}

        with open(way, "w", encoding='utf-8') as file:
            json.dump(obj_new, file)

    def reload(self):
        """deserializes the json file to __objects (only if the file existes)"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        from models.state import State
        way = FileStorage.__file_path
        try:
            with open(way, encoding='utf-8') as file:
                obj_new = json.load(file)
                name_cls = '__class__'
                for key, value in obj_new.items():
                    if name_cls in value:
                        FileStorage.__objects[key] = eval(value[name_cls] + '(**value)')
        except FileNotFoundError:
            pass
