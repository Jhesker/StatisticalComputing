# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:11:10 2019

@author: Jacob Hesker
this takes int input of 10 numbers and returns highest odd number.
"""
# This function requests the numbers from the user and stores them into an
# array then returns the array list for further use
def RequestInput():
    print("Please enter 10 whole numbers of your choosing "+
          ", in any order,"+" seperate them with a space. "+
          "At the end the largest odd number will be returned")
    numArray=list(map(int,input().split()))
    return numArray

# This function takes the array and finds the odd numbers and then stores them
# into another array then returns the array list for further use
def FindOdd(numArray):
    oddArray=[];
    for x in numArray:
        if x%2 != 0:
            oddArray.append(x)
    return oddArray
# This function takes the odd numbers array and compares the values at each
# index in order to find the highest value then returns the highest value
# prints out put based on contents of the array
def FindHighest(oddArray):
    if not oddArray:
        print("You did not enter an odd number this time!")
    else:
        currHighest = oddArray[0]
        for num in oddArray:
            if num > currHighest:
                currHighest = num
        print("The largest odd number entered was", currHighest)
# calls the RequestInput function
numArray = RequestInput()
# calls FindOdd with previous num Array as parameter
oddArray = FindOdd(numArray)
# calls FindHighest with new oddArray as parameter
FindHighest(oddArray)

