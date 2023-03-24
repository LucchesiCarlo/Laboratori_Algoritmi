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

    rminimumSuccess = min(ylinearSuccess)
    
    dminimumSuccess = min(ydoubleSuccess)

    qminimumSuccess = min(yquadraticSuccess)
    

    min_range = min(rminimumSuccess, dminimumSuccess, qminimumSuccess)
    
    xcomparison = [i * 0.05 for i in range(1, 20)]
    ycomparisonSuccess = [(1 / (1 - i)) for i in xcomparison]

    min_comparison = min(ycomparisonSuccess)

    for i in range(len(xcomparison)):
        ycomparisonSuccess[i] *= min_range / min_comparison

    #Successo Lineare  (Troppo Piatto)  

    create_function_plot(xlinearSuccess, ylinearSuccess, "Ricerca Lineare (Successo)", "Lineare", "r", save, "Successo_Lineare_scala_lineare", False, False)

    #Successo Lineare
    create_function_plot(xlinearSuccess, ylinearSuccess, "Ricerca Lineare (Successo)", "Lineare", "r", save, "Successo_Lineare_scala_logaritmica")

    #Successo Quadratico
    create_function_plot(xquadraticSuccess, yquadraticSuccess, "Ricerca Quadratica (Successo)", "Quadratica", "g", save, "Successo_Quadratico_scala_logaritmica")

    #Successo Doppio
    create_function_plot(xdoubleSuccess, ydoubleSuccess, "Ricerca Doppio Hash (Successo)", "Doppio", "b", save, "Successo_Doppio_scala_logaritmica")

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
    x = [i/10 for i in range(10)]

    x_values = [
        xlinearSuccess,
        xquadraticSuccess,
        xdoubleSuccess
    ]

    y_values = [
        [ylinearSuccess, "Lineare", "red"],
        [yquadraticSuccess, "Quadratico", "green"],
        [ydoubleSuccess, "Doppio", "blue"],
    ]

    create_bar_plot(x, x_values, y_values, "Confronto tra Ricerche (Successo)", 0.27, save, "Successo_Confronto_barre_scala_logaritmica")

if(__name__ == "__main__"):
    execute_success(977, 500, 50, True, False)
    plt.show()