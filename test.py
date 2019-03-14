import tkinter as tk
import random
import re    #正規表達
from tkinter import messagebox
window = tk.Tk()
window.title('Guess number')
window.geometry('900x900')
x = 1
y = 100
number = random.randint(1,100)                 #隨機從1~100中產生一個數字
def guess():
    global x,y,number
    answer = -1
    change_number.configure(text = '送出')
    guessnumber = guess_number.get()              #輸入的字
    while answer != number:
        if not re.findall('[0-9]',guessnumber):    #判斷是否為數字
            tk.messagebox.showinfo('提示','只能輸入數字')
            break
        answer = eval(guessnumber)    #從字串轉成整數
        if answer > number:   #猜的大於答案
            if answer > y:     #判斷有沒有超出範圍
                tk.messagebox.showinfo('提示', '請輸入正確的範圍')
            elif answer == y and y != 100:
                l.configure(text='提示:猜過了')
            else:
                l.configure(text = '提示:太大了')
                y = answer
            break
        elif answer < number:   #猜的小於答案
            if answer < x:       #判斷有沒有超出範圍
                tk.messagebox.showinfo('提示','請輸入正確的範圍')
            elif answer == x and x != 1:
                l.configure(text = '提示:猜過了')
            else:
                l.configure(text = '提示:太小了')
                x = answer
            break
        else:
            l.configure(text = '提示:猜對了,點擊重新') #猜的等於答案
            number = random.randint(1, 100)
            guess_number.delete(0,'end')
            x =1
            y =100
        break
    Range.configure(text = '%s~%s' % (x, y))
guess_number = tk.Entry(window,font = ('',70))
guess_number.pack()
change_number = tk.Button(window,text = '開始',width = 20,height = 5,font = ('',20),command = guess)
change_number.pack()
l = tk.Label(window,text ='提示',font = ('',20))
l.pack()
Range = tk.Label(window,text = '1~100',font = ('',20))
Range.pack()

window.mainloop()