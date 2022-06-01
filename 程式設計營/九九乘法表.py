# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:27:01 2022

@author: 702-52
"""


a = int(input('How many?>>>'))
for x in range(1,a+1):
    for y in range(1,10):
        print(x,"*",y,"=",x*y)
    print("*"*(25))