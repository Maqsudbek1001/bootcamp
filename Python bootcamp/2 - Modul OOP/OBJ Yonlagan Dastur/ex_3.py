class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def login(self):
        return f"ism  {self.name}"
    def logout(self):
        return f"email {self.email}"
    def submit_task(self):
        return NotImplemented



class Teacher(User):
    def teacher_name(self):
        return f"Sizning o'quvcgingiz {self.name}"



class Mentor(Teacher):
    def chesk_task(self):
        return f"siz bu email: {self.email} tekshiring."

class Person(Teacher):
    def main(self):
        return f'Sizmning Ismingiz {self.name} \n szining Email {self.email}'

Obj = User("Jasurbek", "jasur@gmail.com")
Obj1 = Mentor("Jasurbek", "jasur@gmail.com")
Obj2 = Teacher("Jasurbek", "jasur@gmail.com")
Obj3 = Person("Jasurbek", "jasur@gmail.com")
print(Obj.login())
print(Obj1.login())
print(Obj3.login())
print(Obj3.main())