from matplotlib import pyplot as plt

from Funzioni_per_Sperimentazioni import *
from Codice.Open_Hash import *


def execute_insert(m, iter, interval, verbose, save):

    hashLinearInsert = open_hash(m, hash_type.Linear)
    hashQuadraticInsert = open_hash(closest_two_power(m), hash_type.Quadratic, 0.5, 0.5)
    hashDoubleInsert = open_hash(m, hash_type.Double)

    start = timer()
    print("Inserimento Lineare")
    xlinearInsert, ylinearInsert = insert_test(hashLinearInsert, iter, interval, verbose)
    

    print("Inserimento Quadratico")
    xquadraticInsert, yquadraticInsert = insert_test(hashQuadraticInsert, iter, interval, verbose)

    print("Inserimento Doppio")
    xdoubleInsert, ydoubleInsert = insert_test(hashDoubleInsert, iter, interval, verbose)
    
    rmaximumInsert = max(ylinearInsert)
    
    dmaximumInsert = max(ydoubleInsert)
    
    qmaximumInsert = max(yquadraticInsert)

    maxcomparisonInsert = max(rmaximumInsert, dmaximumInsert, qmaximumInsert)
    
    xcomparison = [i * 0.05 for i in range(1, 20)]
    ycomparisonInsert = [(math.log2(1 / (1 - i)) / i) for i in xcomparison]

    for i in range(len(xcomparison)):
        ycomparisonInsert[i] *= maxcomparisonInsert / ycomparisonInsert[-1]


    end = timer()
    print("Tempo necessario a concludere tutti i test: %ds" % (end - start))

    #Successo Lineare  (Troppo Piatto)  
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Inserimento Lineare", False)
    plt.plot(xlinearInsert, ylinearInsert, "ro-", markersize = 2, label="Lineare")
    generate_plot(save, "Inserimento_Lineare_scala_lineare")

    #Successo Lineare    
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Inserimento Lineare")
    plt.plot(xlinearInsert, ylinearInsert, "ro-", markersize = 2, label="Lineare")
    plt.annotate(text = "%.2f" % (ylinearInsert[-1]), xy = (xlinearInsert[-1], ylinearInsert[-1]),
                 xytext=(xlinearInsert[-1] * 0.9, ylinearInsert[-1] * 0.8))
    generate_plot(save, "Inserimento_Lineare_scala_logaritmica")

    #Successo Quadratico
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Inserimento Quadratica")
    plt.plot(xquadraticInsert, yquadraticInsert, "go-", markersize = 2, label="Quadratica")
    plt.annotate(text = "%.2f" % (yquadraticInsert[-1]), xy = (xquadraticInsert[-1], yquadraticInsert[-1]),
                 xytext=(xquadraticInsert[-1] * 0.9, yquadraticInsert[-1] * 0.8))
    generate_plot(save, "Inserimento_Quadratico_scala_logaritmica")

    #SUccesso Doppio
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Inserimento Doppio Hash")
    plt.plot(xdoubleInsert, ydoubleInsert, "bo-", markersize = 2, label="Doppio")
    plt.annotate(text = "%.2f" % (ydoubleInsert[-1]), xy = (xdoubleInsert[-1], ydoubleInsert[-1]),
                 xytext=(xdoubleInsert[-1] * 0.9, ydoubleInsert[-1] * 0.8))
    generate_plot(save, "Inserimento_Doppio_scala_logaritmica")

    #Funzione della stima asintotica
    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", "Stima Asintotica Inserimento")
    plt.plot(xcomparison, ycomparisonInsert, "ko-", markersize = 2, label="Funzione")
    generate_plot(save, "Inserimento_Asintotica_scala_logaritmica")

    #Confronto tra le varie ricerce con successo.
    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", "Confronto tra Inserimenti")
    plt.plot(xlinearInsert, ylinearInsert, "ro-", markersize = 2, label="Lineare")
    plt.plot(xquadraticInsert, yquadraticInsert, "go-", markersize = 2, label="Quadratica")
    plt.plot(xdoubleInsert, ydoubleInsert, "bo-", markersize = 2, label="Doppio")
    generate_plot(save, "Inserimento_Confronto_scala_logaritmica")

    #Confronto tra ricerche con successo e la stima asintotica normalizzata.
    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", "Confronto Inserimenti con Stima asintotica")
    plt.plot(xlinearInsert, ylinearInsert, "ro-", markersize = 2, label="Lineare")
    plt.plot(xquadraticInsert, yquadraticInsert, "go-", markersize = 2, label="Quadratica")
    plt.plot(xdoubleInsert, ydoubleInsert, "bo-", markersize = 2, label="Doppio")
    plt.plot(xcomparison, ycomparisonInsert, "ko-", markersize = 2, label="Funzione")
    generate_plot(save, "Inserimento_Confronto_Asintotico_scala_logaritmica")

    #Rappresentazioni stime asintotiche con grafico a barre.
    setup_plot("Raggruppamenti fattore di Caricamento", "Tempo raggruppato", "Confronto tra Inserimenti")

    linear_average, quadratic_average, double_average = generate_bar_values(xlinearInsert, ylinearInsert, xquadraticInsert, yquadraticInsert, xdoubleInsert, ydoubleInsert)

    x = list(range(10))
    width = 0.27
    plt.bar(x, linear_average, width, label = "Lineare", color = "red")
    plt.bar([i + width for i in x], quadratic_average, width, label = "Quadratico", color = "green")
    plt.bar([i + 2 * width for i in x], double_average, width, label = "Doppio", color = "blue")
    plt.xticks([i + width for i in range(10)], list(range(10)))
    
    generate_plot(save, "Inserimento_Confronto_barre_scala_logaritmica")

    return end - start

if(__name__ == "__main__"):
    execute_insert(977, 500, 50, True, False)
    plt.show()