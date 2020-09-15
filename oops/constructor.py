class Employee:
    def __init__(self,Eid,Ename,Designation,Salary):
        self.Eid=Eid
        self.Ename=Ename
        self.Designation=Designation
        self.Salary=Salary

    def printValues(self):
        print(self.Eid)
        print(self.Ename)
        print(self.Designation)
        print(self.Salary)

obj=Employee(1001,"Arun","CEO",100000)
obj.printValues()
