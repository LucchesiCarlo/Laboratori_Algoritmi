from matplotlib import pyplot as plt

from Funzioni_per_Sperimentazioni import execute_test
from Funzioni_per_Sperimentazioni import process_plots
from Funzioni_per_Sperimentazioni import closest_two_power
from Funzioni_per_Sperimentazioni import test_type

#Si è scelto un numero primo abbastanza vicino a 16384 perchè la tabella hash con esplorazione quadratica
#necessita di un numero potenza intera del 2 (per motivi teorici esplorati nella relazione). Questo fa si
#che il confronto con gli altri 2 tipi di esplorazioni sarà migliore.

#Numero primo 16381
#TODO Cambiare 16381. Il fatto che sia troppo vicino ad una potenza esatta del 2 da problemi.
m = 10007
iter = 500
interval = 10
verbose = True
save = False

print("Esperiementi sulla ricerca con successo.")
execute_test(m, closest_two_power(m), iter, interval, verbose, test_type.Success)
process_plots(save, test_type.Success)
print("==================================================")

print("Esperiementi sulla ricerca con insuccesso.")
execute_test(m, closest_two_power(m), iter, interval, verbose, test_type.Fail)
process_plots(save, test_type.Fail)
print("==================================================")

print("Esperiementi sull'inserimento.")
execute_test(m, closest_two_power(m), iter, interval, verbose, test_type.Insert)
process_plots(save, test_type.Insert)

plt.show()