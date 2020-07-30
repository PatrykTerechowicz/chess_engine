from tkinter import Tk, Frame, Canvas, Button, PhotoImage
import cell
from game import Game
import math
from pathlib import Path

"""Used for board size."""
HEIGHT, WIDTH = 500, 500

root = Tk()
cell.init_images()


class App:
    def __init__(self):
        pass


def main():
    game = Game()
    # Initializing cells data
    cells = [[None] * 8] * 8
    for i in range(8):
        for j in range(8):
            cells[i][j] = cell.Cell(i, j, game.board)
            cells[i][j].set_piece(game.board[i][j])
            cells[i][j].grid(column=i, row=j)

    root.mainloop()


if __name__ == '__main__':
    main()
