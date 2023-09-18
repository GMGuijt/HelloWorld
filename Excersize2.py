
def return_function_mandel(x,y, a_n_vorige):
    """use this function to calculate an iteration of a mandelbrot, if it diverges to infinity return 0"""
    #for n 
    n = 0 

    #while loop, als n == 100 -> n = 0, abs momenteel nummer > 2 geef n. anders n + 1 & functie a_n


    a_n = ((a_n_vorige)**2) + complex(x,y)

    #np array array in array 
    # 1 array is een rij met kolommen, andere plaatje
    # min + (variable * deltaminmax/200)
    # maak waarde 0 tot ? naar 0 tot 255 voor kleur 


        
        

def draw_mandel(width):
    """"teken een plaatje van de mandel in een x bij x groote """
    import numpy as np
    import matplotlib.pyplot as plt 
    x_range = [-1.5, 0.5]
    y_range = [-1, -1]

    #gebruik diverging_index voor kleur
    #np array met 40000 itteraties voor elke uitkomst
    


    
 
    


