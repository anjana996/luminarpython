from re import *

#pattern="[a-z]"#to check the lowe case a-z
#pattern="[A-Z]"#to chheck the upper case A_Z
#pattern="[0-9]" #to extract the digits
pattern='[^0-9]'#to extract cahrts except digits
count=0
matcher=finditer(pattern,'abcabcbabcbacbabbabnbajkj 123' )
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("total",count)

