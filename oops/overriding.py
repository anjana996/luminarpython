class Parent:
    def phone(self):
        print("asus")

class Child(Parent):
    def phone(self):
        print("iphone")

c=Child()
c.phone()

p=Parent()
p.phone()