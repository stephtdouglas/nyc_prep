import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import astropy.io.ascii as at

def read_binned_craters():
    """read in cratering data and return crater_diameters, crater_count, count_error."""
    craters = at.read("crater_data.csv")
    crater_diameters = craters["Diam(km)"]
    crater_count = craters["count_per_million_km"]
    count_error = craters["count_error"]
    return crater_diameters, crater_count, count_error

def setup_axes(ax):
    ax.set_xscale("log",basex=2)
    ax.set_yscale("log")
    ax.set_xlim(2,128)
    ax.set_ylim(0.1,1000)
    ax.set_yticklabels([0,0.1,1,10,100,1000])
    ax.set_xticklabels([1,2,4,8,16,32,64,128])
    ax.set_xticks([3,6,12,24,32,48,64,96],minor=True)
    ax.tick_params(labelsize="large")
    ax.grid(which='both',axis='y')
    ax.grid(which='major',axis='x',linestyle="-",color="k")
    ax.set_ylabel("Craters per 1,000,000 square km",fontsize="x-large")
    ax.set_xlabel("Crater Diameter (km)",fontsize="x-large")
    
ax = plt.subplot(111)
setup_axes(ax)
crater_diameters, crater_count, count_error = read_binned_craters()
plt.errorbar(crater_diameters, crater_count, count_error,fmt='o',color='purple',ms=5,elinewidth=2)
plt.savefig("crater_count_data.png",bbox_inches="tight",dpi=600)
