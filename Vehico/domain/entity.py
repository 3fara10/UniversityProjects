from typing import TypeVar

T = TypeVar('T')


class Entity:
    """
    Written for functions parameters.
    """

    def __init__(self, identifier: str, value: T):
        """
            Initializes an Entity object with the provided identifier and value.

            Parameters:
                identifier (str): A string representing the identifier of the entity.
                value (T): The value associated with the entity.

            Returns:
                None
        """

        self.identifier = identifier
        self.value = value
