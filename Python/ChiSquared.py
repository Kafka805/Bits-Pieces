# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 19:18:03 2022

@author: Austin Abreu
"""
import scipy.stat as stat

# Chi^2 Values 
def Chi2Values(fitfunction, xdata, ydata, fitparams, ysigma):
    # Computes ChiSquared and related metrics as a way of testing the 
    # goodness of fit for observed data to hypothesized data.
    yfit = fitfunction(xdata, *fitparams)

    chisq = sum( (ydata - yfit)**2 / ysigma**2 )

    ndf = len(ydata)-len(fitparams)

    chisq_reduced = chisq/float(ndf)

    cdf = stat.chi2.cdf(chisq, df = ndf)

    pvalue = 1-cdf

    print('Chi-square: ',chisq)
    print('Degrees of freedom: ',ndf)
    print('Reduced chi-square: ',chisq_reduced)
    print('CDF: ', cdf)
    print('p-test value (1 Tail bc not symmetric): ',pvalue)