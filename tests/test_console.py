#!/usr/bin/python3
""" Unittest for the console.

"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """ Test cases for method in console.

    """

    def test_quit(self):
        self.assertIs(HBNBCommand().onecmd("quit"), True)
