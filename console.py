#!/usr/bin/python3
"""Create a command line interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """Class for command line interpreter

       Attr:
            class_list (list): list of classes"""
    prompt = '(hbnb) '
    class_list = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit program on EOF"""
        return True

    def emptyline(self):
        """Does nothing when given a empty line"""
        pass

    def postloop(self):
        """print newline after console exit"""
        print()

    def do_create(self, line):
        """create instance of base class, save to JSON and print id"""
        if line is None or line == "":
            print("** class name missing **")
            return False
        elif line not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return False
        else:
            inst = storage.classes()[line]()
            storage.new(inst)
            inst.save()
            print(inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return False
        else:
            words = line.split(' ')
            class_name = words[0]

            if class_name not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return False
            elif len(words) < 2:
                print("** instance id missing **")
                return False
            else:
                inst_id = words[1]
                key = "{}.{}".format(class_name, inst_id)

                if key not in storage.all():
                    print("** no instance found **")
                    return False
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            class_name = words[0]

            if class_name not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                inst_id = words[1]
                key = "{}.{}".format(class_name, inst_id)

                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(" ")
            class_name = words[0]

            if class_name not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            else:
                inst_list = [str(obj) for id_key, obj in storage.all().items()
                      if type(obj).__name__ == class_name]
                print(inst_list)
        else:
            new_list = [str(obj) for id_key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        """update instance based on class name and id"""
        if line is None or line == "":
            print("** class name missing **")
            return False

        words = line.split(" ")
        class_name = words[0]

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return False
        elif len(words) < 2:
            print("** instance id missing **")
            return False

        inst_id = words[1]
        id_key = class_name + "." + inst_id
        if id_key not in storage.all().keys():
            print("** no instance found **")
            return False
        elif len(words) < 3:
                print("** attribute name missing **")
                return False
        elif len(words) < 4:
            print("** value missing **")
            return False

            attr_name = words[2]
            str_attr_val = words[3]
            attr_val = ast.literal_eval(str_attr_val)

            storage.all()[id_key][attr_name] = attr_val
            storage.all()[id_key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
