# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:23:31 2019

@author: jhesk
"""
def search(L, e):
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bSearch(L, e, low, mid)
        else:
           return bSearch(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bSearch (L, e, 0, len(L) - 1)
L = ["a","b","c","d",]
bolVal = search(L, "e")
print(bolVal)

