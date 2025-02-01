from Pieces import Piece
from Empty import Empty
from PinStatus import PinStatus as PS
from Rook import Rook
from Bishop import Bishop
class Queen(Rook, Bishop):
    def __init__(self, color, index):
        super().__init__(color, index)
        self.index = index
        self.pin_state = PS.NOT_PINNED
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
            