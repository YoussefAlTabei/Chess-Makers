
import pygame
from Draw_Pieces import Draw_pieces as dp
class event_handler():
    @staticmethod
    def handle_mouse_event(self, event,dp:dp):
        """Get the position of the mouse click and check if a piece is clicked

        Args:
            event: pygame event
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a piece is clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // self.square_size
            col = mouse_x // self.square_size
            print(row, col)
            index = row * 8 + col
            print (index)
            moves = (self.board_Array[64-index].get_moves())
            dp.draw_circle(moves)
         
