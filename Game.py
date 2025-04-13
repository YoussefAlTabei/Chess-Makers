import pygame
import Board
from BoardPalettes import BoardPalettes as bp
import Draw_Pieces as dp
from Empty import Empty
pygame.init()
# Initialize the board as a 1D list with 64 elements
board_Array = [Empty(_) for _ in range(64)]
# Create factories for white and black pieces
dp.initate_pieces(board_Array)

# Set up the display
WINDOW_SIZE = (800, 800)  # Width and height of the window
SQUARE_SIZE = WINDOW_SIZE[0] // 8
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Chess Game")
chess_board = Board.Board(screen,bp.MODERN_BLUE)
screen.fill((255, 255, 255))
chess_board.draw_board()
pieces = dp.Draw_pieces(screen,SQUARE_SIZE)
pieces.draw_white_pieces()
pieces.draw_black_pieces()
# Main game loop
running = True
# temp = board_Array[35]
# board_Array[35] = board_Array[58]
# board_Array[58] = temp
# board_Array[35].index = 35
# print(board_Array[35], board_Array[58])
for p in board_Array:
    #print(p,p.index)
    if not isinstance(p, Empty):
        print(p, p.index)
        print(p.get_moves())
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          # pieces.handle_mouse_event(event)
          pass

                    
    # Fill the screen with a background color 


# Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
