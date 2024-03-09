#!/usr/bin/pyhton3
"""Module for TestHBNBcommand class"""


import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
import os
import re
import sys


class TestHBNBCommand(unittest.TestCase):
    """"""
    def setUp(self):
        self.cmd = HBNBCommand()
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_create(self):
        with patch('builtins.input', return_value="create BaseModel") as mock_input:
            self.cmd.onecmd("create BaseModel")

        out = self.mock_stdout.getvalue()
        self.assertIn("BaseMode", out)
        self.assertRegex(out, r'\b[0-9a-f-]{36}\b')

    def test_show(self):
        with patch('builtins.input', return_value="show BaseModel") as mock_input:
            self.cmd.onecmd("show BaseModel")
        self.assertIn("** instance id missing **\n", self.mock_stdout.getvalue())

    def classes(self):
        """Returns a list of available class names."""
        return [classname for classname in dir() if re.match(r"Test\w+Command", classname)]

    def assert_help_output(self, command, expected_output):
        """Asserts that the help command produces the expected output."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("help {}".format(command))
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def assert_do_command(self, command, expected_output, expected_key):
        """Asserts that a command produces the expected output and key."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)
            output = mock_stdout.getvalue()
            if expected_output:
                self.assertIn(expected_output, output)
            if expected_key:
                matches = re.search(r'\[([^]]*)\]', output)
                if matches:
                    key = matches.group(1)
                    self.assertEqual(key, expected_key)

    def test_help(self):
        self.assert_help_output("help", """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
""")

    def test_help_EOF(self):
        self.assert_help_output("help EOF", 'Handles End Of File character.\n\n')

    def test_help_quit(self):
        self.assert_help_output("help quit", 'Exits the program.\n\n')

    def test_help_create(self):
        self.assert_help_output("help create", 'Creates an instance.\n\n')

    def test_help_show(self):
        self.assert_help_output("help show", 'Prints the string representation of an instance.\n\n')

    def test_help_destroy(self):
        self.assert_help_output("help destroy", 'Deletes an instance based on the class name and id.\n\n')

    def test_help_all(self):
        self.assert_help_output("help all", 'Prints all string representation of all instances.\n\n')

    def test_help_count(self):
        self.assert_help_output("help count", 'Counts the instances of a class.\n\n')

    def test_help_update(self):
        self.assert_help_output("help update", 'Updates an instance by adding or updating attribute.\n\n')


if __name__ == '__main__':
    unittest.main()
