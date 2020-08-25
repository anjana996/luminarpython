employee={
    "eid":1002,
    "ename":"Arun",
    "desig":"Developer",
    "salary":15000,
}
print(employee["ename"])#employeename
print("company" in employee)#search company name
employee["company"]="Luminar"#add company name

employee["salary"]+=5000#add salary



for keys in employee:#print all keys and values
    print(keys,",",employee[keys])