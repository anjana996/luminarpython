lst=[]
num=int(input("Enter a limit"))
print("Enter list Elements")
for i in range(0,num):
    lst.append(int(input()))
print("list",lst)

for i in range(0,num-1):
    for j in range(0,num-i-1):
        if(lst[j]>lst[j+1]):
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print("sorted list",lst)


