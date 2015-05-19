''' 
Fit a line parametrized by f=A*x+B using least-squares fitting routine.
'''

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
%matplotlib inline
from scipy.optimize import curve_fi


# Define a function for a line. 
def f(x, A, B): 
    return A*x + B


# Fit your data:
# Input the function, the x-axis data, the y-axis data, and the error on the dependent variable.
# This returns the line parameters A,B
# which are the slope and y-intercept of the line.
A,B = curve_fit(f,z,d,sigma=d_err)[0] 

'''
Note that we fit distance to redshift d(z) instead of 
redshift to distance z(d). 
'''

#Plot the fitted line over the data
plt.errorbar(z, d, xerr=z_err, yerr=d_err, marker='.', linestyle='none', color='black')
plt.plot(z, f(z,A,B), color='magenta')
plt.title('Linear fit with least squares')
plt.xlabel('z')
plt.ylabel('d')

print 'slope = ', A
print 'y intercept = ', B
