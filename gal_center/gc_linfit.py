#import two very useful libraries and give them common abbreviations
import matplotlib.pyplot as plt
import numpy as np

# code to read in GC data goes here

# fit a line to a^3 (in AU) versus P^2 (in years) 
from scipy.optimize import curve_fit
import scipy.odr

def f(x, A, B): #define a 'straight line' y=f(x)=A*x + B function
    return A*x + B

A,B = curve_fit(f,period**2.,a_AU**3)[0] # use curve_fit to fit your function using xdata & ydata, reurning A & B
plt.plot(period**2.,f(period**2.,A,B),color='black') # plot the fit

plt.show()


