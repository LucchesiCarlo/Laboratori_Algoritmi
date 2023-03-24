import unittest
import Codice.unittest.Sorting_test

RED: str = "\33[91m"
GREEN: str = "\33[32m"
END: str = "\33[m"


testLoader = unittest.TestLoader()
testSuite = unittest.TestSuite()
testResults = unittest.TestResult()

testSuite.addTests(testLoader.loadTestsFromModule(Codice.unittest.Sorting_test))

testSuite.run(testResults)
failures = testResults.failures
errors = testResults.errors

if(len(errors) + len(failures) == 0):
    print(GREEN + "Non si è verificato nessun errore." + END)
else :
    for failure in failures:
        print(RED + str(failure[0]) + END, failure[1], sep = "\n")
        print("============================================================")
    for error in errors:
        print(RED + str(error[0]) + END, error[1], sep = "\n")
        print("============================================================")
    print("Errori:" + str(len(errors)), "Fallimenti:" + str(len(failures)))

