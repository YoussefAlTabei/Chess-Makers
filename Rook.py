from Pieces import Piece, PinStatus

class Rook(Piece):
    def __init__(self, color, index):
        super().__init__(color)
        self.index = index
        self.has_moved = False
        self.pin_state = PinStatus.NOT_PINNED
    def check_legal_moves(self):
        legal_moves = []
        pass
        # if self.pin_state == PINNED_DIAG:
        #     pass
            