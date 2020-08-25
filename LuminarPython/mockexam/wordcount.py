file="hai hello hai hello"
words=file.split()
dict={}
for word in words:
    if (word not in dict):
        dict[word]=1
    else:
        dict[word]+=1

for k,v in dict.items():
    print(k,",",v)

