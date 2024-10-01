#!/usr/bin/python3
""" module for the user class """

from models.base_model import BaseModel


class User(BaseModel):
    """ Class User that inherits from BaseModel """
    def __init__(self, email, password, first_name, last_name):
        """ Method to initialize the user instance """
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
    