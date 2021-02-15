#!/usr/bin/python3
"""Define HBNBCommand class"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command prompt class"""

    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel}

    def emptyline(self):
        """Empty options - do Nothing"""
        pass

    def do_quit(self, argument):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, argument):
        """ Defines EOF option"""
        return True

    def do_create(self, argument):
        """
        Create a new object in BaseModel
        Save and print the id
        """
        if argument:
            if argument in HBNBCommand.classes.keys():
                newobject = HBNBCommand.classes[argument]()
                newobject.save()
                print(newobject.id)

            if argument not in HBNBCommand.classes.keys():
                print(" **class doesn't exist** ")

        elif not argument:
            print(" **class name missing ** ")

    def do_show(self, argument):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        args = argument.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            dic = models.storage.all()
            show_id = str(args[0]) + '.' + str(args[1])
            if show_id in dic:
                print(dic[show_id])
            else:
                print("** no instance found **")

    def do_destroy(self, argument):
        args = argument.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            dic = models.storage.all()
            show_id = str(args[0]) + '.' + str(args[1])
            if show_id in dic:
                del dic[show_id]
                models.storage.save()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
