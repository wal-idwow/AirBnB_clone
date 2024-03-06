#!/usr/bin/python3
"""define unitests for base_model.py"""


from datetime import datetime
import unittest
from time import sleep
from models.base_model import BaseModel
import models
import os

class TestBaseModel(unittest.TestCase):
    """unitest for BaseModel class."""

    def test_initialization(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_representation(self):
        base_model = BaseModel()
        expect_str = "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expect_str)

    def test_saving(self):
        base_model = BaseModel()
        update_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(update_updated_at, base_model.updated_at)

    def test_dict(self):
        base_model = BaseModel()
        dict_obj = base_model.to_dict()
        self.assertIsInstance(dict_obj, dict)
        self.assertIn('__class__', dict_obj)
        self.assertEqual(dict_obj['__class__'], 'BaseModel')
        self.assertIn('created_at', dict_obj)
        self.assertIn('updated_at', dict_obj)
        self.assertIn('id', dict_obj)
        self.assertIsInstance(dict_obj['created_at'], str)
        self.assertIsInstance(dict_obj['updated_at'], str)
        self.assertIsInstance(dict_obj['id'], str)

        # if converting back to BaseModel results in an equal object
        base_model_new = BaseModel(**dict_obj)
        self.assertEqual(base_model.__dict__, base_model_new.__dict__)

    def test_two_unique_ids(self):
        base_m1 = BaseModel()
        base_m2 = BaseModel()
        self.assertNotEqual(base_m1.id, base_m2.id)

    def test_save_once(self):
        base_m = BaseModel()
        sleep(0.05)
        first_updated_at = base_m.updated_at
        base_m.save()
        self.assertLess(first_updated_at, base_m.updated_at)

    def test_to_dict_type(self):
        base_m = BaseModel()
        self.assertTrue(dict, type(base_m.to_dict()))

if __name__ == '__main__':
    unittest.main()
