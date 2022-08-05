#!/usr/bin/python3
""" A module which defines City class.

"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines the properties of City.

    Attrbutes:
        state_id (str): ID of state
        name (str): Name of city
    """
    state_id = ""
    name = ""
