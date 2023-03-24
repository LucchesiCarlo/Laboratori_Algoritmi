from matplotlib import pyplot as plt

from Esperimenti_Successo_Hash import execute_success
from Esperimenti_Insuccesso_Hash import execute_fail
from Esperimenti_Inserimento_Hash import execute_insert

#Si è scelto un numero primo abbastanza vicino a 16384 perchè la tabella hash con esplorazione quadratica
#necessita di un numero potenza intera del 2 (per motivi teorici esplorati nella relazione). Questo fa si
#che il confronto con gli altri 2 tipi di esplorazioni sarà migliore.

#Numero primo 16381
#TODO Cambiare 16381. Il fatto che sia troppo vicino ad una potenza esatta del 2 da problemi.
m = 10007
iter = 500
interval = 250
verbose = True
save = False

print("Esperiementi sulla ricerca con successo.")
execute_success(m, iter, interval, verbose, save)
print("==================================================")
print("Esperiementi sulla ricerca con insuccesso.")
execute_fail(m, iter, interval, verbose, save)
print("==================================================")
print("Esperiementi sull'inserimento.")
execute_insert(m, iter, interval, verbose, save)

plt.show()