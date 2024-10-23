from domain.masina import Masina
from exceptions.duplicate_error import DuplicateError
from service.masina_service import MasinaService
from ui.command import Command


class AddMasinaCommand(Command):
    def __init__(self, masina_service: MasinaService):
        self.__masina_service = masina_service

    def execute(self):
        try:
            marca = self.read_str("Insereaza marca: ",
                                  "Marca trebuie sa fie un sir de caractere,te rog incearca din nou: ")
            model = self.read_str("Insereaza model: ",
                                  "Modelul trebuie sa fie un sir de caractere,te rog incearca din nou: ")
            token_masina = self.read_str("Insereaza token-ul masinii: ",
                                         "Token-ul trebuie sa fie un sir de caractere,te rog incearca din nou: ")
            pret_achizitie = self.read_int("Insereaza pretul de achizitie al masinii: ",
                                           "Pretul de achizitie trebuie sa fie un numar,te rog incearca din nou: ")
            pret_vanzare = self.read_int("Insereaza Pretul de vanzare al masinii: ",
                                         "Pretul de vanzare trebuie sa fie un numar,te rog incearca din nou: ")
            self.__masina_service.add(Masina(marca, model, token_masina, pret_achizitie, pret_vanzare))
            print("Masina a fost adaugata cu succes")
        except DuplicateError:
            print("The car already exists.")

    def get_help(self):
        return "Add a new car"
