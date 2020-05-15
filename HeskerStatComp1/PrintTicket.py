# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:49:38 2019

@author: jhesk
"""


def PrintRecipt(rowNum, seatNum, personName, amount):
    print(personName," :you are to be seated in row:", rowNum," Seat Number:",
          seatNum)
    ans = input(print("Would you like to purchase and extra parking pass",
                         " for only $10?","Please enter Yes or No"))
    if(ans == "Yes"):
        amount += 10
        print("Thank you for your purchase!")
    else:
        print("Ok, maybe next time!")

    print("Your total is $", amount, "Please enjoy your time at our venue.")

PrintRecipt(1,14,"Steve Irwin", amount = 4)

