'''
Fit a line with the orthogonal distance regression (ODR) routine.
'''

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
%matplotlib inline
import scipy.odr

#Define a linear function y = m*x + b
# B is a vector of the parameters.
def f(B, x):
    return B[0]*x + B[1]

# The Model class stores information about the model you wish to fit (in this case a line)
linear_model = scipy.odr.Model(f) 
mydata = scipy.odr.RealData(z, d, sx=z_err, sy=d_err) # Create a data instance

'''
beta is the array of your parameters:
for a line, 
B[0] = slope
B[1] = y-intercept
beta0 is a vector of your initial guesses for the each parameter. 
What do you think the slope should be? What do you think the y-intercept should be?
''' 

beta0 = [70.,0.]
# Instantiate ODR with your data, model and initial parameter estimate.
myodr = scipy.odr.ODR(mydata, linear_model, beta0=beta0) 

# Run the ODR fitting routine.
fit = myodr.run()

# Print out information about the fit.
fit.pprint()

# Get the line parameters in an vector called beta.
# Get the standard deviation of the parameters in a vector called betastd.
beta = fit.beta 
betastd = fit.sd_beta 

# Plot your data and the fitted line.
plt.errorbar((z),d,xerr=z_err,yerr=d_err,marker='.',linestyle='none',color='black')
plt.plot(z,f(beta,z),color='magenta')
plt.title('Linear fit with 2D error analysis')
plt.xlabel('z')
plt.ylabel('d')

print 'slope = ', beta[0]
print 'y intercept = ', beta[1]
