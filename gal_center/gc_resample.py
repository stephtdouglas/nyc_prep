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


plt.scatter(period**2.,a_AU**3) #but what are the uncertainties?
plt.xlabel("Period^2 (years)")
plt.ylabel("Semi-major Axis^3 (AU)")
plt.show()


#import module for generating random numbers (https://docs.python.org/2/library/random.html)
import random #it's already in numpy so could also do: np.random

n_samples = 10 #number of times to repeat the resampling
mu = mass_BH #mean value of the gaussian function (measured value)
sigma =  mass_BH_err #sigma of the gaussian function (uncertainty)

newdata=np.zeros((n_samples))
print(newdata)

rs = 0
while rs < n_samples:
    print(rs)
    newdata[rs] = random.normal(mu[0],sigma[0])
    print(newdata[rs])
    plt.scatter(a_AU[0],newdata[rs])
    rs+=1

plt.show()

