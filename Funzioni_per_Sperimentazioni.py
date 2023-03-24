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

def setup_plot(xlabel, ylabel, title, isLog: bool = True):
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
            coordinates[coordinate].append(int(value))
    
    return coordinates

