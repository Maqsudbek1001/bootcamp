from abc import ABC, abstractmethod
class SANOQ_SISTEMA_10:
    def __init__(self, son):
        self.son = son

    def oqish(self):
        return int(self.son)

    def saqlash(self):
        return str(self.son)

    @abstractmethod
    def chop_qilish(self):
        pass


class SANOQ_SISTEMA_2(SANOQ_SISTEMA_10):
    def chop_qilish(self):
        print("2 lik sanoq sistemasidagi ko'rinishi:", bin(self.oqish()))
class SANOQ_SISTEMA_8(SANOQ_SISTEMA_10):
    def chop_qilish(self):
        print("8 lik sanoq sistemasidagi ko'rinishi:", oct(self.oqish()))
class SANOQ_SISTEMA_16(SANOQ_SISTEMA_10):
    def chop_qilish(self):
        print("16 lik sanoq sistemasidagi ko'rinishi:", hex(self.oqish()))
if __name__ == "__main__":
    son = "10"
    sanoq_sistema_2 = SANOQ_SISTEMA_2(son)
    sanoq_sistema_8 = SANOQ_SISTEMA_8(son)
    sanoq_sistema_16 = SANOQ_SISTEMA_16(son)

    sanoq_sistema_2.chop_qilish()
    sanoq_sistema_8.chop_qilish()
    sanoq_sistema_16.chop_qilish()

