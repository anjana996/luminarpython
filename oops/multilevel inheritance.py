class Parent:
    def m1(self):
        print("inside parent")


class Child(Parent):
    def m2(self):
        print("inside child")

class SubChild(Child):
    def m3(self):
        print("inside subchild")

       #subchild
su=SubChild()
su.m1()
su.m2()
su.m3()
print("********************")
c=Child()
c.m1()
c.m2()
print("********************")
p=Parent()
p.m1()