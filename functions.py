# Created on 10/3/13
# Author: Taylor Cathcart
# definitions for various interesting physics functions
# for use with writers.py

# imports
from math import sin, cos, sqrt
import math

# function to evaluate series approximating a sawtooth waveform
# n - int
# x - float
# n represents max of j
def sawtooth(n, x):
    result = 0
   
    for j in range(1, n + 1):
        result += (1.0 / j) * sin(j * x)
   
    return result

# function to evaluate square waveform
# n - int
# x - float
def square(n, x):
    result = 0
    
    for j in range(1, n + 1):
        result += (1.0 / (2 * j - 1)) * sin((2 * j - 1) * x)
        
    return result

# function for wave packet series
# n - int
# kc - float/int, dominant wavenumber
# deltak - float/int, wavenumber resolution
# x - current position
def packet(n, x, kc, deltak):
    result = 0
    j0 = (float(kc) / deltak) - n
    
    for offset in range(2 * n + 1):  
        j = j0 + offset
        
        # compute and add y value
        amplitude = math.exp((-1.0 / 4) * (j * deltak - kc) * (j * deltak - kc))
        y = amplitude * cos(j * deltak * x)
        
        result += y
        
    result = result / sqrt(4 * math.pi)
    
    return result

# function for computing time-averaged electric field at a given theta
# bign - int
# theta - float
# slitwidth - float
# wavenum - float/int
def computeE(bign, theta, slitwidth, wavenum):
    
    E = 0
    
    for n in range(1, (bign / 2) + 1):
        
        term = (n - .5) * ((slitwidth * wavenum) / bign) * sin(theta)
        E += cos(term)
        
    E = E * (float(2) / bign)
    
    return E

# intensity defined as square of time-averaged electric field
# function to compute intensity as function of theta for single-slit diffraction
# bign - int
# theta - float
# slitwidth - float
# wavenum = float/int
def diffraction(bign, theta, slitwidth, wavenum):
    x = computeE(bign, theta, slitwidth, wavenum)
    return x * x
