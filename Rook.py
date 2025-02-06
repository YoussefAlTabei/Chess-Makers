from Pieces import Piece
from PinStatus import PinStatus
from PinStatus import PinStatus
import Empty
from Color import Color as c
class Rook(Piece):
    def __init__(self, color, index, arr):
        super().__init__(color, arr,index)
        self.index = index
        self.has_moved = False
        self.pin_state = PinStatus.NOT_PINNED
        self.arr = arr

    def get_moves(self):
        """
        Get the legal moves for the rook
        
        Returns:
            arr[int]: list of indexes of legal moves for the rook
        """
        legal_moves = []
        legal_moves += self.check_legal_rook()
        return legal_moves

    def check_legal_rook(self):
        """
        Check the legal moves for the rook
    
        Returns:
             arr[int]: list of indexes of legal moves for the rook
        """
        legal_moves = []
        color_dir = 1 if self.color == c.WHITE else -1 
        if self.pin_state != PinStatus.PINNED_DIAG:
            if self.pin_state != PinStatus.PINNED_HORZ:
                temp = self.index + 8 * color_dir
                temp2 = self.index - 8* color_dir
                while  temp <= 63 and temp >= 0 and isinstance(self.arr[temp], Empty.Empty) :
                    legal_moves.append(temp)
                    temp += 8* color_dir   
                # print("temp: ",temp,self.arr[temp].color)
                if temp <= 63 and temp >= 0 and self.arr[temp].color != self.color:
                    legal_moves.append(temp)
                while  temp2 <= 63 and temp2 >= 0 and isinstance(self.arr[temp2], Empty.Empty):
                    legal_moves.append(temp2)
                    temp2 -= 8  * color_dir
                if temp2 <= 63 and temp2 >= 0 and self.arr[temp2].color != self.color:
                    legal_moves.append(temp2)
            if self.pin_state != PinStatus.PINNED_VERT:
                if self.index % 8 != 0:
                    temp2 = self.index - 1 
                if self.index % 8 != 8:
                    temp = self.index + 1
                while temp <= 63 and temp >= 0 and temp % 8 != 0 and isinstance(self.arr[temp], Empty.Empty):
                    legal_moves.append(temp)
                    temp += 1 *color_dir
                if temp <= 63 and temp >= 0 and not isinstance(self.arr[temp], Empty.Empty) and self.arr[temp].color != self.color:
                    legal_moves.append(temp)
                while temp2 <= 63 and temp2 >= 0 and temp2 % 8 != 7 and  isinstance(self.arr[temp2], Empty.Empty):
                    legal_moves.append(temp2)
                    temp2 -= 1*color_dir
                if temp2 <= 63 and temp2 >= 0 and not isinstance(self.arr[temp2], Empty.Empty) and self.arr[temp2].color != self.color:
                    legal_moves.append(temp2)
        return legal_moves

