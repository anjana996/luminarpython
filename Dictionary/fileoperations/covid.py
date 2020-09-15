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
print("**********************************")
sum=0
for k,v in dict.items():
    sum+=int(v)
print("Total confirmed cases:",sum)
# maxvalue=(max(dict,key=dict.get))
# print(maxvalue,":")
print("*************************************")
# all_items = dict.items()
# max_value = max(all_items)
# print(max_value)
lst=[]
for k,v in dict.items():
    lst.append(int(v))
for k,v in dict.items():

    if(max(lst))==int(v):


        print("highest no:of confirmed cases is in",k,v)