# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 20:22:14 2019

@author: jhesk
"""
import random
import sklearn.linear_model
import pylab
import warnings

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
        data['age'].append(int(split[2]))
        data['division'].append(split[3])
        data['country'].append(split[4])
        data['time'].append(float(split[5][:-1]))
        line = f.readline()
    f.close()
    return data


def divide80_20(examples):
    sampleIndices = random.sample(range(len(examples)), len(examples)//5)
    trainingSet, testSet = [], []
    for i in range(len(examples)):
        if i in sampleIndices:
            testSet.append(examples[i])
        else:
            trainingSet.append(examples[i])
    return trainingSet, testSet


def accuracy(truePos, falsePos, trueNeg, falseNeg):
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator/denominator


def sensitivity(truePos, falseNeg):
    try:
        return truePos/(truePos + falseNeg)
    except ZeroDivisionError:
        return float('nan')


def specificity(trueNeg, falsePos):
    try:
        return trueNeg/(trueNeg + falsePos)
    except ZeroDivisionError:
        return float('nan')


def posPredVal(truePos, falsePos):
    try:
        return truePos/(truePos + falsePos)
    except ZeroDivisionError:
        return float('nan')


def getStats(truePos, falsePos, trueNeg, falseNeg, toPrint=True):
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    if toPrint:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Pos. Pred. Val. =', round(ppv, 3))
    return (accur, sens, spec, ppv)


class Runner(object):
    def __init__(self, gender, age, time):
        self.featureVec = (age, time)
        self.label = gender

    def featureDist(self, other):
        dist = 0.0
        for i in range(len(self.featureVec)):
            dist += abs(self.featureVec[i] - other.featureVec[i])**2
        return dist**.05

    def getTime(self):
        return self.featureVec[1]

    def getAge(self):
        return self.featureVec[0]

    def getLabel(self):
        return self.label

    def getFeatures(self):
        return self.featureVec

    def __str__(self):
        return str(self.getAge()) + ', ' + str(self.getTime()) +\
            ', ' + self.label


def buildMarathonExamples(fileName):
    data = getBMData(fileName)
    examples = []
    for i in range(len(data['age'])):
        a = Runner(data['gender'][i], data['age'][i], data['time'][i])
        examples.append(a)
    return examples


def applyModel(model, testSet, label, prob=0.5):
    testFeatureVecs = [e.getFeatures() for e in testSet]
    probs = model.predict_proba(testFeatureVecs)
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if testSet[i].getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else:
            if testSet[i].getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg


examples = buildMarathonExamples('bostonMarathonData.txt')
training, test = divide80_20(examples)

featureVecs, labels = [], []
def modelBuild(numOfTraining):
    trainingSample = random.sample(training, numOfTraining)
    for e in trainingSample:
        featureVecs.append([e.getAge(), e.getTime()])
        labels.append(e.getLabel())
    return sklearn.linear_model.LogisticRegression().fit(featureVecs, labels)


def buildROC(model, testSet, label, title, i, plot=True):
    xVals, yVals = [], []
    p = 0.0
    while p <= 1.0:
        truePos, falsePos, trueNeg, falseNeg = \
            applyModel(model, testSet, label, p)
        xVals.append(1.0 - specificity(trueNeg, falsePos))
        yVals.append(sensitivity(truePos, falseNeg))
        p += 0.01
    auroc = sklearn.metrics.auc(xVals, yVals, True)
    if plot:
        pylab.figure(i)
        pylab.plot(xVals, yVals)
        pylab.plot([0, 1], [0, 1], '--')
        pylab.title(title + ' (AROC = ' +\
                              str(round(auroc, 3)) + ')' +\
                              'Training Size' + str(i))
        pylab.xlabel('1 - Specificity')
        pylab.ylabel('Sensitivity')
    return auroc
warnings.filterwarnings('ignore')
test2 = random.sample(test, 200)
x = 10
while x <= 1010:
    print('Feature weights for label M:', 'age =',
      str(round(model.coef_[0][0], 3)) + ',',
      'time =', round(model.coef_[0][1], 3))
    truePos, falsePos, trueNeg, falseNeg = applyModel(model, test, 'M', .578)
    getStats(truePos, falsePos, trueNeg, falseNeg)
    model2 = modelBuild(x)
    buildROC(model2, test2, 'M', 'ROC for Predicting Gender', i = x)
    x += 50