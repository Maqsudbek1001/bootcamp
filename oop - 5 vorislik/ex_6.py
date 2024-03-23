class TUPLAM_AB:
    def __init__(self, tuplam):
        self.tuplam = tuplam

    def qoshish(self, element):

        return self.tuplam + (element,)

    def ochirish(self, element):


        return tuple(x for x in self.tuplam if x != element)


    def chop_qilish(self):
        print("Tuplam:", self.tuplam)


class TUPLAM_AMALLARI:
    @staticmethod
    def keshishmasini(tuplam):
        return tuple(set(tuplam))

    @staticmethod
    def birlashmasini(tuplam1, tuplam2):
        return tuplam1 + tuplam2

    @staticmethod
    def ayirmasini(tuplam1, tuplam2):
        return tuple(x for x in tuplam1 if x not in tuplam2)


class TUPLAM(TUPLAM_AB, TUPLAM_AMALLARI):
    pass


if __name__ == "__main__":
    tuplam1 = (1, 2, 3)
    tuplam2 = (3, 4, 5)
    tuplam = TUPLAM(tuplam1)

    print("Tuplam keshishmasi:", TUPLAM_AMALLARI.keshishmasini(tuplam1))
    print("Tuplam birlanishi:", TUPLAM_AMALLARI.birlashmasini(tuplam1, tuplam2))
    print("Tuplam ayirishi:", TUPLAM_AMALLARI.ayirmasini(tuplam1, tuplam2))


    print("Tuplam:", tuplam.tuplam)
    print("Qo'shilgan tuplam:", tuplam.qoshish(4))
    print("O'chirilgan tuplam:", tuplam.ochirish(2))
