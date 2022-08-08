#!/usr/bin/python3
""" Unittest for Storage Varibale.

"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    """ Test Cases for Storage Variable.

    """

    def test_attr(self):
        """ Test attriutes of storage variable """
        self.assertEqual(type(storage), FileStorage)
        self.assertEqual(type(storage.all()), dict)
