class Arr:
    def __init__(self, arr):
        self.arr = arr

    def max_indeksi(self):
        max_raqam = max(self.arr)
        return self.arr.index(max_raqam) + 1

if __name__ == "__main__":
    arr1 = list(map(int, input("Masalan 1, 2, 3, 4,: ").split(',')))
    arr = arr1
    operations = Arr(arr)
    print("Enga kata elementi :", operations.max_indeksi())
