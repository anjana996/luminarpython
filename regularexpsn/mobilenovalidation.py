from re import *

rule='[\d]{10}'
number=input("Enter number")
matcher=fullmatch(rule,number)

if(matcher!=None):
    print("valid")
else:
    print("invalid")