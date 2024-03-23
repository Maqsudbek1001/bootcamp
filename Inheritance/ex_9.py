class Kam:
    def __init__(self, N, K):
        self.K = K
        self.N = N

    def hisoblash(self):
        while self.N % self.K != 0:
            self.N = int(self.K ** 0.5)
        return self.N

K = int(input("K ni kiriting: "))
N = int(input("N ni kiriting: "))  
result = Kam(N, K).hisoblash()
print(f"Berilgan K soniga karrali bo'lgan birinchi N ta son: {result}")
