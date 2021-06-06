# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:00:55 2021

@author: LENOVO
"""

import rstr
import re

# ask the user to input the regular expression
regex=input("Enter regex :\n")

# print examples for strings that accepted
print("Examples for regex :\n",rstr.xeger(regex))

# ask the user to input if he want to check some string acceptance
check=input("Do you want to check specific string acceptance :Enter Y :\n")

# check if the string accepted or not
if check =='y' or check=='Y':
        string=input("Enter string :\n")
        if re.fullmatch(regex,string):
            print("accepted")
        else:
            print ("not accepted")