import datetime
class Person:
    def SetValues(self,pname,age):
        self.pname=pname
        self.age=age

    def PrintValue(self):
        print("Name",self.pname)
        print("Age",self.age)


class Bank(Person):
    bankName="Union"
    def __init__(self,AccNo):
        self.AccNo=AccNo
        self.Balance=1000

    def Deposite(self,amount):
        self.amount=amount
        print("You have deposited",self.amount,"in your",self.AccNo,"on",datetime.date.today(),"in your",Bank.bankName)

    def Withdwaw(self,amount):
        if(amount>self.Balance):
            print("Transaction error 1001")
        else:
            print("You have debited",amount,"in your",self.AccNo,"on",datetime.date.today())
    def BalanceEnqiry(self):
        print("Your availabe balance is:",self.Balance)

obj=Bank(1001)
obj.Deposite(1000)
obj.Withdwaw(500)
obj.BalanceEnqiry()
obj.SetValues("Vinu",27)
obj.PrintValue()