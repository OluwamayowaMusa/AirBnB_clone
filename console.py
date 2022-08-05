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
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                all_instances = storage.all()
                dict_key = args[0] + '.' + args[1]
                if dict_key not in all_instances:
                    print("** no instance found **")
                else:
                    print(all_instances[dict_key])

    def do_destroy(self, args):
        """ Destroys an istance based on className and id """
        if not args:
            print("** class name missing  **")
        else:
            args = args.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                all_instances = storage.all()
                dict_key = args[0] + '.' + args[1]
                if dict_key not in all_instances:
                    print("** no instance found **")
                else:
                    del all_instances[dict_key]
                    storage.save()
 
    def do_all(self, args):
        all_instances =  storage.all()
        str_list = []
        if len(args) == 0:
            for instance in all_instances:
                str_list.append(str(all_instances[instance]))
            print(str_list)
        else:
            class_instance = args.split()[0]
            if class_instance != "BaseModel":
                print("** class doesn't exist **")
            else:
                for instance in all_instances.keys():
                    if class_instance in instance:
                       str_list.append(str(instance))
                print(str_list)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
