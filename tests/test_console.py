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

    def test_show(self):
        """ Test the do_show method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            tmp = f.getvalue()
            self.assertEqual(tmp, "** instance id missing **\n")

    def test_destroy(self):
        """ Test do_destroy method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            tmp = f.getvalue()
            self.assertEqual(tmp, "** instance id missing **\n")
            
    def test_all(self):
        """ Test do_all method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            tmp = f.getvalue()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")

    def test_update(self):
        """ Test do_update """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            tmp = f.getvalue()
            self.assertEqual(tmp, "** instance id missing **\n")

    def test_method_all(self):
        """ Test <class_name>.all() """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            tmp = f.getvalue()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], '[')
            self.assertEqual(tmp_list[-2], ']')
            HBNBCommand().onecmd("Review.all()")
            position = len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0],"[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("User.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("State.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("City.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("Amenity.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("Place.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")

    def test_method_count(self):
        """ Test <class_name>.count() """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            tmp = int(f.getvalue().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("Review.count()")
            position = len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("User.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("Amenity.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("State.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("Place.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("City.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
