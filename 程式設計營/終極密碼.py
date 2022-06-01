# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:19:16 2022

@author: 702-52
"""


import random
a = random.randint(0,100)
for life in range(10,0,-1):
    num = int(input('請輸入數字:'))
    if num > a:
        print('答案小於{}'.format(num))
    elif num < a:
        print('答案大於{}'.format(num))
    else:
        print("猜中了!好棒!")
        break