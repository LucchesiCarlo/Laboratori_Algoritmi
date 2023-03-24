from matplotlib import pyplot as plt

from Funzioni_per_Sperimentazioni import *
from Codice.Open_Hash import *


def execute_fail(m, iter, interval, verbose, save):

    hashLinearFail = open_hash(m, hash_type.Linear)
    hashQuadraticFail = open_hash(closest_two_power(m), hash_type.Quadratic, 0.5, 0.5)
    hashDoubleFail = open_hash(m, hash_type.Double)

    start = timer()
    print("Ricerca Lineare Insuccesso")
    xlinearFail, ylinearFail = search_test(hashLinearFail, test_type.Fail, iter, interval, verbose)

    print("Ricerca Quadratico Insuccesso")
    xquadraticFail, yquadraticFail = search_test(hashQuadraticFail, test_type.Fail, iter, interval, verbose)

    print("Ricerca Doppio Insucesso")
    xdoubleFail, ydoubleFail = search_test(hashDoubleFail, test_type.Fail, iter, interval, verbose)
   
    rmaximumFail = max(ylinearFail)

    dmaximumFail = max(ydoubleFail)

    qmaximumFail = max(yquadraticFail)
    

    maxcomparisonFail = max(rmaximumFail, dmaximumFail, qmaximumFail)
    
    xcomparison = [i * 0.05 for i in range(1, 20)]
    ycomparisonFail = [(1 / (1 - i)) for i in xcomparison]

    for i in range(len(xcomparison)):
        ycomparisonFail[i] *= maxcomparisonFail / ycomparisonFail[-1]

    end = timer()
    print("Tempo necessario a concludere tutti i test: %ds" % (end - start))

    #Successo Lineare  (Troppo Piatto)  
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Ricerca Lineare (Insuccesso)", False)
    plt.plot(xlinearFail, ylinearFail, "ro-", markersize = 2, label="Lineare")
    generate_plot(save, "Insuccesso_Lineare_scala_lineare")

    #Successo Lineare    
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Ricerca Lineare (Insuccesso)")
    plt.plot(xlinearFail, ylinearFail, "ro-", markersize = 2, label="Lineare")
    plt.annotate(text = "%.2f" % (ylinearFail[-1]), xy = (xlinearFail[-1], ylinearFail[-1]),
                 xytext=(xlinearFail[-1] * 0.9, ylinearFail[-1] * 0.8))
    generate_plot(save, "Insuccesso_Lineare_scala_logaritmica")

    #Successo Quadratico
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Ricerca Quadratica (Insuccesso)")
    plt.plot(xquadraticFail, yquadraticFail, "go-", markersize = 2, label="Quadratica")
    plt.annotate(text = "%.2f" % (yquadraticFail[-1]), xy = (xquadraticFail[-1], yquadraticFail[-1]),
                 xytext=(xquadraticFail[-1] * 0.9, yquadraticFail[-1] * 0.8))
    generate_plot(save, "Insuccesso_Quadratico_scala_logaritmica")

    #SUccesso Doppio
    setup_plot("Fattore di Caricamento", "Tempo (ms)", "Ricerca Doppio Hash (Insuccesso)")
    plt.plot(xdoubleFail, ydoubleFail, "bo-", markersize = 2, label="Doppio")
    plt.annotate(text = "%.2f" % (ydoubleFail[-1]), xy = (xdoubleFail[-1], ydoubleFail[-1]),
                 xytext=(xdoubleFail[-1] * 0.9, ydoubleFail[-1] * 0.8))
    generate_plot(save, "Insuccesso_Doppio_scala_logaritmica")

    #Funzione della stima asintotica
    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", "Stima Asintotica Ricerca (Insuccesso)")
    plt.plot(xcomparison, ycomparisonFail, "ko-", markersize = 2, label="Funzione")
    generate_plot(save, "Insuccesso_Asintotica_scala_logaritmica")

    #Confronto tra le varie ricerce con successo.
    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", "Confronto tra Ricerche (Insuccesso)")
    plt.plot(xlinearFail, ylinearFail, "ro-", markersize = 2, label="Lineare")
    plt.plot(xquadraticFail, yquadraticFail, "go-", markersize = 2, label="Quadratica")
    plt.plot(xdoubleFail, ydoubleFail, "bo-", markersize = 2, label="Doppio")
    generate_plot(save, "Insuccesso_Confronto_scala_logaritmica")

    #Confronto tra ricerche con successo e la stima asintotica normalizzata.
    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", "Confronto Ricerca (Insuccesso) con Stima asintotica")
    plt.plot(xlinearFail, ylinearFail, "ro-", markersize = 2, label="Lineare")
    plt.plot(xquadraticFail, yquadraticFail, "go-", markersize = 2, label="Quadratica")
    plt.plot(xdoubleFail, ydoubleFail, "bo-", markersize = 2, label="Doppio")
    plt.plot(xcomparison, ycomparisonFail, "ko-", markersize = 2, label="Funzione")
    generate_plot(save, "Insuccesso_Confronto_Asintotico_scala_logaritmica")

    #Rappresentazioni stime asintotiche con grafico a barre.
    setup_plot("Raggruppamenti fattore di Caricamento", "Tempo raggruppato", "Confronto tra Ricerche (Insuccesso)")

    linear_average, quadratic_average, double_average = generate_bar_values(xlinearFail, ylinearFail, xquadraticFail, yquadraticFail, xdoubleFail, ydoubleFail)

    x = list(range(10))
    width = 0.27
    plt.bar(x, linear_average, width, label = "Lineare", color = "red")
    plt.bar([i + width for i in x], quadratic_average, width, label = "Quadratico", color = "green")
    plt.bar([i + 2 * width for i in x], double_average, width, label = "Doppio", color = "blue")
    plt.xticks([i + width for i in range(10)], list(range(10)))
    
    generate_plot(save, "Insuccesso_Confronto_barre_scala_logaritmica")

    return end - start

if(__name__ == "__main__"):
    execute_fail(977, 500, 50, True, False)
    plt.show()