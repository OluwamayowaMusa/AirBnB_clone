#!/usr/bin/python3
""" Unittest for BaseModel class.

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup test examples as class attributes """
        cls.model1 = BaseModel()
        cls.model1.name = "Azezz"

    def test_id(self):
        """ Test attributes of BaseModel class """
        self.assertEqual(type(self.model1), BaseModel)
        self.assertEqual(type(self.model1.id), str)
        self.assertEqual(type(self.model1.created_at), datetime)

    def test_save(self):
        """ Test the save method of the BaseModel """
        temp = self.model1.updated_at
        self.model1.save()
        temp_1 = self.model1.updated_at
        self.assertNotEqual(temp, temp_1)

    @classmethod
    def tearDownClass(cls):
        """ Destroy Test examples """
        del cls.model1
