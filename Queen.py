from Pieces import Piece
import Empty
import PinStatus as PS
import Rook
import Bishop
class Queen(Rook, Bishop):
    def __init__(self, color, index):
        super().__init__(color)
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
            