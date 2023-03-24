import unittest
from Codice.Open_Hash import *

class hash_initialization(unittest.TestCase):

    def test_bad_initializzation(self):
        with self.assertRaises(ValueError, msg = "Non genera l'eccezione se è inizializzata con un numero negativo."):
            open_hash(-3, hash_type.Linear)

    def test_good_initializzation(self):
        hash = open_hash(3, hash_type.Double)
        self.assertIsInstance(hash, open_hash, msg = "Non crea l'oggetto.")
