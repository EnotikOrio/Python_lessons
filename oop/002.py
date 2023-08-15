
class Calc:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        pass
    def summ(self):
        return self.n1 + self.n2

res_1 = Calc(5, 7)
print(res_1.summ())