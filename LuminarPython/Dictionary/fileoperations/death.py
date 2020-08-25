f=open("covid_19_india.csv","r")
dict={}
for line in f:
    data=line.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    print(state,death)

#
#     if(death not in state):
#         dict[state]=death
#     else:
#         dict[state] = death
#
# for k,v in dict.items():
#     print(k,",",v)
# print("*************************")
#
# sum=0
#
# for k,v in dict.items():
#     sum+=int(v)
# print("Total death",sum)
#
# print("*************")
#
# lst=[]
# for k,v in dict.items():
#     lst.append(int(v))
# for k,v in dict.items():
#
#     if(max(lst)==int(v)):
#
#         print("Highest death rate:",k,v)