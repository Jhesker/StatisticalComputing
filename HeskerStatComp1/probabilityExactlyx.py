# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:32:37 2019

@author: jhesk
"""
import math
import pylab


def probabilityPlot(numOcc):
    value = []
    numRolls = []
    y = (1/6)
    z = (5/6)
    for k in range(2, 100):
        x = (math.factorial(k)/(math.factorial(numOcc) *
                            math.factorial(k - numOcc)))
        result = x * (y ** numOcc) * (z ** (k - numOcc))
        value.append(result)
        numRolls.append(k)
    pylab.plot(numRolls, value,'ko')
    pylab.ylabel('Probability')
    pylab.xlabel('Number of rolls')


probabilityPlot(2)

