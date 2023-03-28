import copy
import unittest
import numpy as np
from numpy import integer
from Codice.Sorting_Algorithm import *

class sorting_test(unittest.TestCase):

    def test_best_case(self):
        array =  list(range(0, 150, 5))
        k = max(array)
        argument_1 = np.array(array)
        argument_2 = np.array(array)
        result = np.array(sorted(array))
        B = np.zeros(30, dtype = np.integer)

        insertion_sort(argument_1)
        standard_counting_sort(argument_2, B, k)
        self.assertTrue(np.array_equal(argument_1, result), msg = "Insertion Sort non ordina nel caso migliore.")
        self.assertTrue(np.array_equal(B, result), msg = "Counting Sort non ordina nel caso migliore.")

    def test_worst_case(self):
        array = list(range(150, 0, -5))
        k = max(array)
        argument_1 = np.array(array)
        argument_2 = np.array(array)
        result = np.array(sorted(array))
        B = np.zeros(30, dtype = np.integer)

        insertion_sort(argument_1)
        standard_counting_sort(argument_2, B, k)
        self.assertTrue(np.array_equal(argument_1, result), msg = "Insertion Sort non ordina nel caso peggiore.")
        self.assertTrue(np.array_equal(B, result), msg = "Counting Sort non ordina nel caso peggiore.")

    def test_random_case(self):
        
        #Attenzione: l'array non viene generato pseudo-casualmente ogni volta che viene eseguito il test,
        # ma è stato generato usando il generatore di numeri casuali del Pyhton in anticipo.
        #Questo al fine di far si che ogni volta che viene eseguito il test si abbia lo stesso input.
        array = [107, 12, 35, 78, 122, 107, 128, 42, 17, 100, 11, 100, 26, 87, 38, 88, 124, 14, 59, 140, 116, 135, 126, 31, 133, 124, 105, 122, 35, 13]
        k = max(array)
        argument_1 = np.array(array)
        argument_2 = np.array(array)
        result = np.array(sorted(array))
        B = np.zeros(30, dtype = np.integer)

        insertion_sort(argument_1)
        standard_counting_sort(argument_2, B, k)
        self.assertTrue(np.array_equal(argument_1, result), msg = "Insertion Sort non ordina nel caso \"casuale\".")
        self.assertTrue(np.array_equal(B, result), msg = "Counting Sort non ordina nel caso \"casuale\".")
