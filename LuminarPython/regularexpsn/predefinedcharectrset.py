from re import *

#pattern="\s"#check for spaces
#pattern="\d"#print digits
#pattern="\D"#print ecept digits
#pattern="\w"#all charechtrs exept special char
#pattern="\W"#all special char
pattern=
count=0
matcher=finditer(pattern,'abcabcbabcbacbabbabnbajkj &*123' )
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("total",count)

