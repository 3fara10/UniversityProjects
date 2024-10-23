class Masina:
    """
    The class required in the problem.
    """

    def __init__(self, marca: str, model: str, token_masina: str, pret_achizitie: int, pret_vanzare: int):
        """
        Initializes a "Masina" type object with the attributes given as parameters.

        Parameters:
            marca:The brand of the car.
            model:The car model.
            token_masina:A unique token identifier for the car.
            pret_achizitie:The purchase price of the car.
            pret_vanzare:The selling price of the car.

        Returns:
            None:

        Raises:
            TypeError: If any of the input parameters are of incorrect types.
            ValueError: If the purchase price or selling price are negative.
        """
        self._marca = marca
        self._model = model
        self._tokenMasina = token_masina
        self._pretAchizitie = pret_achizitie
        self._pretVanzare = pret_vanzare
        self._profit = self._pretVanzare - pret_achizitie

    def __getattribute__(self, __name):
        """
           Retrieves the value of the attribute with the given name.

           Parameters:
               __name (str): The name of the attribute to retrieve.

           Returns:
               The value of the attribute with the given name.

           Raises:
               AttributeError: If the attribute with the given name does not exist.
        """

        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        """
           Sets the value of the attribute with the given name.

           Parameters:
               __name (str): The name of the attribute to set.
               __value: The value to set for the attribute.

           Returns:
               None

           Raises:
               AttributeError: If the attribute with the given name does not exist.
        """

        super().__setattr__(__name, __value)

    def __str__(self):
        """
           Returns a string representation of the object.

           Returns:
               str: A string representation of the object.
        """

        string = str(self.__getattribute__('_marca')) + " " + str(self.__getattribute__(
            '_model')) + " " + str(self.__getattribute__('_tokenMasina')) + " " + str(
            self.__getattribute__('_pretAchizitie')) + " " + str(self.__getattribute__('_pretVanzare'))

        return string
