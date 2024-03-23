class Sanoq_sistema:
    def __init__(self, son):
        self.son = son

    def sanoq(self):

        ikki = bin(self.son)[2:]
        print(f"2 lik Sanoq sistemasi {ikki}")
        sakkiz = oct(self.son)[2:]
        print(f"8 lik sanoq sistemasi {sakkiz}")
        onolti = hex(self.son)[2:].upper()
        print(f"16 lik sanoq sistemasi {onolti}")

        return ikki, sakkiz, onolti

son = int(input("10 lik sanoq sistemasidagi sonni kiriting: "))
obj = Sanoq_sistema(son).sanoq()


