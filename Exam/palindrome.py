num=int(input("Enter a number:"))
temp=num
reverse=0
while(num>0):
    dig=num%10
    reverse=reverse*10+dig
    num=num//10
if(temp==reverse):
    print("The number is palindrome")
else:
    print("Not a palindrome")