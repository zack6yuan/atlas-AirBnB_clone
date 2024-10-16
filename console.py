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

    """ "help" is a built in command provided by the cmd module """

    def do_quit(self, arg):
        """ Method: exits the console """
        return True

    def do_EOF(self, arg):
        """ Method: exits the program """
        print("")
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
            split_name = arg.split()[0]
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
            return
        split_name = arg.split()
        if (split_name[0]) not in HBNBCommand.class_dictionary:
            print("** class doesn't exist **")
            return
        elif len(split_name) == 1:
            print("** instance id missing **")
            return
        # if the instance of the class name doesn't exist for the id
        key = split_name[1]
        if (key) not in HBNBCommand.class_dictionary:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Method: deletes an instance based on the class
        name and the id, and saves change to JSON file """
        if len(arg) == 0:
            print("** class name missing **")
            return
        split_name = arg.split()
        if (arg[0]) not in HBNBCommand.class_dictionary:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        # if the instance of the class name doesn't exist for the id (here)
        elif not isinstance(arg[1], str):
            print("** no instance found **")
            return

    def do_all(self, arg):
        """ Method: prints all string representation of all 
        instances based or not on the class name """
        if len(arg) > 0:
            split_name = arg.split()[0]
            if (split_name) not in HBNBCommand.class_dictionary:
                print("** class doesn't exist **")
                return

    def do_update(self, arg):
        """ Method: updates an instance based on the class
        name and id by adding or updating attribute, and saves
        change to JSON file """
        if len(arg) == 0:
            print("** class name missing **")
        split_name = arg.split()
        class_name = split_name[0]
        if (class_name) not in HBNBCommand.class_dictionary:
            print("** class doesn't exist **")
            return
        elif len(split_name) < 2:
            print("** instance id missing **")
            return
        elif len(split_name) < 3:
            print("** attribute name missing **")
            return
        elif len(split_name) < 4:
            print("** value missing **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()