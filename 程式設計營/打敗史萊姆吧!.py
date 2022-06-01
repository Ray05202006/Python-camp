# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:02:40 2022

@author: 702-52
"""


health = 100
for time in range(100,0,-1):
    damge = int(input('請輸入傷害:'))
    health = health - damge
    if health <= 0:
        print("史萊姆剩下 0 滴血")
        break
    else:
        print("史萊姆剩下 {} 滴血".format(health))
print("史萊姆死亡了!")