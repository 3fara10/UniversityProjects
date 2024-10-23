from typing import List, Callable

from domain.entity import Entity
from domain.masina import Masina


def quicksort(lista: List[Entity], comparator: Callable):
    """
       Sorts a list of entities using the quicksort algorithm.

       Parameters:
           lista (List[Entity]): The list of entities to be sorted.
           comparator (Callable[[Entity, Entity], int]): A comparator function that takes two Entity objects as input and returns an integer:
               - Negative if the first entity should come before the second entity.
               - Zero if the entities are considered equal in terms of sorting.
               - Positive if the first entity should come after the second entity.

       Returns:
           List[Entity]: The sorted list of entities.
    """
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if comparator(x, pivot) < 0]
    middle = [x for x in lista if comparator(x, pivot) == 0]
    right = [x for x in lista if comparator(x, pivot) > 0]
    return quicksort(left, comparator) + middle + quicksort(right, comparator)
