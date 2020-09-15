num=int(input("Enter a number"))
temp=num
sum=0
while(temp>0):
    rem=temp%10
    sum+=rem**3
    temp//=10
if(num==sum):
    print("Number is amstrong")
else:
    print("Number is not amstrong")