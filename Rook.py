from Pieces import Piece
import PinStatus
import Empty

class Rook(Piece):
    def __init__(self, color, index):
        super().__init__(color)
        self.index = index
        self.has_moved = False
        self.pin_state = PinStatus.NOT_PINNED
    def check_legal_rook(self):
        """
        Check the legal moves for the rook
    
        Returns:
             arr[int]: list of indexes of legal moves for the rook
        """
        legal_moves = []
        if self.pin_state != PinStatus.PINNED_DIAG:
            if self.pin_state != PinStatus.PINNED_HORZ:
                temp = self.index + 8
                temp2 = self.index - 8
                while isinstance(super().arr[temp], Empty) and temp <= 64 and temp >=0:
                    legal_moves.append(temp)
                    temp += 8         
                while isinstance(super().arr[temp2], Empty) and temp2 <= 64 and temp2 >=0:
                    legal_moves.append(temp2)
                    temp2 -= 8   
            if self.pin_state != PinStatus.PINNED_VERT:
                temp = self.index + 1
                temp2 = self.index - 1
                while isinstance(super().arr[temp], Empty) and temp % 8 != 0:
                    legal_moves.append(temp)
                    temp += 1
                while isinstance(super().arr[temp2], Empty) and temp2 % 8 != 7:
                    legal_moves.append(temp2)
                    temp2 -= 1
        return legal_moves

