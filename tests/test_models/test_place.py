#!/usr/bin/python3

"""Unittest case for BaseModel"""

import os
import time
import unittest
from datetime import datetime
from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    """test case for BaseModel"""

    def test_init(self):
        """test empty basemodel init"""
        info = datetime.now()
        bn1 = Place()
        info2 = datetime.now()

        self.assertIsInstance(bn1.id, str)
        self.assertTrue(len(bn1.id) > 0)
        self.assertTrue('Place.' + bn1.id in storage.all().keys())

        self.assertIsInstance(bn1.created_at, datetime)
        self.assertLess(bn1.created_at, info2)
        self.assertGreater(bn1.created_at, info)
        
        self.assertIsInstance(bn1.updated_at, datetime)
        self.assertLess(bn1.updated_at, info2)
        self.assertGreater(bn1.updated_at, info)
        
        bn1.save()
        self.assertIsInstance(bn1.updated_at, datetime)
        self.assertGreater(bn1.updated_at, info)
        self.assertGreater(bn1.updated_at, info2)
        del bn1
        
    def test_init_dict(self):
        """test case for dict basemodel init"""
        test_dict = {'updated_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        bn2 = Place(**test_dict)

        self.assertIsInstance(bn2.id, str)
        self.assertTrue(len(bn2.id) > 0)
        self.assertTrue(bn2.id == test_dict['id'])
        
        self.assertIsInstance(bn2.created_at, datetime)
        self.assertTrue(bn2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(bn2.updated_at, datetime)
        self.assertTrue(bn2.updated_at.isoformat('T') == test_dict['updated_at'])
        bn2.save()
        self.assertGreater(bn2.updated_at, bn2.created_at)
        del bn2

    def test_attribute(self):
        """test case for attribute"""
        bn3 = Place()

        self.assertTrue(hasattr(bn3, "city_id"))
        self.assertTrue(hasattr(bn3, "user_id"))
        self.assertTrue(hasattr(bn3, "name"))
        self.assertTrue(hasattr(bn3, "description"))
        self.assertTrue(hasattr(bn3, "number_rooms"))
        self.assertTrue(hasattr(bn3, "number_bathrooms"))
        self.assertTrue(hasattr(bn3, "max_guest"))
        self.assertTrue(hasattr(bn3, "price_by_night"))
        self.assertTrue(hasattr(bn3, "latitude"))
        self.assertTrue(hasattr(bn3, "longitude"))
        self.assertTrue(hasattr(pm3, "amenity_ids"))

        self.assertIsInstance(bn3.city_id, str)
        self.assertIsInstance(bn3.user_id, str)
        self.assertIsInstance(bn3.name, str)
        self.assertIsInstance(bn3.description, str)
        self.assertIsInstance(bn3.number_rooms, int)
        self.assertIsInstance(bn3.number_bathrooms, int)
        self.assertIsInstance(bn3.max_guest, int)
        self.assertIsInstance(bn3.price_by_night, int)
        self.assertIsInstance(bn3.latitude, float)
        self.assertIsInstance(bn3.longitude, float)
        self.assertIsInstance(bn3.amenity_ids, list)

