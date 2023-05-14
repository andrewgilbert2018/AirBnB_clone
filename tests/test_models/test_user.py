#!/usr/bin/python3

"""Unittest case  for BaseModel"""

import os
import time
import unittest
from datetime import datetime
from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """test case for BaseModel"""

    def test_init(self):
        """test case for empty basemodel init"""
        info = datetime.now()
        s1 = User()
        info2 = datetime.now()

        self.assertIsInstance(s1.id, str)
        self.assertTrue(len(s1.id) > 0)
        self.assertTrue('User.' + s1.id in storage.all().keys())

        self.assertIsInstance(s1.created_at, datetime)
        self.assertLess(s1.created_at, info2)
        self.assertGreater(s1.created_at, info)
        
        self.assertIsInstance(s1.updated_at, datetime)
        self.assertLess(s1.updated_at, info)
        self.assertGreater(s1.updated_at, info2)
        
        s1.save()
        self.assertIsInstance(s1.updated_at, datetime)
        self.assertGreater(s1.updated_at, info)
        self.assertGreater(s1.updated_at, info2)
        del s1
        
    def test_init_dict(self):
        """test case for dict basemodel init"""
        test_dict = {'updated_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        s2 = User(**test_dict)

        self.assertIsInstance(s2.id, str)
        self.assertTrue(len(s2.id) > 0)
        self.assertTrue(s2.id == test_dict['id'])
        
        self.assertIsInstance(s2.created_at, datetime)
        self.assertTrue(s2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(s2.updated_at, datetime)
        self.assertTrue(s2.updated_at.isoformat('T') == test_dict['updated_at'])
        s2.save()
        self.assertGreater(s2.updated_at, s2.created_at)
        del s2

    def test_attribute(self):
        """test case attribute"""
        s3 = User()

        self.assertTrue(hasattr(s3, "email"))
        self.assertTrue(hasattr(s3, "password"))
        self.assertTrue(hasattr(s3, "first_name"))
        self.assertTrue(hasattr(s3, "last_name"))

        self.assertIsInstance(s3.email, str)
        self.assertIsInstance(s3.password, str)
        self.assertIsInstance(s3.first_name, str)
        self.assertIsInstance(s3.last_name, str)
