line=[1,2,3]
lst=[]
for i in range(0,len(line)-1):
    data=line[i],line[i+1]
    if(data not in lst):
        lst.append(data)
    digit=line[0],line[len(line)-1]
    if(digit not in lst):
        lst.append(digit)
print(lst)
