f=open("numbers", "r")

lst=[]
even=[]
odd=[]

for i in f:
    lst.append(int(i))
print(lst)

for i in lst:
    if(i%2==0):
        even.append(i)

    else:
        odd.append(i)


print("Even",even)
print("Odd",odd)

