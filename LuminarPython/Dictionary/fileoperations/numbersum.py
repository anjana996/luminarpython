f=open("numbers", "r")
lst=[]

for i in f:
    lst.append(int(i))
res=sum(lst)

print(res)