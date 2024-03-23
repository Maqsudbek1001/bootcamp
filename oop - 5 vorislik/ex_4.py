class SATR:
    def __init__(self, satr):
        self.satr = satr
    def chop_qilish(self):
        print("Berilgan satr kirit:", self.satr)
class ARIFM_AMAL(SATR):
    def __init__(self, satr):
        super().__init__(satr)
        self.amal = ['+', '-', '*', '/']

    def amalni_bajarish(self, son1, son2):
        for amal in self.amal:
            if amal in self.satr:
                if amal == '+':
                    return son1 + son2
                elif amal == '-':
                    return son1 - son2
                elif amal == '*':
                    return son1 * son2
                elif amal == '/':
                    if son2 != 0:
                        return son1 / son2
                    else:
                        return "0 ga teng bo'lmaydi"

if __name__ == "__main__":
    satr = "3+5"
    arifm_amal = ARIFM_AMAL(satr)
    arifm_amal.chop_qilish()
    son1 = int(satr[0])
    son2 = int(satr[2])
    print("Natija:", arifm_amal.amalni_bajarish(son1, son2))
