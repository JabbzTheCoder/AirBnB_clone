#!/usr/bin/python3
'''Entrance of the program'''
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
    }

    def do_create(self, arg):
        new_instance = None
       
        """Create a new instance of a specified class."""
        if not arg:
            print("** class name missing **")
            return

        # Check if the class exists in the dictionary.
        if arg not in classes:
            print("** class doesn't exist **")
            return

        # Dynamically instantiate the class.
        new_instance = self.classes[arg]()
        if new_instance:
            new_instance.save()
            print(new_instance.id)
    
    def do_show(self, arg):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program at end of file (Ctrl+D)"""
        print("")  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
