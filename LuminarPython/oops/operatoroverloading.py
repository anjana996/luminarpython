class Book:
    def __init__(self,pages):
        self.pages=pages
#to print the +operator between books
    def __add__(self, other):
        return Book(self.pages+other.pages)

    def __str__(self):
        return str(self.pages)

obj=Book(100)
print(type(obj))
obj2=Book(200)
obj3=Book(100)
print(obj+obj2+obj3)
