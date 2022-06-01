# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = int(input('How many?>>>'))
# for i in range(1,10):
#     print(i)

# for i in range(0,a,1):
#     print('フ')

#靠左三角形
for i in range(1,a+1,1):
    print('*'*i)
    
print("—"*a)

#靠左倒三角形    
for i in range(a,0,-1):
    print('*'*i)
    
print("—"*a)
 
#靠右三角形
for i in range(1,a+1,1):
    print(" "*(a-i),end='')
    print('*'*(i))
    

#靠右倒三角形    
for i in range(a,0,-1):
    print(" "*(a-i),end='')
    print('*'*(i))

#等腰三角形
for n in range(1,a+1,1):
    print(' '*(a-n),end='')
    print('*'*(1+(n-1)*2))
