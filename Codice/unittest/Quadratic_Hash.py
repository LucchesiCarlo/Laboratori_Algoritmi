import unittest
from Codice.Open_Hash import *


class quadratic_hash_usage(unittest.TestCase):

    def setUp(self):
        self.__quadratic_hash = open_hash(7, hash_type.Quadratic, 0.5, 0.5)

        self.__quadratic_hash.insert(6)
        self.__quadratic_hash.insert(3)
        self.__quadratic_hash.insert(10)
        self.__quadratic_hash.insert(24)

    def test_insert(self):
        self.assertEqual(self.__quadratic_hash.array[6], "6", msg = "Non inserisce correttamente il valore.")
        self.assertEqual(self.__quadratic_hash.array[3], "3", msg = "Non inserisce correttamente il valore.")
        self.assertEqual(self.__quadratic_hash.array[4], "10", msg = "L'esplorazione quadratica non funziona.")
        self.assertEqual(self.__quadratic_hash.array[2], "24", msg = "L'esplorazione quadratica non funziona.")

        with self.assertRaises(ValueError, msg = "Non si accorge che vengono inseriti 2 valori uguali."):
            self.__quadratic_hash.insert(6)

    def test_search(self):
        self.assertEqual(self.__quadratic_hash.search(1), "NIL", msg = "Non inizializza correttamente la tavola hash.")
        self.assertEqual(self.__quadratic_hash.search(6), 6, msg = "Non risce a trovare l'elemento nella tavola.")
        self.assertEqual(self.__quadratic_hash.search(10), 4, msg = "Non riesce a trovare un elemento usando l'esplorazione quadratica.")
        self.assertEqual(self.__quadratic_hash.search(24), 2, msg = "Non riesce a trovare un elemento usando l'esplorazione quadratica.")
    
    def test_delete(self):
        self.assertFalse(self.__quadratic_hash.delete(34), msg = "Non riconosce che l'elemento non è presente.")
        self.assertTrue(self.__quadratic_hash.delete(6), msg = "Non segnala l'eliminazione.")
        self.assertTrue(self.__quadratic_hash.delete(24), msg = "Non segnala l'eliminazione seguendo l'esplorazione quadratica.")

        self.assertEqual(self.__quadratic_hash.array[2], "DEL", msg = "Non inserisce il flag DEL correttamente.")

        self.__quadratic_hash.insert(24)
        self.assertEqual(self.__quadratic_hash.search(24), 6, msg = "Non riesce ad inserire dopo un elemento rimosso.")
        self.__quadratic_hash.delete(3)
        self.assertEqual(self.__quadratic_hash.search(24), 6, msg = "Non riesce a trovare l'elemento dopo in una ispezione dopo una rimozione.")

        self.__quadratic_hash.delete(24)
        self.__quadratic_hash.insert(24)
        self.assertEqual(self.__quadratic_hash.search(24), 3, msg = "Non sovrascrive su una posizione in cui c'è DEL.")


class quadratic_population(unittest.TestCase):

    def test_population(self):
        #In questo caso si è contravvenuto alla regola di scegliere una grandezza della tabella pari ad un numero primo.
        # Questo si è fatto allo scopo di garantire la generazione di una permutazione nella sequenza di esplorazione.
        # https://en.wikipedia.org/wiki/Quadratic_probing
        quadratic_hash = open_hash(16, hash_type.Quadratic, 0.5, 0.5)
        elements = [123, 4, 1, 33, 97, 25, 890, 13, 12, 9, 11, 3400, 22, 74, 9834, 1900]
        for i in elements:
            quadratic_hash.insert(i)

        self.assertFalse(("NIL" in quadratic_hash.array), msg = "La tabella hash non si è riempita.")
