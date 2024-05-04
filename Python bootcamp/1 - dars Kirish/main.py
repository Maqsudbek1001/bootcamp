kompany_name = input("kompany name = ")
kompany_password = int(input("kompany age = "))

newkompany_name = kompany_name.lower()
server_loginname = "pdpsupport"
server_loginpasword = 1988
data_baza = {
    "Jasurbek": 1989,
    "Asdbek": 1767,
    "Abdulloh":1878,
    "Ikromjon":2020
}
if kompany_password == server_loginpasword :
    if kompany_name == server_loginname:
        name_open = input("kompaniyadagi ismingiz: ")
        newname_open = name_open.capitalize()
        if newname_open == data_baza:
            print(data_baza[newname_open])
    else:
        print("qaytaddan urinib ko'ring")

