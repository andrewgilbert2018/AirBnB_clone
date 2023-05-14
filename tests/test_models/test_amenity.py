#!/usr/bin/python3
"""Unittest testcase for Amenity"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """testcase for Amenity"""

    def test_init(self):
        """testcase for empty amenity init"""
        info = datetime.now()
        serv1 = Amenity()
        info2 = datetime.now()

        self.assertIsInstance(serv1.id, str)
        self.assertTrue(len(serv1.id) > 0)
        self.assertTrue('Amenity.' + serv1.id in storage.all().keys())

        self.assertIsInstance(serv1.created_at, datetime)
        self.assertLess(serv1.created_at, info2)
        self.assertGreater(serv1.created_at, info)
        
        self.assertIsInstance(serv1.updated_at, datetime)
        self.assertLess(serv1.updated_at, info2)
        self.assertGreater(serv1.updated_at, info)
        
        serv1.save()
        self.assertIsInstance(serv1.updated_at, datetime)
        self.assertGreater(serv1.updated_at, info)
        self.assertGreater(serv1.updated_at, info2)
        del serv1

    def test_init_dict(self):
        """testcase for dict basemodel init"""
        test_dict = {'updated_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        serv2 = Amenity(**test_dict)

        self.assertIsInstance(serv2.id, str)
        self.assertTrue(len(serv2.id) > 0)
        self.assertTrue(serv2.id == test_dict['id'])
        
        self.assertIsInstance(serv2.created_at, datetime)
        self.assertTrue(serv2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(serv2.updated_at, datetime)
        self.assertTrue(serv2.updated_at.isoformat('T') == test_dict['updated_at'])
        serv2.save()
        self.assertGreater(serv2.updated_at, serv2.created_at)
        del serv2

    def test_attribute(self):
        """testcase for atrribute"""
        serv3 = Amenity()

        self.assertTrue(hasattr(serv3, "name"))
        self.assertIsInstance(serv3.name, str)
