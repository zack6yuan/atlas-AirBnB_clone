#!/usr/bin/python3
""" module for the user class """

from models.base_model import BaseModel


class User(BaseModel):
    """ Class User that inherits from BaseModel """
    def __init__(self, email, password, first_name, last_name):
        """ Method to initialize the user instance """
        super().__init__()
        email = ""
        password = ""
        first_name = ""
        last_name = ""
    