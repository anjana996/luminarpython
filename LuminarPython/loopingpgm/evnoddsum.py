low=int(input("enter a limit"))
upp=int(input("enter a limit"))
sum=0
oddsum=0
for i in range(low,(upp+1)):
    if(i%2==0):
        sum=sum+i


else:
    oddsum+=i
print(sum)
print(oddsum)