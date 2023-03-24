from matplotlib import pyplot as plt

from Funzioni_per_Sperimentazioni import *
from Codice.Open_Hash import *


def execute_insert(m, iter, interval, verbose, save, suffix = ""):

    total_time = insert_experiments(m, closest_two_power(m), iter, interval, verbose, suffix)
    
    process_plots(save, "Inserimento", suffix)

    return total_time

def process_plots(save, prefix, suffix = ""):

    xlinearInsert, ylinearInsert = load_from_file("Risultati/" + prefix + "_Lineare" + suffix + ".txt")
    
    xquadraticInsert, yquadraticInsert = load_from_file("Risultati/" + prefix + "_Quadratico" + suffix + ".txt")

    xdoubleInsert, ydoubleInsert = load_from_file("Risultati/" + prefix + "_Doppio" + suffix + ".txt")    

    rmaximumInsert = max(ylinearInsert)
    
    dmaximumInsert = max(ydoubleInsert)
    
    qmaximumInsert = max(yquadraticInsert)

    maxcomparisonInsert = max(rmaximumInsert, dmaximumInsert, qmaximumInsert)
    
    xcomparison = [i * 0.05 for i in range(1, 20)]
    ycomparisonInsert = [(math.log2(1 / (1 - i)) / i) for i in xcomparison]

    for i in range(len(xcomparison)):
        ycomparisonInsert[i] *= maxcomparisonInsert / ycomparisonInsert[-1]
 
    #Inserimento Lineare  (Troppo Piatto)   
    create_function_plot(xlinearInsert, ylinearInsert, "Inserimento Lineare", "Lineare", "r", save, "Inserimento_Lineare_scala_lineare", False, False)

    #Inseriemnto Lineare  
    create_function_plot(xlinearInsert, ylinearInsert, "Inserimento Lineare", "Lineare", "r", save, "Inserimento_Lineare_scala_logaritmica")

    #Inserimento Quadratico
    create_function_plot(xquadraticInsert, yquadraticInsert, "Inseriemnto Quadratica", "Quadratica", "g", save, "Inserimento_Quadratico_scala_logaritmica")

    #SUccesso Doppio
    create_function_plot(xdoubleInsert, ydoubleInsert, "Inserimento Doppio Hash", "Doppio", "b", save, "Inserimento_Doppio_scala_logaritmica")

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

if(__name__ == "__main__"):
    execute_insert(977, 500, 50, True, False)
    plt.show()