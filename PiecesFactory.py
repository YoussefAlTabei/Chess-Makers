from __future__ import annotations

from abc import ABC

from Bishop import Bishop
from Color import Color
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook


class PiecesFactory(ABC):

    """
    Abstract Factory class for creating pieces
    """
    def __init__(self):
        self.color = ""

    def create_pawn(self) -> Pawn:
        """
        Create a pawn        :return:
        """
        return Pawn(self.color)

    def create_bishop(self) -> Bishop:
        """
        Create a bishop        :return:
        """
        return Bishop(self.color)

    def create_knight(self) -> Knight:
        """
        Create a knight        :return:
        """
        return Knight(self.color)

    def create_rooks(self) -> Rook:
        """
        Create a rook        :return:
        """
        return Rook(self.color)

    def create_queen(self) -> Queen:
        """
        Create a queen        :return:
        """
        return Queen(self.color)

    def create_king(self) -> King:
        """
        Create a king        :return:
        """
        return King(self.color)



class WhiteFactory(PiecesFactory):

    """
    Factory class for creating white pieces
    """
    def __init__(self):
        super().__init__()
        self.color = Color.WHITE


class BlackFactory(PiecesFactory):

    """
    Factory class for creating black pieces
    """

    def __init__(self):
        super().__init__()
        self.color = Color.BLACK


if __name__ == '__main__':
    white_factory = WhiteFactory()
    white_pawn = white_factory.create_pawn()
    white_bishop = white_factory.create_bishop()
    white_knight = white_factory.create_knight()
    white_rooks = white_factory.create_rooks()
    white_queen = white_factory.create_queen()
    white_king = white_factory.create_king()
    print(white_pawn)
    print(white_bishop)
    print(white_knight)
    print(white_rooks)
    print(white_queen)
    print(white_king)
    black_factory = BlackFactory()
    black_pawn = black_factory.create_pawn()
    black_bishop = black_factory.create_bishop()
    black_knight = black_factory.create_knight()
    black_rooks = black_factory.create_rooks()
    black_queen = black_factory.create_queen()
    black_king = black_factory.create_king()
    print(black_pawn)
    print(black_bishop)
    print(black_knight)
    print(black_rooks)
    print(black_queen)
    print(black_king)




