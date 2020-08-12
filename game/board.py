import pieces
from player import Player

class Board:
    def __init__(self):
        self.pieces = set()
        for i in range(8):
            self.pieces.add(pieces.Pawn(i, 0, Player.WHITE if i%2 == 0 else Player.BLACK))

    def __getitem__(self, item: tuple):
        for piece in self.pieces:
            if piece.x == item[0] and piece.y == item[1]:
                return piece
        return None