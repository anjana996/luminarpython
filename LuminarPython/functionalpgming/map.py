lst=[2,3,4,5]

def square(num):
    return num*num

sq=list(map(square,lst))
print(sq)

def even(num):
    return num%2==0

even=list(filter(even,lst))
print(even)