#import modules for plotting and math
import matplotlib.pyplot as plt
import numpy as np
#import module for generating random numbers (https://docs.python.org/2/library/random.html)
import random #it's already in numpy so could also do: np.random

# add code here to read in and/or define the x and y values and errors of your data

# plot the data with error bars
plt.errorbar(x_values, y_values, xerr=x_errors, yerr=y_errors, marker='.',markersize=.9,linestyle='none',color='black')

mux = x_values #mean value of the gaussian function (array of measured values)
sigmax =  x_errors #sigma of the gaussian function (array of uncertainties)

muy = y_values #mean value of the gaussian function (array of measured values)
sigmay =  y_errors #sigma of the gaussian function (array of uncertainties)

n_samples = 10 #number of times to repeat the resampling

# make zero arrays the dimensions of your data and the number of samples for storing new (resampled) values
newxdata=np.zeros((len(mux),n_samples))
newydata=np.zeros((len(muy),n_samples))
# print(newxdata)
# print(newydata)

rs = 0 # rs for "resample"
while rs < n_samples:
    # print(rs)
    newxdata[:,rs] = random.gauss(mux,sigmax) #resample x values
    newydata[:,rs] = random.gauss(muy,sigmay) #resample y values
    # print(newxdata[:,rs])
    # print(newydata[:,rs])
    plt.scatter(newxdata[:,rs],newydata[:,rs],color='red') # plot new data (no error bars)
    rs+=1

plt.show()



