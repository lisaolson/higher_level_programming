#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):

    classes = ['BaseModel', 'User']

    def do_EOF(self, *args):
        """Quit command to exit the program\n"""
        return True

    def do_quit(self, *args):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, *args):
        """Creates new instance of BaseModel\n"""
        if args[0] == '':
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")

    def do_show(self, *args):
        """Prints the string representation of an instance\n"""
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class name doesn't exist **")
            return
        elif len(args) < 2:
             print("** instance id missing **")
             return
        else:
            newobj = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in newobj.keys():
                return (newobj, key)
            else:
                print("** no instance found **")
            print(newobj)

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id\n"""


    def do_all(self, *args):
        """Prints all string representation of all instances\n"""


    def do_update(self, *args):
        """Updates an instance based on the class name and id\n"""

    def emptyline(self):
        pass

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
