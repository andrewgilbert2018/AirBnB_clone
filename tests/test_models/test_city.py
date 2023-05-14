#!/usr/bin/python3

"""Unittest case for BaseModel"""

import os
import time
import unittest
from datetime import datetime
from models import storage
from models.city import City


class TestCity(unittest.TestCase):
    """test case for BaseModel"""

    def test_init(self):
        """test empty basemodel init"""
        info = datetime.now()
        mkd1 = City()
        info2 = datetime.now()

        self.assertIsInstance(mkd1.id, str)
        self.assertTrue(len(mkd1.id) > 0)
        self.assertTrue('City.' + mkd1.id in storage.all().keys())

        self.assertIsInstance(mkd1.created_at, datetime)
        self.assertLess(mkd1.created_at, info2)
        self.assertGreater(mkd1.created_at, info)
        
        self.assertIsInstance(mkd1.updated_at, datetime)
        self.assertLess(mkd1.updated_at, info2)
        self.assertGreater(mkd1.updated_at, info)
        
        mkd1.save()
        self.assertIsInstance(mkd1.updated_at, datetime)
        self.assertGreater(mkd1.updated_at, info)
        self.assertGreater(mkd1.updated_at, info2)
        del mkd1
        
    def test_init_dict(self):
        """test case for dict basemodel init"""
        test_dict = {'updated_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        mkd2 = City(**test_dict)

        self.assertIsInstance(mkd2.id, str)
        self.assertTrue(len(mkd2.id) > 0)
        self.assertTrue(mkd2.id == test_dict['id'])
        
        self.assertIsInstance(mkd2.created_at, datetime)
        self.assertTrue(mkd2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(mkd2.updated_at, datetime)
        self.assertTrue(mkd2.updated_at.isoformat('T') == test_dict['updated_at'])
        mkd2.save()
        self.assertGreater(mkd2.updated_at, mkd2.created_at)
        del mkd2

    def test_attribute(self):
        """test case for attribute"""
        mkd3 = City()

        self.assertTrue(hasattr(mkd3, "state_id"))
        self.assertTrue(hasattr(mkd3, "name"))

        self.assertIsInstance(mkd3.state_id, str)
        self.assertIsInstance(mkd3.name, str)
