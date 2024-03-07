import unittest
from models.place import Place
from datetime import datetime
from time import sleep

class TestPlace(unittest.TestCase):
    def test_instantiation(self):
        # Test Case 1: Minimal data
        place = Place()
        self.assertIsInstance(place, Place)

        # Test Case 2: Full data
        place_data = {
            'id': '1',
            'city_id': 'city_1',
            'user_id': 'user_1',
            'name': 'Sample Place',
            'description': 'A beautiful place',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 6,
            'price_by_night': 150,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenity_ids': ['amenity_1', 'amenity_2'],
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        place = Place(**place_data)
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        # Test Case 3: Public attributes
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)

    def test_unique_ids(self):
        # Test Case 4: Unique IDs
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_different_created_at(self):
        # Test Case 5: Different created_at
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_different_updated_at(self):
        # Test Case 6: Different updated_at
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_str_representation(self):
        # Test Case 7: __str__ representation
        dt = datetime.today()
        dt_repr = repr(dt)
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = dt
        place_str = str(place)
        self.assertIn("[Place] (123456)", place_str)
        self.assertIn("'id': '123456'", place_str)
        self.assertIn("'created_at': " + dt_repr, place_str)
        self.assertIn("'updated_at': " + dt_repr, place_str)

    def test_save_method(self):
        # Test Case 8: Save method
        place = Place()
        first_updated_at = place.updated_at
        sleep(0.05)
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_to_dict_method(self):
        # Test Case 9: to_dict method
        place = Place()
        place.id = "123456"
        dt = datetime.today()
        place.created_at = place.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), tdict)

    def test_invalid_instantiation(self):
        # Test Case 10: Invalid instantiation with None kwargs
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

if __name__ == '__main__':
    unittest.main()
