#import two very useful libraries and give them common abbreviations
import matplotlib.pyplot as plt
import numpy as np

#use the loadtxt routine to import the CSV file containing all of the information on the orbital motion of the stars around Sgr A*. Each parameter (or error on the parameter) is placed into an array (like a matrix) with a name that corresponds to the given parameter.
index, star, a_arcsec, a_arcsec_err, a_AU, a_AU_err, ecc, ecc_err, inc, inc_err, Omega, Omega_err, omega, omega_err, t_P, t_P_err, period, period_err, m_K, r, mass_BH, mass_BH_err = np.loadtxt('SgrAStarTable.csv', delimiter=',', skiprows=1, unpack=True)

#individual values of each array can be called using the index in square brackets
print(a_AU[0],period[0],mass_BH[0])
