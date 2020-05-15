# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:22:17 2019

@author: jhesk
"""
def fib(n,x):
    if n == 2:
        x +=1
        print("a computation of 2 has been completed")
    if n ==0 or n==1:
        return x/2
    else:
        return fib(n-1,x) + fib(n-2,x)
count = fib(5,0)
print (count, "times")


