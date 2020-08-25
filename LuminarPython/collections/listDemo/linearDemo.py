lst=[1,2,3,4,5]

element=int(input("enter an element to search"))
flg=0
for i in lst:
    if(i==element):
        flg=1
        break
    else:
        pass
if(flg>0):
    print("element foung")
else:
    print("not found")




