from breezypythongui import EasyFrame
import random

class CompGuess(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Computer Guesses")
        self.low, self.high = 1, 100
        self.guess = random.randint(self.low, self.high)
        self.msg = self.addLabel(text=f"Is it {self.guess}?", row=0, column=0)
        self.addButton(text="Too Small", row=1, column=0, command=self.too_small)
        self.addButton(text="Too Large", row=2, column=0, command=self.too_large)
        self.addButton(text="Correct", row=3, column=0, command=self.correct)

    def too_small(self):
        self.low = self.guess + 1
        self.next_guess()

    def too_large(self):
        self.high = self.guess - 1
        self.next_guess()

    def correct(self):
        self.msg["text"] = "I guessed it!"

    def next_guess(self):
        if self.low <= self.high:
            self.guess = random.randint(self.low, self.high)
            self.msg["text"] = f"Is it {self.guess}?"
        else:
            self.msg["text"] = "Something went wrong!"

CompGuess().mainloop()