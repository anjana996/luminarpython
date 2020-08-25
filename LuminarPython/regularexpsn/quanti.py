from re import *
pattern="a+"#combination of a
# pattern="a?"  q
#pattern="a{2,3}"
matcher=finditer(pattern,"abcLKMdakkanaakkaaaakaaakaaef121mKLnbjk")
for match in matcher:
    print(match.start())
    print(match.group())
