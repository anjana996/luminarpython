pattern="ABABABCAAA"
dict={}
lst=[]
for char in pattern:

    if(char not in dict):
        dict[char]=1
    else:
        dict[char]+= 1
print(dict)
result=max(dict,key=dict.get)
print("Most frequent element:",result)