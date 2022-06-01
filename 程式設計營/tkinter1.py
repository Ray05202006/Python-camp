
#匯入套件
import tkinter as tk


#建立視窗
win = tk.Tk()
#字體
from tkinter import font
fonts=list(font.families())
print(fonts)
#標題名
win.wm_title("Game")

#command_write
def write():
    lb_1.config(bg='red')
    word_1 = en_1.get()
    lb_2.config(text='你叫{}'.format(word_1))



#視窗
win.geometry('500x300',)
win.wm_maxsize(width=1600,height=900)

#Label_1
lb_1 = tk.Label(text='Hi',font=('Arial',40))
lb_1.pack()
lb_2 = tk.Label(text="你的名子?")
lb_2.pack()

#entry_1
en_1 = tk.Entry(font='標楷體',background='#888888')
en_2 = tk.Entry(font='標楷體',background='#888888')
en_1.pack()
en_2.pack()
#按鈕
Btn_1 = tk.Button(text='點擊開始',command = write)
Btn_1.pack()















#執行
win.mainloop()