#!/usr/bin/python3
"""Defines comprehensive unittests for the entire AirBnB project."""

import os
import json
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class TestModels(unittest.TestCase):
    """Comprehensive unittests for the AirBnB project."""

    @classmethod
    def setUpClass(cls):
        """Setup for the test class."""
        cls.file_path = "file.json"
        cls.objects = FileStorage._FileStorage__objects
        try:
            os.rename(cls.file_path, "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Teardown for the test class."""
        try:
            os.remove(cls.file_path)
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", cls.file_path)
        except FileNotFoundError:
            pass

    def setUp(self):
        """Setup for each test."""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()
        self.city = City()
        self.place = Place()
        self.amenity = Amenity()
        self.review = Review()
        self.state = State()

    def tearDown(self):
        """Teardown for each test."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_base_model(self):
        """Test methods of the BaseModel class."""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertEqual(str(self.base_model),
                         "[BaseModel] ({}) {}".format(
                             self.base_model.id, self.base_model.__dict__))

    def test_user(self):
        """Test methods of the User class."""
        self.assertIsInstance(self.user, User)
        self.assertEqual(str(self.user),
                         "[User] ({}) {}".format(
                             self.user.id, self.user.__dict__))

    def test_city(self):
        """Test methods of the City class."""
        self.assertIsInstance(self.city, City)
        self.assertEqual(str(self.city),
                         "[City] ({}) {}".format(
                             self.city.id, self.city.__dict__))

    def test_place(self):
        """Test methods of the Place class."""
        self.assertIsInstance(self.place, Place)
        self.assertEqual(str(self.place),
                         "[Place] ({}) {}".format(
                             self.place.id, self.place.__dict__))

    def test_amenity(self):
        """Test methods of the Amenity class."""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(str(self.amenity),
                         "[Amenity] ({}) {}".format(
                             self.amenity.id, self.amenity.__dict__))

    def test_review(self):
        """Test methods of the Review class."""
        self.assertIsInstance(self.review, Review)
        self.assertEqual(str(self.review),
                         "[Review] ({}) {}".format(
                             self.review.id, self.review.__dict__))

    def test_state(self):
        """Test methods of the State class."""
        self.assertIsInstance(self.state, State)
        self.assertEqual(str(self.state),
                         "[State] ({}) {}".format(
                             self.state.id, self.state.__dict__))

    def test_file_storage(self):
        """Test methods of the FileStorage class."""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(self.storage.all(), self.objects)

    def test_serialization_deserialization(self):
        """Test serialization and deserialization of objects."""
        obj_list = [
            self.base_model, self.user, self.city,
            self.place, self.amenity, self.review, self.state
            ]
        for obj in obj_list:
            obj_id = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.storage.new(obj)
            self.storage.save()
            with open(self.file_path, "r", encoding='utf-8') as file:
                saved_data = json.load(file)
                self.assertIn(obj_id, saved_data)
                self.assertEqual(
                    saved_data[obj_id]['__class__'],
                    obj.__class__.__name__
                    )
                self.assertEqual(saved_data[obj_id]['id'], obj.id)
                self.assertEqual(
                    saved_data[obj_id]['created_at'],
                    obj.created_at.isoformat()
                    )
                self.assertEqual(
                    saved_data[obj_id]['updated_at'],
                    obj.updated_at.isoformat()
                    )
            new_storage = FileStorage()
            new_storage.reload()
            loaded_obj = new_storage.all()[obj_id]
            self.assertIsInstance(loaded_obj, obj.__class__)
            self.assertEqual(loaded_obj.id, obj.id)
            self.assertEqual(loaded_obj.created_at, obj.created_at)
            self.assertEqual(loaded_obj.updated_at, obj.updated_at)


if __name__ == "__main__":
    unittest.main()
