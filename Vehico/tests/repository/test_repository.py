import unittest

from domain.masina import Masina
from repository.generic_repository import GenericRepository


class TestBookRepostiory(unittest.TestCase):
    def setUp(self):
        self.masina_repository = GenericRepository(Masina)
        self.masina1 = Masina("Chevrolet", "Malibu", "fuvjx4hgj4", 4236, 4199)
        self.masina2 = Masina("Chevrolet", "Silverado", "wjckx944uj", 7693,  7494)
        self.masina3 = Masina("Ford", "Transit", "iumj7qirqq", 3214, 9045)
        self.masina4 = Masina("Volvo", "850", "bv55fq9ewq", 2640, 13400)
        self.masina_repository.add(self.masina2)
        self.masina_repository.add(self.masina3)
        self.masina_repository.add(self.masina4)

    def tearDown(self):
        print("Test {0} for masina.repository finished with success".format(self._testMethodName))

    def test_add(self):
        self.assertIn(self.masina2, self.masina_repository.get_all())
        self.assertIsInstance(self.masina2, Masina)

    def test_find_by_token(self):
        current_token = self.masina2.__getattribute__('_tokenMasina')
        self.assertIs(self.masina_repository.find_by_token(current_token), self.masina2)

    def test_delete_by_token(self):
        self.masina_repository.delete_by_token("wjckx944uj")
        self.assertIsNot(self.masina2, self.masina_repository.get_all())

    def test_get_all(self):
        self.assertIn(self.masina2, self.masina_repository.get_all())

    def test_update(self):
        self.masina4 = Masina("Vooolvo", "850", "bv55fq9ewq", 2640, 13400)
        self.masina_repository.update(self.masina4)
        self.assertEqual(getattr(self.masina4, '_marca'), "Vooolvo")
