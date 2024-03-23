from abc import ABC, abstractmethod
class PROGRESSIYA(ABC):
    @abstractmethod
    def had_topish(self):
        pass
    @abstractmethod
    def yigindini_hisoblash(self, n):
        pass
class ARIFM_PROGRESS(PROGRESSIYA):
    def __init__(self, a1, d):
        self.a1 = a1
        self.d = d
    def had_topish(self):
        return "har bir had oldingisiga qo'shilgan o'rtacha ayirma bilan topiladi."

    def yigindini_hisoblash(self, n):
        return n * (self.a1 + (n - 1) * self.d) / 2
class GEOM_PROGRESS(PROGRESSIYA):
    def __init__(self, a1, q):
        self.a1 = a1
        self.q = q

    def had_topish(self):
        return "Geometrikda har bir had, oldingisiga ko'paytma bilan topiladi."

    def yigindini_hisoblash(self, n):
        if self.q == 1:
            return n * self.a1
        else:
            return self.a1 * (1 - self.q ** n) / (1 - self.q)

if __name__ == "__main__":
    arifm_progressiya = ARIFM_PROGRESS(2, 3)
    geom_progressiya = GEOM_PROGRESS(2, 3)

    print(arifm_progressiya.had_topish())
    print("Arifmetik 5 ta hadi yig'indisi:", arifm_progressiya.yigindini_hisoblash(5))

    print(geom_progressiya.had_topish())
    print("Geometrining 5 ta hadi yig'indisi:", geom_progressiya.yigindini_hisoblash(5))
