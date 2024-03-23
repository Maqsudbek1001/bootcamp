class Fibonachi:
    def __init__(self, sum_fib):
        self.sum_fib = sum_fib

    def hisobla(self):
        fib = [0, 1]
        while len(fib) < self.sum_fib:
            fib.append(fib[-1] + fib[-2])
        return sum(fib[:self.sum_fib])
class Person(Fibonachi):
    def __init__(self, sum_fib):
        super().__init__(sum_fib)
sum_fit = int(input("n ni kiriting: "))
result = Fibonachi(sum_fit).hisobla()
print(f"Fibonachi sonlarining birinchi {sum_fit} tasining yig'indisi: {result}")