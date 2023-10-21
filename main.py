class Student:
    group = "C2018"
    subject = "Python"
    count = 0

    def __init__(self, age, height, name="Nick"):
        self.name = name
        self.age = age
        self.height = height
        Student.count += 1

    def printer(self):
        print("my name is", self.name)

    def grow(self, height=1):
        self.height += height

    def __str__(self):
        return f"I'm student. My name's {self.name}. My age is {self.age}"



nick = Student(15, 165)
kate = Student(16, 160, name="Kate")
jane = Student(15, 170, "Jane")

nick.grow()
print(nick.height)
kate.grow(10)
print(kate.height)
print(nick)

print(2 + 5)

