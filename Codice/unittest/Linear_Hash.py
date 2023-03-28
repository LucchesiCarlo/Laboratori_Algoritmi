import random
import unittest
from Codice.Open_Hash import *


class linear_hash_usage(unittest.TestCase):

    def setUp(self):
        self.__linear_hash = open_hash(7, hash_type.Linear)

        self.__linear_hash.insert(6)
        self.__linear_hash.insert(3)
        self.__linear_hash.insert(10)

    def test_insert(self):
        self.assertEqual(self.__linear_hash.array[6], "6", msg = "Non inserisce correttamente il valore.")
        self.assertEqual(self.__linear_hash.array[3], "3", msg = "Non inserisce correttamente il valore.")
        self.assertEqual(self.__linear_hash.array[4], "10", msg = "L'esplorazione lineare non funziona.")

        with self.assertRaises(ValueError, msg = "Non si accorge che vengono inseriti 2 valori uguali."):
            self.__linear_hash.insert(6)

    def test_search(self):
        self.assertEqual(self.__linear_hash.search(1), "NIL", msg = "Non inizializza correttamente la tavola hash.")
        self.assertEqual(self.__linear_hash.search(6), 6, msg = "Non risce a trovare l'elemento nella tavola.")
        self.assertEqual(self.__linear_hash.search(10), 4, msg = "Non riesce a trovare un elemento usando l'esplorazione lineare.")
    
    def test_delete(self):
        self.assertFalse(self.__linear_hash.delete(34), msg = "Non riconosce che l'elemento non è presente.")
        self.assertTrue(self.__linear_hash.delete(6), msg = "Non segnala l'eliminazione.")
        self.assertTrue(self.__linear_hash.delete(10), msg = "Non segnala l'eliminazione seguendo l'esplorazione lineare.")

        self.assertEqual(self.__linear_hash.array[4], "DEL", msg = "Non inserisce il flag DEL correttamente.")

        self.__linear_hash.insert(10)
        self.assertEqual(self.__linear_hash.search(10), 4, msg = "Non riesce ad inserire dopo un elemento rimosso.")
        self.__linear_hash.delete(3)
        self.assertEqual(self.__linear_hash.search(10), 4, msg = "Non riesce a trovare l'elemento dopo in una ispezione dopo una rimozione.")

class different_linear_hash_usage(unittest.TestCase):

    def setUp(self):
        self.__new_linear_hash = open_hash(11, hash_type.Linear, 7)
        self.__new_linear_hash.insert(4)
        self.__new_linear_hash.insert(15)


    def test_insert(self):
        self.assertEqual(self.__new_linear_hash.array[4], "4", msg = "Non inserisce correttamente.")
        self.assertEqual(self.__new_linear_hash.array[0], "15", msg = "Non segue l'esplorazione lineare.")

    def test_search(self):
        self.assertEqual(self.__new_linear_hash.search(1), "NIL", msg = "Non inizializza correttamente la tavola hash.")
        self.assertEqual(self.__new_linear_hash.search(4), 4, msg = "Non funziona la ricerca")
        self.assertEqual(self.__new_linear_hash.search(15), 0, msg = "Non funziona l'esplorazione durante la ricerca")

    def test_delete(self):
        self.assertFalse(self.__new_linear_hash.delete(467), msg = "Non riconosce che l'elemento non si trova all'interno dell'insieme.")
        self.assertTrue(self.__new_linear_hash.delete(4), msg = "Non rimuove l'elemento.")

        self.assertEqual(self.__new_linear_hash.array[4], "DEL", msg = "Il flag DEL non viene inserito.")
        self.assertEqual(self.__new_linear_hash.search(15), 0, msg = "L'esplorazione lineare non funziona dopo una rimozione.")

class linear_population(unittest.TestCase):

    def test_population(self):
        linear_hash = open_hash(11, hash_type.Linear)
        elements = [1, 33, 97, 25, 890, 12, 9, 11, 74, 9834, 1900]
        for i in elements:
            linear_hash.insert(i)

        self.assertFalse(("NIL" in linear_hash.array), msg = "La tabella hash non si è riempita.")
    
    def test_different_population(self):
        linear_hash = open_hash(11, hash_type.Linear, 31)
        elements = [1, 33, 97, 25, 890, 12, 9, 11, 74, 9834, 1900]
        for i in elements:
            linear_hash.insert(i)

        self.assertFalse(("NIL" in linear_hash.array), msg = "La tabella hash non si è riempita.")
