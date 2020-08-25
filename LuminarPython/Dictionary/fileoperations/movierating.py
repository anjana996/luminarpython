#rating count
f=open("movies.csv","r")
dict={}
for line in f:
    data=line.rstrip("\n").split(",")
    movie=data[1]
    rating=data[3]
    if rating not in dict:
        dict[rating] = 1
    else:
        dict[rating]+= 1
for k, v in dict.items():
    print("rating",k, ":", v)