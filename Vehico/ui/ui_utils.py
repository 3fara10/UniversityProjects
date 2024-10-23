from typing import List

from domain.masina import Masina
from exceptions.empty_list import EmptyList


def print_masina(masini: List[Masina]):
    """
        Prints information about each Masina object in the provided list.

        Parameters:
            masini (List[Masina]): The list of Masina objects to print.

        Returns:
            None

        Raises:
            EmptyList: If the list of Masina objects is empty.
    """
    try:
        if len(masini) != 0:
            for masina in masini:
                print(to_string_masina(masina) + "\n")
        else:
            raise EmptyList
    except EmptyList:
        print("The list of cars is empty!")


def to_string_masina(masina: Masina):
    """
       Converts a Masina object to a string representation.

       Parameters:
           masina (Masina): The Masina object to convert to a string.

       Returns:
           str: A string representation of the Masina object.
    """

    string = "Marca masinii: " + masina.__getattribute__(
        '_marca') + "\n" + "Modelul masinii: " + masina.__getattribute__('_model') + "\n" + "Token Masina: " + str(
        masina.__getattribute__('_tokenMasina')) + "\n" + "Pretul de achizitie al masinii: " + str(
        masina.__getattribute__('_pretAchizitie')) + "\n" + "Pretul de vanzare al masinii:  " + str(
        masina.__getattribute__('_pretVanzare'))

    return string
