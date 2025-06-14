from abc import ABC, abstractmethod
import Game_logic.Color as Color
from Game_logic.PinStatus import PinStatus


class Piece(ABC):
    def __init__(self, color: Color,arr, index: int, is_pinned: PinStatus = PinStatus.NOT_PINNED):
        self.color = color
        self.index = index
        self.is_pinned = is_pinned
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

    def check_Orthogonal_pin(self, king_index, piece_index,arr):
        """
        checks if the piece is pinned to the king in a horizontal and vertical directions

        Args:
            king_index (int): position of the king
            piece_index (int): position of piece

        Returns:
             PinStatus(Enum): returns the pin status of the piece 
        """
        king_file = king_index % 8
        king_rank = king_index // 8
        piece_file = piece_index % 8
        piece_rank = piece_index // 8

        if king_file == piece_file:
            temp = piece_file
            while temp < 8:
                temp += 1
                if isinstance(arr[temp * 8 + piece_rank], ('Queen', 'Rook')):
                    return self.PinStatus.PINNED_VERT

        if king_rank == piece_rank:
            temp = piece_rank
            while temp < 8:
                temp += 1
                if isinstance(arr[piece_file * 8 + temp], ('Queen', 'Rook')):
                    return self.PinStatus.PINNED_HORZ
        return self.PinStatus.NOT_PINNED

    def check_Diagonal_pin(self, king_index, piece_index,arr):
        """
        checks if the piece is pinned to the king in a diagonal directions

        Args:
            king_index (int): position of the king
            piece_index (int): position of piece

        Returns:
             PinStatus(Enum): returns the pin status of the piece 
        """
        king_file = king_index % 8
        king_rank = king_index // 8
        piece_file = piece_index % 8
        piece_rank = piece_index // 8

        if abs(king_file - piece_file) / abs(king_rank - piece_rank) == 1:
            temp_file = piece_file
            temp_rank = piece_rank
            while temp_file < 8 and temp_rank < 8:
                temp_file += 1
                temp_rank += 1
                if isinstance(arr[temp_file * 8 + temp_rank], ('Queen', 'Bishop')):
                    return self.PinStatus.PINNED_DIAG
            temp_file = piece_file
            temp_rank = piece_rank
            while temp_file < 8 and temp_rank > 0:
                temp_file += 1
                temp_rank -= 1
                if isinstance(arr[temp_file * 8 + temp_rank], ('Queen', 'Bishop')):
                    return self.PinStatus.PINNED_DIAG
            temp_file = piece_file
            temp_rank = piece_rank
            while temp_file > 0 and temp_rank < 8:
                temp_file -= 1
                temp_rank += 1
                if isinstance(arr[temp_file * 8 + temp_rank], ('Queen', 'Bishop')):
                    return self.PinStatus.PINNED_DIAG
            temp_file = piece_file
            temp_rank = piece_rank
            while temp_file > 0 and temp_rank > 0:
                temp_file -= 1
                temp_rank -= 1
                if isinstance(arr[temp_file * 8 + temp_rank], ('Queen', 'Bishop')):
                    return self.PinStatus.PINNED_DIAG        
        return self.PinStatus.NOT_PINNED
