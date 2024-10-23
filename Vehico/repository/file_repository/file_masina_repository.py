from domain.masina import Masina
from repository.generic_repository import GenericRepository


class MasinaRepositoryFile(GenericRepository):
    def __init__(self, filename):
        """
         Initializes a FileMasinaRepository object.

         Parameters:
             filename (str): The name of the file to read from/write to.

         Returns:
             None
        """
        super().__init__()
        self._fileName = filename
        self.readFile()

    def add(self, masina: Masina):
        """
           Adds a Masina object to the repository and writes it to the file.

           Parameters:
               masina (Masina): The Masina object to add to the repository and write to the file.

           Returns:
               None
           """
        super().add(masina)
        self.writeinFile()

    def update(self, masina: Masina):
        """
            Updates a Masina object in the repository and modifies the file accordingly.

            Parameters:
                masina (Masina): The Masina object to update in the repository and file.

            Returns:
                None
        """
        super().update(masina)
        self.modifyFile()

    def delete_by_id(self, token: str):
        """
          Deletes a Masina object from the repository based on its token and updates the file.

          Parameters:
              token (str): The token of the Masina object to delete.

          Returns:
              None

          Raises:
              NotFoundException: If no Masina object with the specified token is found.
        """
        super().delete_by_token(token)
        self.writeinFile()

    def find_by_id(self, token: str):
        """
            Finds a Masina object in the repository based on its token.

            Parameters:
                token (str): The token of the Masina object to find.

            Returns:
                Masina: The Masina object with the specified token.

            Raises:
                NotFoundException: If no Masina object with the specified token is found.
        """
        masina = super().find_by_token(token)
        return masina

    def readFile(self):
        """
            Reads Masina objects from the file and adds them to the repository.

            Returns:
                None
        """
        f = open(self._fileName, "r")
        line = f.readline().strip("\n")
        while line != "":
            attr = line.split(" ")
            marca_masina = attr[0]
            model_masina = attr[1]
            token_masina = attr[2]
            pret_achizitie = int(attr[3])
            pret_vanzare = int(attr[4])
            masina = Masina(marca_masina, model_masina, token_masina, pret_achizitie, pret_vanzare)
            super().add(masina)
            line = f.readline().strip("\n")
        f.close()

    def writeinFile(self):
        """
            Writes all Masina objects from the repository to the file.

            Returns:
                None
        """
        f = open(self._fileName, "w")
        masinas = super().get_all()
        for masina in masinas:
            masina_marca = masina.__getattribute__('_marca')
            masina_model = masina.__getattribute__('_model')
            masina_token = masina.__getattribute__('_tokenMasina')
            masina_pretachizite = masina.__getattribute__('_pretAchizitie')
            masina_pretvanzare = masina.__getattribute__('_pretVanzare')
            line = Masina(masina_marca, masina_model, masina_token, masina_pretachizite, masina_pretvanzare)
            f.write(line.__str__())
        f.close()

    def modifyFile(self):
        """
            Modifies the file with the updated Masina objects from the repository.

            Returns:
                None
        """
        f = open(self._fileName, "w")
        masinas = super().get_all()
        for masina in masinas:
            masina_marca = masina.__getattribute__('_marca')
            masina_model = masina.__getattribute__('_model')
            masina_token = masina.__getattribute__('_tokenMasina')
            masina_pretachizite = masina.__getattribute__('_pretAchizitie')
            masina_pretvanzare = masina.__getattribute__('pretVanzare')
            line = Masina(masina_marca, masina_model, masina_token, masina_pretachizite, masina_pretvanzare)
            f.write(line.__str__())
        f.close()

    def __appendToFile(self, masina: Masina):
        """
            Appends a Masina object to the file.

            Parameters:
                masina (Masina): The Masina object to append to the file.

            Returns:
                None
        """
        try:
            current_file = open(self._fileName, "a")
        except IOError:
            # file not exist
            return
        line = str(masina.__getattribute__('_marca')) + "," + str(masina.__getattribute__('_model')) + "," + str(
            masina.__getattribute__('_tokenMasina')) + "," + str(masina.__getattribute__('_pretAchizitie')) + "," + str(
            masina.__getattribute__('_pretVanzare'))
        current_file.write("\n")
        current_file.write(line)
        current_file.close()
