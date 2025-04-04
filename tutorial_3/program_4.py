from breezypythongui import EasyFrame

class TempConv(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")
        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)
        self.f_in = self.addFloatField(value=32, row=1, column=0)
        self.c_in = self.addFloatField(value=0, row=1, column=1)
        self.addButton(text=">>>>", row=2, column=0, command=self.to_c)
        self.addButton(text="<<<<", row=2, column=1, command=self.to_f)
    
    def to_c(self):
        f = self.f_in.getNumber()
        self.c_in.setNumber((f - 32) * 5 / 9)
    
    def to_f(self):
        c = self.c_in.getNumber()
        self.f_in.setNumber((c * 9 / 5) + 32)

TempConv().mainloop()