#!/usr/bin/python3
""" A module which Defines the User class.

"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines the properties of the User.

    Attributes:
        mail (str): Mail of the user
        password (str): Password of the user
        first_name (str): User's first name
        last_name (str): User's last name
    """
    email = ""
    password = ""
    first_name = ""
#    last_name = ""
