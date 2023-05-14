#!/usr/bin/python3
"""Unittest case for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """testcase for BaseModel"""

    def test_init(self):
        """test empty basemodel init"""
        info = datetime.now()
        base1 = BaseModel()
        info2 = datetime.now()

        self.assertIsInstance(base1.id, str)
        self.assertTrue(len(base1.id) > 0)
        self.assertTrue('BaseModel.' + base1.id in storage.all().keys())

        self.assertIsInstance(base1.created_at, datetime)
        self.assertLess(base1.created_at, info2)
        self.assertGreater(base1.created_at, info)
        
        self.assertIsInstance(base1.updated_at, datetime)
        self.assertLess(base1.updated_at, info2)
        self.assertGreater(base1.updated_at, info)
        
        base1.save()
        self.assertIsInstance(base1.updated_at, datetime)
        self.assertGreater(base1.updated_at, info)
        self.assertGreater(base1.updated_at, info2)
        del base1
        
    def test_init_dict(self):
        """testcase for dict basemodel init"""
        test_dict = {'updated_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        base2 = BaseModel(**test_dict)

        self.assertIsInstance(base2.id, str)
        self.assertTrue(len(base2.id) > 0)
        self.assertTrue(base2.id == test_dict['id'])
        
        self.assertIsInstance(base2.created_at, datetime)
        self.assertTrue(base2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(base2.updated_at, datetime)
        self.assertTrue(base2.updated_at.isoformat('T') == test_dict['updated_at'])
        base2.save()
        self.assertGreater(base2.updated_at, base2.created_at)
        del base2
