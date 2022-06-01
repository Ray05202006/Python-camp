#匯入套件
import tkinter as tk

#建立視窗
win = tk.Tk()
win.geometry('210x180')
win.wm_maxsize(width=210,height=180)
win.wm_minsize(width=210,height=180)
#標題名
win.wm_title("BMI查詢")
#判斷
def bmi():
    h = int(en_1.get())
    w = int(en_2.get())
    BMI = w / ((h / 100) ** 2)
    lb_end.config(text=round(BMI,2))
    if BMI <= 18.5:
        lb_t.config(text='親,過輕囉!')
    elif BMI >= 18.5 and BMI < 24:
        lb_t.config(text='很正常!請繼續保持')
    else:
        if BMI < 27 and BMI >= 24:
            lb_t.config(text='親,過重囉!')
        elif BMI < 30 and BMI >= 27:
            lb_t.config(text='已經輕度肥胖囉!')
        elif BMI < 35 and BMI >= 30:
            lb_t.config(text='已經中度肥胖囉!')
        else:
            lb_t.config(text='已經重度肥胖囉!')


#版面
lb_title = tk.Label(text='BMI值查詢',font=(100))
lb_end = tk.Label()
lb_t = tk.Label()
lb_1 = tk.Label(text='身高(cm)')
en_1 = tk.Entry(text='身高',background='#888888')
lb_2 = tk.Label(text='體重(kg)')
en_2 = tk.Entry(background='#888888')
lb_title.pack()
lb_end.pack()
lb_t.pack()
lb_1.pack()
en_1.pack()
lb_2.pack()
en_2.pack()
#按鈕
Btn_1 = tk.Button(text='確認',command = bmi)
Btn_1.pack()







win.mainloop()