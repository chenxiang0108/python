class shoppingcar():
    def __init__(self,owner):
        self.__owner = owner
        self.__product = []
    def getowner(self):
        return self.__owner
    # 新增到購物車
    def addproduct(self,product):
        self.__product.append(product)
    # 從購物車移除
    def removeproduct(self,product):
        self.__product.remove(product)
    #回傳 product
    def getproduct(self):
        return self.__product
obj = shoppingcar('小丸子')
obj.addproduct('巧克力')
obj.addproduct('咖啡豆')
obj.addproduct('馬卡龍')
obj.addproduct('草莓果醬')
obj.addproduct('手工餅乾')
obj.removeproduct("咖啡豆")
print(obj.getowner(),'的購物車裡面有',obj.getproduct())