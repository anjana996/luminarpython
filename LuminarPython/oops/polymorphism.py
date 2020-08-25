#Method Overloading

class Addition:
    def add(self):
        num1=10
        num2=20
        print("result:",num1+num2)

    def add(self,num2):
        num1=10
        print("Sum",num1+num2)

    def add(self,num1,num2):
        print(num1+num2)

a=Addition()


a.add(12,13)
print(a.add)