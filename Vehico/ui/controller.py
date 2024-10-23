from exceptions.not_found_exception import NotFoundException
from exceptions.validation_exception import ValidationException
from service.masina_service import MasinaService
from ui.commands.addmasina import AddMasinaCommand
from ui.commands.analyse_time_complexity import AnalyseTimeComplexity
from ui.commands.printallmasini import PrintAllMasini
from ui.commands.search_marca import SearchMarcaMasina
from ui.commands.search_model import SearchModelMasina
from ui.commands.search_pret_achizitie import SearchPretAchizitieMasina
from ui.commands.search_pret_vanzare import SearchPretVanzareMasina
from ui.commands.search_token import SearchTokenMasina
from ui.commands.sort_marca import SortMarcaMasina
from ui.commands.sort_marca_model import SortMarcaModel
from ui.commands.sort_marca_model_token import SortMarcaModelToken
from ui.commands.sort_model import SortModelMasina
from ui.commands.sort_pret_achizitie import SortPretAchizitie
from ui.commands.sort_pret_vanzare import SortPretVanzare
from ui.commands.sort_profit import SortProfit
from ui.commands.sort_token import SortTokenMasina


class Controller:
    def __init__(self, masini_service: MasinaService):
        """
            Initializes a CommandProcessor object with a MasinaService.

            Parameters:
                masini_service (MasinaService): The MasinaService object to be used by the CommandProcessor.

            Returns:
                None
        """
        self.__commands = [
            AddMasinaCommand(masini_service),
            PrintAllMasini(masini_service),
            SearchTokenMasina(masini_service),
            SearchMarcaMasina(masini_service),
            SearchModelMasina(masini_service),
            SearchPretAchizitieMasina(masini_service),
            SearchPretVanzareMasina(masini_service),
            SortTokenMasina(masini_service),
            SortMarcaMasina(masini_service),
            SortModelMasina(masini_service),
            SortPretVanzare(masini_service),
            SortPretAchizitie(masini_service),
            SortProfit(masini_service),
            SortMarcaModel(masini_service),
            SortMarcaModelToken(masini_service),
            AnalyseTimeComplexity(masini_service)

        ]

    def run(self):
        while True:
            """
               Runs the command processor until the user decides to exit.

               Returns:
                   None
            """

            self.print_help()
            command = self.read_command()
            if command == 0:
                break
            if len(self.__commands) < command:
                print("Command does not exist")
                continue
            try:
                self.__commands[command - 1].execute()
            except ValidationException as e:
                print("Invalid field: " + e.get_field_name())
            except NotFoundException:
                print("Entity not found!")

    def read_command(self):
        """
            Reads and returns a command entered by the user.

            Returns:
                int: The integer representing the command entered by the user.
        """

        number_str = input("Enter command: ")
        try:
            return int(number_str)
        except:
            print("Invalid command")

    def print_help(self):
        """
           Prints the available commands and their descriptions.

           Returns:
               None
        """

        print()
        print("0 -- Exit")
        for i, command in enumerate(self.__commands):
            print(str(i + 1) + " -- " + command.get_help())
