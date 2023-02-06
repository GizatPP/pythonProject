class Shape:
    class Square:
        def __init__(self, length):
            self.length = length

        def area(self, length):
            a = 4 * 3.14 * length * length
            print(a)
        def __str__(self):
            return f"{self.length}"

obj = Shape.Square(4)
print(obj)
obj.area(45)

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

obj = Employee("Gizat", 22)
print(obj)


