# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 19:19:37 2022

@author: Austin Abreu
"""
import numpy as np

def regression(*, K, y, n = 1):
    ### INPUTS ###
    # K: Independent variable, X
    # y: Dependent variable for which to determine coefficents
    # n: order of regression, 0 < n <= 3
    # For method see Strang "Introduction to Linear Algebra," 2016, page 218
    ### OUTPUTS ###
    # P@y: the coefficients of the regression, in ascending order
    # C: covariance matrix
    # MSE: Mean-squared error, naive distance of each point from the regression
    ##########################################################################
    
    #Guard Clause
    if isinstance(K, np.ndarray) is False and isinstance(y, np.ndarray) is False:
        K = np.array(K)
        y = np.array(y)
    
    #Switch case for Order of Regression
    if n == 1:
        A = np.array([np.ones(len(K)), K]).T  # [1 K].T
        
    elif n == 2:
        A = np.array([np.ones(len(K)), K, K**2]).T # [1 K K^2].T
        
    elif n == 3:
        A = np.array([np.ones(len(K)), K, K**2, K**3]).T # [1 K K^2 K^3].T
    
    #Perform Regression
    AT_A = A.T @ A 
    P = np.linalg.inv(AT_A) @ A.T
    p = A @ P @ y
    C = P @ P.T
    MSE = sum((y - p)**2/p)
    
    # This is one of my favorite applications of linear algebra
    return P @ y, C, MSE


def error(xVals, errors):
    """
    #Propagates error into regression. See Lyons,"Practical Guide to Data
     Analysis for Physical Science Students," Section 2.4
    ### INPUTS ###
     xVals: 1D array of independent variables
     errors: 1D array of error on Y-VALUES of dataset
    ### OUTPUTS ###
    err_Coeffs: The standard deviation on each coefficient of the regression. 
                Ascending order.
    
    I have to admit that after using this many times and staring at the math for longer,
    I still don't feel like it makes sense...
    """
    #Convert to np array if necessary
    if isinstance(xVals,np.ndarray) is False:
        xVals = np.array(xVals)
    if isinstance(errors,np.ndarray) is False:
        errors = np.array(errors)
    
    #Perform error propagation
    oneBrace = sum(1 / errors)
    xBrace = sum(xVals / errors)
    xCenter = xBrace / oneBrace
    xPrimes = xVals - xCenter
    
    slopeErr = 1/ sum(xPrimes**2 / errors)
    interceptErr = 1 / oneBrace
    
    #Collect coefficients
    err_Coeffs = np.array([np.sqrt(interceptErr), np.sqrt(slopeErr)])
    
    return err_Coeffs