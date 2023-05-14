#!/usr/bin/python3
"""test case for pep8"""
import unittest
import pep8


class TestCodeFormat(unittest.TestCase):
    """test case for pep8"""
    def test_pep8_base_model(self):
        """test case for pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_amenity(self):
        """test case for pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_city(self):
        """test case for pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_user(self):
        """test case for pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_state(self):
        """test case for pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_review(self):
        """test case for pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_place(self):
        """test case for pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_file_storage(self):
        """test case for  pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)
