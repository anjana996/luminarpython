import functools
lst=[1,2,4,5]

sum=functools.reduce(lambda num1,num2:num1+num2,lst)
print("sum",sum)

maxval=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print("maxvalue",maxval)

minval=functools.reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print("minval",minval)