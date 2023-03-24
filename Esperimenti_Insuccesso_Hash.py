from matplotlib import pyplot as plt

from Funzioni_per_Sperimentazioni import *
from Codice.Open_Hash import *


def execute_fail(m, iter, interval, verbose, save, suffix = ""):

    total_time = search_experiments(m, closest_two_power(m), iter, interval, verbose, test_type.Fail, suffix)
    
    process_plots(save, "Insuccesso", suffix)

    return total_time

def process_plots(save, prefix, suffix = ""):

    xlinearFail, ylinearFail = load_from_file("Risultati/" + prefix + "_Lineare" + suffix + ".txt")
    
    xquadraticFail, yquadraticFail = load_from_file("Risultati/" + prefix + "_Quadratico" + suffix + ".txt")

    xdoubleFail, ydoubleFail = load_from_file("Risultati/" + prefix + "_Doppio" + suffix + ".txt")    
   
    rmaximumFail = max(ylinearFail)

    dmaximumFail = max(ydoubleFail)

    qmaximumFail = max(yquadraticFail)    

    maxcomparisonFail = max(rmaximumFail, dmaximumFail, qmaximumFail)
    
    xcomparison = [i * 0.05 for i in range(1, 20)]
    ycomparisonFail = [(1 / (1 - i)) for i in xcomparison]

    for i in range(len(xcomparison)):
        ycomparisonFail[i] *= maxcomparisonFail / ycomparisonFail[-1]

    #Insuccesso Lineare  (Troppo Piatto)  
    create_function_plot(xlinearFail, ylinearFail, "Ricerca Lineare (Insuccesso)", "Lineare", "r", save, "Insuccesso_Lineare_scala_lineare", False, False)

    #Inuccesso Lineare 
    create_function_plot(xlinearFail, ylinearFail, "Ricerca Lineare (Insuccesso)", "Lineare", "r", save, "Insuccesso_Lineare_scala_logaritmica")

    #Insuccesso Quadratico
    create_function_plot(xquadraticFail, yquadraticFail, "Ricerca Quadratica (Insuccesso)", "Quadratica", "g", save, "Insuccesso_Quadratico_scala_logaritmica")

    #Insuccesso Doppio
    create_function_plot(xdoubleFail, ydoubleFail, "Ricerca Doppio Hash (Inuccesso)", "Doppio", "b", save, "Insucceso_Doppio_scala_logaritmica")

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


if(__name__ == "__main__"):
    execute_fail(977, 500, 50, True, False)
    plt.show()