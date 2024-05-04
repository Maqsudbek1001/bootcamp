import math

num = int(input("Son kiriting: "))
sign = math.floor(math.log10(abs(num)))
result = num / 10 ** sign

print(f"{num} ning ilmiy ko'rinishi: {result} * 10 ^ {sign}")