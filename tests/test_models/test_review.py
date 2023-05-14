#!/usr/bin/python3

"""Unittest case for BaseModel"""

import os
import time
import unittest
from datetime import datetime
from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    """test case for BaseModel"""

    def test_init(self):
        """test empty basemodel init"""
        info = datetime.now()
        vp1 = Review()
        info2 = datetime.now()

        self.assertIsInstance(vp1.id, str)
        self.assertTrue(len(vp1.id) > 0)
        self.assertTrue('Review.' + vp1.id in storage.all().keys())

        self.assertIsInstance(vp1.created_at, datetime)
        self.assertLess(vp1.created_at, info2)
        self.assertGreater(vp1.created_at, info)
        
        self.assertIsInstance(vp1.updated_at, datetime)
        self.assertLess(vp1.updated_at, info2)
        self.assertGreater(vp1.updated_at, info)
        
        vp1.save()
        self.assertIsInstance(vp1.updated_at, datetime)
        self.assertGreater(vp1.updated_at, info)
        self.assertGreater(vp1.updated_at, info2)
        del vp1
        
    def test_init_dict(self):
        """test case for dict basemodel init"""
        test_dict = {'updated_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(2000, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        vp2 = Review(**test_dict)

        self.assertIsInstance(vp2.id, str)
        self.assertTrue(len(vp2.id) > 0)
        self.assertTrue(vp2.id == test_dict['id'])
        
        self.assertIsInstance(vp2.created_at, datetime)
        self.assertTrue(vp2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(vp2.updated_at, datetime)
        self.assertTrue(vp2.updated_at.isoformat('T') == test_dict['updated_at'])
        vp2.save()
        self.assertGreater(vp2.updated_at, vp2.created_at)
        del vp2

    def test_attribute(self):
        """test case for attribute"""
        vp3 = Review()

        self.assertTrue(hasattr(vp3, "place_id"))
        self.assertTrue(hasattr(vp3, "user_id"))
        self.assertTrue(hasattr(vp3, "text"))

        self.assertIsInstance(vp3.place_id, str)
        self.assertIsInstance(vp3.user_id, str)
        self.assertIsInstance(vp3.text, str)
