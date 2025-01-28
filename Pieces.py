from abc import ABC, abstractmethod
import Color


class Piece(ABC):
    def __init__(self, color: Color):
        self.color = color

    def __repr__(self):
        return f"{self.color.value} {self.__class__.__name__}"
