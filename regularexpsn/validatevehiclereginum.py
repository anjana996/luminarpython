from re import *

rule='[kK][lL][0-9]{2}[a-z]{1,2}\d{4}'

regno=input("Enter reg no")

matcher=fullmatch(rule,regno)

if(matcher!=None):
    print("Valid")
else:
    print("invalid")