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
            self.assertEqual(f.getvalue(), "\nDocumented commands "
                                           "(type help <topic>):\n======"
                                           "================================"
                                           "==\nEOF  all  create  destroy"
                                           "  help  quit  show  update\n\n")

    def test_emptyline(self):
        """ Test the emptyline method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            tmp = f.getvalue()
            self.assertEqual(tmp, '')

    def test_create(self):
        """ Test the do_create method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            tmp = f.getvalue()
            tmp_list = tmp.split('-')
            self.assertEqual(len(tmp_list), 5)
            for i in tmp_list:
                self.assertEqual(i.isascii(), True)
