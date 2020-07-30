class Board:
    def __init__(self):
        self.pieces = set()

    def __getitem__(self, item: tuple):
        for piece in self.pieces:
            if piece.x == item[0] and piece.y == item[1]:
                return piece
        return None
