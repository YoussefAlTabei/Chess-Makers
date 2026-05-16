from abc import ABC, abstractmethod
import Game_logic.Color as Color


class Piece(ABC):
    def __init__(self, color: Color,arr, index: int):
        self.color = color
        self.index = index
        self.arr = arr
    def __repr__(self):
        """
        Returns a string representation of the chess piece.

        The string representation includes the color and the class name of the piece.

        Returns:
            str: A string in the format "{color} {class name}".
        """
        return f"{self.color.value} {self.__class__.__name__}"
    @abstractmethod
    def get_moves(self):
        pass



