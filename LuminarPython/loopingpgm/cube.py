num=int(input("Enter a number"))
sum=0
while(num>0):
    rem=num%10
    sum+=rem**3
    num//=10
print(sum)