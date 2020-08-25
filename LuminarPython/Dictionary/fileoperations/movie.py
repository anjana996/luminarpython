#yearwise movie count


f=open("movies.csv","r")
dict={}
lst=[]
for line in f:
    data=line.rstrip("\n").split(",")
    movie=data[1]
    year=data[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
for k,v in dict.items():
    print(k,":",v,"movies")


