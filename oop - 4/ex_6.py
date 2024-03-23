class UY_library:
    def __init__(self):
        self.kitob = {}

    def add(self, name, muallifi):
        self.kitob[name] = muallifi

    def find(self, mualif):
        return [name for name, auth in self.kitob.items() if auth == mualif]

    def find(self, year):
        return [name for name in self.kitob if year in name]

    def remove(self, name):
        if name in self.kitob:
            del self.kitob[name]
            return True
        return False

# Test qilish
uy_kutubxona = UY_library()
uy_kutubxona.add("Sherlock Holmes", "Arthur Conan Doyle")
uy_kutubxona.add("Pride and Prejudice", "Jane Austen")
uy_kutubxona.add("1984", "George Orwell")
print("Muallif kitoblar:")
print(uy_kutubxona.find("Arthur Conan Doyle"))

print("\nYil bo‘yicha kitoblar:")
print(uy_kutubxona.find("1984"))

uy_kutubxona.remove("Pride and Prejudice")
print("\nO‘chirilgan kitoblar:")
print(uy_kutubxona.kitob)
