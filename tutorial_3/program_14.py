from breezypythongui import EasyFrame
import math

class SqrtGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square Root Calculator")
        self.inp = self.addIntegerField(value=0, row=0, column=0)
        self.res = self.addFloatField(value=0, row=1, column=0, state="readonly")
        self.addButton(text="Compute", row=2, column=0, command=self.compute)

    def compute(self):
        try:
            num = self.inp.getNumber()
            if num < 0:
                raise ValueError("Negative number")
            self.res.setNumber(math.sqrt(num))
        except:
            self.messageBox(title="Error", message="Invalid Input")

SqrtGUI().mainloop()