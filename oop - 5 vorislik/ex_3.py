class KITOB:
    def __init__(self, nomi, muallifi, nashriyoti, chop_qilingan_yil):
        self.nomi = nomi
        self.muallifi = muallifi
        self.nashriyoti = nashriyoti
        self.chop_qilingan_yil = chop_qilingan_yil

    def malumotlarni_chiqar(self):

        print("Kitobning nomi:", self.nomi)
        print("Muallifi nomi:", self.muallifi)
        print("Nashriyoti:", self.nashriyoti)
        print("Chop qilingan yili:", self.chop_qilingan_yil)

class UY_KUTUBXONASI:
    def __init__(self, uy_manzili, kutubxona_egasi_familiya, kutubxona_egasi_ismi):
        self.uy_manzili = uy_manzili
        self.kutubxona_egasi_familiya = kutubxona_egasi_familiya
        self.kutubxona_egasi_ismi = kutubxona_egasi_ismi
        self.kitoblar = []
    def kitob_qoshish(self, kitob):

        self.kitoblar.append(kitob)
    def kitoblar_soni(self):
        return len(self.kitoblar)

if __name__ == "__main__":
    kitob1 = KITOB("Alanganga qolgan buxoro", "Abdulla qodiiriy", "Harper & Brothers", 1838)
    kitob1.malumotlarni_chiqar()
    uy_kutubxonasi = UY_KUTUBXONASI("Buxoro viloyati", "Aziza", "Jahonhir")
    uy_kutubxonasi.kitob_qoshish(kitob1)
    print("kitoblar soni:", uy_kutubxonasi.kitoblar_soni())
