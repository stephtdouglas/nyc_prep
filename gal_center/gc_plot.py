#import two very useful libraries and give them common abbreviations
import matplotlib.pyplot as plt
import numpy as np

#code to read in GC data

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

