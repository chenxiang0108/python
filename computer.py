from tkinter import *
window = Tk()
window.title('計算機')
window.geometry('635x600')
#window.resizable(0,0)
class display:
    def click(self,event):
        if event.widget['text'] != '=':
            if event.widget['text'] != 'c':
                self.ent.insert(END,event.widget['text'])
            else:
                l = len(self.ent.get())
                self.ent.delete(0,'end')
        else:
            num = eval(self.ent.get())
            self.ent.delete(0,'end')
            self.ent.insert(END,num)
    def __init__(self,number):
        self.number = number
        self.ent = Entry(window,font = ('',50),bd = 5)
        self.ent.grid(row = 0,column = 0,columnspan = 4)
        x = -1
        for i in range(1,5):
            for j in range(4):
                x += 1
                self.btn = Button(window,text = number[x],font = ('',50),bd = 3)
                self.btn.bind('<Button-1>',self.click)
                self.btn.grid(row = i,column = j,sticky = EW)

display('789/456*123-0c=+')
window.mainloop()