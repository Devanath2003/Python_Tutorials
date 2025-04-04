from breezypythongui import EasyFrame

class BouncyBall(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Bouncy Ball Distance")
        self.h = self.addFloatField(value=0, row=0, column=0)
        self.b = self.addFloatField(value=0, row=1, column=0)
        self.n = self.addIntegerField(value=0, row=2, column=0)
        self.res = self.addFloatField(value=0, row=3, column=0, state="readonly")
        self.addButton(text="Compute", row=4, column=0, command=self.compute)

    def compute(self):
        h = self.h.getNumber()
        b = self.b.getNumber()
        n = self.n.getNumber()
        d = h
        for _ in range(n):
            h *= b
            d += 2 * h
        self.res.setNumber(d)

BouncyBall().mainloop()