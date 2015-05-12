#import two very useful libraries and give them common abbreviations
import matplotlib.pyplot as plt
import numpy as np

#use the loadtxt routine to import the CSV file containing all of the information on the orbital motion of the stars around Sgr A*. Each parameter (or error on the parameter) is placed into an array (like a matrix) with a name that corresponds to the given parameter.
index, star, a_arcsec, a_arcsec_err, a_AU, a_AU_err, ecc, ecc_err, inc, inc_err, Omega, Omega_err, omega, omega_err, t_P, t_P_err, period, period_err, m_K, r, mass_BH, mass_BH_err = np.loadtxt('SgrAStarTable.csv', delimiter=',', skiprows=1, unpack=True)

#plt.scatter(a_AU,mass_BH)
plt.errorbar(a_AU[0],mass_BH[0],mass_BH_err[0],marker='.',markersize=.9,linestyle='none',color='black')

#import module for generating random numbers (https://docs.python.org/2/library/random.html)
import random

n_samples = 10
mu = mass_BH
sigma =  mass_BH_err

newdata=np.zeros((n_samples))
print(newdata)

rs = 0
while rs < n_samples:
    print(rs)
    newdata[rs] = random.gauss(mu[0],sigma[0])
    print(newdata[rs])
    plt.scatter(a_AU[0],newdata[rs])
    rs+=1

plt.show()

