from service.masina_service import MasinaService
from service.sort.comparators import marca_model_token_comparator
from service.sort.quicksort import quicksort
from ui.command import Command
from ui.ui_utils import print_masina


class SortMarcaModelToken(Command):
    def __init__(self, masina_service: MasinaService):
        self.__masina_service = masina_service

    def execute(self):
        print_masina(
            self.__masina_service.sort_alg_type(self.__masina_service.get_all_cars(), marca_model_token_comparator, quicksort))

    def get_help(self):
        return "sort the cars by brand and in case of equality, by model and if it's equality,by token"