from matplotlib import pyplot as plt

from Funzioni_per_Sperimentazioni import *
from Codice.Open_Hash import *


def execute_success(m, iter, interval, verbose, save):

    hashLinearSuccess = open_hash(m, hash_type.Linear)
    hashQuadraticSuccess = open_hash(closest_two_power(m), hash_type.Quadratic, 0.5, 0.5)
    hashDoubleSuccess = open_hash(m, hash_type.Double)

    start = timer()
    print("Ricerca Lineare Successo")
    xlinearSuccess, ylinearSuccess = search_test(hashLinearSuccess, test_type.Success, iter, interval, verbose)

    print("Ricerca Quadratico Successo")
    xquadraticSuccess, yquadraticSuccess = search_test(hashQuadraticSuccess, test_type.Success, iter, interval, verbose)
    print("Ricerca Quadratico Insuccesso")

    print("Ricerca Doppio Successo")
    xdoubleSuccess, ydoubleSuccess = search_test(hashDoubleSuccess, test_type.Success, iter, interval, verbose)
    print("Ricerca Doppio Insucesso")

    rmaximumSuccess = max(ylinearSuccess)
    
    dmaximumSuccess = max(ydoubleSuccess)

    qmaximumSuccess = max(yquadraticSuccess)
    

    maxcomparisonSuccess = max(rmaximumSuccess, dmaximumSuccess, qmaximumSuccess)
    
    xcomparison = [i * 0.05 for i in range(1, 20)]
    ycomparisonSuccess = [(1 / (1 - i)) for i in xcomparison]

    for i in range(len(xcomparison)):
        ycomparisonSuccess[i] *= maxcomparisonSuccess / ycomparisonSuccess[-1]


    end = timer()
    print("Tempo necessario a concludere tutti i test: %ds" % (end - start))

    #Successo Lineare  (Troppo Piatto)  
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Ricerca Lineare (Successo)", False)
    plt.plot(xlinearSuccess, ylinearSuccess, "ro-", markersize = 2, label="Lineare")
    generate_plot(save, "Successo_Lineare_scala_lineare")

    #Successo Lineare    
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Ricerca Lineare (Successo)")
    plt.plot(xlinearSuccess, ylinearSuccess, "ro-", markersize = 2, label="Lineare")
    plt.annotate(text = "%.2f" % (ylinearSuccess[-1]), xy = (xlinearSuccess[-1], ylinearSuccess[-1]),
                 xytext=(xlinearSuccess[-1] * 0.9, ylinearSuccess[-1] * 0.8))
    generate_plot(save, "Successo_Lineare_scala_logaritmica")

    #Successo Quadratico
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Ricerca Quadratica (Successo)")
    plt.plot(xquadraticSuccess, yquadraticSuccess, "go-", markersize = 2, label="Quadratica")
    plt.annotate(text = "%.2f" % (yquadraticSuccess[-1]), xy = (xquadraticSuccess[-1], yquadraticSuccess[-1]),
                 xytext=(xquadraticSuccess[-1] * 0.9, yquadraticSuccess[-1] * 0.8))
    generate_plot(save, "Successo_Quadratico_scala_logaritmica")

    #SUccesso Doppio
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Ricerca Doppio Hash (Successo)")
    plt.plot(xdoubleSuccess, ydoubleSuccess, "bo-", markersize = 2, label="Doppio")
    plt.annotate(text = "%.2f" % (ydoubleSuccess[-1]), xy = (xdoubleSuccess[-1], ydoubleSuccess[-1]),
                 xytext=(xdoubleSuccess[-1] * 0.9, ydoubleSuccess[-1] * 0.8))
    generate_plot(save, "Successo_Doppio_scala_logaritmica")

    #Funzione della stima asintotica
    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", "Stima Asintotica Ricerca (Successo)")
    plt.plot(xcomparison, ycomparisonSuccess, "ko-", markersize = 2, label="Funzione")
    generate_plot(save, "Successo_Asintotica_scala_logaritmica")

    #Confronto tra le varie ricerce con successo.
    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", "Confronto tra Ricerche (Successo)")
    plt.plot(xlinearSuccess, ylinearSuccess, "ro-", markersize = 2, label="Lineare")
    plt.plot(xquadraticSuccess, yquadraticSuccess, "go-", markersize = 2, label="Quadratica")
    plt.plot(xdoubleSuccess, ydoubleSuccess, "bo-", markersize = 2, label="Doppio")
    generate_plot(save, "Successo_Confronto_scala_logaritmica")

    #Confronto tra ricerche con successo e la stima asintotica normalizzata.
    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", "Confronto Ricerca (Successo) con Stima asintotica")
    plt.plot(xlinearSuccess, ylinearSuccess, "ro-", markersize = 2, label="Lineare")
    plt.plot(xquadraticSuccess, yquadraticSuccess, "go-", markersize = 2, label="Quadratica")
    plt.plot(xdoubleSuccess, ydoubleSuccess, "bo-", markersize = 2, label="Doppio")
    plt.plot(xcomparison, ycomparisonSuccess, "ko-", markersize = 2, label="Funzione")
    generate_plot(save, "Successo_Confronto_Asintotico_scala_logaritmica")

    #Rappresentazioni stime asintotiche con grafico a barre.
    setup_plot("Raggruppamenti fattore di Caricamento", "Tempo raggruppato", "Confronto tra Ricerche (Successo)")

    linear_average, quadratic_average, double_average = generate_bar_values(xlinearSuccess, ylinearSuccess, xquadraticSuccess, yquadraticSuccess, xdoubleSuccess, ydoubleSuccess)

    x = list(range(10))
    width = 0.27
    plt.bar(x, linear_average, width, label = "Lineare", color = "red")
    plt.bar([i + width for i in x], quadratic_average, width, label = "Quadratico", color = "green")
    plt.bar([i + 2 * width for i in x], double_average, width, label = "Doppio", color = "blue")
    plt.xticks([i + width for i in range(10)], list(range(10)))
    
    generate_plot(save, "Successo_Confronto_barre_scala_logaritmica")

    return end - start

if(__name__ == "__main__"):
    execute_success(977, 500, 50, True, False)
    plt.show()