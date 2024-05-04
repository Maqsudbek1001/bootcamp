def recursiv_name(name):
    if len(name) == 0:
        return " "
    else:
        return name[-1] + recursiv_name(name[:-1])

input_name = input("Ismni kiriting: ")
reversed_name = recursiv_name(input_name)
print(f"Teskari tartibdagi ism: {reversed_name}")
