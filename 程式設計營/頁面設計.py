import tkinter as tk

win = tk.Tk()   #建立主視窗
win.title('我的視窗')
win.geometry('1680x720')
win.iconbitmap('C:/Users/702-52/Desktop/icon.ico')
win.minsize(width = 400,height = 400)
win.maxsize(width = 2100,height = 900)
win.config(background = '#003D79')

def ok():
    a = en.get()
    lb.config(text=a)
def push():
    b = btn.getboolean()
    
#label
lb = tk.Label(text = 'This is s label')
lb.pack()



#輸入
en = tk.Entry()
en.pack()
#win.attributes('-alpha',0.97)
btn = tk.Button(text = '開始',command = ok)
btn.config(width = 10,height = 5,bg='white')
#三種布局方式
btn.pack()







win.mainloop()