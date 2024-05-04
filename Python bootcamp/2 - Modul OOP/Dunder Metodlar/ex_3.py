import math

class Student:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.magnitude < other.magnitude

    def __gt__(self, other):
        return self.magnitude > other.magnitude

    def __eq__(self, other):
        return self.magnitude == other.magnitude

    def __bool__(self):
        a = self.magnitude > self

    @property
    def magnitude(self):
        return self.age

john = Student('Maqsudne', 21)
bob = Student('Bob', 32)
alice = Student('Alice', 21)

print(john > bob)
print(john < bob)
print(john == alice)

# elif john < bob:
#     print(True)
# elif john == alice:
#     print(True)
