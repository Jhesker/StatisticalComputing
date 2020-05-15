# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:09:39 2019

@author: jhesk
"""
import pylab
import random
import scipy.integrate


def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
        return tot/len(X)


def stdDev(X):
    return variance(X)**0.5


def getBMData(fileName):
    data = {}
    f = open(fileName)
    line = f.readline()
    data['name'], data['gender'], data['age'] = [], [], []
    data['division'], data['country'], data['time'] = [], [], []
    while line != '':
        split = line.split(',')
        data['name'].append(split[0])
        data['gender'].append(split[1])
        data['age'].append(int (split[2]))
        data['division'].append(split[3])
        data['country'].append(split[4])
        data['time'].append(float (split[5][:-1]))
        line = f.readline()
    f.close()
    return data


def makeHist(data, bins, title, xLabel, yLabel):
    pylab.figure()
    pylab.hist(data, bins)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    mean = sum(data)/len(data)
    std = stdDev(data)
    pylab.annotate('Mean = ' + str(round(mean, 2)) + '\nSD = ' +
                   str(round(std, 2)), fontsize = 10, xy = (0.65, 0.75),
                   xycoords = 'axes fraction')


def sampleTimes(times, numExamples):
    sample = random.sample(times, numExamples)
    makeHist(sample, 10, 'Sample of Size' + str(numExamples),
             'Minutes to Complete Race', 'Number of Runners')


def gaussian(x, mu, sigma):
    factor1 = (1/(sigma*((2*pylab.pi)**.05)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2


def testSamples(numTrials, sampleSize):
    tightMeans, wideMeans = [], []
    for t in range(numTrials):
        sampleTight, sampleWide = [], []
        for i in range(sampleSize):
            sampleTight.append(random.gauss(0, 1))
            sampleWide.append(random.gauss(0, 100))
        tightMeans.append(sum(sampleTight)/len(sampleTight))
        wideMeans.append(sum(sampleWide)/len(sampleWide))
    return tightMeans, wideMeans


times = getBMData('bostonMarathonData.txt')['time']
makeHist(times, 20, '2012 Boston Marathon', 'Minutes to Complete Race',
         'Number of Runners')
sampleSize = 40
sampleTimes(times, sampleSize)
area = round(scipy.integrate.quad(gaussian, -3, 3, (0, 1))[0], 4)
print('probability of being within 3 of the true mean of tight dist. =', area)
area = round(scipy.integrate.quad(gaussian, -3, 3, (0, 100))[0], 4)
print('probability of being within 3 of the true mean of wide dist. =', area)
tightMeans, wideMeans = testSamples(1000, 40)
pylab.figure()
pylab.plot(wideMeans, 'y*', label = ' SD = 100')
pylab.plot(tightMeans, 'bo', label = 'SD = 1')
pylab.xlabel('Sample Number')
pylab.ylabel('Sample Mean')
pylab.title('Means of Samples of Size ' + str(40))
pylab.legend()

pylab.figure()
pylab.hist(wideMeans, bins = 20, label = 'SD = 100')
pylab.title('Distribution of the Sample Means')
pylab.xlabel('Sample Mean')
pylab.ylabel('Frequency of Occurance')
pylab.legend()
