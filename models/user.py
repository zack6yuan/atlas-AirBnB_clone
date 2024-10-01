#!/usr/bin/python3
""" module for the user class """

from models.base_model import BaseModel


class User(BaseModel):
    """ Class User that inherits from BaseModel 
    
    Attributes:
    email(str): the email address of the user interacting with the console
    password(str): the password of the user interacting with the console
    first_name(str): the first name of the user interacting with the console
    last_name(str): the last name of the user interacting with the console
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, email, password, first_name, last_name):
        """ Method to initialize the user instance """
        super().__init__()
    