from re import *

rule='\w*[@]gmail[.]com'
lst=[]
f=open("gmail_check","r")
for line in f:
    data=line.rstrip("\n")
    matcher=fullmatch(rule,data)
    if(matcher!=None):
        lst.append(data)
    else:
        pass
print(lst)
