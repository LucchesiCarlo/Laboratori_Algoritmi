import random
import math
from matplotlib import pyplot as plt
from timeit import default_timer as timer
from matplotlib.ticker import FormatStrFormatter


from Codice.Open_Hash import *

class test_type(IntEnum):
    Success = 1
    Fail = 2
    Mixed = 3

"""
In questo esperimento adremo a verificare il funzionamento di una tabella hash 
con eplorazione lineare.
"""
def search_test(hash: open_hash, type: test_type, iterations: int = 1, interval:int= 1, verbose: bool = False, percent: float = 10):

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
                if(type == test_type.Success):
                    to_find = random.choice(inserted_elements)
                elif(type == test_type.Fail):
                    to_find = random.choice(not_inserted_elements)
                elif(type == test_type.Mixed):
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

def search_experiments(m, m_q, iter, interval, verbose, type: test_type,  suffix = ""):
    prefix = ""

    if(type == test_type.Success):
        prefix = "Successo"
    elif(type == test_type.Fail):
        prefix = "Insuccesso"
    elif(type == test_type.Mixed):
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

def create_function_plot(x, y, title, label, color, save, file_name = "", annotate = True, isLog = True):
    setup_plot("Fattore di Caricamento", "Tempo (ms)", title, isLog)
    plt.plot(x, y, color + "o-", markersize = 2, label = label)
    if(annotate):
        plt.annotate(text = "%.2f" % (y[-1]), xy = (x[-1], y[-1]), xytext=(x[-1] * 0.9, y[-1] * 0.8))
    generate_plot(save, file_name)

def create_bar_plot(indexes, x_values, y_values, title, width, save, file_name = "", isLog = True):
    setup_plot("Raggruppamenti fattore di Caricamento", "Tempo raggruppato", title, isLog)
    for i in range(len(y_values)):
        average = generate_bar_valuess(x_values[i], y_values[i][0])
        num_values = len(average)
        plt.bar([j + i * width for j in range(num_values)], average, width, label = y_values[i][1], color = y_values[i][2])

    offset = int(len(y_values) / float(2) - 0.5)
    plt.xticks([i + offset * width for i in range(10)], indexes)
    
    generate_plot(save, file_name)

def generate_bar_values(xfirst, yfirst, xsecond, ysecond, xthird, ythird):
    first_average = [0] * 10
    first_numbers = [0] * 10
    second_average = [0] * 10
    second_numbers = [0] * 10
    third_average = [0] * 10
    third_numbers = [0] * 10

    for i, j in zip(xfirst, yfirst):
        i *= 10
        index = math.floor(i / 1)
        if(index == 10):
            index = 9
        first_average[index] += j
        first_numbers[index] += 1

    for i, j in zip(xsecond, ysecond):
        i *= 10
        index = math.floor(i / 1)
        if(index == 10):
            index = 9
        second_average[index] += j
        second_numbers[index] += 1

    for i, j in zip(xthird, ythird):
        i *= 10
        index = math.floor(i / 1)
        if(index == 10):
            index = 9
        third_average[index] += j
        third_numbers[index] += 1

    for i in range(10):
        if(first_numbers[i] != 0):
            first_average[i] /= first_numbers[i]
        if(second_numbers[i] != 0):
            second_average[i] /= second_numbers[i]
        if(third_numbers[i] != 0):
            third_average[i] /= third_numbers[i]

    return first_average, second_average, third_average


def generate_bar_valuess(x, y):
    average = [0] * 10
    numbers = [0] * 10

    for i, j in zip(x, y):
        i *= 10
        index = math.floor(i / 1)
        if(index == 10):
            index = 9
        average[index] += j
        numbers[index] += 1


    for i in range(10):
        if(numbers[i] != 0):
            average[i] /= numbers[i]

    return average

def setup_plot(xlabel , ylabel, title, isLog: bool = True):
    plt.figure()
    ax = plt.gca()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    if(isLog):
        plt.yscale("log")
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

def generate_plot(save: bool = False, file_name = "Plot"):
    plt.legend(loc = 'upper left')
    if(save):
        plt.savefig("./Relazione/Immagini/" + file_name + ".png")
    plt.draw()

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
