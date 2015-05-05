#!/usr/bin/python

#This is a bit of sample code for you to use as a backbone for your plotting program. It reads in the entire Sgr A* data table and places each column into an array

import matplotlib.pyplot as plt
import numpy as np

index, star, a_arcsec, a_arcsec_err, a_AU, a_AU_err, ecc, ecc_err, inc, inc_err, Omega, Omega_err, omega, omega_err, t_P, t_P_err, period, period_err, m_K, r, mass_BH, mass_BH_err = np.loadtxt('SgrAStarTable.csv', delimiter=',', skiprows=1, unpack=True)

#print(index)
#print(mass_BH)

plt.scatter(index,mass_BH)

#
#plt.errorbar(index, mass_BH, xerr=None, yerr=mass_BH_err, capsize=0, ls='none', color='black', elinewidth=1, marker="o")

plt.xlabel("Index")
plt.ylabel("Mass of Black Hole")

plt.show()
plt.savefig("plot.pdf")
