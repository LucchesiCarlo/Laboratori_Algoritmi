import math
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def create_function_plot(x, y, title: str, label: str, color: str, save: bool, file_name: str = "", annotate: bool = True, is_log: bool = True):
    setup_plot("Fattore di Caricamento", "Tempo (ms)", title, is_log)
    plt.plot(x, y, color = color, marker = "o", markersize = 2, label = label)
    if(annotate):
        plt.annotate(text = "%.2f" % (y[-1]), xy = (x[-1], y[-1]), xytext=(x[-1] * 0.9, y[-1] * 0.8))
    generate_plot(save, file_name)

def create_multiple_function_plot(x_values, y_values, title: str, save: bool, file_name: str = "", is_log: bool = True):
    setup_plot("Fattore di Caricamento", "Tempo (ms)", title, is_log)
    for i in range(len(y_values)):
        x ,y = x_values[i], y_values[i][0]
        plt.plot(x, y, color = y_values[i][2], marker = "o", markersize = 2, label = y_values[i][1])
    generate_plot(save, file_name)

def create_bar_plot(x_values, y_values, title: str, width: float, save: bool = False, file_name: str = "", indexes = [i/10 for i in range(10)], is_log: bool = True):
    setup_plot("Raggruppamenti fattore di Caricamento", "Tempo raggruppato", title, is_log)
    for i in range(len(y_values)):
        average = generate_bar_values(x_values[i], y_values[i][0])
        num_values = len(average)
        plt.bar([j + i * width for j in range(num_values)], average, width, label = y_values[i][1], color = y_values[i][2])

    offset = int(len(y_values) / float(2) - 0.5)
    plt.xticks([i + offset * width for i in range(len(indexes))], indexes)
    
    generate_plot(save, file_name)

def generate_bar_values(x, y):
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

def setup_plot(xlabel: str, ylabel: str, title: str, is_log: bool = True):
    plt.figure()
    ax = plt.gca()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    if(is_log):
        plt.yscale("log")
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

def generate_plot(save: bool = False, file_name: str = "Plot"):
    plt.legend(loc = 'upper left')
    if(save):
        plt.savefig("./Relazione/Immagini/" + file_name + ".png")
    plt.draw()
