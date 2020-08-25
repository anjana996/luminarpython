from re import *

rule='\w*[@]gmail[.]com'
gmail=input("enter gmail id")

matcher=fullmatch(rule,gmail)

if(matcher!=None):
    print("valid")

else:
    print("invalid")