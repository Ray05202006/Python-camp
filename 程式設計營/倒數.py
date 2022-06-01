# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:03:53 2022

@author: 702-52
"""
a = int(input('功能選擇?倒數0/計時1>>>'))
import time
counttime = 0
countdowntime = 300
while a == 1:
    b = int(counttime / 60)
    b = round(b, 0)
    c = counttime % 60
    print(b, c)
    time.sleep(1)
    counttime = counttime + 1
while countdowntime >= 0 and a == 0:
   b = int(countdowntime / 60)
   b = round(b, 0)
   c = countdowntime % 60
   print(b, c)
   time.sleep(1)
   countdowntime = countdowntime - 1
print('DONE')