# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:40:09 2022

@author: 702-52
"""


h = float(input('身高多少?(公尺)'))
w = float(input('體重多少?(公斤)'))
BMI = w / h ** 2
BMI = round(BMI, 2)
print("BMI值為{}" . format(BMI))
if BMI <= 18.5:
    print('親,過輕囉!')
elif BMI >= 18.5 and BMI < 24:
    print('很正常!請繼續保持')
else:
    if BMI < 27 and BMI >= 24:
        print('親,過重囉!')
    elif BMI < 30 and BMI >= 27:
        print('已經輕度肥胖囉!')
    elif BMI < 35 and BMI >= 30:
        print('已經中度肥胖囉!')
    else:
        print('已經重度肥胖囉!')