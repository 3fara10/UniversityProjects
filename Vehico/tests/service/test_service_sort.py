import unittest

from domain.masina import Masina
from exceptions.duplicate_error import DuplicateError
from repository.file_repository.file_masina_repository import MasinaRepositoryFile
from service.masina_service import MasinaService
from service.sort.bubblesort import bubblesort
from service.sort.comparators import marca_model_comparator, marca_model_token_comparator, generic_comparator
from service.sort.quicksort import quicksort


class TestMasinaServiceSort(unittest.TestCase):
    def setUp(self):
        self.file_masini_repository = MasinaRepositoryFile("masini.txt")
        self.masina_service = MasinaService(self.file_masini_repository)

    def tearDown(self):
        print("Test {0} for masina.repository finished with success".format(self._testMethodName))

    def test_sort_basic_comparators_quicksort(self):
        # cazul marca crecator
        lista1 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_marca'),
                                                   quicksort)
        assert (lista1[0].__getattribute__('_marca') == 'Audi')

        # cazul model crecator
        lista3 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_model'), quicksort)
        assert (lista3[0].__getattribute__('_model') == '1Series')

        # cazul tokenMasina crecator
        lista5 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_tokenMasina'), quicksort)
        assert (lista5[0].__getattribute__('_tokenMasina') == '0ibdu3n47t')

        # cazul pretAchizite crecator
        lista7 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_pretAchizitie'),
                                                   quicksort)
        assert (lista7[0].__getattribute__('_pretAchizitie') == 1278)

        # cazul pretVanzare crecator
        lista9 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_pretVanzare'),
                                                   quicksort)
        assert (lista9[0].__getattribute__('_pretVanzare') == 2391)

    def test_sort_complex_comparators_quicksort(self):
        lista1 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), marca_model_comparator,
                                                   quicksort)
        assert (lista1[0].__getattribute__('_tokenMasina') == 'wt98fnpsku')

        # cazul model crecator
        lista3 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), marca_model_token_comparator,
                                                   quicksort)
        assert (lista3[0].__getattribute__('_tokenMasina') == 'at98fnpsku')

    def test_sort_basic_comparators_bubblesort(self):
        # cazul marca crescator
        lista1 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_marca'),
                                                   bubblesort)
        assert (lista1[0].__getattribute__('_marca') == 'Audi')

        # cazul model crecator
        lista3 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_model'), bubblesort)
        assert (lista3[0].__getattribute__('_model') == '1Series')

        # cazul tokenMasina crecator
        lista5 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_tokenMasina'), bubblesort)
        assert (lista5[0].__getattribute__('_tokenMasina') == '0ibdu3n47t')

        # cazul pretAchizite crecator
        lista7 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_pretAchizitie'),
                                                   bubblesort)
        assert (lista7[0].__getattribute__('_pretAchizitie') == 1278)

        # cazul pretVanzare crecator
        lista9 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), generic_comparator('_pretVanzare'),
                                                   bubblesort)
        assert (lista9[0].__getattribute__('_pretVanzare') == 2391)

    def test_sort_complex_comparators_bubblesort(self):
        lista1 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), marca_model_comparator,
                                                   bubblesort)
        assert (lista1[0].__getattribute__('_tokenMasina') == 'wt98fnpsku')

        # cazul model crecator
        lista3 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), marca_model_token_comparator,
                                                   bubblesort)
        assert (lista3[0].__getattribute__('_tokenMasina') == 'at98fnpsku')


