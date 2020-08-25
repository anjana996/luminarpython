num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=int(input("Enter a number"))

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print("Sorted numbers are:",num1,num2,num3)
    else:
        print("Sorted numbers are:",num1,num3,num2)
elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print("Sorted numbers are:",num2,num1,num3)
    else:
        print("Sorted numbers are:",num2,num3,num1)
elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print("Sorted numbers are:",num3,num1,num2)
    else:
        print("Sorted numbers are:",num3,num2,num1)