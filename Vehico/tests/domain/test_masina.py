import unittest

from domain.masina import Masina


class TestMasina(unittest.TestCase):
    """
    This is where the methods of the Masina class are tested.
    """

    def setUp(self):
        self.masina: Masina = Masina("Chevrolet", "Silverado", "wjckx944uj", 7693, 7494)

    def tearDown(self):
        print("Test {0} for domain.book finished with success".format(self._testMethodName))

    def test_get_marca(self):
        self.assertEqual(getattr(self.masina, '_marca'), "Chevrolet")
        self.assertNotEqual(getattr(self.masina, '_marca'), "x")

    def test_get_model(self):
        self.assertEqual(getattr(self.masina, '_model'), "Silverado")
        self.assertNotEqual(getattr(self.masina, '_model'), "x")

    def test_get_token(self):
        self.assertEqual(getattr(self.masina, '_tokenMasina'), "wjckx944uj")
        self.assertNotEqual(getattr(self.masina, '_tokenMasina'), "x")

    def test_get_pret_achizitie(self):
        self.assertEqual(getattr(self.masina, '_pretAchizitie'), 7693)
        self.assertNotEqual(getattr(self.masina, '_pretAchizitie'), 0)

    def test_get_pret_vanzare(self):
        self.assertEqual(getattr(self.masina, '_pretVanzare'), 7494)
        self.assertNotEqual(getattr(self.masina, '_pretVanzare'), -1)

    def test_set_marca(self):
        setattr(self.masina, '_marca', "Chevrolett")
        self.assertEqual(getattr(self.masina, '_marca'), "Chevrolett")

    def test_set_model(self):
        setattr(self.masina, '_model', "Audi")
        self.assertEqual(getattr(self.masina, '_model'), "Audi")

    def test_set_token(self):
        setattr(self.masina, '_tokenMasina', "xxxxxx")
        self.assertEqual(getattr(self.masina, '_tokenMasina'), "xxxxxx")

    def test_set_pret_achizitie(self):
        setattr(self.masina, '_pretAchizitie', 1000)
        self.assertEqual(getattr(self.masina, '_pretAchizitie'), 1000)

    def test_set_pret_vanzare(self):
        setattr(self.masina, '_pretVanzare', 9999)
        self.assertEqual(getattr(self.masina, '_pretVanzare'), 9999)
