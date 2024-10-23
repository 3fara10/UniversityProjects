from typing import Tuple, List

from domain.entity import Entity
from domain.masina import Masina


def linear_search(lista: List[Entity], searching_criteria: Tuple[str, any]):
    """
    Perform classic linear search on a list of cars based on a specified attribute and value,
    and return the list of cars that meet the search criteria.

    Parameters:
        lista (List[Entity]): The list of cars.
        searching_criteria (Tuple[str, any]): Tuple containing attribute name and value to search for.

    Returns:
        List[Entity]: A list of cars that meet the search criteria.
    """
    attribute, value = searching_criteria
    found_lista = []

    for masina in lista:
        if getattr(masina, attribute) == value:
            found_lista.append(masina)

    return found_lista