# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:09:02 2022

@author: Austin Abreu
"""
import random

def interpolate(n, instances, price):
    
    ## Binary Search Function to locate n within lists
    def locate(n,items):
        L, R = 0, len(items)
        while L < R:
            M = (L+R) // 2
            if items[M] < n:
                L = M + 1
            else:
                R = M
        return L
    
    ## Clean data to ignore prices < 0
    cleanPrice = []
    cleanInstance = []
    for i, val in enumerate(price):
        if val > 0:
            cleanPrice += [val]
            cleanInstance += [instances[i]]
            # These names are verbose but I'll keep them for clarity
    
    ## Single-valued item guard clause
    if isinstance(cleanInstance,int) == True:
            expPrice = cleanPrice
            
    else:     
        
        ## Exterior logic for if there is a direct match in the database
        if n in cleanInstance:
            idx = locate(n, cleanInstance)
            expPrice = cleanPrice[idx]
    
        ## Continue to other cases if no direct match is found
        elif n not in cleanInstance:
            
            #Greater-than Case
            if n > cleanInstance[-1]:
                #Order for x & y should always be descending
                x, y = [cleanInstance[-1],
                        cleanInstance[-2]], [cleanPrice[-1],
                                         cleanPrice[-2]]
                
                slope = (y[0]-y[1]) / (x[0]-x[1])
                horiz = [i for i in range(x[0],n+1)]
                extrapolation = [y[0] + i*slope for i in range(len(horiz))]
                idx = locate(n,horiz)
                
                expPrice = extrapolation[idx]
            
            #Less-than Case
            elif n < cleanInstance[0]:
                x, y = [cleanInstance[1],
                        cleanInstance[0]], [cleanPrice[1],
                                        cleanPrice[0]]
                
                slope = (y[0]-y[1]) / (x[0]-x[1])
                horiz = [i for i in range(0,x[1])]
                extrapolation = [y[1] - i*slope for i in range(len(horiz))]
                idx = locate(n,horiz)
                
                expPrice = extrapolation[idx]
    
            #Interpolation case   
            else:
                #First step is to find index right above n
                idx = locate(n,cleanInstance)
                
                #Continue with interpolation logic
                x, y  = [cleanInstance[idx],
                         cleanInstance[idx-1]], [cleanPrice[idx],
                                             cleanPrice[idx-1]]
                
                slope = (y[0]-y[1]) / (x[0]-x[1])
                horiz = [i for i in range(x[1],x[0])]
                interpolation = [y[1] + i*slope for i in range(len(horiz))]
                
                jdx = locate(n,horiz)
                expPrice = interpolation[jdx]
                
    #I'm not a fan of 'silent' errors, so I've included this exception
    if expPrice <= 0:
        raise ValueError(f'''Projected price less than zero ({expPrice}); 
    consider new parameters''') 
    
    else:
        return f'{expPrice:.2f}'

if __name__ == '__main__':
    # Testing
    n = random.randint(1, 300)
    print(f'Amount of desired instances: {n}')
    
    instances = random.sample(range(0,200), 10)
    instances.sort()
    print(f'Database of Volumes: {instances}')
    
    price = random.sample(range(0,30), 10)
    print(f'Database of price/vol: {price}')
    
    test = interpolate(n, instances, price)
    print(f'Expected Price per volume: {test}')