import re

count=0
matcher=re.finditer("ab","aaaaabbbbbababababababababababaabbabab")
for match in matcher:
    print(match.start())#match found in which positions
    print(match.group())#ethokke object aayit matching
    count+=1
print(count)
