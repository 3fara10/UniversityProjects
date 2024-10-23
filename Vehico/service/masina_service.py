import time
from typing import List, Callable, Tuple

from domain.entity import Entity
from domain.masina import Masina
from exceptions.duplicate_error import DuplicateError
from repository.generic_repository import GenericRepository
from service.complexity import generate_car_objects_list
from service.search.binary_search import binary_search
from service.search.linear_search import linear_search
from service.sort.bubblesort import bubblesort
from service.sort.comparators import generic_comparator
from service.sort.quicksort import quicksort

class MasinaService:
    def __init__(self, masina_repository: GenericRepository):
        """
           Initializes a CarService object with a Masina repository.

           Parameters:
               masina_repository (GenericRepository): The repository for storing Masina objects.

           Returns:
               None
        """
        self._masina_repository = masina_repository

    def add(self, car: Masina):
        """
           Adds a Masina object to the repository.

           Parameters:
               car (Masina): The Masina object to be added to the repository.

           Returns:
               None
        """
        if self.is_token_unique(car.__getattribute__('_tokenMasina')):
            self._masina_repository.add(car)
        else:
            raise DuplicateError

    """def export_data_graph_excel(self):
        algorithms = ['Quicksort', 'Bubblesort', 'BinarySearch', 'SequentialSearch']
        execution_times = [
            self.analyze_time_complexity(quicksort),
            self.analyze_time_complexity(bubblesort),
            self.analyze_time_complexity(binary_search),
            self.analyze_time_complexity(linear_search)
        ]
        plt.bar(algorithms, execution_times, color='blue')
        plt.xlabel('Algorithms')
        plt.ylabel('Execution Time')
        plt.title('Execution Time Comparison')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig('execution_times_graph.png')  # Save the plot as an image
        plt.show()
    """
    @staticmethod
    def analyze_time_complexity(function: Callable[[List[Entity]], List[Entity]]):
        """
        Analyzes the execution time of a given sorting function.

        Parameters:
        - lista (List[Entity]): The list of entities to be sorted.
        - comparator (Callable): The comparator function used for sorting.

        Returns:
        - None

        Prints:
        - Execution time of the sorting function in seconds.
        """
        lista = generate_car_objects_list(100)
        start_time = time.time()
        if function == quicksort or function == bubblesort:
            sorted_cars = function(lista, generic_comparator('_tokenMasina'))
        elif function == linear_search or function == binary_search:
            the_searched_cars = function(lista, ('_tokenMasina', lista[55].__getattribute__('_tokenMasina')))

        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time

    def get_all_cars(self):
        """
           Retrieves all Masina objects from the repository.

           Returns:
               List[Masina]: A list containing all Masina objects stored in the repository.
           Raises:
                EmptyList:If lista:List[Entity] is empty.
        """
        return self._masina_repository.get_all()

    @staticmethod
    def sort_alg_type(lista: List[Entity], comparator: Callable,
                      sorting_function: Callable[[List[Entity]], List[Entity]]):
        """
            Sorts a list of entities based on a specified comparator and sorting function.

            Parameters:
                lista (List[Entity]): The list of entities to be sorted.
                comparator (Callable): The comparator function used for sorting.
                sorting_function (Callable[[List[Entity]], List[Entity]]): The sorting function to be applied.

            Returns:
                List[Entity]: The sorted list of entities.

            Raises:
                EmptyList:If lista:List[Entity] is empty.
        """
        sorted_cars = sorting_function(lista, comparator)
        return sorted_cars

    @staticmethod
    def search(lista: List[Entity], search_criteria: Tuple[str, str],
               searching_function: Callable[[List[Entity]], List[Entity]]):
        """
            Searches for entities in a list based on specified search criteria and searching function.

            Parameters:
                lista (List[Entity]): The list of entities to be searched.
                search_criteria (Tuple[str, str]): The criteria for searching.
                searching_function (Callable[[List[Entity]], List[Entity]]): The searching function to be applied.

            Returns:
                List[Entity]: A list of entities that meet the specified search criteria.

            Raises:
                EmptyList:If lista:List[Entity] is empty.
        """
        the_searched_cars = searching_function(lista, search_criteria)
        return the_searched_cars

    def is_token_unique(self, token: str):
        """
        Checks if the token is unique within the provided list of cars.

        Parameters:
            token (str): The token to check for uniqueness.

        Returns:
            bool: True if the token is unique

        Raise:
            DuplicateError otherwise.
        """
        for masina in self._masina_repository.get_all():
            if getattr(masina, '_tokenMasina') == token:
                return False
        return True
