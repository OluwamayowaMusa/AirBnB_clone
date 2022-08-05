#!/usr/bin/python3
""" A module which defines the Review class.

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the properties of the Review objects.

    Attributes:
        place_id (str): Unique ID of place
        user_id (str): Unique ID of place
        text (str): A review of a place
    """
    place_id = ""
    user_id = ""
    text = ""
