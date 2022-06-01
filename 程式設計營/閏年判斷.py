# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:46:58 2022

@author: 702-52
"""


year = int(input('哪一年?'))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print('{}年是閏年' . format(year))
        else:
            print('{}年不是閏年' . format(year))
    else:
        print('{}年是閏年' . format(year))
else:
    print('{}年不是閏年' . format(year))