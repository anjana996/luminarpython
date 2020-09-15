from re import *
pattern="[abc]"#check eithe a,b or c

# pattern="[a-zA-Z]"
# pattern='[A-z]'
#
matcher=finditer(pattern,"abacabcabcabacabcabcabcabcabcabcabcabcabc")
for match in matcher:
    print(match.start())
    print(match.group())

