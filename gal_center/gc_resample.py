#import two very useful libraries and give them common abbreviations
import matplotlib.pyplot as plt
import numpy as np

#use the loadtxt routine to import the CSV file containing all of the information on the orbital motion of the stars around Sgr A*. Each parameter (or error on the parameter) is placed into an array (like a matrix) with a name that corresponds to the given parameter.
index, star, a_arcsec, a_arcsec_err, a_AU, a_AU_err, ecc, ecc_err, inc, inc_err, Omega, Omega_err, omega, omega_err, t_P, t_P_err, period, period_err, m_K, r, mass_BH, mass_BH_err = np.loadtxt('SgrAStarTable.csv', delimiter=',', skiprows=1, unpack=True)

#individual values of each array can be called using the index in square brackets
print(a_AU[0],period[0],mass_BH[0])

#plt.scatter(a_AU,mass_BH)
#plt.errorbar(period, a_arcsec, xerr=period_err, yerr=a_arcsec_err, marker='.',markersize=.9,linestyle='none',color='black')
plt.errorbar(period, a_AU, xerr=period_err, yerr=a_AU_err, marker='.',markersize=.9,linestyle='none',color='black')
plt.xlabel("Period (years)")
plt.ylabel("Semi-major Axis (AU)")
plt.show()


plt.scatter(period**2.,a_AU**3,color='black') #but what are the uncertainties?
plt.xlabel("Period^2 (years)")
plt.ylabel("Semi-major Axis^3 (AU)")
plt.show()

from scipy.optimize import curve_fit
import scipy.odr

def f(x, A, B): # this is your 'straight line' y=f(x)
    return A*x + B

A,B = curve_fit(f,period**2.,a_AU**3)[0] # fit, xdata, ydata
plt.plot(period**2.,f(period**2.,A,B),color='black')

#import module for generating random numbers (https://docs.python.org/2/library/random.html)
import random #it's already in numpy so could also do: np.random

mux = period #mean value of the gaussian function (array of measured values)
sigmax =  period_err #sigma of the gaussian function (array of uncertainties)

muy = a_AU #mean value of the gaussian function (array of measured values)
sigmay =  a_AU_err #sigma of the gaussian function (array of uncertainties)

n_samples = 100 #number of times to repeat the resampling
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
    # print(newxdata[:,rs])
    # print(newxdata[:,rs])
    A[rs],B[rs] = curve_fit(f,newxdata[:,rs]**2.,newydata[:,rs]**3)[0] # fit, xdata, ydata
    plt.scatter(newxdata[:,rs]**2.,newydata[:,rs]**3.,color='red')
    plt.plot(newxdata[:,rs]**2.,f(newxdata[:,rs]**2.,A[rs],B[rs]),color='green')
    rs+=1

plt.show()

print(np.mean(A),np.std(A))
