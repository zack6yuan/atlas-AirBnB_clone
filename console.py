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

class HBNBCommand(cmd.Cmd):
    """ Method: create class for HBNB console """
    prompt = "(hbnb) "

    class_dictionary = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Place": Place,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """ Method: exits the console """
        return True

    def do_EOF(self, arg):
        """ Method: exits the program """
        return True
    
    def emptyline(self):
        """ Method: empty line doesn't affect anything """
        pass

    def do_create(self, arg):
        """ Method: creates new instance of BaseModel,
        saves it to the JSON file, and prints the id """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            split_name = arg.split()
            if (split_name) not in HBNBCommand.class_dictionary:
                print("** class doesn't exist **")
            else: # create new instance and print id
                instance = HBNBCommand.class_dictionary[split_name]()
                instance.save()
                print("{}".format(instance.id))
    
    def do_show(self, arg):
        """ Method: prints the string representation of an
        instance based on the class name and the id """
        if len(arg) == 0:
            print("** class name missing **")
        split_name = arg.split()
        if (split_name) not in HBNBCommand.class_dictionary:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        # if the instance of the class name doesn't exist for the id (here)
        if not isinstance(arg[1], str):
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Method: deletes an instance based on the class
        name and the id, and saves change to JSON file """
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0]) not in HBNBCommand.class_dictionary:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        # if the instance of the class name doesn't exist for the id (here)
        elif not isinstance(arg[1], str):
            print("** no instance found **")


    def do_all(self, arg):
        """ Method: prints all string representation of all 
        instances based or not on the class name """
        if len(arg) > 0:
            split_name = arg.split()[0]
            if (split_name) not in HBNBCommand.class_dictionary:
                print("** class doesn't exist **")
        

    def do_update(self, arg):
        """ Method: updates an instance based on the class
        name and id by adding or updating attribute, and saves
        change to JSON file """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()