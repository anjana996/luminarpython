low=int(input("Enter a lower limit"))#10
upp=int(input("Enter an upper limit"))#20
for i in range(low,upp+1):#10,19+1
    if i>1:#10>1#all prime numbers are greater than 1
        for j in range(2,i):#we need to check each num is prime of not
            if (i%j==0):#10/2,10/3....10/i
                break

        else:
            print(i)


