class student:
    def __init__(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    @property
    def calcAvg(self):
        return (self.sub1 + self.sub2 + self.sub3) / 3


s1 = student(98, 97, 100)
print(s1.calcAvg)
s1.sub3 = 90
print(s1.calcAvg)