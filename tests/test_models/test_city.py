import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_inheritance(self):
        """"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_initialization(self):
        """"""
        city_data = {
            'id': 'test_id',
            'created_at': datetime.strptime('2024-03-07T16:13:49.817455', '%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': datetime.strptime('2024-03-07T16:13:49.817485', '%Y-%m-%dT%H:%M:%S.%f'),
            'state_id': 'test_state_id',
            'name': 'test_name'
        }

        city = City(**city_data)

        self.assertEqual(city.id, 'test_id')
        self.assertEqual(city.created_at, datetime.strptime('2024-03-07T16:13:49.817455', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(city.updated_at, datetime.strptime('2024-03-07T16:13:49.817485', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(city.state_id, 'test_state_id')
        self.assertEqual(city.name, 'test_name')

if __name__ == '__main__':
    unittest.main()
