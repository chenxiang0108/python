class Employee:               #定義父類別 Employee 用來表示員工
    #初始化設定員工的姓名
    def __init__(self,name):
        self.__name = name

    #用來回傳員工姓名
    def getName(self):
        return self.__name

    #回傳員工的本月薪水，根據 hours(小時) 以及 payrate(鐘點費)計算員工本月薪水
    def getSalary(self,hours,payrate):
        return hours * payrate

class SalesPerson(Employee):   #定義子類別 SalesPerson 用來表示銷售人員
                               #用來回傳銷售人員的本月薪水(含業績獎金)，繼承自父類別的 getSalary()，並加上業績獎金 bonus
    def getSalary(self,hours,payrate,bonus):
        return hours * payrate + bonus

E1 = Employee('小丸子')        #自動呼叫__init__()將員工姓名設定為小丸子
E2 = SalesPerson('小紅豆')     #雖然 子類別沒有定義 __init__() ，但父類別有，於是自動呼叫父類別的__init__()將銷售人員的姓名設定為小紅豆
print('員工',E1.getName(),'的本月薪水為',E1.getSalary(120,150))          #使用父類別的 getSalary()
print('銷售人員',E2.getName(),'的本月薪水為',E2.getSalary(120,150,3000)) #使用子類別的 getSalary()