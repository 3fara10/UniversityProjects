import unittest

from repository.file_repository.file_masina_repository import MasinaRepositoryFile
from service.masina_service import MasinaService
from service.search.binary_search import binary_search
from service.search.linear_search import linear_search
from service.sort.comparators import token_comparator, marca_comparator, pret_achizitie_comparator, model_comparator, \
    pret_vanzare_comparator
from service.sort.quicksort import quicksort


class TestMasinaServiceSearch(unittest.TestCase):
    def setUp(self):
        self.file_masini_repository = MasinaRepositoryFile("masini.txt")
        self.masina_service = MasinaService(self.file_masini_repository)

    def tearDown(self):
        print("Test {0} for masina.repository finished with success".format(self._testMethodName))

    def test_search_binary(self):
        # cazul caut masina dupa token
        lista51 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), token_comparator,
                                                    quicksort)
        lista5 = self.masina_service.search(lista51, ('_tokenMasina', '4mq9w00wct'),
                                            binary_search)
        assert (lista5[0].__getattribute__('_tokenMasina') == '4mq9w00wct')

        # cazul caut marca
        lista11 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), marca_comparator,
                                                    quicksort)
        lista1 = self.masina_service.search(lista11, ('_marca', 'Audi'), binary_search)
        assert (lista1[0].__getattribute__('_marca') == 'Audi')

        # cazul caut dupa pretul de achizitie
        lista71 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), pret_achizitie_comparator,
                                                    quicksort)
        lista7 = self.masina_service.search(lista71, ('_pretAchizitie', 1278), binary_search)
        assert (lista7[0].__getattribute__('_pretAchizitie') == 1278)

        # cazul caut masina dupa model
        lista61 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), model_comparator,
                                                    quicksort)
        lista6 = self.masina_service.search(lista61, ('_model', 'Fiesta'),
                                            binary_search)
        assert (lista6[0].__getattribute__('_model') == 'Fiesta')

        # cazul caut masina dupa pretVanzare
        lista21 = self.masina_service.sort_alg_type(self.masina_service.get_all_cars(), pret_vanzare_comparator,
                                                    quicksort)
        lista2 = self.masina_service.search(lista21, ('_pretVanzare', 8993),
                                            binary_search)
        assert (lista2[0].__getattribute__('_pretVanzare') == 8993)

    def test_search_linear(self):
        # cazul caut masina dupa token
        lista5 = self.masina_service.search(self.masina_service.get_all_cars(), ('_tokenMasina', '4mq9w00wct'),
                                            linear_search)
        assert (lista5[0].__getattribute__('_tokenMasina') == '4mq9w00wct')

        # cazul caut marca
        lista1 = self.masina_service.search(self.masina_service.get_all_cars(), ('_marca', 'Audi'), linear_search)
        assert (lista1[0].__getattribute__('_marca') == 'Audi')

        # cazul caut dupa pretul de achizitie
        lista7 = self.masina_service.search(self.masina_service.get_all_cars(), ('_pretAchizitie', 1278), linear_search)
        assert (lista7[0].__getattribute__('_pretAchizitie') == 1278)

        # cazul caut masina dupa model
        lista6 = self.masina_service.search(self.masina_service.get_all_cars(), ('_model', 'Fiesta'),
                                            linear_search)
        assert (lista6[0].__getattribute__('_model') == 'Fiesta')

        # cazul caut masina dupa pretVanzare
        lista2 = self.masina_service.search(self.masina_service.get_all_cars(), ('_pretVanzare', 8993),
                                            linear_search)
        assert (lista2[0].__getattribute__('_pretVanzare') == 8993)
