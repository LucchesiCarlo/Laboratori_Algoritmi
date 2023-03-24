import unittest
import Codice.unittest.Hash_Test
import Codice.unittest.Linear_Hash
import Codice.unittest.Quadratic_Hash
import Codice.unittest.Double_Hash

RED: str = "\33[91m"
GREEN: str = "\33[32m"
END: str = "\33[m"


testLoader = unittest.TestLoader()
testSuite = unittest.TestSuite()
testResults = unittest.TestResult()

testSuite.addTests(testLoader.loadTestsFromModule(Codice.unittest.Hash_Test))
testSuite.addTests(testLoader.loadTestsFromModule(Codice.unittest.Linear_Hash))
testSuite.addTests(testLoader.loadTestsFromModule(Codice.unittest.Quadratic_Hash))
testSuite.addTests(testLoader.loadTestsFromModule(Codice.unittest.Double_Hash))

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

