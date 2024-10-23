from service.masina_service import MasinaService
from service.search.binary_search import binary_search
from ui.command import Command
from ui.ui_utils import print_masina


class SearchMarcaMasina(Command):
    def __init__(self, masina_service: MasinaService):
        self.__masina_service = masina_service

    def execute(self):
        marca_masina = self.read_str("Insereaza marca masinii: ",
                                     "Marca trebuie sa fie un sir de caractere,te rog incearca din nou: ")
        print_masina(self.__masina_service.search(self.__masina_service.get_all_cars(), ('_marca', marca_masina),
                                                  binary_search))

    def get_help(self):
        return "Search the car after its marca."
