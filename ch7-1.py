class a:  #定義類 a
    __x = '我是屬性__x' #定義私有屬性，無法被子類別繼承
    y = '我是屬性y'     #定義非私有屬性，能被子類別繼承

    def __m1(self):     #定義私有方法，無法被子類別繼承
        print('我是方法 m1()')

    def m2(self):       #定義非私有屬性，能被子類別繼承
        print('我是方法 m2()')

class b(a):     #類別 b 繼承自類別 a
    z = '我是屬性 z'
    def m3(self):
        print('我是方法 z')
c = b() #建立一個隸屬於類別 b 的物件，並指派給變數 c