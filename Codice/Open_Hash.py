from enum import IntEnum
import numpy as np

"""
Questo file contiene una classe che rappresenta un Hash ad Indirizzamento Aperto.
Questa classe fornisce i metodi utili all'utilizzo di un hash:
    - Inserimento di un dato
    - Ricerca di un dato
    - Rimozione di un dato
In questo contesto gli "oggetti" che verranno inseriti al suo interno sono direttamente le chiavi che le identificano come oggetti, mentre ovviamante i corrispondenti valori hash saranno calcolati successivamente.
"""

#Questa enumerazione ci permette di limitare la scelta del valore che identifica la funzione
# hash nel costruttore di open_hash, al fine di evitare che un utente utilizzi un numero non
# associato ad una funzione hash.  
class hash_type(IntEnum):
    Linear = 1
    Quadratic = 2
    Double = 3


class open_hash(object):

    elements: int = 0

    def __init__(self, length: int, type: hash_type, c1: float = 1.0, c2: float = 0.5):
        """
        Questo costruttore richiede la lungezza della tabella hash.
        Se il valore fornito è <= 0 allora genera l'eccezione ValueError.
        """
        #I valori c1 e c2 sono utilizzati per la generazione dei valori delle seguenze di
        # esplorazione dei vari tipi di funzioni hash.
        #Nel caso di quella lineare il parametro intero c sarà il valore di c1.
        if (length <= 0):
            raise ValueError("La lunghezza di un Hash non può essere negativa.")
        
        self.array = np.full(length, fill_value = "NIL", dtype = np.dtype("U10"))
        
        self.hash_type = type
        self.__c1 = c1
        self.__c2 = c2

        #Il parametro M è maiuscolo per evidenziare il fatto che sia dovrebbe rimanere costante.
        #D'altra parte non è privato in quanto è un dato che potenzialemnte potrebbe essere
        # di interesso per eventuale funzione chiamante
        self.M = length 

    def insert(self, x: int):
        #L'utilizzo di un while(True) seguito poi da un break interno si è reso necessario
        # in quanto in Pyhton non esiste il ciclo do-while, che quindi può essere tradotto
        # con questo uso idiomatico.
        key = 0
        i = 0
        while(True):
            #L'utilizzo di una cascata di if-else è necessaria per la shelta della funzione
            # dato che nel Python non esiste l'istruzione per il controllo di flusso switch-case
            
            key = self.__calculate_hash(x, i)
            i+= 1

            if(self.array[key] == str(x)):
                raise ValueError("Non è possibile inserie nello stessa tavola hash 2 valori uguali.")
            if(self.array[key] == "NIL" or self.array[key] == "DEL"):
               self.array[key] = str(x)
               self.elements += 1
               return
            if(i == self.M):
                raise MemoryError("Impossibile aggiungere un nuovo elemento perchè la tabella è piena.")

        #Per quanto questo controllo si potesse fare in testa al metodo si è scelto controllarlo
        # attendendo che il valore di i raggiungesse il massimo per non falzare le prestazioni di un 
        # inserimento senza successo per via della tavola piena.
        
    def search(self, x: int):
        key = 0
        i = 0
        while(True):
            key = self.__calculate_hash(x, i)
            i+= 1
            if(self.array[key] == str(x)):
                return int(key)
            if(i == self.M or self.array[key] == "NIL"):
                return "NIL"
    #Questa funzione da come valore di ritorno True se l'elemento è stato trovato ed eliminato.
    #Altrimenti ritorna False
    def delete(self, x: int) -> bool:
        key = 0
        i = 0
        while(True):
            key = self.__calculate_hash(x, i)
            i+= 1

            if(self.array[key] == str(x)):
                self.array[key] = "DEL"
                self.elements -= 1
                return True
            if(self.M == i):
                return False
            
    def load_factor(self):
        return float(self.elements) / self.M
    
    def undo_element(self, x: int):
        """
        Questo metodo serve per permettere di rimuovere un elemento dalla tabella hash inserendo 
        un NIL invece di un DEL. E' utilie in quanto per i nostri eperiemnti abbiamo bisogno di 
        una tabella hash su cui non sono state fatte rimozioni. ATTENZIONE: la tabella hash continua 
        a funzionare correttamente solo se x è stato l'ultimo elemento inserito.
        """
        key = 0
        i = 0
        while(True):
            key = self.__calculate_hash(x, i)
            i += 1
            if(self.array[key] == str(x)):
                self.array[key] = "NIL"
                self.elements -= 1
                return True
            if(i == self.M or self.array[key] == "NIL"):
                return False

    #Questo metodo serve per raggruppare il codice che identifica la funzione hash da usare
    def __calculate_hash(self, x: int, i: int) -> int:
        key = 0
        if(self.hash_type == hash_type.Linear):
            key = self.__linear_probing(x, i)
        elif(self.hash_type == hash_type.Quadratic):
            key = self.__quadratic_probing(x, i)
        elif(self.hash_type == hash_type.Double):
            key = self.__double_probing(x, i)
        else:
            raise Exception("E' stata chiamata una funzione hash che non esiste.")
        return key
    
    #Implementa il metodo di calcolo dell'hash per divisione
    def __division_probing(self, k: int):
        return k % self.M

    #Implementa il metodo di esplorazione dell'hash lineare per un singolo elemento
    def __linear_probing(self, k:int , i: int):
        return (self.__division_probing(k) + int(self.__c1) * i) % self.M

    #Implementa il metodo di esplorazione dell'hash qudratico per un singolo elemento
    def __quadratic_probing(self, k: int, i: int):
        #Notare come il secondo addendo è equivalente alla forma c1 * i + c2 * i^2
        return int((self.__division_probing(k) + (self.__c1  +  self.__c2 * i) * i) % self.M)

    #Implementa il metodo di esplorazione dell'hash doppio per un singolo elemento
    def __double_probing(self,k: int, i: int):
        return (self.__division_probing(k) + ((k % (self.M - 1)) + 1) * i) % self.M

