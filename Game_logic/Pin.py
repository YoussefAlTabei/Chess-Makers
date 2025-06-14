from Pieces import Piece
from Empty import Empty
from Rook import Rook
from Bishop import Bishop
from Queen import Queen
from Knight import Knight
from Pawn import Pawn
from Color import Color as c
from PinStatus import PinStatus
class Pin:
    
    @staticmethod
    def pin_check(self,index,boardArray):
        """
        Checks if a piece is pinned to its king and determines the direction of the pin.

        Args:
            index (int): The index of the piece to check on the board.
            boardArray (list): The current state of the board as an array of pieces.

        Returns:
            PinStatus: An enum indicating whether the piece is pinned and, if so, in which direction.

        Notes:
            - The function checks for vertical, horizontal, and diagonal pins relative to the king.
            - Assumes that the boardArray supports a 'find' method to locate the king.
        """

        if boardArray[index].color == c.WHITE:
            King = boardArray.find(lambda x: isinstance(x, King) and x.color == c.WHITE)
        else:
            King = boardArray.find(lambda x: isinstance(x, King) and x.color == c.BLACK)
        if index % 8 == King.index % 8:
            return self.vert_pin(index, boardArray, King)
        elif index // 8 == King.index // 8:
            return self.horz_pin(index, boardArray, King)
        elif abs(index % 8 - King.index % 8) == abs(index // 8 - King.index // 8):
           return self.diag_pin(index, boardArray, King)
        return PinStatus.NOT_PINNED
    def vert_pin(index, boardArray, King):
        if index < King.index:
                direction = -1
        else:
            direction = 1
        for i in range(King.index + direction, index + direction, direction):
            if isinstance(boardArray[i], Empty):
                continue
            elif isinstance(boardArray[i], Rook) or isinstance(boardArray[i], Queen):
                return PinStatus.PINNED_VERT
    def horz_pin(index, boardArray, King):
        if index < King.index:
                direction = -8
        else:
            direction = 8
        for i in range(King.index + direction, index + direction, direction):
            if isinstance(boardArray[i], Empty):
                continue
            elif isinstance(boardArray[i], Rook) or isinstance(boardArray[i], Queen):
                return PinStatus.PINNED_HORZ
        return PinStatus.NOT_PINNED
    def diag_pin(index, boardArray, King):
        if index < King.index:
                direction = -9 if index % 8 < King.index % 8 else -7
        else:
            direction = 9 if index % 8 < King.index % 8 else 7
        for i in range(King.index + direction, index + direction, direction):
            if isinstance(boardArray[i], Empty):
                continue
            elif isinstance(boardArray[i], Bishop) or isinstance(boardArray[i], Queen):
                return PinStatus.PINNED_DIAG