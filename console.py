#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Command prompt class"""

    prompt = '(hbnb)'

    def emptyline(self):
        """Empty options - do Nothing"""
        pass

    def do_quit(self, argument):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, argument):
        """ Defines EOF option"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
