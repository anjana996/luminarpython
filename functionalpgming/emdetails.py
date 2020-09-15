import functools
class Employee:
    def __init__(self,ID,Name,Desgn,Salary):
        self.ID = ID
        self.Name = Name
        self.Desgn = Desgn
        self.Salary = int(Salary)

    def printvalues(self):
        print("ID:", self.ID)
        print("Name:", self.Name)
        print("Designation:", self.Desgn)
        print("Salary:", self.Salary)

    def __str__(self):
        return self.Name


f=open("empdata","r")
elist=[]

for data in f:
    values=data.rstrip("\n").split(",")
    ID=values[0]
    Name=values[1]
    Desgn=values[2]
    Salary=values[3]
    obj=Employee(ID,Name,Desgn,Salary)

    # print(obj)
    elist.append(obj)




up=list(map(lambda emp:emp.Name.upper(),elist))

sal=list(filter(lambda emp:emp.Salary>25000,elist))
inc=list(map(lambda emp:emp.Salary+5000,elist))
print("UPPERCASE")
for lst in up:
    print(lst)
print("SALARY>25000")
for lst in sal:
    print(lst)
print("updated salary")
for lst in inc:
    print(lst)
salary=list(map(lambda emp:emp.Salary,elist))
print("Salaries",salary)
maxsal=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salary)
print("maximim value",maxsal)


maxemp=list(filter(lambda emp:emp.Salary==maxsal,elist))
print(maxemp)

for emp in maxemp:
    print(emp)