from service.masina_service import MasinaService
from ui.command import Command
from ui.ui_utils import print_masina

class PrintAllMasini(Command):
    def __init__(self, masina_service: MasinaService):
        self.__masina_service = masina_service

    def execute(self):
        print_masina(self.__masina_service.get_all_cars())

    def get_help(self):
        return "Print all cars"
