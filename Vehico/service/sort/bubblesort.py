from typing import List, Callable

from domain.entity import Entity


def bubblesort(lista: List[Entity], comparator: Callable):
    """
    Sorts the list of cars using the bubble sort algorithm based on the provided comparator function.

    Parameters:
        lista (List[Entity]): The list of cars to be sorted.
        comparator (Callable): The comparator function used for comparing two cars.

    Returns:
        lista:The sorted list of entities.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparator(lista[j], lista[j + 1]) > 0:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista
