class Google:
    def __init__(self,ID,Name,Desgn,Salary):
        self.ID=ID
        self.Name=Name
        self.Desgn=Desgn
        self.Salary=int(Salary)

    def printvalues(self):
        print("ID:",self.ID)
        print("Name:",self.Name)
        print("Designation:",self.Desgn)
        print("Salary:",self.Salary)

    def __str__(self):
        return self.Name
f=open("edetails","r")

elist=[]
for data in f:
    values=data.rstrip("\n").split(",")
    ID=values[0]
    Name=values[1]
    Desgn=values[2]
    Salary=values[3]
    obj=Google(ID,Name,Desgn,Salary)
    # print(obj)
    elist.append(obj)



    up=list(map(lambda emp:emp.Name.upper(),elist))
    sal=list(filter(lambda emp:emp.Salary>100000,elist))
    inc=list(filter(lambda emp:emp.Salary+5000,elist))
print("UPPERCASE")
for lst in up:
    print(lst)
print("SALARY>100000")
for lst in sal:
    print(lst)
print("updated salary")
for lst in inc:
    print(lst)