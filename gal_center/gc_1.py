#!/usr/bin/python

import csv
import re

import matplotlib.pyplot as plt
import numpy as num

#testarray = ["a", "b", "c"]
#print(testarray)

with open('SgrAStarTable.csv') as csvfile:
    datareader = csv.reader(csvfile, delimiter=",")
    ##test of whether the read-in works
    #for row in datareader:
    #print(', '.join(row))
    
    #set up a bunch of arrays, one for each of the columns in the dataset
    index = num.array([])
    star = num.array([])
    #a = semi-major axis, in two different unites
    a_arcsec = num.array([])
    #parameter_err = the measured or calculated error on that parameter
    a_arcsec_err = num.array([])
    a_AU = num.array([])
    a_AU_err = num.array([])
    #ecc = eccentricity
    ecc = num.array([])
    ecc_err = num.array([])
    #inc = inclination, measured in degrees
    inc = num.array([])
    inc_err = num.array([])
    #omega = XXX, measured in degrees
    omega = num.array([])
    omega_err = num.array([])
    #t_P = XXX, measured in XXX
    t_P = num.array([])
    t_P_err = num.array([])
    #period = orbital period, measured in years
    period = num.array([])
    period_err = num.array([])
    #sp = spectral type???
    sp = num.array([])
    #m_K = K-band magnitude
    m_K = num.array([])
    #r = XXX
    r = num.array([])
    #mass_BH = my calculated mass of Sgr A*, measured in solar masses
    mass_BH = num.array([])
    #mass_BH_err = my calculated error on the mass, calculated using error propagation
    mass_BH_err = num.array([])
    
    for row in datareader:
        row = re.split(',', row)
index = num.append(index,num.int(row[1]))

#print ', '.join(index)
#print(index)
