from enum import Enum
from player import Player


class Piece_Type(Enum):
    PAWN = 'P'
    ROOK = 'R'
    BISHOP = 'B'
    KNIGHT = 'N'
    QUEEN = 'Q'
    KING = 'K'


class Piece:
    def __init__(self, x, y, player: Player, piece_type: Piece_Type):
        self.x = x
        self.y = y
        self.player = player
        self.piece_type = piece_type
