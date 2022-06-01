#匯入套件
import tkinter as tk
import math
import random

ans = []
def answer():
    ans.clear()
    Btn_2.config(text='重來一次')
    while len(ans) != 4:
        num = random.randint(0,9)
        if len(ans) == 0 and num == 0:
            continue
        elif num in ans:
            continue
        else:
            ans.append(num)
    print(ans)
    return(ans)
    
def game():
    user = int(en_1.get())
    y = []
    p = 0
    q = 0
    a=math.floor(user/1000)
    b=math.floor(user%1000/100)
    c=math.floor(user%100/10)
    d=math.floor(user%10)
    y.append(a)
    y.append(b)
    y.append(c)
    y.append(d)
    for i in range(4):#x
        m = y[i] in ans
        print(m)
        if m == True:
            if y[i] == ans[i]:
                p=p+1
                continue
            else:
                q=q+1
                continue
        else:
            pass     
    lb_2.config(text='{}A{}B'.format(p, q))
    lb_3.config(text='前次輸入值:{}'.format(user),)
    if p == 4 and q == 0:
        lb_3.config(text='猜中了')
#建立視窗
win = tk.Tk()
win.title('幾A幾B')
win.geometry('210x300')
win.config(bg='#1E90FF')
win.wm_maxsize(width=210,height=240)
win.wm_minsize(width=210,height=180)
lb_1 = tk.Label(text='幾A幾B',font=('繁黑體',25),bg='#4169E1')
lb_2 = tk.Label(text=' A B',font=('繁黑體',20),bg='#4169E1')
lb_3 = tk.Label(bg='#1E90FF',font=('繁黑體',14))
en_1 = tk.Entry()
Btn_2 = tk.Button(text='開始',command=answer,bg='#4169E1',relief='raised')
Btn_1 = tk.Button(text='輸入確認',command=game,bg='#4169E1',relief='raised')
lb_1.pack(pady=5)
lb_2.pack(pady=7)
en_1.pack()
lb_3.pack()
Btn_1.pack(side='right', ipadx=5, padx=15)
Btn_2.pack(side='left', ipadx=5, padx=20)



win.mainloop()