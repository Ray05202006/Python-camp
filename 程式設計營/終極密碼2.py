#匯入套件
import tkinter as tk
import random
#建立視窗
win = tk.Tk()

#標題名
win.wm_title("終極密碼")

#隨機數
num = random.randint(0,100)
#tap
taptime=0
#command_user
def game():
    global taptime
    b = (en_1.get())
    ans = int(b)
    taptime = taptime + 1
    if ans != num:
        if ans > num:
            lb_2.config(text='the answer is more smaller. Try again!')
            lb_3.config(text="次數:{}".format(taptime))
        elif ans < num:
            lb_2.config(text='the answer is more bigger. Try again!')
            lb_3.config(text="次數:{}".format(taptime))
    else:
        lb_2.config(text='you are right!!!')
        lb_3.config(text="次數:{}".format(taptime))
    


#Label_1
lb_1 = tk.Label(text='猜一個0~100的數字',font=('標楷體',40))
lb_1.pack()
#label_2
lb_2 = tk.Label(text=" ",font=(40))
lb_2.pack()
#label_3
lb_3 = tk.Label(text="次數:0",font=(40))
lb_3.pack()

#entry_1
en_1 = tk.Entry(font='標楷體',background='#888888')
en_1.pack()
#按鈕
Btn_1 = tk.Button(text='確認',command = game)
Btn_1.pack()

win.mainloop()