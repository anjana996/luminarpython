f=open("empfile")
emp={}
for line in f:
    id,name,designation,salary=line.rstrip("\n").split(",")
    if id not in emp:
        emp[id]={"id":id,"name":name,"designation":designation,"salary":salary}
def fetchdata(**kwargs):
    id=str(kwargs["id"])
    if (id not in emp):
        print("Employee does not exist")
    else:
        print(emp)
    print(emp[id]["name"])
    if "prop" in kwargs:
        val=kwargs["prop"]
        print(emp[id][val])




fetchdata(id=1002,prop="salary")
