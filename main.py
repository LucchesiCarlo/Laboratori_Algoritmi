from matplotlib import pyplot as plt

from Codice.Open_Hash import *
from Funzioni_per_Sperimentazioni import *

def main_test(m, iter, interval, verbose, save):
    print("Esperiementi sulla ricerca con successo.")
    execute_test(m, closest_two_power(m), iter, interval, verbose, save, test_type.Success)
    process_plots(save, test_type.Success)
    print("==================================================")

    print("Esperiementi sulla ricerca con insuccesso.")
    execute_test(m, closest_two_power(m), iter, interval, verbose, save, test_type.Fail)
    process_plots(save, test_type.Fail)
    print("==================================================")

    print("Esperiementi sull'inserimento.")
    execute_test(m, closest_two_power(m), iter, interval, verbose, save, test_type.Insert)
    process_plots(save, test_type.Insert)


def test_linear_different_coefficent(m: int, c_1: int, c_2: int, iter: int, interval: int, verbose: bool, type: test_type, suffix: str = ""):

    hash_c_1 = open_hash(m, hash_type.Linear, c_1)
    hash_c_2 = open_hash(m, hash_type.Linear, c_2)
    
    c_1_load = []
    c_1_times = []
    c_2_load = []
    c_2_times = []

    prefix = ""

    if(type == test_type.Success):
        prefix = "Successo"
        c_1_load, c_1_times = search_test(hash_c_1, test_type.Success, iter, interval, verbose)
        c_2_load, c_2_times = search_test(hash_c_2, test_type.Success, iter, interval, verbose)
    elif(type == test_type.Fail):
        prefix = "Insuccesso"
        c_1_load, c_1_times = search_test(hash_c_1, test_type.Fail, iter, interval, verbose)
        c_2_load, c_2_times = search_test(hash_c_2, test_type.Fail, iter, interval, verbose)
    elif(type == test_type.Insert):
        prefix = "Inserimento"
        c_1_load, c_1_times = insert_test(hash_c_1, iter, interval, verbose)
        c_2_load, c_2_times = insert_test(hash_c_2, iter, interval, verbose)

    save_on_file(c_1_load, c_1_times, prefix + "_Lineare_%d" % (c_1) + suffix)
    save_on_file(c_2_load, c_2_times, prefix + "_Lineare_%d" % (c_2) + suffix)

def plot_test_linear_different_coefficent(c_1: int, c_2: int,save: bool, type: test_type, suffix: str = ""):

    prefix = ""

    if(type == test_type.Success):
        prefix = "Successo"
    elif(type == test_type.Fail):
        prefix = "Insuccesso"
    elif(type == test_type.Insert):
        prefix = "Inserimento"
    
    c_1_load, c_1_times = load_from_file(prefix + "_Lineare_%d" % (c_1) + suffix)
    c_2_load, c_2_times = load_from_file(prefix + "_Lineare_%d" % (c_2) + suffix) 

    title_name = get_title_name(type)
    
    create_function_plot(c_1_load, c_1_times, title_name + " Lineare (coefficente %d)" % (c_1), str(c_1), "red", save, prefix + "_Lineare_%d_scala_logaritmica" % (c_1) + suffix)
    create_function_plot(c_2_load, c_2_times, title_name + " Lineare (coefficente %d)" % (c_2), str(c_1), "green", save, prefix + "_Lineare_%d_scala_logaritmica" % (c_2) + suffix)

    x_values = [
        c_1_load,
        c_2_load,
    ]

    y_values = [
        [c_1_times, str(c_1), "red"],
        [c_2_times, str(c_2), "green"],
    ]

    create_multiple_function_plot(x_values, y_values, "Confronto tra " + title_name + " Lineare", save, prefix + "_Confronto_Lineare_%d_%d_scala_logaritmica" % (c_1, c_2) + suffix)

if (__name__ == "__main__"):
    #Si è scelto il numero primo 24571 in quanto è un numero di considerevoli dimensioni, e si 
    # trova in un punto mediano circa tra i 2 numeri primi 16384 e 32768.

    #Numero primo 24571

    m = 997
    iter = 500
    interval = 10
    verbose = False
    save = False

    #main_test(m, iter, interval, verbose, save)
    test_linear_different_coefficent(m, 1, 5, iter, interval, verbose, test_type.Success)
    plot_test_linear_different_coefficent(1, 5, save, test_type.Success)
    plt.show()
