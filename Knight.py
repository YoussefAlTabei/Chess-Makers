from Pieces import Piece
import PinStatus as PS

class Knight(Piece):
    def __init__(self, color, index):
        super().__init__(color)
        self.index = index
        self.pin_state = PS.NOT_PINNED
    def check_legal(self):
        """
        Check the legal moves for the knight
         arr[int]: list of indexes of legal moves for the knight
        """
        legal_moves = []
        if self.pin_state != PS.NOT_PINNED:
            if self.index % 8 != 0 and self.index > 15 and super().arr[self.index - 17].color != self.color:
                legal_moves.append(self.index - 17)
            if self.index % 8 != 0 and self.index < 48 and super().arr[self.index + 15].color != self.color:
                legal_moves.append(self.index + 15)
            if self.index % 8 != 7 and self.index > 15 and super().arr[self.index - 15].color != self.color:
                legal_moves.append(self.index - 15)
            if self.index % 8 != 7 and self.index < 48 and super().arr[self.index + 17].color != self.color:
                legal_moves.append(self.index + 17)
            if self.index % 8 > 1 and self.index > 7 and super().arr[self.index - 10].color != self.color:
                legal_moves.append(self.index - 10)
            if self.index % 8 > 1 and self.index < 56 and super().arr[self.index + 6].color != self.color:
                legal_moves.append(self.index + 6)
            if self.index % 8 < 6 and self.index > 7 and super().arr[self.index - 6].color != self.color:
                legal_moves.append(self.index - 6)
            if self.index % 8 < 6 and self.index < 56 and super().arr[self.index + 10].color != self.color:
                legal_moves.append(self.index + 10)
        return legal_moves