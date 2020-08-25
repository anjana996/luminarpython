f=open("temperaturedata","r")
dict={}
for line in f:
    data=line.rstrip("\n").split(",")
    district=data[0]
    temperature=data[1]

    if(district not in dict):
        dict[district]=temperature
    else:
        old=dict[district]
        if temperature>old:
            dict[district]=temperature
print(dict)