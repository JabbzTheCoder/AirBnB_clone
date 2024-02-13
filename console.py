#!/usr/bin/python3
'''Entrance of the program'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {
        'BaseModel': BaseModel,
        'User': User
    }

    def do_create(self, arg):
        new_instance = None
       
        """Create a new instance of a specified class."""
        if not arg:
            print("** class name missing **")
            return

        # Check if the class exists in the dictionary.
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return

        # Dynamically instantiate the class.
        new_instance = self.__classes[arg]()
        if new_instance:
            new_instance.save()
            print(new_instance.id)
    
    def do_show(self, arg):
        """Print the string representation of an instance."""
        obj_dict = storage.all()
        args = arg.split()
        key = ""
        

        if not arg:
            print("** class name missing **")
            return

        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        
        key = args[0] + '.' + args[1]

        if key not in obj_dict:
            print("** no instance found **")
            return
        else:
            print(obj_dict[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        obj_dict = storage.all()

        if key not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict[key]
            storage.save()

    def do_all(self, arg):
        """Print string representation of all instances."""
        if arg:
            if arg not in self.__classes:
                print("** class doesn't exist **")
                return

            objs = storage.all(arg)
        else:
            objs = storage.all()

        print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        obj_dict = storage.all()

        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]

        obj = obj_dict[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        sys.exit(0)

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        sys.exit(0)

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
