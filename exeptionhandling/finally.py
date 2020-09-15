num1=int(input("Enter a number"))
num2=int(input("Enter a number"))

try:
    res=num1/num2

    print("Result",res)


# except:
#     print("Error occured")
except Exception as e:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    res=num1/num2

except Exception as e:
    print(e.args)

finally:
    print("We have data base transactions")
    print("file operations")