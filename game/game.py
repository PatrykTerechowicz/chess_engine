import pieces
from player import Player
from board import Board

class Game:
    def __init__(self):
        self.board = Board()

    def print_board(self):
        pass

    def move(self, x0, y0, x1, y1):
        piece_first = self.board[x0][y0]
        if isinstance(piece_first, pieces.Piece):
            return
        piece_second = self.board[x1][y1]
        # first we need to check if first piece can reach second piece
        possible_moves, possible_attacks = piece_first.calculate_moves()
        pass

    def checkmate(self) -> tuple:
        pass

    def mate(self) -> tuple:
        pass
