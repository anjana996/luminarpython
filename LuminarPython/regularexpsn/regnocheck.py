from re import *

rule='[kK][lL][0-9]{2}[a-z]{1,2}\d{4}'
lst=[]
f=open("reg_no","r")


for data in f:
    line=data.rstrip("\n")
    matcher=fullmatch(rule,line)
    if(matcher!=None):
        lst.append(line)

    else:
        pass
print(lst)



