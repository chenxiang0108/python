import tkinter as tk
window = tk.Tk()
window.title('按鈕')
window.geometry('700x700')
window.config(bg = 'black')
def push():
    if b['text'] != '成功':
        b['text'] = '成功'
        b['bg'] = 'white'
    else:
        b['text'] = '測試'
        b['bg'] = 'red'

b = tk.Button(window,bg = 'red',text = '測試',font =('Arial',100),width =10,height =5,command = push)
b.pack()

window.mainloop()