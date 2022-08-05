#!/usr/bin/python3
""" A Command Line Interpreter using the built-in cmd module.

The class HBNBCommand inherits from the cmd.Cmd class which allows us to
make us of the methods and attributes associted with the cmd.Cmd class

"""
import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_quit(self, args):
        """ Quit command to exit the program

        Args:
            args (str): Arguments passed
        """
        if not args:
            return True
        else:
            print(f"*** Unknowm syntax: quit {args}")

    def do_EOF(self, args):
        """ Indicates end of file. Quits the program

        Args:
            args (str): Arguments passed
        """
        if not args:
            return True
        else:
            print(f"*** Unknown syntax: EOF {args}")

    def emptyline(self):
        """ Do nothing """
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel.

        Args:
            args (...): Name of Model passed
        """
        if not args:
            print("**class name missing **")
        else:
            args = args.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                print(new_instance.id)
                new_instance.save()
    def do_show(self, args):
        """ Print string representation of an instance based on classname and id

        """
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            args_len = len(args)
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif args_len < 2:
                print("** instance id missing **")
            all_dict = storage.all()
            all_ids = []
            for item in all_dict.keys():
               all_ids.append(item.split('.')[1])
            if args[1] not in all_ids:
                print("** instance id missing **")
            else:
                print(all_dict[args[0] + '.' + args[1]])
if __name__ == '__main__':
    HBNBCommand().cmdloop()
