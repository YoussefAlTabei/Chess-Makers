from Pieces import Piece
from Game_logic.PinStatus import PinStatus as PS
from Game_logic.Color import Color as c
from Empty import Empty
class Knight(Piece):
    def __init__(self, color, index, arr):
        super().__init__(color, arr,index)
        self.index = index
        self.pin_state = PS.NOT_PINNED
        self.arr = arr
        self.name = "knight"
    def get_moves(self):
        """
        Get the legal moves for the knight

        Returns:
            arr[int]: list of indexes of legal moves for the knight
        """
        legal_moves = []
        legal_moves += self.check_legal()
        return legal_moves
    def check_legal(self):
        """
        Check the legal moves for the knight
         arr[int]: list of indexes of legal moves for the knight
        """
        legal_moves = []
        color_dir = -1 if self.color == c.WHITE else 1
            if self.index % 8 != 0 and self.index > 15 and (isinstance(self.arr[self.index - 17], Empty) or self.arr[self.index - 17].color != self.color):
                legal_moves.append(self.index - 17)
            if self.index % 8 != 0 and self.index < 48 and (isinstance(self.arr[self.index + 15], Empty) or self.arr[self.index + 15].color != self.color):
                legal_moves.append(self.index + 15)
            if self.index % 8 != 7 and self.index > 15 and (isinstance(self.arr[self.index - 15], Empty) or self.arr[self.index - 15].color != self.color):
                legal_moves.append(self.index - 15)
            if self.index % 8 != 7 and self.index < 48 and (isinstance(self.arr[self.index + 17], Empty) or self.arr[self.index + 17].color != self.color):
                legal_moves.append(self.index + 17)
            if self.index % 8 > 1 and self.index > 7 and (isinstance(self.arr[self.index - 10], Empty) or self.arr[self.index - 10].color != self.color):
                legal_moves.append(self.index - 10)
            if self.index % 8 > 1 and self.index < 56 and (isinstance(self.arr[self.index + 6], Empty) or self.arr[self.index + 6].color != self.color):
                legal_moves.append(self.index + 6)
            if self.index % 8 < 6 and self.index > 7 and (isinstance(self.arr[self.index - 6], Empty) or self.arr[self.index - 6].color != self.color):
                legal_moves.append(self.index - 6)
            if self.index % 8 < 6 and self.index < 56 and (isinstance(self.arr[self.index + 10], Empty) or self.arr[self.index + 10].color != self.color):
                legal_moves.append(self.index + 10)
        return legal_moves