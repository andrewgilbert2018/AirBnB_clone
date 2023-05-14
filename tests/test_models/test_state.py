#!/usr/bin/python3

"""Unittest case for BaseModel"""

import os
import time
import unittest
from datetime import datetime
from models import storage
from models.state import State


class TestState(unittest.TestCase):
    """test case BaseModel"""

    def test_init(self):
        """test case empty basemodel init"""
        info = datetime.now()
        abj1 = State()
        info2 = datetime.now()

        self.assertIsInstance(abj1.id, str)
        self.assertTrue(len(abj1.id) > 0)
        self.assertTrue('State.' + abj1.id in storage.all().keys())

        self.assertIsInstance(abj1.created_at, datetime)
        self.assertLess(abj1.created_at, info2)
        self.assertGreater(abj1.created_at, info)
        
        self.assertIsInstance(abj1.updated_at, datetime)
        self.assertLess(abj1.updated_at, info2)
        self.assertGreater(abj1.updated_at, info)
        
        abj1.save()
        self.assertIsInstance(abj1.updated_at, datetime)
        self.assertGreater(abj1.updated_at, info)
        self.assertGreater(abj1.updated_at, info2)
        del abj1
        
    def test_init_dict(self):
        """test case for dict basemodel init"""
        test_dict = {'updated_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        abj2 = State(**test_dict)

        self.assertIsInstance(abj2.id, str)
        self.assertTrue(len(abj2.id) > 0)
        self.assertTrue(abj2.id == test_dict['id'])
        
        self.assertIsInstance(abj2.created_at, datetime)
        self.assertTrue(abj2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(abj2.updated_at, datetime)
        self.assertTrue(abj2.updated_at.isoformat('T') == test_dict['updated_at'])
        abj2.save()
        self.assertGreater(abj2.updated_at, abj2.created_at)
        del abj2

    def test_attribute(self):
        """test case for attribute"""
        abj3 = State()

        self.assertTrue(hasattr(abj3, "name"))
        self.assertIsInstance(abj3.name, str)
