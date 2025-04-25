from Pieces import Piece
from Empty import Empty
from PinStatus import PinStatus as PS
from Rook import Rook
from Bishop import Bishop
from Empty import Empty
from PinStatus import PinStatus as PS
from Rook import Rook
from Bishop import Bishop
class Queen(Rook, Bishop):
    def __init__(self, color, index,arr):
        super().__init__(color,arr, index)
        self.index = index
        self.pin_state = PS.NOT_PINNED
        self.arr = arr
        self.name = "queen"
    def get_moves(self):
        """
        Get the legal moves for the Queen

        Returns:
            arr[int]: list of indexes of legal moves for the Queen
        """
        legal_moves = []
        legal_moves += self.check_legal_queen()
        return legal_moves
    def check_legal_queen(self):
        """
        Check the legal moves for the Queen

        Returns:
            arr[int]: list of indexes of legal moves for the Queen
        """
        legal_moves = []
        legal_moves += self.check_legal_rook()
        legal_moves += self.check_legal_bishop()
        return legal_moves
            