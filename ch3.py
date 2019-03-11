import tkinter as tk
window = tk.Tk()
window.title('Listbox')
window.geometry('700x700')

def add():
    var = e.get()
    if var != '':            #輸入欄空白，則不新增到 Listbox裡面
        lb.insert('end',var)
        e.delete(0,'end')
def delete():
    lb.delete(0,'end')

e = tk.Entry(window,show = None,bg ='black',fg = 'white',font = ('',50))
e.pack()
b1 = tk.Button(window,text = 'add',width = 10,height = 2,command = add)
b1.pack()
b2 = tk.Button(window,text = 'delete',width = 10,height = 2,command = delete )
b2.pack()
lb = tk.Listbox(window)
lb.pack()

window.mainloop()