#!/usr/bin/python3
"""Defines unittests for models/user.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_01_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_02_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_03_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_04_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_05_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_06_email_is_public_class_attribute(self):
        usr = User()
        self.assertEqual(str, type(User.email))
        self.assertIn("email", dir(usr))
        self.assertNotIn("email", usr.__dict__)

    def test_07_password_is_public_class_attribute(self):
        usr = User()
        self.assertEqual(str, type(User.password))
        self.assertIn("password", dir(usr))
        self.assertNotIn("password", usr.__dict__)

    def test_08_first_name_is_public_class_attribute(self):
        usr = User()
        self.assertEqual(str, type(User.first_name))
        self.assertIn("first_name", dir(usr))
        self.assertNotIn("first_name", usr.__dict__)

    def test_09_last_name_is_public_class_attribute(self):
        usr = User()
        self.assertEqual(str, type(User.last_name))
        self.assertIn("last_name", dir(usr))
        self.assertNotIn("last_name", usr.__dict__)

    def test_10_two_users_unique_ids(self):
        usr1 = User()
        usr2 = User()
        self.assertNotEqual(usr1.id, usr2.id)

    def test_11_two_users_different_created_at(self):
        usr1 = User()
        sleep(0.05)
        usr2 = User()
        self.assertLess(usr1.created_at, usr2.created_at)

    def test_12_two_users_different_updated_at(self):
        usr1 = User()
        sleep(0.05)
        usr2 = User()
        self.assertLess(usr1.updated_at, usr2.updated_at)

    def test_13_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        usr = User()
        usr.id = "123456"
        usr.created_at = usr.updated_at = dt
        usr_str = usr.__str__()
        self.assertIn("[User] (123456)", usr_str)
        self.assertIn("'id': '123456'", usr_str)
        self.assertIn("'created_at': " + dt_repr, usr_str)
        self.assertIn("'updated_at': " + dt_repr, usr_str)

    def test_14_args_unused(self):
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_15_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        usr = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(usr.id, "345")
        self.assertEqual(usr.created_at, dt)
        self.assertEqual(usr.updated_at, dt)

    def test_16_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Unittests for testing save method of the User class."""

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

    def test_01_one_save(self):
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        self.assertLess(first_updated_at, usr.updated_at)

    def test_02_two_saves(self):
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        second_updated_at = usr.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        usr.save()
        self.assertLess(second_updated_at, usr.updated_at)

    def test_03_save_with_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_04_save_updates_file(self):
        usr = User()
        usr.save()
        usr_id = "User." + usr.id
        with open("file.json", "r") as f:
            self.assertIn(usr_id, f.read())


class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_01_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_02_to_dict_contains_correct_keys(self):
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def test_03_to_dict_contains_added_attributes(self):
        usr = User()
        usr.middle_name = "Holberton"
        usr.my_number = 98
        self.assertEqual("Holberton", usr.middle_name)
        self.assertIn("my_number", usr.to_dict())

    def test_04_to_dict_datetime_attributes_are_strs(self):
        usr = User()
        usr_dict = usr.to_dict()
        self.assertEqual(str, type(usr_dict["id"]))
        self.assertEqual(str, type(usr_dict["created_at"]))
        self.assertEqual(str, type(usr_dict["updated_at"]))

    def test_05_to_dict_output(self):
        dt = datetime.today()
        usr = User()
        usr.id = "123456"
        usr.created_at = usr.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(usr.to_dict(), tdict)

    def test_06_contrast_to_dict_dunder_dict(self):
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def test_07_to_dict_with_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)


if __name__ == "__main__":
    unittest.main()
