from tkinter import Tk, Frame, Canvas, Button, PhotoImage
from cell import Cell, BLACK_BOARD, WHITE_BOARD
from game import Game
import math
from pathlib import Path

"""Used for board size."""
HEIGHT, WIDTH = 500, 500
"""Used for determining cell colour."""
root = Tk()


# intended to one use
def draw_background(canvas):
    x0, y0 = 0, 0
    padding = 2
    xh = math.floor(HEIGHT / 8)
    yh = math.floor(WIDTH / 8)
    for i in range(8):
        y0 = i * yh + padding
        for j in range(8):
            x0 = j * xh + padding
            canvas.create_rectangle(x0, y0, x0 + xh, y0 + yh, fill=WHITE_BOARD if (i + j) % 2 == 0 else BLACK_BOARD)


def main():
    frame = Frame(width=WIDTH, height=HEIGHT)
    photo = PhotoImage(file=Path.cwd().parents[0] / "res" / "empty.png")
    photo_taken = PhotoImage(file=Path.cwd().parents[0] / "res" / "generalPiece.png")
    game = Game()

    pieces = game.pieces #todo : change it all

    slots = set()
    for i in range(8):
        for j in range(8):
            slots.add((i, j))

    taken_pieces = set()
    for piece in pieces:
        taken_pieces.add((piece.x, piece.y))

    free_slots = slots.difference(taken_pieces)

    for free_slot in free_slots:
        x = free_slot[0]
        y = free_slot[1]
        cell = Cell(x, y, master=frame, image=photo, width=60, height=60)
        cell.grid(column=x, row=y)

    for taken_slot in taken_pieces:
        x = taken_slot[0]
        y = taken_slot[1]
        cell = Cell(x, y, master=frame, image=photo_taken, width=60, height=60)
        cell.grid(column=x, row=y)
    frame.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
