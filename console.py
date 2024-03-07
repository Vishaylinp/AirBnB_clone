#!/usr/bin/python3
"""Create a command line interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for command line interpreter"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit program on EOF"""
        return True

    def emptyline(self):
        """Does nothing when given a empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
