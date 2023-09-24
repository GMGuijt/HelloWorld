import numpy as np
import matplotlib.pyplot as plt
def calculate_coördinates(x_range: type(list), y_range : type(list), width : type(int)):
    """hierbij gebruiken we de range van de waarde om x aantal waardes te leggen op de assen en een 2d numpy array te maken met de bijbehorende coordinaten"""
    value_array = np.zeros([width, width, 1])
    for i in range(0, width):
        y = y_range[0] + i*(y_range[1]-y_range[0])/width #bereken width aantal y coordinaten
        X = np.zeros([width, 1])
        for j in range(0, width):
            x = x_range[0] + j*(x_range[1]-x_range[0])/width #bereken voor elk y coordinaat een width aantal x coordinaten
            value = calculate_value(x,y) 
            X[j] = value
        value_array[i] = X
    
    #np array array in array 
    # 1 array is een rij met kolommen, andere plaatje
    #min + (variable * deltaminmax/200)

def calculate_value(x,y):
    """use this function to calculate an iteration of a mandelbrot, if it diverges to infinity return 0"""
    n = 1
    a_n = 0

    while n != 0:
        if n == 100:
            n = 0
        if abs(a_n) > 2:
            breakpoint
        
        a_n = a_n**2 + complex (x, y)
        n += 1
    return n

    #while loop, als n == 100 -> n = 0, abs momenteel nummer > 2 geef n. anders n + 1 & functie a_n

#def combine_values(coordinates_graph, width):
#    values = np.zeros([width, width, 1])
#    for i in range(0, width):
#        itteration = coordinates_graph[i]
#        values_row = zeros([width, 1])
#        for j in range(0, width):
#            coord = itteration[j]
#            value_one_cord = calculate_value(coord[0], coord[1])
#            values_row[j] = value_one_cord
#        values[i] = values_row


def assign_color(all_values):
    """hierbij wordt de diverging index omgezet naar een value op het kleurenschema"""
    # maak waarde 0 tot ? naar 0 tot 255 voor kleur 
    max_n = all_values.max()
    color_values = np.array()
    for i in all_values:
        color_row = np.array()
        for j in i:
            color = (j*255)/max_n
            color_row.append(color)
        color_values.append(color_row)

def plot_image(array_color_values):
    plt.imshow(array_color_values)

def draw_mandel(width):
    """"teken een plaatje van de mandel in een x bij x groote """
    import numpy as np
    import matplotlib.pyplot as plt 
    x_range = [-1.5, 0.5]
    y_range = [-1, 1]

    values_array = calculate_coördinates_values(x_range, y_range, width)
    color_array = assign_color(values_array)

    plot_image(color_array)


draw_mandel(200)
    
 
    


