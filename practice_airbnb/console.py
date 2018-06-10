#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):

    def do_EOF(self, *args):
        """Quit command to exit the program\n"""
        return True

    def do_quit(self, *args):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, *args):
        """Creates new instance of BaseModel\n"""
        

    def do_show(self, *args):
        """Prints the string representation of an instance\n"""
        prints = str(
        
    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id\n"""


    def do_all(self, *args):
        """Prints all string representation of all instances\n"""


    def do_update(self, *args):
        """Updates an instance based on the class name and id\n"""



if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
