
import pygame
from Draw_Pieces import Draw_pieces as dp
from Empty import Empty 
class event_handler():
    def __init__(self):
        prev = []
    @staticmethod
    def left_click(event,board_Array,dp:dp):
        """Get the position of the mouse click and check if a piece is clicked

        Args:
            event: pygame event
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a piece is clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // dp.square_size
            col = mouse_x // dp.square_size
            print(row, col)
            index = row * 8 + col
            print (index)
        return index