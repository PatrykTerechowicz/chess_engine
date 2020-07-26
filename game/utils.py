def at(board, pos):
    if pos[0] > 8 or pos[0] < 0 or pos[1] > 8 or pos[1] < 0:
        return '*'  # wartownik oznaczający koniec planszy
    return board[pos[0], pos[1]]
