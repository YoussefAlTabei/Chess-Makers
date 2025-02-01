from Pieces import Piece
import PinStatus as PS
import Empty
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.index = None
        self.pin_state = PS.NOT_PINNED
    def check_legal_bishop(self):
        """
        Check the legal moves for the bishop

        Returns:
            arr[int]: list of indexes of legal moves for the bishop
        """
        if self.pin_state != PS.PINNED_HORZ and self.pin_state != PS.PINNED_VERT:
            legal_moves = []
            temp = self.index + 7
            while temp % 8 != 0 and temp > 7 and (super().arr[temp].color != self.color or isinstance(super().arr[temp], Empty)):
                legal_moves.append(temp)
                if super().arr[temp].color != self.color:
                    break
                temp += 7
            temp = self.index + 9
            while temp % 8 != 7 and temp < 56 and (super().arr[temp].color != self.color or isinstance(super().arr[temp], Empty)):
                legal_moves.append(temp)
                if super().arr[temp].color != self.color:
                    break
                temp += 9
            temp = self.index - 7
            while temp % 8 != 7 and temp > 7 and (super().arr[temp].color != self.color or isinstance(super().arr[temp], Empty)):
                legal_moves.append(temp)
                if super().arr[temp].color != self.color:
                    break
                temp -= 7
            temp = self.index - 9
            while temp % 8 != 0 and temp < 56 and (super().arr[temp].color != self.color or isinstance(super().arr[temp], Empty)):
                legal_moves.append(temp)
                if super().arr[temp].color != self.color:
                    break
                temp -= 9
            return legal_moves
            