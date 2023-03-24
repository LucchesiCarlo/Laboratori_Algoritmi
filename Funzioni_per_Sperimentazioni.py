import random
import math
from timeit import default_timer as timer
from Funzioni_per_Grafici import *

from Codice.Open_Hash import *

class search_test_type(IntEnum):
    Success = 1
    Fail = 2
    Mixed = 3

class test_type(IntEnum):
    Success = 1
    Fail = 2
    Insert = 3

def execute_test(m, m_q, iter, interval, verbose, type, suffix = ""):
    total_time = 0
    
    if(type == test_type.Success):
        total_time = search_experiments(m, m_q, iter, interval, verbose, search_test_type.Success, suffix)
    elif(type == test_type.Fail):
        total_time = search_experiments(m, m_q, iter, interval, verbose, search_test_type.Fail, suffix)
    elif(type == test_type.Insert):
        total_time = insert_experiments(m, m_q, iter, interval, verbose, suffix)

    return total_time

def process_plots(save, type, suffix = ""):
    
    test_prefix = ""

    if(type == test_type.Success):
        test_prefix = "Successo"
    elif(type == test_type.Fail):
        test_prefix = "Insuccesso"
    elif(type == test_type.Insert):
        test_prefix = "Inserimento"

    x_linear, y_linear = load_from_file("Risultati/" + test_prefix + "_Lineare" + suffix + ".txt")
    
    x_quadratic, y_quadratic = load_from_file("Risultati/" + test_prefix + "_Quadratico" + suffix + ".txt")

    x_double, y_double = load_from_file("Risultati/" + test_prefix + "_Doppio" + suffix + ".txt")    

    l_minimum = min(y_linear)
    
    q_minimum = min(y_quadratic)
    
    d_minimum = min(y_double)

    min_registered = min(l_minimum, q_minimum, d_minimum)

    x_values = [
        x_linear,
        x_quadratic,
        x_double
    ]

    y_values = [
        [y_linear, "Lineare", "red"],
        [y_quadratic, "Quadratico", "green"],
        [y_double, "Doppio", "blue"],
    ]

    num_elements = 20
    x_comparison = []
    y_comparison =[]
    for i in range(num_elements):
        i *= 1 / num_elements
        if(type == test_type.Insert and i != 0):
            x_comparison.append(i)
            y_comparison.append(math.log2(1 / (1 - i)) / i)
        elif(type != test_type.Insert):
            x_comparison.append(i)
            y_comparison.append(1 / (1 - i))


    min_comaprison = min(y_comparison)

    for i in range(len(x_comparison)):
        y_comparison[i] *= min_registered / min_comaprison

    title_name = ""
    
    if(type == test_type.Success):
        title_name = "Ricerca con Successo"
    elif(type == test_type.Fail):
        title_name = "Ricerca con Insuccesso"    
    elif(type == test_type.Insert):
        title_name = "Inserimento"
   
    create_function_plot(x_linear, y_linear, title_name + " Lineare", "Lineare", "r", save, "Inserimento_Lineare_scala_lineare", False, False)

    create_function_plot(x_linear, y_linear, title_name + " Lineare", "Lineare", "r", save, "Inserimento_Lineare_scala_logaritmica")

    create_function_plot(x_quadratic, y_quadratic, title_name + " Quadratica", "Quadratica", "g", save, "Inserimento_Quadratico_scala_logaritmica")

    create_function_plot(x_double, y_double, title_name + " Doppio Hash", "Doppio", "b", save, "Inserimento_Doppio_scala_logaritmica")

    setup_plot("Fattore di Caricamento ", "Tempo Asintotico ", title_name + " Stima Asintotica")
    plt.plot(x_comparison, y_comparison, "ko-", markersize = 2, label="Funzione")
    generate_plot(save, "Inserimento_Asintotica_scala_logaritmica")

    create_multiple_function_plot(x_values, y_values, "Confronto tra " + title_name, save, "Inserimento_Confronto_scala_logaritmica", False)
    
    x_values_expanded = [
        x_linear,
        x_quadratic,
        x_double,
        x_comparison
    ]

    y_values_expanded = [
        [y_linear, "Lineare", "red"],
        [y_quadratic, "Quadratico", "green"],
        [y_double, "Doppio", "blue"],
        [y_comparison, "Funzione", "black"]
    ]

    create_multiple_function_plot(x_values_expanded, y_values_expanded, "Confronto tra " + title_name + " con Stima asintotica", save, test_prefix + "_Confronto_scala_logaritmica", False)

    create_bar_plot(x_values, y_values, "Confronto tra " + title_name, 0.27, save, "Inserimento_Confronto_barre_scala_logaritmica")




"""
In questo esperimento adremo a verificare il funzionamento di una tabella hash 
con eplorazione lineare.
"""
def search_test(hash: open_hash, type: search_test_type, iterations: int = 1, interval:int= 1, verbose: bool = False, percent: float = 10):

    inserted_elements = []
    times = []
    load_factors = []

    #Inoltre qui si farà la ricerca di soli valori presenti.
    not_inserted_elements = list(range(0, hash.M * 10))

    milestone = math.ceil(hash.M / 100 * percent)
    for i in range(hash.M):
        x = random.choice(not_inserted_elements)
        hash.insert(x)
        inserted_elements.append(x)
        not_inserted_elements.remove(x)
        if((i - (hash.M - 1) % interval) % interval == 0):
            final_time = 0
            for j in range(iterations):
                to_find = 0
                if(type == search_test_type.Success):
                    to_find = random.choice(inserted_elements)
                elif(type == search_test_type.Fail):
                    to_find = random.choice(not_inserted_elements)
                elif(type == search_test_type.Mixed):
                    if(random.random() < 0.5):
                       to_find = random.choice(inserted_elements)
                    else:
                        to_find = random.choice(not_inserted_elements)

                time_start = timer()
                hash.search(to_find)
                time_end = timer()
                final_time += time_end - time_start
            final_time /= iterations
            times.append(final_time * 1000)
            load_factors.append(hash.load_factor())

        if(verbose and i % milestone == 0):
            print(i / milestone * percent, "% Test completati.")
    if (verbose):
        print("Test conclusi")

    return (load_factors, times)

