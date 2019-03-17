class Transport:
    def __init__(self,owner,cc):
        self.__owner = owner
        self.__cc = cc

    def getowner(self):
        return self.__owner
    def getcc(self):
        return self.__cc

    def launch(self):
        print('在此寫上發動交通工具的敘述')
    def park(self):
        print('在此寫上停止交通工具的敘述')

class Motorcycle(Transport): #繼承 Transport
    def launch(self):
        print('在此寫上發動摩托車的敘述')
    def park(self):
        print('在此寫上停止摩托車的敘述')

class Car(Transport):       #繼承 Transport
    def launch(self):
        print('在此寫上發動汽車的敘述')
    def park(self):
        print('在此寫上停止汽車的敘述')


obj = Motorcycle('小明',125)
print('這個交通工具的車主、CC數 :',obj.getowner(),obj.getcc())
obj.launch()
obj.park()

obj2 = Car('大偉',2000)
print('這個交通工具的車主、CC數 :',obj2.getowner(),obj2.getcc())
obj2.launch()
obj2.park()
