# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:56:52 2022

@author: Austin Abreu
"""

def norm(x, *, order = 2):
    #Default is the Euclidean Norm
    
    if isinstance(order,int) is False:
        raise Exception('Please provide an integer dimension for the norm')
    
    step = [i**order for i in x]
    out = sum(step)**(1/order)
    
    return out