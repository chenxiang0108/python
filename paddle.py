import tkinter as tk
import random
import time
window = tk.Tk()
window.title('paddle')
window.geometry('700x700')
#window.resizable(0,0)

# 創建畫布
canvas = tk.Canvas(window,width = 500,height = 700,bg = 'gray')
canvas.pack()

# 建立 球拍
class Paddle:
    def __init__(self,color):
        self.paddle = canvas.create_rectangle(0,0,100,25,fill = color)
        self.x = 0
        canvas.move(self.paddle,200,650)
        canvas.bind_all('<Left>',self.Move_left)
        canvas.bind_all('<Right>',self.Move_right)
        self.hit_space = True
    # 移動球拍
    def draw(self):
        canvas.move(self.paddle,self.x,0)
        self.paddle_coords = canvas.coords(self.paddle)
        if self.paddle_coords[0] <= 0:
            self.x = 0
        elif self.paddle_coords[2] >= canvas.winfo_width():
            self.x = 0
    def Move_left(self,event):
        self.x = -10
    def Move_right(self,event):
        self.x = 10

# 建立 球
class Ball:
    def __init__(self,color):
        self.ball = canvas.create_oval(0,0,25,25,fill = color)
        canvas.move(self.ball,225,425)
        move = [10,-10]
        random.shuffle(move)
        self.x = move[0]
        self.y = move[0]
    # 移動 球
    def draw(self):
        canvas.move(self.ball,self.x,self.y)
        self.ball_coords = canvas.coords(self.ball)
        if self.ball_coords[0] <= 0:
            self.x = 10
        elif self.ball_coords[1] <= 0:
            self.y = 10
        elif self.ball_coords[2] >= canvas.winfo_width():
            self.x = -10
        elif self.ball_coords[3] >= canvas.winfo_height():
            self.y = -10
        elif self.ball_coords[2] >= paddle.paddle_coords[0] and self.ball_coords[2] <= paddle.paddle_coords[2]:
            if self.ball_coords[3] >= paddle.paddle_coords[1]: # 球的底部觸碰到球拍頂部
                self.y = -10
# 建立磚塊
class Brick:
    def __init__(self):
        x = -100
        color = ['darkgray','gray','lightgray']

        # 5*3 的磚塊
        for i in range(5):
            x += 100
            y = -25
            c = -1
            for j in range(3):
                y += 25
                c += 1
                self.brick = canvas.create_rectangle(x,y,x + 100,y + 25,fill = color[c])
                self.brick_coords = canvas.coords(self.brick)
    def hit_brick(self):
        if ball.ball_coords[1] <= self.brick_coords[3]:  #撞到磚塊底部
            ball.y = 10
            canvas.delete(self.brick)
        #elif ball.ball_coords[3] >= self.brick_coords[1]: #撞到磚塊頂部
             #ball.y = -10

paddle = Paddle('blue') # 藍色球拍
ball = Ball('red') # 紅色球
brick = Brick()
while True:
    if paddle.hit_space == True:
        paddle.draw()
        ball.draw()
        brick.hit_brick()
    window.update()
    canvas.update()
    canvas.update_idletasks()
    time.sleep(0.02)


