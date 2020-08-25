class Employee:
    def setValues(self,Eid,Ename,Designation,Salary):
        self.Eid=Eid
        self.Ename=Ename
        self.Designation=Designation
        self.Salary=Salary

    def printValues(self):
        print(self.Eid)
        print(self.Ename)
        print(self.Designation)
        print(self.Salary)

obj=Employee()
obj.setValues(1001,"Arun","HR",25000)
obj.printValues()
