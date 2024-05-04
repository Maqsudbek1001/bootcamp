print("ax^2 + bx + c kvadrat tenglamani \n index xadlarini kiriting")
a = float(input("a inde -> "))
b = float(input("b inde -> "))
c = float(input("c inde -> "))
diskriminant = (b*b)-4*a*c

if diskriminant > 0:
    print("tenglama 2 ta yechimga ega: ")
elif diskriminant == 0:
    print("Bitta yechimga ega: ")
else:
    print("Yechimga ega emas: ")