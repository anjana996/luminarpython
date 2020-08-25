class Employee:
    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def printdetails(self):
        print("Id",self.id)
        print("name",self.name)
        print("desig",self.desig)
        print("salary",self.salary)

    def __str__(self):
        return self.name



f=open("emp","r")
emplst=[]
for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    desig=values[2]
    salary=values[3]
    obj=Employee(id,name,desig,salary)
    emplst.append(obj)
    print(obj)

for emp in emplst:
    print(emp)
    # obj.printdetails()



