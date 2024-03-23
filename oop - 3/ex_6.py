class Arr:
    def __init__(self, arr):
        self.arr = arr

    def total(self, k):
        k %= len(self.arr)
        return self.arr[:-k] + self.arr[-k:]


if __name__ == "__main__":
    arr1 = list(map(int, input("Masalan 1, 2, 3, 4,  ").split(',')))
    k = 3

    arr = arr1
    operations = Arr(arr)
    name_arr = operations.total(k)
    print(f"Elementlari {k} marta olding surilfdi:", name_arr)
