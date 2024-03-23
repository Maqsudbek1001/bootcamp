class Arr:
    def __init__(self, arr):
        self.arr = arr

    def sum(self):
        return sum(self.arr)

    def product(self):
        yigindi = 1
        for num in self.arr:
            yigindi *= num
        return yigindi

    def max_raqam(self):
        return max(self.arr)

    def min_raqam(self):
        return min(self.arr)


if __name__ == "__main__":
    arr1 = list(map(int, input("masalan 1, 2, 3, 4 : ").split(',')))

    arr = arr1
    operations = Arr(arr)
    print("yig'indisi:", operations.sum())
    print("ko'paytmasi:", operations.product())
    print("katta elementi:", operations.max_raqam())
    print("kichik elementi:", operations.min_raqam())
