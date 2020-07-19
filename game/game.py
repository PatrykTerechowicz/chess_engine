from array import array
from collections import Set
from player import Player
from pieces import Piece, Piece_Type

import pieces

initial_pieces = [Piece_Type.ROOK, Piece_Type.KNIGHT, Piece_Type.BISHOP,
                  Piece_Type.KING, Piece_Type.QUEEN,
                  Piece_Type.BISHOP,Piece_Type.KNIGHT, Piece_Type.ROOK]


class Game:
    def __init__(self):
        self.pieces = set()
        # PAWNS
        self.pieces.update([Piece(i, 6, Player.WHITE, Piece_Type.PAWN) for i in range(8)])
        self.pieces.update([Piece(i, 1, Player.BLACK, Piece_Type.PAWN) for i in range(8)])
        # rest pieces
        self.pieces.update([Piece(i, 7, Player.WHITE, initial_pieces[i]) for i in range(8)])
        self.pieces.update([Piece(i, 0, Player.BLACK, initial_pieces[i]) for i in range(8)])

    def print_board(self):
        board = []
        for i in range(8):
            board.append([])
            for j in range(8):
                board[i].append(' ')
        for piece in self.pieces:
            x, y = piece.x, piece.y
            board[x][y] = piece.piece_type.name
        for i in range(8):
            print(board[i])

    def checkmate(self) -> tuple:
        for piece in self.pieces:
            pass
        return False

    def mate(self) -> tuple:
        pass
