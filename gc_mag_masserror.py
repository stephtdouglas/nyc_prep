#This bit of code tells the computer this is a Python script.
#!/usr/bin/python

#Python plotter written by Ashley Pagnotta for use during the 2014 AMNH REU/AstroCom Inquiry Activity, specifically for the Sgr A* dataset, but extremely generic, so feel free to modify and use for other plotting needs.

#This is a bit of sample code for you to use as a backbone for your plotting program. It does not do everything you will want it to do, but it gives you an idea of where to go. If you have questions, remember that Google is your friend! 

#The # character is used to denote a comment in Python. You will find (hopefully) useful explanations in comments, and you can comment/uncomment certain sections of code to test how things are going if necessary, as well as change the output of the code. It's good practice to comment heavily and clearly, so when you change the code, note what you're doing and why you are doing it.

#import two very useful libraries and give them common abbreviations
import matplotlib.pyplot as plt
import numpy as np

#use the loadtxt routine to import the CSV file containing all of the information on the orbital motion of the stars around Sgr A*. Each parameter (or error on the parameter) is placed into an array (like a matrix) with a name that corresponds to the given parameter.
index, star, a_arcsec, a_arcsec_err, a_AU, a_AU_err, ecc, ecc_err, inc, inc_err, Omega, Omega_err, omega, omega_err, t_P, t_P_err, period, period_err, m_K, r, mass_BH, mass_BH_err = np.loadtxt('SgrAStarTable.csv', delimiter=',', skiprows=1, unpack=True)

#If you want to be sure the import has gone correctly, try printing out one or two of the arrays and make sure the values match up.
#print(index)
#print(mass_BH)

#This gives you a standard scatter plot, created using two inputs, of the form (x,y).
plt.scatter(m_K,mass_BH_err)
plt.gca().invert_xaxis()
#plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d'))

#This gives a scatter plot (because of ls='none') but with error bars, which in this case are also drawn from the array. If you want to use this line, you can uncomment it (delete the # character before plt.errorbar) and also comment out the above plain scatter plot (add a # character before plt.scatter).
#plt.errorbar(index, mass_BH, xerr=None, yerr=mass_BH_err, capsize=0, ls='none', color='black', elinewidth=1, marker="o")

#Label your axes!
plt.xlabel("K Band Magnitude")
plt.ylabel("Error on Mass of Sgr A*")

#Uncomment this to save a version of your plot whenever you are happy with what you're seeing. It will write over previous versions, so make sure you change the name if you want to save a new plot.
plt.savefig("magnitude.png")

#This shows you what your plot looks like in a temporary window. The window will stay open until you close it, but the plot will not be saved on your computer.
plt.show()