def insert_test(hash: open_hash, iterations: int = 1, interval:int = 1, verbose: bool = False, percent: float = 10):

    times = []
    load_factors = []

    #Inoltre qui si farà la ricerca di soli valori presenti.
    not_inserted_elements = list(range(0, hash.M * 10))

    milestone = math.ceil(hash.M / 100 * percent)
    for i in range(hash.M):
        x = random.choice(not_inserted_elements)
        hash.insert(x)
        if((i - (hash.M - 1) % interval) % interval == 0):
            final_time = 0
            for j in range(iterations):
                hash.delete(x)
                x = random.choice(not_inserted_elements)
                time_start = timer()
                hash.insert(x)
                time_end = timer()
                final_time += time_end - time_start

            final_time /= iterations
            times.append(final_time * 1000)
            load_factors.append(hash.load_factor())

        not_inserted_elements.remove(x)
        if(verbose and i % milestone == 0):
            print(i / milestone * percent, "% Test completati.")
    if (verbose):
        print("Test conclusi")

    return (load_factors, times)

def search_experiments(m, m_q, iter, interval, verbose, type: search_test_type,  suffix = ""):
    prefix = ""

    if(type == search_test_type.Success):
        prefix = "Successo"
    elif(type == search_test_type.Fail):
        prefix = "Insuccesso"
    elif(type == search_test_type.Mixed):
        prefix == "Misto"

    hashLinear = open_hash(m, hash_type.Linear)
    hashQuadratic = open_hash(m_q, hash_type.Quadratic, 0.5, 0.5)
    hashDouble = open_hash(m, hash_type.Double)

    start = timer()
    if(verbose):
        print("Ricerca Lineare " + prefix)
    xlinear, ylinear = search_test(hashLinear, type, iter, interval, verbose)

    if(verbose):
        print("Ricerca Quadratico " + prefix)
    xquadratic, yquadratic = search_test(hashQuadratic, type, iter, interval, verbose)

    if(verbose):
        print("Ricerca Doppio " + prefix)
    xdouble, ydouble = search_test(hashDouble, type, iter, interval, verbose)

    end = timer()


    save_on_file(xlinear, ylinear, "Risultati/" + prefix +"_Lineare" + suffix + ".txt")
    save_on_file(xquadratic, yquadratic, "Risultati/" + prefix +"_Quadratico" + suffix + ".txt")
    save_on_file(xdouble, ydouble, "Risultati/" + prefix + "_Doppio" + suffix + ".txt")

    return end - start

def insert_experiments(m, m_q, iter, interval, verbose,  suffix = ""):
    start = timer()

    hashLinear = open_hash(m, hash_type.Linear)
    hashQuadratic = open_hash(m_q, hash_type.Quadratic, 0.5, 0.5)
    hashDouble = open_hash(m, hash_type.Double)

    if(verbose):
        print("Inserimento Lineare")
    xlinear, ylinear = insert_test(hashLinear, iter, interval, verbose)

    if(verbose):
        print("Inserimento Quadratico")
    xquadratic, yquadratic = insert_test(hashQuadratic, iter, interval, verbose)

    if(verbose):
        print("Inserimento Doppio")
    xdouble, ydouble = insert_test(hashDouble, iter, interval, verbose)

    end = timer()

    save_on_file(xlinear, ylinear, "Risultati/Inserimento_Lineare" + suffix + ".txt")
    save_on_file(xquadratic, yquadratic, "Risultati/Inserimento_Quadratico" + suffix + ".txt")
    save_on_file(xdouble, ydouble, "Risultati/Inserimento_Doppio" + suffix + ".txt")

    return end - start

def save_on_file(x, y, file_name):
    file = open(file_name, "w")
    file.write("x = " + str(x) + "\n")
    file.write("y = " + str(y) + "\n")
    file.close()

def load_from_file(file_name):
    
    coordinates = {
        "x" : [],
        "y" : []
    }

    file = open(file_name, "r")
    data = file.readlines()
    for i in range(len(data)):
        array = data[i]

        axis = array.strip().removesuffix("]")

        coordinate = axis[0]
        axis = axis.partition("[")[2]
        elements = axis.split(",")
        for value in elements:
            value = value.strip()
            coordinates[coordinate].append(float(value))
    
    return coordinates["x"], coordinates["y"]

"""
Questa funzione genera come risultato la potenza esatta del 2 più vicina al parametro fornito.
Questo ci serve perchè per poter usare l'eplorazione quadratica nel caso linerare con 
coefficienti 1/2.
"""
def closest_two_power(x: int):
    res = 1
    next = 2
    distance = x - res
    while(distance > abs(x - next)):
        distance = abs(x - next)
        res = next
        next *= 2
    return res
