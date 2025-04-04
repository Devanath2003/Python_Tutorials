from breezypythongui import EasyFrame
import random

class GuessGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Guess the Number")
        self.num = random.randint(1, 100)
        self.guesses = 0
        self.inp = self.addIntegerField(value=0, row=0, column=0)
        self.msg = self.addLabel(text="Guess a number!", row=1, column=0)
        self.addButton(text="Check", row=2, column=0, command=self.check)

    def check(self):
        self.guesses += 1
        g = self.inp.getNumber()
        if g > self.num:
            self.msg["text"] = "Too large, try again"
        elif g < self.num:
            self.msg["text"] = "Too small, try again"
        else:
            self.msg["text"] = f"Correct! Guesses: {self.guesses}"

GuessGame().mainloop()