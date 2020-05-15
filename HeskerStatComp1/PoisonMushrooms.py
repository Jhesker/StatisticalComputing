# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:16:32 2019

@author: jhesk
"""
"""looking for the probability that probIsNot given probCor"""
def probGiven(probIs, probIsNot, probCor, probError):
    prob = float((probIsNot * probCor)/(probCor * probIsNot +
                 probError * probIs))
    return prob

confidance = probGiven(.8, .2, .95, .05)
print(confidance)
