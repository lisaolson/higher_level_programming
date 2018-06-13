#!/usr/bin/python3

from models.base_model import BaseModel
import models
import cmd

class HBNBCommand(cmd.Cmd):

    classes = ['BaseModel']

    def do_create(self, args):
        new_args = args.split(' ')
        new = eval("{}()".format(new_args[0]))
        new.save()
        print(new.id)

    def do_quit(self, args):
        '''exits the program'''
        return True

    def do_EOF(self, args):
        '''exits the program'''
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
