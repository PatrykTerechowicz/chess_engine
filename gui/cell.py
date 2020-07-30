from tkinter import Button, PhotoImage
from pathlib import Path
import pieces

BLACK_BOARD, WHITE_BOARD, BLACK_BOARD_H, WHITE_BOARD_H = "#2b9466", "#84e0cb", "#78942b", "#c6e084"
PAWN_IMAGE = ''
EMPTY_IMAGE = ''
def init_images():
    global PAWN_IMAGE, EMPTY_IMAGE
    PAWN_IMAGE = PhotoImage(file=Path.cwd().parents[0] / "res" / "generalPiece.png")
    EMPTY_IMAGE = PhotoImage(file=Path.cwd().parents[0] / "res" / "empty.png")
'''
    photo = 
    photo_taken = PhotoImage(file=Path.cwd().parents[0] / "res" / "generalPiece.png")
'''


def slot_callback():
    print("button clocked")


class Cell(Button):
    def __init__(self, x, y, board, **kw):  # czy da się zmienić **kw przed odpaleniem konstruktora nadrzędnego?
        super().__init__(command=self.slot_callback, **kw)
        self.x = x
        self.y = y
        self.colour = WHITE_BOARD if (x + y) % 2 == 0 else BLACK_BOARD
        self.board = board
        self.config({'background': self.colour})
        # style options

    def set_piece(self, piece):
        if piece is None:
            self.config({'image': EMPTY_IMAGE})
        if isinstance(piece, pieces.Pawn):
            self.config({'image': PAWN_IMAGE})

    def slot_callback(self):
        print("this button is at %d, %d" % (self.x, self.y))
