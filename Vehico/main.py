import unittest

from domain.masina import Masina
from repository.generic_repository import GenericRepository
from service.masina_service import MasinaService
from ui.controller import Controller

masini_repository = GenericRepository(Masina)
masini_service = MasinaService(masini_repository)

controller = Controller(masini_service)


controller.run()
unittest.main()

