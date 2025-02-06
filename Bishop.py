from Pieces import Piece
from PinStatus import PinStatus as PS
import Empty
from Color import Color as c 
class Bishop(Piece):
    def __init__(self, color, index, arr):
        super().__init__(color,arr, index)
        self.index = index
        self.pin_state = PS.NOT_PINNED
        self.arr = arr

    def get_moves(self):
        """
        Get the legal moves for the bishop

        Returns:
            arr[int]: list of indexes of legal moves for the bishop
        """
        legal_moves = []
        legal_moves += self.check_legal_bishop()
        return legal_moves

    def check_legal_bishop(self):
        """
        Check the legal moves for the bishop

        Returns:
            arr[int]: list of indexes of legal moves for the bishop
        """
        legal_moves = []
       # color_dir = 1 if self.color == c.WHITE else -1
        if self.pin_state != PS.PINNED_HORZ and self.pin_state != PS.PINNED_VERT:
            legal_moves = []
            temp = self.index + 7 
            while temp <= 63 and temp >= 0 and temp % 8 != 0 and temp > 7 and (isinstance(self.arr[temp], Empty.Empty) or self.arr[temp].color != self.color):
                legal_moves.append(temp)
                if not isinstance(self.arr[temp], Empty.Empty) and  self.arr[temp].color != self.color:
                    break
                temp += 7   
            if temp <= 63 and temp >= 0 and temp % 8 != 7 and (isinstance(self.arr[temp], Empty.Empty) or self.arr[temp].color != self.color):
                legal_moves.append(temp)
            temp = self.index + 9   
            while  temp <= 63 and temp >= 0 and temp % 8 != 7 and temp < 56 and (isinstance(self.arr[temp], Empty.Empty) or self.arr[temp].color != self.color):
                legal_moves.append(temp)
                if not isinstance(self.arr[temp], Empty.Empty) and self.arr[temp].color != self.color:
                    break
                temp += 9   
            if temp <= 63 and temp >= 0 and temp % 8 != 0 and (isinstance(self.arr[temp], Empty.Empty) or self.arr[temp].color != self.color):
                legal_moves.append(temp)
            temp = self.index - 7   
            while  temp <= 63 and temp >= 0 and temp % 8 != 7 and temp > 7 and (isinstance(self.arr[temp], Empty.Empty) or self.arr[temp].color != self.color):
                legal_moves.append(temp)
                if not isinstance(self.arr[temp], Empty.Empty) and self.arr[temp].color != self.color:
                    break
                temp -= 7   
            if temp <= 63 and temp >= 0 and temp % 8 != 0 and (isinstance(self.arr[temp], Empty.Empty) or self.arr[temp].color != self.color):
                legal_moves.append(temp)
            temp = self.index - 9   
            while  temp <= 63 and temp >= 0 and  temp % 8 != 0 and temp < 56 and (isinstance(self.arr[temp], Empty.Empty) or self.arr[temp].color != self.color):
                legal_moves.append(temp)
                if not isinstance(self.arr[temp], Empty.Empty) and self.arr[temp].color != self.color:
                    break
                temp -= 9    
            if temp <= 63 and temp >= 0 and temp % 8 !=7  and (isinstance(self.arr[temp], Empty.Empty) or self.arr[temp].color != self.color):
                legal_moves.append(temp)
            return legal_moves
