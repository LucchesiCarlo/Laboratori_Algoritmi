from matplotlib import pyplot as plt

from Codice.Open_Hash import *
from Funzioni_per_Sperimentazioni import *

def main_test(m, iter, interval, verbose, save):
    print("Esperiementi sulla ricerca con successo.")
    execute_test(m, closest_two_power(m), iter, interval, verbose, test_type.Success)
    process_plots(save, test_type.Success)
    print("==================================================")

    print("Esperiementi sulla ricerca con insuccesso.")
    execute_test(m, closest_two_power(m), iter, interval, verbose, test_type.Fail)
    process_plots(save, test_type.Fail)
    print("==================================================")

    print("Esperiementi sull'inserimento.")
    execute_test(m, closest_two_power(m), iter, interval, verbose, test_type.Insert)
    process_plots(save, test_type.Insert)


def test_linear_different_coefficent(m: int, c_1: int, c_2: int, iter: int, interval: int, verbose: bool, test: test_type, suffix: str = ""):

    hash_c_1 = open_hash(m, hash_type.Linear, c_1)
    hash_c_2 = open_hash(m, hash_type.Linear, c_2)
    
    c_1_load = []
    c_1_times = []
    c_2_load = []
    c_2_times = []

    prefix = get_prefix_name(test)

    if(test == test_type.Success):
        c_1_load, c_1_times = search_test(hash_c_1, test_type.Success, iter, interval, verbose)
        c_2_load, c_2_times = search_test(hash_c_2, test_type.Success, iter, interval, verbose)
    elif(test == test_type.Fail):
        c_1_load, c_1_times = search_test(hash_c_1, test_type.Fail, iter, interval, verbose)
        c_2_load, c_2_times = search_test(hash_c_2, test_type.Fail, iter, interval, verbose)
    elif(test == test_type.Insert):
        c_1_load, c_1_times = insert_test(hash_c_1, iter, interval, verbose)
        c_2_load, c_2_times = insert_test(hash_c_2, iter, interval, verbose)

    save_on_file(c_1_load, c_1_times, prefix + "_Lineare_c_%d" % (c_1) + suffix)
    save_on_file(c_2_load, c_2_times, prefix + "_Lineare_c_%d" % (c_2) + suffix)

def plot_test_linear_different_coefficent(c_1: int, c_2: int,save: bool, test: test_type, suffix: str = ""):

    prefix = get_prefix_name(test)
    
    c_1_load, c_1_times = load_from_file(prefix + "_Lineare_c_%d" % (c_1) + suffix)
    c_2_load, c_2_times = load_from_file(prefix + "_Lineare_c_%d" % (c_2) + suffix) 

    title_name = get_title_name(test)
    
    create_function_plot(c_1_load, c_1_times, title_name + " Lineare (coefficente %d)" % (c_1), str(c_1), "red", save, prefix + "_Lineare_c%d_scala_logaritmica" % (c_1) + suffix)
    create_function_plot(c_2_load, c_2_times, title_name + " Lineare (coefficente %d)" % (c_2), str(c_2), "green", save, prefix + "_Lineare_c%d_scala_logaritmica" % (c_2) + suffix)

    x_values = [
        c_1_load,
        c_2_load,
    ]

    y_values = [
        [c_1_times, str(c_1), "red"],
        [c_2_times, str(c_2), "green"],
    ]

    create_multiple_function_plot(x_values, y_values, "Confronto tra " + title_name + " Lineare", save, prefix + "_Confronto_Lineare_c%d_c%d_scala_logaritmica" % (c_1, c_2) + suffix)

def test_different_dimensions(m_1: int, m_2: int, iter: int, interval: int, verbose: bool, hash: hash_type, test: test_type, suffix: str = ""):

    hash_m_1 = 0
    hash_m_2 = 0

    if(hash == hash_type.Quadratic):
        hash_m_1 = open_hash(m_1, hash_type.Quadratic, 0.5, 0.5)
        hash_m_2 = open_hash(m_2, hash_type.Quadratic, 0.5, 0.5)
    else:
        hash_m_1 = open_hash(m_1, hash)
        hash_m_2 = open_hash(m_2, hash)
        
    m_1_load = []
    m_1_times = []
    m_2_load = []
    m_2_times = []

    prefix = get_prefix_name(test)

    if(test == test_type.Success):
        m_1_load, m_1_times = search_test(hash_m_1, test_type.Success, iter, interval, verbose)
        m_2_load, m_2_times = search_test(hash_m_2, test_type.Success, iter, interval, verbose)
    elif(test == test_type.Fail):
        m_1_load, m_1_times = search_test(hash_m_1, test_type.Fail, iter, interval, verbose)
        m_2_load, m_2_times = search_test(hash_m_2, test_type.Fail, iter, interval, verbose)
    elif(test == test_type.Insert):
        m_1_load, m_1_times = insert_test(hash_m_1, iter, interval, verbose)
        m_2_load, m_2_times = insert_test(hash_m_2, iter, interval, verbose)

    exploration = get_exploration_name(hash)

    save_on_file(m_1_load, m_1_times, prefix + "_" + exploration + "_d_%d" % (m_1) + suffix)
    save_on_file(m_2_load, m_2_times, prefix + "_" + exploration + "_d_%d" % (m_2) + suffix)

