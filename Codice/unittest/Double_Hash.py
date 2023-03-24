import unittest
from Codice.Open_Hash import *


class double_hash_usage(unittest.TestCase):

    def setUp(self):
        self.__double_hash = open_hash(7, hash_type.Double)

        self.__double_hash.insert(6)
        self.__double_hash.insert(3)
        self.__double_hash.insert(10)

    def test_insert(self):
        self.assertEqual(self.__double_hash.array[6], 6, msg = "Non inserisce correttamente il valore.")
        self.assertEqual(self.__double_hash.array[3], 3, msg = "Non inserisce correttamente il valore.")
        self.assertEqual(self.__double_hash.array[1], 10, msg = "L'esplorazione doppia non funziona.")

        with self.assertRaises(ValueError, msg = "Non si accorge che vengono inseriti 2 valori uguali."):
            self.__double_hash.insert(6)

    def test_search(self):
        self.assertEqual(self.__double_hash.search(1), "NIL", msg = "Non inizializza correttamente la tavola hash.")
        self.assertEqual(self.__double_hash.search(6), 6, msg = "Non risce a trovare l'elemento nella tavola.")
        self.assertEqual(self.__double_hash.search(10), 1, msg = "Non riesce a trovare un elemento usando l'esplorazione doppia.")
    
    def test_delete(self):
        self.assertFalse(self.__double_hash.delete(34), msg = "Non riconosce che l'elemento non è presente.")
        self.assertTrue(self.__double_hash.delete(6), msg = "Non segnala l'eliminazione.")
        self.assertTrue(self.__double_hash.delete(10), msg = "Non segnala l'eliminazione seguendo l'esplorazione doppia.")

        self.assertEqual(self.__double_hash.array[1], "DEL", msg = "Non inserisce il flag DEL correttamente.")

        self.__double_hash.insert(10)
        self.assertEqual(self.__double_hash.search(10), 1, msg = "Non riesce ad inserire dopo un elemento rimosso.")
        self.__double_hash.delete(3)
        self.assertEqual(self.__double_hash.search(10), 1, msg = "Non riesce a trovare l'elemento dopo in una ispezione dopo una rimozione.")


class double_population(unittest.TestCase):

    def test_population(self):
        double_hash = open_hash(11, hash_type.Double)
        elements = [1, 33, 97, 25, 890, 12, 9, 11, 74, 9834, 1900]
        for i in elements:
            double_hash.insert(i)

        self.assertFalse(("NIL" in double_hash.array), msg = "La tabella hash non si è riempita.")
