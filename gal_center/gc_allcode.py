#import two very useful libraries and give them common abbreviations
import matplotlib.pyplot as plt
import numpy as np

#use the loadtxt routine to import the CSV file containing all of the information on the orbital motion of the stars around Sgr A*. Each parameter (or error on the parameter) is placed into an array (like a matrix) with a name that corresponds to the given parameter.
index, star, a_arcsec, a_arcsec_err, a_AU, a_AU_err, ecc, ecc_err, inc, inc_err, Omega, Omega_err, omega, omega_err, t_P, t_P_err, period, period_err, m_K, r, mass_BH, mass_BH_err = np.loadtxt('SgrAStarTable.csv', delimiter=',', skiprows=1, unpack=True)

#individual values of each array can be called using the index in square brackets
print(a_AU[0],period[0],mass_BH[0])

#plot a (in AU) versus P (in years) with error bars
plt.errorbar(period, a_AU, xerr=period_err, yerr=a_AU_err, marker='.',markersize=.9,linestyle='none',color='black')
plt.xlabel("Period (years)")
plt.ylabel("Semi-major Axis (AU)")
plt.show()

# plot a^3 (in AU) versus P^2 (in years) with error bars
plt.scatter(period**2.,a_AU**3,color='black') # but what are the uncertainties?
p2_err = np.abs(2 * period * period_err) # propogate the errors
a3_err = np.abs(3 * a_AU**2 * a_AU_err) # propogate the errors
plt.errorbar(period**2., a_AU**3., xerr=p2_err, yerr=a3_err, marker='.',markersize=.9,linestyle='none',color='black')
plt.xlabel("Period^2 (years)")
plt.ylabel("Semi-major Axis^3 (AU)")
plt.show()


# fit a line to a^3 (in AU) versus P^2 (in years) 
from scipy.optimize import curve_fit
import scipy.odr

def f(x, A, B): #define a 'straight line' y=f(x)=A*x + B function
    return A*x + B

A,B = curve_fit(f,period**2.,a_AU**3)[0] # use curve_fit to fit your function using xdata & ydata, reurning A & B
plt.plot(period**2.,f(period**2.,A,B),color='black') # plot the fit


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
