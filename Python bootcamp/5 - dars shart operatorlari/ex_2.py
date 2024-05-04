name_number = int(input("Son kiring: "))

if name_number%3 == 0 and name_number % 5 != 0:
    print("Fiz")
elif name_number % 5 == 0 and name_number%3 != 0:
    print("Biz")
elif name_number % 5 == 0 and name_number%3 == 0:
    print("FizBiz")
else:
    print(name_number)

