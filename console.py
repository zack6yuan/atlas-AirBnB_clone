#!/usr/bin/python3
""" Module for the console of the AirBnB clone """
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.storage import Storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    """ Method: create class for HBNB console """

    def console_quit(self, arg):
        """ Method: exits the console """
        return True

    def console_EOF(self, arg):
        """ Method: exits the program """
        return True
    
    def console_empty(self):
        """ Method: empty line doesn't affect anything """
        pass
