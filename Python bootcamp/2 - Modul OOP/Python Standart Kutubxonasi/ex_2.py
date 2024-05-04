from abc import ABC, abstractmethod

class Resource(ABC):
    @abstractmethod
    def kitoblar(self):
        pass
class Computer(Resource):
    def kitoblar(self):
        return "Kompyuter sayt yaratishda yordam beradi."
class Book(Resource):
    def kitoblar(self):
        return "Kitob foydalanuvchilarga ma'lumot beradi."
def main():
    computer = Computer()
    book = Book()
    print(computer.kitoblar())
    print(book.kitoblar())

if __name__ == "__main__":
    main()
