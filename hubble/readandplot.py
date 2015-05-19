import numpy as np
from numpy import *
import matplotlib.pyplot as plt


# Plot the data with x and y error
plt.errorbar(z,d,xerr=z_err,yerr=d_err,marker='.',linestyle='none',color='black')
plt.xlabel('z')
plt.ylabel('d [Mpc]')
plt.title('SNe Ia')
