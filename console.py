#!/usr/bin/python3
"""Define HBNBCommand class"""

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command prompt class"""

    prompt = '(hbnb)'
    
    classes= {'BaseModel': BaseModel}
    

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
        """Create a new object in BaseModel
        Save and print the id """

        if argument:
            if argument in HBNBCommand.classes.keys():
                newobject = HBNBCommand.classes[argument]()
                newobject.save()
                print(newobject.id)

            if argument not in HBNBCommand.classes.keys():
                print("**class doesn't exist**")

        elif not argument:
            print('**class name missing **')
        
    """def do_show(self,"""

if __name__ == "__main__":
    HBNBCommand().cmdloop()
