from Pieces import Piece
from PinStatus import PinStatus

import Empty
class Pawn(Piece):

    def __init__(self, color, index):
        super().__init__(color, index)
        self.index = index
        self.has_moved = False
        self.pin_state = PinStatus.NOT_PINNED
        self.en_passant = False

    def check_legal_moves(self):
        """
        Check the legal moves for the pawn
        
        arr[int]: list of indexes of legal moves for the pawn
        """
        legal_moves = []
        if self.pin_state != PinStatus.PINNED_DIAG and self.pin_state != PinStatus.PINNED_HORZ:
            if isinstance(super().arr[self.index + 8], Empty):
                legal_moves.append(self.index + 8)
            if isinstance(super().arr[self.index + 16], Empty):
                if not self.has_moved:
                    legal_moves.append(self.index + 16)
        if self.pin_state != PinStatus.PINNED_VERT and self.pin_state != PinStatus.PINNED_HORZ:
            if self.index % 8 != 0 and super().arr[self.index + 7].color != self.color:
                legal_moves.append(self.index + 7)
            if self.index % 8 != 7 and super().arr[self.index + 9].color != self.color:
                legal_moves.append(self.index + 9)  
        if super().arr[self.index-1].color != self.color and isinstance(super().arr[self.index-1], Pawn) and super().arr[self.index-1].en_passant:
            legal_moves.append(self.index-7)
        if super().arr[self.index+1].color != self.color and isinstance(super().arr[self.index+1], Pawn) and super().arr[self.index+1].en_passant:
            legal_moves.append(self.index+9)
        return legal_moves