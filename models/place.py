#!/usr/bin/python3
""" A module which defines the Place class.

"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Defines the properties of Place.

    Attributes:
        city_id (str): Unique ID of city
        user_id (str): Unique ID of User
        name (str): Name of place
        description (str): A brief description of place
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests
        price_by_night (int): Price
        latitude (float): Latitude of the place
        longitude (float): Longitude of the place
        amenity_ids (list): List of availiable
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
