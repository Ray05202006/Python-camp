# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:30:14 2022

@author: 702-52
"""


# a = 0
# while a<10:
#     print("NOW>>{}".format(a))
#     a += 1
a = int(input('which number?>>>'))
import random
num = random.randint(0,100)
while a != num:
    while a > num:
        print('the answer is more smaller.',end='')
        a = int(input('Nope,try again!>>>'))
    while a < num:
        print('The answer is more bigger.',end='')
        a = int(input('Try again!>>>'))
print('you are right!!!')    