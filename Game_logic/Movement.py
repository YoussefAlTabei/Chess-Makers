import config  # Will auto set paths
from Empty import Empty
import pygame
from MouseEvents import event_handler as eh

 
class Movement:

    @staticmethod
    def move_piece(board_Array, from_index, to_index):
        '''Moves a piece from one index to another on the board.
        Args:
            board_Array (list): The current state of the chess board.
            from_index (int): The index of the piece to move.
            to_index (int): The index where the piece should be moved.
        '''
        if isinstance(board_Array[to_index], Empty):  
            temp = board_Array[from_index]
            board_Array[from_index] = board_Array[to_index]
            board_Array[to_index] = temp
            board_Array[to_index].index = to_index
            board_Array[from_index].index = from_index
        elif board_Array[from_index].color != board_Array[to_index].color:
            board_Array[to_index] = board_Array[from_index]
            board_Array[from_index] = Empty(from_index)
            board_Array[to_index].index = to_index
            board_Array[from_index].index = from_index
        try:
            board_Array[to_index].has_moved = True
        except AttributeError:
            pass