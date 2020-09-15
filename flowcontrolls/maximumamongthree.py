num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=int(input("Enter a number"))

if((num1>num2)&(num1>num3)):
    print("max=",num1)
elif((num2>num1)&(num2>num3)):
    print("max=",num2)
else:
    print("max=",num3)