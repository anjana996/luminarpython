num1=int(input("Enter a number"))
num2=int(input("Enter a number"))

try:
    res=num1/num2

    print("Result",res)
    print("We have data base transactions")
    print("file operations")

# except:
#     print("Error occured")
except Exception as e:
    print(e.args)