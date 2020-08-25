lst=[1,2,3,4,5]

#1)
sq=[(i*i)for i in lst]
print(sq)
#2)
pairs=[(i,j)for i in lst for j in lst]
print(pairs)
#3)even
even=[(i) for i in lst if i%2==0]
odd=[(j)for j in lst if j%2!=0 ]
print(even)
print(odd)