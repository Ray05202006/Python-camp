# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 14:08:50 2022

@author: 702-52
"""


a = [1, 2, 5, 3, 10, 7, 2, 3, 2, 2]
#list
print('長度' , len(a))
print('最大值' , max(a))
print('最小值' , min(a))
print('總和' , sum(a))
a.append(2)
print('2出現次數',a.count(2))
print(8 in a)
print(2 in a)
print(a[0])
print(a[4])
print(a[-3])
print(2 not in a)
print(6 not in a)
a.append(2)
a.pop(1)#去除第某位數
#set
b = {1, 2, 2, 3, 3, 77}
print(8 not in b)
print(3 not in b)
print(set(b))
print(b)
#dict
c = {"name":"Ray","number":3,'test':'www'}
print(c["name"])
#更新
c["number"] = 4
#新增
c["class"] = 104
#刪除
del c["test"]
print(dict(c))
print(c)
#tuple
d = (1, 2, 3, 4, 7, 88, 101)