# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 02:34:17 2019

@author: jhesk
"""
import pylab


def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline()
    for line in dataFile:
        d, m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return(masses, distances)


def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    forces = pylab.array(masses)*9.81
    pylab.plot(forces, distances, 'ko', label = 'Measured displacements' )
    pylab.title('Measured Displacements of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    #LinearFit
    a,b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a*pylab.array(forces) + b
    k = 1.0/a
    pylab.plot(forces, predictedDistances, label =
               'Displacements predicted by\nlinear fit, k=' + str(round(k, 5)))
    pylab.legend(loc = 'best')
    #cubicFit
    a,b,c,d = pylab.polyfit(forces, distances, 3)
    predictedDistances = a*(forces**3) + b*forces**2 + c*forces + d
    nV = 1.5 * 9.81
    pD2 = a*(nV**3) + b*nV**2 + c*nV + d
    pylab.plot(forces, predictedDistances, 'k:', label = 'cubit fit')
    pylab.plot(nV, pD2,'k:')
fitData('springData.txt')