num1=int(input("Enter a number"))#10
num2=int(input("Enter a number"))#12
num3=int(input("Enter a number"))#13

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print("Second largest number is ",num2)
    else:
        print("Second largest number is ",num3)

elif((num2>num3)&(num2>num1)):
    if(num3>num1):
        print("Second largest number is ",num3)
    else:
        print("Second largest number is ",num1)


elif((num3>num2)&(num3>num1)):
    if(num2>num1):
        print("Second largest number is ",num2)
    else:
        ("Second largest number is ",num1)

else:
    print("Fool")


