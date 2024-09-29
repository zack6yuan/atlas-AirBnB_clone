#!/usr/bin/python3
"""Module for the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class to represent a review of a listing"""

    place_id = ""
    user_id = ""
    text = ""
