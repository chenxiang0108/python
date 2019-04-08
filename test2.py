import tkinter as tk
window = tk.Tk()
window.title('paddle')
window.geometry('700x700')
window.resizable(0,0)
# 創建畫布
canvas = tk.Canvas(window,width = 500,height = 700,bg = 'gray')
canvas.pack()
canvas.update()
# 建立 球拍
class Paddle:

    def __init__(self,color):
        self.paddle = canvas.create_rectangle(0,0,100,25,fill = color)
        self.id = canvas.coords(self.paddle)
        canvas.move(self.paddle,200,650)
        # 移動球拍
        canvas.bind_all('<Left>',self.Move_left)
        canvas.bind_all('<Right>',self.Move_right)

    def Move_left(self,event):
        if self.id <= canvas.winfo_width:
            canvas.move(self.paddle,0, 0)
        #else:canvas.move(self.paddle,-10,0)

    def Move_right(self,event):
        canvas.move(self.paddle,10,0)
# 建立 球
class Ball:
    def __init__(self,color):
        self.ball = canvas.create_oval(0,0,25,25,fill = color)
        canvas.move(self.ball,225,625)

paddle = Paddle('blue') # 藍色球拍
ball = Ball('red') # 紅色球

canvas.update()
window.mainloop()