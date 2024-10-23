from typing import List

from domain.masina import Masina
from exceptions.not_found_exception import NotFoundException


class GenericRepository:
    def __init__(self, entity=Masina):
        """
            Initializes a Repository object with an optional entity type.

            Parameters:
                entity: The type of entity to be stored in the repository. Defaults to Masina.

            Returns:
                None
        """

        self.__all_entities: List[entity] = []

    def add(self, entity):
        """
           Adds an entity to the repository.

           Parameters:
               entity: The entity to be added to the repository.

           Returns:
               None
        """

        self.__all_entities.append(entity)

    def get_all(self):
        """
          Retrieves all entities stored in the repository.

          Returns:
              List: A list of all entities stored in the repository.
        """
        return self.__all_entities

    # we use them for file_masina_repository

    # SA LE MODIFIC,sa fie generice!!!
    def find_by_token(self, token: str):
        """
           Finds an entity in the repository by its token.

           Parameters:
               token (str): The token of the entity to find.

           Returns:
               Masina: The entity with the specified token.

           Raises:
               NotFoundException: If no entity with the specified token is found.
        """
        for entity in self.__all_entities:
            if getattr(entity, '_tokenMasina') == token:
                return entity
        raise NotFoundException

    def update(self, entity):
        """
            Updates an entity in the repository.

            Parameters:
                entity: The entity to be updated in the repository.

            Returns:
                None

            Raises:
                NotFoundException: If the entity to be updated is not found in the repository.
        """
        token = getattr(entity, '_tokenMasina')
        existing_entity = self.find_by_token(token)
        setattr(existing_entity, '_marca', getattr(entity, '_marca'))
        setattr(existing_entity, '_marca', getattr(entity, '_marca'))
        setattr(existing_entity, '_tokenMasina', getattr(entity, '_tokenMasina'))
        setattr(existing_entity, '_pretAchizitie', getattr(entity, '_pretAchizitie'))
        setattr(existing_entity, '_pretVanzare', getattr(entity, '_pretVanzare'))

    def delete_by_token(self, token: str):
        """
           Deletes an entity from the repository based on its token.

           Parameters:
               token (str): The token of the entity to be deleted.

           Returns:
               None

           Raises:
               NotFoundException: If no entity with the specified token is found in the repository.
        """
        self.__all_entities.remove(self.find_by_token(token))

    def delete(self, entity):
        """
           Deletes an entity from the repository.

           Parameters:
               entity: The entity to be deleted from the repository.

           Returns:
               None

           Raises:
               ValueError: If the specified entity is not found in the repository.
           """
        self.__all_entities.remove(entity)
