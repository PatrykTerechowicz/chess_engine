from tkinter import Tk, Frame, Canvas, Button, PhotoImage
from cell import Cell, BLACK_BOARD, WHITE_BOARD
from game import Game
import math
from pathlib import Path

"""Used for board size."""
HEIGHT, WIDTH = 500, 500
"""Used for determining cell colour."""
root = Tk()

def main():
    frame = Frame(width=WIDTH, height=HEIGHT)
    photo = PhotoImage(file=Path.cwd().parents[0] / "res" / "empty.png")
    photo_taken = PhotoImage(file=Path.cwd().parents[0] / "res" / "generalPiece.png")
    game = Game()

    frame.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
