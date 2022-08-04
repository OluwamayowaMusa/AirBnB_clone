#!/usr/bin/python3
""" A Command Interpreter Class.

"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Defines instance attribute for Command Interpreter Class.

    """

    def __init__(self):
        """ Initializes the object. """
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'


if __name__ == '__main__':
    HBNBCommand().cmdloop()
