from player import Player



class Piece:
    def __init__(self, x, y, player: Player):
        self.x = x
        self.y = y
        self.player = player
