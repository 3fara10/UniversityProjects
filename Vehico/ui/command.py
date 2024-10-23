import re
from abc import ABC, abstractmethod

from exceptions.string_exception import StringException


class Command(ABC):
    @abstractmethod
    def execute(self):
        """
           Executes the command.

           Returns:
               None
        """
        pass

    @abstractmethod
    def get_help(self):
        """
           Returns a help message for the command.

           Returns:
               str: A help message describing the command.
        """
        pass

    def read_int(self, prompt: str, retry_prompt: str):
        """
           Reads and returns an integer input from the user.

           Parameters:
               prompt (str): The prompt to display to the user.
               retry_prompt (str): The prompt to display if the input is invalid.

           Returns:
               int: The integer entered by the user.

           Raises:
               ValueError: If the input cannot be converted to an integer.
        """

        number_str = input(prompt)
        while True:
            try:
                return int(number_str)
            except:
                number_str = input(retry_prompt)

    def read_str(self, prompt: str, retry_prompt: str):
        """
            Reads and returns a string input from the user.

            Parameters:
                prompt (str): The prompt to display to the user.
                retry_prompt (str): The prompt to display if the input is invalid.

            Returns:
                str: The string entered by the user.

            Raises:
                StringException: If the input contains characters other than alphanumeric characters, underscores, or hyphens.
        """

        new_string = input(prompt)
        while True:
            try:
                if re.match("^[A-Za-z0-9_-]*$", new_string):
                    return str(new_string)
                else:
                    raise StringException
            except StringException:
                new_string = input(retry_prompt)
