#total confirmed cases


f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    cases=data[8]
    if cases not in dict:
        dict[state]=cases
    else:
        dict[state]=cases
for k,v in dict.items():
    print(k,",",v)
    totalcases=int(v)
    if int(v>maxtotalcases):
        max