def plot_test_different_dimensions(m_1: int, m_2: int, save: bool, hash: hash_type, test: test_type, suffix: str = ""):

    prefix = get_prefix_name(test)
    exploration = get_exploration_name(hash)
    title_name = get_title_name(test)
    
    m_1_load, m_1_times = load_from_file(prefix + "_" + exploration + "_d_%d" % m_1 + suffix)
    m_2_load, m_2_times = load_from_file(prefix + "_" + exploration + "_d_%d" % m_2 + suffix) 

    title_name = get_title_name(test)
    
    create_function_plot(m_1_load, m_1_times, title_name + " " + exploration + " (dimensione %d)" % m_1, str(m_1), "red", save, prefix + "_" + exploration + "_d%d_scala_logaritmica" % m_1 + suffix)
    create_function_plot(m_2_load, m_2_times, title_name + " " + exploration + " (dimensione %d)" % m_2, str(m_2), "green", save, prefix + "_" + exploration + "_d%d_scala_logaritmica" % m_2 + suffix)

    x_values = [
        m_1_load,
        m_2_load,
    ]

    y_values = [
        [m_1_times, str(m_1), "red"],
        [m_2_times, str(m_2), "green"],
    ]

    create_multiple_function_plot(x_values, y_values, "Confronto tra " + title_name + " " + exploration, save, prefix + "_Confronto_" + exploration + "_d%d_d%d_scala_logaritmica" % (m_1, m_2) + suffix)

def test_load_factor(m: int, type: test_type, iter: int, verbose: bool, suffix: str = ""):
    prefix = get_prefix_name(type)

    hash_linear = open_hash(m, hash_type.Linear)
    hash_quadratic = open_hash(closest_two_power(m), hash_type.Quadratic, 0.5)
    hash_double = open_hash(m, hash_type.Double)

    times = [[0 for j in range(3)] for i in range(11)]
    
    for i in range(11):
        a = i / 10.
        times [i][0] = load_factor_experiments(hash_linear, a, iter, type)
        times [i][1] = load_factor_experiments(hash_quadratic, a, iter, type)
        times [i][2] = load_factor_experiments(hash_double, a, iter, type)
        if(verbose):
            print("%.2f%% Test completati." % (i * 10))
    
    file = open("Risultati/" + prefix + "_Fattori_Caricamento" + suffix + ".txt", "w")

    for i in range(11):
        for j in range(3):
            file.write(str(times[i][j]) + ", ")
        file.write("\n")

    file.close()

if (__name__ == "__main__"):
    #Si è scelto il numero primo 24571 in quanto è un numero di considerevoli dimensioni, e si 
    # trova in un punto mediano circa tra i 2 numeri primi 16384 e 32768.

    #Numero primo 24571
    test = 0
    test_list = [0, 0, 0, 0]
    ok = False
    while(not ok):    
        ok = True
        test = input("Inserisci il numero la cui codifica bianaria indica quali test fare (exit con 0): ")
        test = test.strip()
        if(len(test) > len(test_list)):
            print("Errore! Hai insrito un numero non valido.")
            ok = False
        else:
            add = len(test_list) - len(test)
            if(add >  0):
                test = test + "0" * add
            for i in range(len(test)):
                if(test[i] == "1"):
                    test_list[i] = 1
                elif(test[i] == "0"):
                    test_list[i] = 0
                else:
                    print("Errore! Hai insrito un numero non valido.")
                    ok = False
    if(int(test) == 0):
        exit()


    m_1 = 997
    m_2 = 10007
    iter = 500
    interval = 50
    verbose = True
    save = False

    if(test_list[0] == 1):
        main_test(m_1, iter, interval, verbose, save)

    if(test_list[1] == 1):
        test_linear_different_coefficent(m_1, 1, 5, iter, interval, verbose, test_type.Success)
        plot_test_linear_different_coefficent(1, 5, save, test_type.Success)

    if(test_list[2] == 1):
        test_different_dimensions(m_1, m_2, iter, interval, verbose, hash_type.Linear, test_type.Fail, "_suffisso")
        plot_test_different_dimensions(m_1, m_2, save, hash_type.Linear, test_type.Fail, "_suffisso")

    if(test_list[3] == 1):
        iter_2 = 1000
        print()
        test_load_factor(m_1, test_type.Success, verbose, iter_2)
        test_load_factor(m_1, test_type.Fail, verbose, iter_2)
        test_load_factor(m_1, test_type.Insert, verbose, iter_2)

    plt.show()
