from breezypythongui import EasyFrame

class UppercaseGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Uppercase Converter")
        self.inp = self.addTextField(text="", row=0, column=0)
        self.res = self.addTextField(text="", row=1, column=0, state="readonly")
        self.addButton(text="Convert", row=2, column=0, command=self.convert)

    def convert(self):
        self.res.setText(self.inp.getText().upper())

UppercaseGUI().mainloop()