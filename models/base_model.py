#!/usr/bin/python3
""" A module which defines the BaseModel class.

"""
import uuid
from datetime import datetime


class BaseModel:
    """ Defines all common attributes/methods for all other classes.

    """

    def __init__(self):
        """ Initializes the object. """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns the string representattion of the object """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Updates the updated_at attribute """
        self.updated_at = datetime.now()
