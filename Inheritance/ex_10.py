class Kam:
    def __init__(self, K):
        self.K = K

    def hisoblash(self):
        N = 1
        while True:
            if N % self.K == 0:
                return N
            else:
                N += 1

K = int(input("K ni kiriting: "))
result = Kam(K).hisoblash()
print(f"Berilgan K soniga qoldiqsiz bo'linadigan birinchi N ta son: {result}")
