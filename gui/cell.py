from tkinter import Button

BLACK_BOARD, WHITE_BOARD = "#2b9466", "#84e0cb"


def slot_callback():
    print("button clocked")


class Cell(Button):
    def __init__(self, x, y, **kw):  # czy da się zmienić **kw przed odpaleniem konstruktora nadrzędnego?
        super().__init__(command=slot_callback, **kw)
        self.x = x
        self.y = y
        self.colour = WHITE_BOARD if (x + y) % 2 == 0 else BLACK_BOARD
        self.config({'background':self.colour})
        # style options
