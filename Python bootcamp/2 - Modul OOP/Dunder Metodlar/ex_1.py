class Student:
    def __init__(self, ismi, yoshi, telefon):
        self.ismi = ismi
        self.yoshi = yoshi
        self.telefon = telefon


    def about(self):
        print(f"sizni Ismingiz {self.ismi}")

Yoshi = int(input("Yoshingiz: "))
Telefon = int(input("telefon Masalan (91)9098087: "))
obj = Student("JOHN", Yoshi, Telefon)
obj.about()
