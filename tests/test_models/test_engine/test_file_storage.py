#!/usr/bin/python3
""" Unittest For FileStorage class.

"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """ Test cases for the FileStorage.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup Test Examples """
        cls.storage = FileStorage()
        cls.model1 = BaseModel()
        cls.model1.name = "Test Model"
        cls.model1.number = 1

    def test_attr(self):
        """ Test the attributes of File Storage """
        self.storage.new(self.model1)
        self.storage.save()
        self.storage.reload()
        temp_dict = self.storage.all()
        self.assertEqual(type(temp_dict), dict)
        for key in temp_dict:
            if key.split('.')[0] == "BaseModel":
                self.assertEqual(type(temp_dict[key]), BaseModel)
            elif key.split('.')[0] == "User":
                self.assertEqual(type(temp_dict[key]), User)

    @classmethod
    def tearDownClass(cls):
        """ Destroy Test Examples """
        del cls.storage
