from service.masina_service import MasinaService
from service.sort.comparators import generic_comparator
from service.sort.quicksort import quicksort
from ui.command import Command
from ui.ui_utils import print_masina


class SortModelMasina(Command):
    def __init__(self, masina_service: MasinaService):
        self.__masina_service = masina_service

    def execute(self):
        print_masina(
            self.__masina_service.sort_alg_type(self.__masina_service.get_all_cars(), generic_comparator('_model'), quicksort))

    def get_help(self):
        return "Sort the cars by model"
