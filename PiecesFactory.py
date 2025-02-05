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

    def create_pawn(self, index: int, arr: list) -> Pawn:
        """
        Create a pawn
        :return:
        """
        return Pawn(self.color, index, arr)

    def create_bishop(self, index: int, arr: list) -> Bishop:
        """
        Create a bishop
        :return:
        """
        return Bishop(self.color, index, arr)

    def create_knight(self, index: int, arr: list) -> Knight:
        """
        Create a knight
        :return:
        """
        return Knight(self.color, index, arr)

    def create_rooks(self, index: int, arr: list) -> Rook:
        """
        Create a rook
        :return:
        """
        return Rook(self.color, index, arr)

    def create_queen(self, index: int, arr: list) -> Queen:
        """
        Create a queen
        :return:
        """
        return Queen(self.color, index, arr)

    def create_king(self, index: int, arr: list) -> King:
        """
        Create a king
        :return:
        """
        return King(self.color, index, arr)


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
    white_pawn = white_factory.create_pawn(1)
    white_bishop = white_factory.create_bishop(2)
    white_knight = white_factory.create_knight(3)
    white_rooks = white_factory.create_rooks(4)
    white_queen = white_factory.create_queen(5)
    white_king = white_factory.create_king(6)
    print(white_pawn)
    print(white_bishop)
    print(white_knight)
    print(white_rooks)
    print(white_queen)
    print(white_king)
    black_factory = BlackFactory()
    black_pawn = black_factory.create_pawn(1)
    black_bishop = black_factory.create_bishop(2)
    black_knight = black_factory.create_knight(3)
    black_rooks = black_factory.create_rooks(4)
    black_queen = black_factory.create_queen(5)
    black_king = black_factory.create_king(6)
    print(black_pawn)
    print(black_bishop)
    print(black_knight)
    print(black_rooks)
    print(black_queen)
    print(black_king)
