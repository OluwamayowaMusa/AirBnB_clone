#!/usr/bin/python3
""" Unittest For FileStorage class.

"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test cases for the FileStorage.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup Test Examples """
        cls.storage = FileStorage()

    def test_attr(self):
        """ Test the attributes of File Storage """
        temp_dict = self.storage.all()
        self.assertEqual(type(temp_dict), dict)
        for key in temp_dict:
            self.assertEqual(type(temp_dict[key]), BaseModel)

    @classmethod
    def tearDownClass(cls):
        """ Destroy Test Examples """
        del cls.storage
