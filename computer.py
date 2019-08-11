from tkinter import *
window = Tk()
window.title('計算機')
window.geometry('600x555')
window.resizable(0,0)
class computer:
    def click(self,event): # 按下按鈕的判斷
        if event.widget['text'] != '=' and event.widget['text'] != 'c':
            self.ent.insert(END,event.widget['text'])
        elif event.widget['text'] == '=':
            num = self.ent.get()
            self.ent.delete(0,'end')
            try:
                self.ent.insert(END,eval(num))
            except SyntaxError:        # 出現語法錯誤的時候
                self.ent.insert(END,'0')
            else:
                pass
        else:
            self.ent.delete(0,'end')

    def __init__(self,number):  # 建立計算機
        self.number = number
        self.ent = Entry(window,font = ('arial',40),bd = 5,bg = 'lightgray',justify = RIGHT) # justify為元件上顯示文字的位置
        self.ent.grid(row = 0,column = 0,columnspan = 4)    # 位子在(0,0)並且橫跨 4 格到(0,3)
        x = -1
        for i in range(1,5):
            for j in range(4):
                x += 1
                self.btn = Button(window,text = number[x],font = ('arial',45),bd = 3,bg = 'black',fg = 'white')
                self.btn.bind('<Button-1>',self.click)
                self.btn.grid(row = i,column = j,sticky = EW)
computer('789/456*123-0c=+') # 計算機按鈕的文字
window.mainloop()