import copy
import unittest
from Codice.Sorting_Algorithm import *

class sorting_test(unittest.TestCase):

    def test_best_case(self):
        array1 = list(range(0, 150, 5))
        array2 = copy.deepcopy(array1)
        result = sorted(array1)
        B = [0] * 30 

        insertion_sort(array1)
        autonomus_conunting_sort(array2, B)
        self.assertEqual(array1, result, msg = "Insertion Sort non ordina nel caso migliore.")
        self.assertEqual(B, result, msg = "Counting Sort non ordina nel caso migliore.")

    def test_worst_case(self):
        array1 = list(range(150, 0, -5))
        array2 = copy.deepcopy(array1)
        result = sorted(array1)
        B = [0] * 30 

        insertion_sort(array1)
        autonomus_conunting_sort(array2, B)
        self.assertEqual(array1, result, msg = "Insertion Sort non ordina nel caso peggiore.")
        self.assertEqual(B, result, msg = "Counting Sort non ordina nel caso peggiore.")

def test_random_case(self):
        
        #Attenzione: l'array non viene generato pseudo-casualmente ogni volta che viene eseguito il test,
        # ma è stato generato usando il generatore di numeri casuali del Pyhton in anticipo.
        #Questo al fine di far si che ogni volta che viene eseguito il test si abbia lo stesso input.
        array1 = [107, 12, 35, 78, 122, 107, 128, 42, 17, 100, 11, 100, 26, 87, 38, 88, 124, 14, 59, 140, 116, 135, 126, 31, 133, 124, 105, 122, 35, 13]
        array2 = copy.deepcopy(array1)
        result = sorted(array1)
        B = [0] * 30 

        insertion_sort(array1)
        autonomus_conunting_sort(array2, B)
        self.assertEqual(array1, result, msg = "Insertion Sort non ordina nel caso \"casuale\".")
        self.assertEqual(B, result, msg = "Counting Sort non ordina nel caso \"casuale\".")
