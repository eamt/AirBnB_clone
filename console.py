#!/usr/bin/python3
"""
Implementation HBNBCommand class

"""
import cmd
import models
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command prompt class"""
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel, 'User': User, 'State': State,
        'City': City, 'Amenity': Amenity, 'Place': Place,
        'Review': Review
    }

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
        args = split(argument)
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
        """
        Deletes an instance based on the class name and id
        and saved the change into the JSON file
        """
        args = split(argument)
        if len(args) == 0:
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

    def do_all(self, argument):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = split(argument)
        dic = models.storage.all()
        objects = []
        if len(args) == 0:
            for key, value in dic.items():
                objects.append(str(value))
            print(objects)
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **'")
        else:
            for key, value in dic.items():
                if args[0] in key:
                    objects.append(str(value))
            print(objects)

    def do_update(self, argument):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute and saved the change
        into the JSON file
        """
        args = split(argument)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            dic = models.storage.all()
            show_id = str(args[0]) + '.' + str(args[1])
            if show_id not in dic:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(dic, args[2], args[3])
                models.storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
