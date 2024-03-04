#!/usr/bin/env python3
"""entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the cmd for 'quit' as an arg to cmd
        """
        return True

    def do_EOF(self, line):
        """Exits the program cleanly
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
