import pygame
import os
from Color import Color
from Empty import Empty

def draw_legal(board_Array, index, dp, moves_override=None):
    """Draws legal moves for a piece at the given index on the board.
    Args:
        Board_Array (list): The current state of the chess board.
        index (int): The index of the piece to check for legal moves.
        dp (Draw_pieces): An instance of the Draw_pieces class for drawing.
        moves_override (list, optional): A list of moves to draw. Defaults to None.
    """
    moves = moves_override if moves_override is not None else board_Array[index].get_moves()
    for i in moves:
       # print(f"Drawing legal move at index jere: {i}")
        if isinstance(board_Array[i], Empty):
            dp.draw_circle(i)
        else:
            dp.draw_sqr(i)
    return moves  # Return the list of legal moves for further processing if needed