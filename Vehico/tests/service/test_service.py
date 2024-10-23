import unittest

from domain.masina import Masina
from exceptions.duplicate_error import DuplicateError
from repository.file_repository.file_masina_repository import MasinaRepositoryFile
from service.masina_service import MasinaService


class TestMasinaService(unittest.TestCase):
    def setUp(self):
        self.file_masini_repository = MasinaRepositoryFile("masini.txt")
        self.masina_service = MasinaService(self.file_masini_repository)

    def tearDown(self):
        print("Test {0} for masina.repository finished with success".format(self._testMethodName))

    def test_add(self):
        self.masina2 = Masina("Chevrolet", "Silverado", "q2dip9g0uy", 7693, 7494)
        with self.assertRaises(DuplicateError):
            self.masina_service.add(self.masina2)

    def test_is_token_unique(self):
        assert(self.masina_service.is_token_unique("k6xeulillw")==True)
        assert (self.masina_service.is_token_unique("k6xeulilfw") == False)