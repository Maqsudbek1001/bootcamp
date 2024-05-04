son_kiritish = int(input("Son kiriting: "))

if son_kiritish % 2 == 0 and son_kiritish != 0:
    print(f"bu {son_kiritish} juft son")
elif son_kiritish % 2 != 0:
    print(f"bu toq son {son_kiritish}")
elif son_kiritish == 0:
    print(f"bu 0 son --> {son_kiritish}")
