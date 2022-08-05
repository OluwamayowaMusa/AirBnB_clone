#!/usr/bin/python3
""" A Command Line Interpreter using the built-in cmd module.

The class HBNBCommand inherits from the cmd.Cmd class which allows us to
make us of the methods and attributes associted with the cmd.Cmd class

"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Defines attributes(method and fields) for Command Interpreter Class.

    Attributes:
        intro (str): An introduction to the CLI
        prompt (str): A prompt which takes in commands
    """
    intro = "\tWelcome to HBNB CLI\n"\
            "\tfor help, enter '?'\n"\
            "\tto quit, enter 'quit'"

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """ Indicates end of file. Quits the program
        """
        return True

    def emptyline(self):
        """ Do nothing """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel. """
        if not line:
            print("**class name missing **")
        else:
            line = line.split()
            if line[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                print(new_instance.id)
                new_instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
