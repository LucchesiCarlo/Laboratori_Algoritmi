
def insertion_sort(A):
    """
    A è l'array che deve ordinare, non che anche l'oggetto in cui verrà salvato il
    risultato. 
    """
    length = len(A)
    for j in range(1, length):
        key = A[j]
        i = j - 1
        while(i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i-= 1
        A[i + 1] = key

def autonomus_conunting_sort(A, B):
    """
    I parametri sono i seguenti:
     -A è l'array da ordinare
     -B è l'array in cui si inserirà il risultato
    Il k che indica la massima oscillazione dei valori nell'array A viene 
    calcolato direttamente dalla funzione.
    """
    length = len(A)
    minimum = min(A)
    maximum = max(A)
    k = maximum - minimum
    C = []
    for i in range(k + 1):
        C.append(0)
    for i in range(length):
        C[A[i] - minimum] += 1
    for i in range(k):
        C[i + 1] += C[i]
    for i in range(length - 1, -1, -1):
        B[C[A[i] - minimum] - 1] = A[i]
        C[A[i] - minimum] -= 1

def standard_counting_sort(A, B, k):
    """
    I parametri sono i seguenti:
     -A è l'array da ordinare
     -B è l'array in cui si inserirà il risultato
     -k numero massimo di presente nell'array A 
    """
    length = len(A)
    C = []
    for i in range(k + 1):
        C.append(0)
    for i in range(length):
        C[A[i]] += 1
    for i in range(k):
        C[i + 1] += C[i]
    for i in range(length - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i] ] -= 1