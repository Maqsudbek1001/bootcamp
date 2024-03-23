class Arr:
    def __init__(self, arr):
        self.arr = arr

    def rearrange(self):
        manfiy_num = [num for num in self.arr if num < 0]
        musbat_num = [num for num in self.arr if num >= 0]
        return manfiy_num[::-1] + musbat_num[::-1]


if __name__ == "__main__":
    arr1 = list(map(int, input("Masalan 1, 2, 3, 4:  ").split(',')))

    arr = arr1
    operations = Arr(arr)
    rearranged_arr = operations.rearrange()
    print("natija: ", rearranged_arr)
