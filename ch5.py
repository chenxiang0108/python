import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title('+1')
count = 0

def show():
    tk.messagebox.showinfo('測試', 'hello')  # ShowMessage
def clickok():
    global count
    count =count +1
    l.config(text ='click  ' +str(count) +' times')
# row = 行 column = 列
b = tk.Button(window, text='show', command=show, width=20, height=5).grid(row = 0,column = 0) # 位子(0,0)
b2 = tk.Button(window, text='+1', command=clickok, width=20, height=5).grid(row = 1,column = 0) # 位子(1,0)
l = tk.Label(window,text = '標題',width = 20,height = 5)
l.grid(row =1,column = 1)
window.mainloop()
