name = {
    "Jasurbek": 3,
    "Abbos": 4,
    "Azamat": 8,
    "Axror": 5,
}
print(f"{list(name.keys())} shu ismlardan kiritng")
person = input("ism kiritng ")
if person.capitalize() in name.keys():
    name.pop(person.capitalize())
    print(name)
else:
    print("Bunday ism mavjud emas")
