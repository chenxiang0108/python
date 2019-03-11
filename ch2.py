import tkinter as tk
window = tk.Tk()
window.title('輸入')
window.geometry('700x700')

def hit_me():
    l['text'] = t.get() #Label顯示的字為輸入的字
    t.delete(0,'end')   #清空輸入欄

l = tk.Label(window,width = 50,height = 2,bg ='red',fg ='blue',text = '測試',font =('',30)) #背景顏色bg 文字顏色fg
l.pack()
t = tk.Entry(window,width = 50,show ='',font = ('',50)) # show = '*'打出來的字都會是*
t.pack()
b = tk.Button(window,text = '轉換',width = 20,height = 5,bg = 'black',fg = 'white',font = ('',15),command = hit_me)
b.pack()

window.mainloop()