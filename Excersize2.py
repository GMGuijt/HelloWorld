import numpy as np
def calculate_coördinates(x_range: type(list), y_range : type(list), width : type(int)):
    """hierbij gebruiken we de range van de waarde om x aantal waardes te leggen op de assen en een 2d numpy array te maken met de bijbehorende coordinaten"""
    coords = np.array()
    for i in width:
        y = y_range[0] + i*(y_range[1]-y_range[0])/width #bereken width aantal y coordinaten
        X = np.array()
        for j in width:
            x = x_range[0] + j*(x_range[1]-x_range[0])/width #bereken voor elk y coordinaat een width aantal x coordinaten 
            X.append([x,y])
        Y.append(X)
    
    #np array array in array 
    # 1 array is een rij met kolommen, andere plaatje
    #min + (variable * deltaminmax/200)

def calculate_value(x: type(int),y: type(int)):
    """use this function to calculate an iteration of a mandelbrot, if it diverges to infinity return 0"""
    n = 1
    a_n = 0

    while n != 0:
        if n == 100:
            return n = 0
        if abs(a_n) > 2:
            return n
        
        a_n = a_n**2 + complex (x, y)
        n += 1


    #while loop, als n == 100 -> n = 0, abs momenteel nummer > 2 geef n. anders n + 1 & functie a_n

def combine_values(coordinates_graph):
    values = np.array()
    for i in coordinates_graph:
        values_row = np.array()
        for j in i:
            value_one_cord = calculate_value(j[0], j[1])
            values_row.append(value_one_cord)
        values.append(values_row)  


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

def draw_mandel(width):
    """"teken een plaatje van de mandel in een x bij x groote """
    import numpy as np
    import matplotlib.pyplot as plt 
    x_range = [-1.5, 0.5]
    y_range = [-1, 1]

    coördinate_array = calculate_coördinates(x_range, y_range, width)
    values_array = combine_values(coördinate_array)
    color_array = assign_color(values_array)


    
 
    


