#import two very useful libraries and give them common abbreviations
import matplotlib.pyplot as plt
import numpy as np

# code to read in GC data goes here

# resample a and P from within uncertainties and re-fit line to  a^3 (in AU) versus P^2 (in years)

#import module for generating random numbers (https://docs.python.org/2/library/random.html)
import random #it's already in numpy so could also do: np.random

mux = period #mean value of the gaussian function (array of measured values)
sigmax =  period_err #sigma of the gaussian function (array of uncertainties)

muy = a_AU #mean value of the gaussian function (array of measured values)
sigmay =  a_AU_err #sigma of the gaussian function (array of uncertainties)

n_samples = 10 #number of times to repeat the resampling
newxdata=np.zeros((len(mux),n_samples))
newydata=np.zeros((len(muy),n_samples))
A=np.zeros(n_samples)
B=np.zeros(n_samples)
#print(newxdata)
#print(newydata)

rs = 0 # rs for "resample"
while rs < n_samples:
    # print(rs)
    newxdata[:,rs] = random.gauss(mux,sigmax) #resample in x
    newydata[:,rs] = random.gauss(muy,sigmay) #resample in y
    print(newxdata[3,rs])
    print(newydata[3,rs])
    A[rs],B[rs] = curve_fit(f,newxdata[:,rs]**2.,newydata[:,rs]**3)[0] # fit, xdata, ydata
    plt.scatter(newxdata[:,rs]**2.,newydata[:,rs]**3.,color='red')
    plt.plot(newxdata[:,rs]**2.,f(newxdata[:,rs]**2.,A[rs],B[rs]),color='green')
    rs+=1

plt.show()

# examine resampling results
print(np.mean(A),np.std(A))
plt.hist(A, bins=n_samples/10.)
