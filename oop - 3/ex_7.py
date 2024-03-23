class Bank:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def yillik_hisobati(self):
        total = 0
        for i in range(len(self.A)):
            miqdor = self.A[i] * self.B[i] / 100
            total += miqdor
        return total

if __name__ == "__main__":
    n = int(input("Bo'limlar sonini: "))
    A = []
    B = []
    for i in range(n):
        A.append(float(input(f"{i + 1} pul miqdori: ")))
        B.append(float(input(f"{i + 1} foizini kirit: ")))

    bank = Bank(A, B)
    total = bank.yillik_hisobati()
    print(f"Bankning  1 yil foyidasi: {total}")
