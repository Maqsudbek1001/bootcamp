name = int(input("name "))
total = {}
for i in range(1, name):
    if i >= 1:
        total.update({i: i*i})
print(total)
