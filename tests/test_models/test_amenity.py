#!/usr/bin/python3
"""Defines unittests for models/amenity.py"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityInst(unittest.TestCase):
    """unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amnity_inst = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(amnity_inst))
        self.assertNotIn("name", amnity_inst.__dict__)

    def test_two_amenities_unique_ids(self):
        amenity_instance1 = Amenity()
        amenity_instance2 = Amenity()
        self.assertNotEqual(amenity_instance1.id, amenity_instance2.id)

    def test_two_amenities_different_created_at(self):
        amenity_instance1 = Amenity()
        sleep(0.05)
        amenity_instance2 = Amenity()
        self.assertLess(amenity_instance1.created_at,
                        amenity_instance2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity_instance1 = Amenity()
        sleep(0.05)
        amenity_instance2 = Amenity()
        self.assertLess(amenity_instance1.updated_at,
                        amenity_instance2.updated_at)

    def test_str_representation(self):
        current_dt = datetime.today()
        dt_repr = repr(current_dt)
        amnity_inst = Amenity()
        amnity_inst.id = "123456"
        amnity_inst.created_at = amnity_inst.updated_at = current_dt
        amenity_str = amnity_inst.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': " + dt_repr, amenity_str)
        self.assertIn("'updated_at': " + dt_repr, amenity_str)

    def test_args_unused(self):
        amnity_inst = Amenity(None)
        self.assertNotIn(None, amnity_inst.__dict__.values())

    def test_instantiation_with_kwargs(self):
        current_dt = datetime.today()
        curnt_dt = current_dt.isoformat()
        amnity_inst = Amenity(
            id="345", created_at=curnt_dt, updated_at=curnt_dt)
        self.assertEqual(amnity_inst.id, "345")
        self.assertEqual(amnity_inst.created_at, current_dt)
        self.assertEqual(amnity_inst.updated_at, current_dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenitySaving(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_saving1(self):
        amnity_inst = Amenity()
        sleep(0.05)
        first_updated_at = amnity_inst.updated_at
        amnity_inst.save()
        self.assertLess(first_updated_at, amnity_inst.updated_at)

    def test_saving2(self):
        amnity_inst = Amenity()
        sleep(0.05)
        first_updated_at = amnity_inst.updated_at
        amnity_inst.save()
        second_updated_at = amnity_inst.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amnity_inst.save()
        self.assertLess(second_updated_at, amnity_inst.updated_at)

    def test_save_with_arg(self):
        amnity_inst = Amenity()
        with self.assertRaises(TypeError):
            amnity_inst.save(None)

    def test_save_updates_file(self):
        amnity_inst = Amenity()
        amnity_inst.save()
        amenity_id = "Amenity." + amnity_inst.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestAmenityDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_correct_keys(self):
        amnity_inst = Amenity()
        self.assertIn("id", amnity_inst.to_dict())
        self.assertIn("created_at", amnity_inst.to_dict())
        self.assertIn("updated_at", amnity_inst.to_dict())
        self.assertIn("__class__", amnity_inst.to_dict())

    def test_to_dict_more_attr(self):
        amnity_inst = Amenity()
        amnity_inst.middle_name = "example"
        amnity_inst.my_number = 98
        self.assertEqual("example", amnity_inst.middle_name)
        self.assertIn("my_number", amnity_inst.to_dict())

    def test_to_dict_datetime_attr_strs(self):
        amnity_inst = Amenity()
        amenity_dict = amnity_inst.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_output_to_dict_(self):
        current_dt = datetime.today()
        amnity_inst = Amenity()
        amnity_inst.id = "123456"
        amnity_inst.created_at = amnity_inst.updated_at = current_dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': current_dt.isoformat(),
            'updated_at': current_dt.isoformat(),
        }
        self.assertDictEqual(amnity_inst.to_dict(), tdict)

    def test_to_dict_fewer_dict(self):
        amnity_inst = Amenity()
        self.assertNotEqual(amnity_inst.to_dict(), amnity_inst.__dict__)

    def test_to_dict_arg(self):
        amnity_inst = Amenity()
        with self.assertRaises(TypeError):
            amnity_inst.to_dict(None)


if __name__ == "__main__":
    unittest.main()
