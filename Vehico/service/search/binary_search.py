from typing import List, Tuple

from domain.entity import Entity
from domain.masina import Masina


def binary_search(lista: List[Entity], searching_criteria: Tuple[str, str]):
    """
    Perform binary search on a list of lista based on a specified key function
    and return the lista that meet the search criteria.

    Parameters:
        lista (List[Entity]): Sorted list of entities(ascending).
        searching_criteria (Tuple[str, any]): Tuple containing attribute name and value to search for.

    Returns:
        List[Entity]: A list of entities that meet the search criteria.
    """
    attribute, value = searching_criteria
    found_lista = []
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        obj = lista[mid]
        if getattr(obj, attribute) == value:
            # If the criteria match, expand search to both sides
            found_lista.append(obj)
            left, right = mid - 1, mid + 1
            while left >= 0 and getattr(lista[left], attribute) == value:
                found_lista.append(lista[left])
                left -= 1
            while right < len(lista) and getattr(lista[right], attribute) == value:
                found_lista.append(lista[right])
                right += 1
            return found_lista
        elif getattr(obj, attribute) < value:
            low = mid + 1
        else:
            high = mid - 1

    return found_lista
