class Super:
    def __init__(self, new, narx, qiymat):
        self.new = new
        self.narx = narx
        self.qiymat = qiymat

    def calculat(self):
        total = sum(s * p for s, p in zip(self.qiymat, self.narx))
        remaining = [q - s for q, s in zip(self.new, self.qiymat)]
        print(f"Total sales: {total}")
        print(f"qolgan miqdori: {remaining}")
        return total, remaining

new = list(map(int, input("Masalan 1, 2, 3, 4,  ").split(',')))
narx = list(map(int, input("Masalan 1, 2, 3, 4,  ").split(',')))
qiymat = list(map(int, input("Masalan 1, 2, 3, 4,  ").split(',')))

supermarket = Super(new, narx, qiymat)

total, remaining_quantities = supermarket.calculat()
