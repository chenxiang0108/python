class circle:
    pi = 3.14
    def __init__(self,r = 1):  #建立物件的時候，會自動呼叫這個方法將物件初始化
        self.radius = r
    def getarea(self):
        return self.pi*self.radius*self.radius

c1 = circle()       #變數 c1 參照 cicle 物件
print('半徑為:',c1.radius,'園面積為:',c1.getarea())
c2 = circle(10)
print('半徑為:',c2.radius,'園面積為:',c2.getarea())