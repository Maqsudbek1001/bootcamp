class Arr:
    def __init__(self, arr):
        self.arr = arr

    def sanoq(self):
        minus_sanash = sum(1 for num in self.arr
                                if num < 0)
        plyus_sabash = sum(1
                             for num in self.arr
                                if num >= 0)
        return minus_sanash, plyus_sabash


if __name__ == "__main__":
    arr1 = list(map(int, input("Msalan 1, w, 5, 5, 6: ").split(',')))
    arr = arr1
    operations = Arr(arr)
    minus_sanash, plyus_sanash = operations.sanoq()
    print("Manfiy soni:", minus_sanash)
    print("Musbat soni:", plyus_sanash)
