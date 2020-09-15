class Bank:
    def __init__(self,AcNo,Person,Balance,BankName):
        self.AcNo=AcNo
        self.Person=Person
        self.Balance=5000
        self.BankName=BankName

    def printValues(self):
        print("AcNo:",self.AcNo)
        print("name:",self.Person)
        print("BalanceAmount:",self.Balance)
        print("BranchName:",self.BankName)


    def Witdraw(self,wamount):
        self.Balance -= wamount
        if (self.Balance>wamount):
            print("Withdrawed Amount is", wamount)
            print("Available balace is:",self.Balance)

        else:
            print("insufficient balance")


    def Deposit(self,Amount):
        self.Balance+=Amount
        print("You have deposited",Amount)
        print("Available balance is",self.Balance)

    def BalaceEnquiry(self):

        print("Your available balance",self.Balance)



obj=Bank(12345,"Arun",10000,"UnionBank")



obj.printValues()

obj.Deposit(1000)
obj.BalaceEnquiry()
obj.Witdraw(11100)
