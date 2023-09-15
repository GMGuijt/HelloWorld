
def return_function_mandel(x,y, a_n_vorige):
    """use this function to calculate an itteration of a mandelbot, if it diverges to infinity return 0"""
       a_n = ((a_n_vorige)**2) + complex(x,y)
       if abs(a_n) > 100:
            a_n = 0
        
        

def draw_mandel(width):
    """"teken een plaatje van de mandel in een x bij x groote """
    import numpy as np
    import matplotlib.pyplot as plt 
    x_range = [-1.5, 0.5]
    y_range = [-1, -1]

    #gebruik diverging_index voor kleur
    


    
 
    


