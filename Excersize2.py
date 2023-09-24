import numpy as np
import matplotlib.pyplot as plt
def calculate_coördinates_values(x_range, y_range, width):
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
    return value_array

def calculate_value(x,y):
    """use this function to calculate an iteration of a mandelbrot, if it diverges to infinity return 0"""
    n = 1
    a_n = 0
    end = False

    while end == False:
        if n == 100:
            n = 0
            end = True
        if abs(a_n) > 2:
            end = True
        
        a_n = a_n**2 + complex (x, y)
        n += 1
    return n

def plot_image(array_color_values):
    plt.imshow(array_color_values)
    plt.show()

def draw_mandel(width):
    """"teken een plaatje van de mandel in een x bij x groote """
    import numpy as np
    import matplotlib.pyplot as plt 
    x_range = [-1.5, 0.5]
    y_range = [-1, 1]

    values_array = calculate_coördinates_values(x_range, y_range, width)

    plot_image(values_array)

draw_mandel(200)
    
 
    


