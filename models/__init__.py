#!/usr/bin/python3
"""initialize the models package"""
from models.engine.file_storage import FileStorage

classes = {
    'BaseModel': 'BaseModel',
    'Amenity': 'Amenity',
    'State': 'State',
    'Place': 'Place',
    'Review': 'Review',
    'User': 'User'}
storage = FileStorage()
storage.reload()
