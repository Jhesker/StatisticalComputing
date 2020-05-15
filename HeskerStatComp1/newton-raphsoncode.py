# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:40:10 2019

@author: jhesk
"""

def Newton():
    epsilon = 0.01
    k = 24
    guess = k/2.0
    iteration = 0
    while abs(guess*guess - k) >= epsilon:
        guess = guess-(((guess**2)-k)/(2*guess))
        iteration+=1
    print('Square root of', k, 'is about', guess,
          'and took', iteration,'iterations')
    return iteration
def Bisection():
    x = 24
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = max(1.0,x)
    ans = (high+low)/2
    while abs(ans**2 - x) >=epsilon:
        print('low =', low, 'high=', high, 'ans =', ans)
        numGuesses +=1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses =', numGuesses)
    print(ans, 'is close to square root of', x)
    return numGuesses
def MostEfficient(newtonIter,bisectionIter):
    if newtonIter<bisectionIter:
        print("newton is more efficient because it took",
              (bisectionIter - newtonIter), 'less steps' )
    elif bisectionIter<newtonIter:
        print("Bisection is more efficient because it took",
              (newtonIter - bisectionIter), 'less steps' )
    elif bisectionIter == newtonIter:
        print("they are the same because they took the same amount of",
              "iterations")
newtonIter = int(Newton())
bisectionIter = int(Bisection())
MostEfficient(newtonIter,bisectionIter)


