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
        """ Test the do_quit method """
        self.assertIs(HBNBCommand().onecmd("quit"), True)

    def test_EOF(self):
        """ Test the do_EOF method """
        self.assertIs(HBNBCommand().onecmd("EOF"), True)

    def test_help(self):
        """ Test the default help method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(type(f.getvalue()), str)

    def test_emptyline(self):
        """ Test the emptyline method """
        self.assertEqual(HBNBCommand().onecmd("\n"), None)

    def test_create(self):
        """ Test the do_create method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertEqual(type(f.getvalue()), str)
