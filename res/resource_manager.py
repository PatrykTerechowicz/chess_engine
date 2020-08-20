from tkinter import *
from pathlib import Path

res_path = Path.cwd() / 'res'
menu_image_path = Path.cwd() / 'res' / 'menu.png'
empty_cell_path = Path.cwd() / 'res' / 'empty.png'


class PieceImages:
    def __init__(self):
        self.black_bishop = PhotoImage(file=res_path / 'black_bishop.png')
        self.black_king = PhotoImage(file=res_path / 'black_king.png')
        self.black_knight = PhotoImage(file=res_path / 'black_knight.png')
        self.black_pawn = PhotoImage(file=res_path / 'black_pawn.png')
        self.black_queen = PhotoImage(file=res_path / 'black_queen.png')
        self.black_rook = PhotoImage(file=res_path / 'black_rook.png')
        self.white_bishop = PhotoImage(file=res_path / 'white_bishop.png')
        self.white_king = PhotoImage(file=res_path / 'white_king.png')
        self.white_knight = PhotoImage(file=res_path / 'white_knight.png')
        self.white_pawn = PhotoImage(file=res_path / 'white_pawn.png')
        self.white_queen = PhotoImage(file=res_path / 'white_queen.png')
        self.white_rook = PhotoImage(file=res_path / 'white_rook.png')
        self.empty = PhotoImage(file=str(empty_cell_path))


images = None


def init_image():
    global images
    images = PieceImages()
