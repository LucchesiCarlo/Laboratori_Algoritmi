from matplotlib import pyplot as plt

from Funzioni_per_Sperimentazioni import *
from Codice.Open_Hash import *


def execute_success(m, iter, interval, verbose, save, suffix = ""):
    
    total_time = search_experiments(m, closest_two_power(m), iter, interval, verbose, test_type.Success, suffix)
    
    process_plots(save, "Successo", suffix)

    return total_time


def process_plots(save, prefix, suffix = ""):
    xlinearSuccess, ylinearSuccess = load_from_file("Risultati/" + prefix + "_Lineare" + suffix + ".txt")
    
    xquadraticSuccess, yquadraticSuccess = load_from_file("Risultati/" + prefix + "_Quadratico" + suffix + ".txt")

    xdoubleSuccess, ydoubleSuccess = load_from_file("Risultati/" + prefix + "_Doppio" + suffix + ".txt")    

    rmaximumSuccess = max(ylinearSuccess)
    
    dmaximumSuccess = max(ydoubleSuccess)

    qmaximumSuccess = max(yquadraticSuccess)
    

    maxcomparisonSuccess = max(rmaximumSuccess, dmaximumSuccess, qmaximumSuccess)
    
    xcomparison = [i * 0.05 for i in range(1, 20)]
    ycomparisonSuccess = [(1 / (1 - i)) for i in xcomparison]

    for i in range(len(xcomparison)):
        ycomparisonSuccess[i] *= maxcomparisonSuccess / ycomparisonSuccess[-1]

    #Successo Lineare  (Troppo Piatto)  

    create_function_plot(xlinearSuccess, ylinearSuccess, "Ricerca Lineare (Successo)", "Lineare", "r", save, "Successo_Lineare_scala_lineare", False, False)

    #Successo Lineare
    create_function_plot(xlinearSuccess, ylinearSuccess, "Ricerca Lineare (Successo)", "Lineare", "r", save, "Successo_Lineare_scala_logaritmica")

    #Successo Quadratico
    create_function_plot(xlinearSuccess, ylinearSuccess, "Ricerca Quadratica (Successo)", "Quadratica", "g", save, "Successo_Quadratico_scala_logaritmica")

    #Successo Doppio
    create_function_plot(xlinearSuccess, ylinearSuccess, "Ricerca Doppio Hash (Successo)", "Doppio", "b", save, "Successo_Doppio_scala_lineare")

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

if(__name__ == "__main__"):
    execute_success(977, 500, 50, True, False)
    plt.show()