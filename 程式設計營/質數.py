# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:15:18 2022

@author: 702-52
"""
a = int(input('How many?>>>'))
m = [2]

# for x in range(2,a+1):
#     for i in range(2,x+1):
#         if x == i:
#             print(x)
#             m.append(x)
#         elif x%i == 0:
#             break
# print(m)
def check(a):
    for i in range(2,a+1):
        if a == i:
            return('是質數')
        elif a%i == 0:
            return('不是質數')
            break 
print(check(a))