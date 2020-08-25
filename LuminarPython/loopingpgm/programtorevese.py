num=int(input("Enter a number"))
sub=0
rev=0
while(num!=0):
    sub=num%10
    rev=rev+10+sub
    num=num//10
print(rev)
