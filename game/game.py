import pieces
from player import Player

class Game:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        for i in range(8):
            self.board[i][0] = pieces.Pawn(i, 0, player=Player.WHITE)

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
