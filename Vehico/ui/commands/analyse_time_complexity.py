from service.masina_service import MasinaService
from service.search.binary_search import binary_search
from service.search.linear_search import linear_search
from service.sort.bubblesort import bubblesort
from service.sort.quicksort import quicksort
from ui.command import Command


class AnalyseTimeComplexity(Command):
    def __init__(self, masina_service: MasinaService):
        self.__masina_service = masina_service

    def execute(self):
        print("The execution time for QuickSort is:", self.__masina_service.analyze_time_complexity(quicksort))
        print("The execution time for BubbleSort is:", self.__masina_service.analyze_time_complexity(bubblesort))

        print("The execution time for BinarySearch is:",self.__masina_service.analyze_time_complexity(binary_search))
        print("The execution time for SequentialSearch is:",self.__masina_service.analyze_time_complexity(linear_search))
    def get_help(self):
        return "Analizeaza complexitatile functiilor de sortare si cautare."
