import pygame
import Board
from BoardPalettes import BoardPalettes as bp
import Draw_Pieces as dp
from PiecesFactory import WhiteFactory, BlackFactory
from Empty import Empty
pygame.init()
# Initialize the board as a 1D list with 64 elements
board_Array = [Empty() for _ in range(64)]

# Create factories for white and black pieces
white_factory = WhiteFactory()
black_factory = BlackFactory()

# Place white pieces
board_Array[0] = white_factory.create_rooks()      # a1
board_Array[1] = white_factory.create_knight()     # b1
board_Array[2] = white_factory.create_bishop()     # c1
board_Array[3] = white_factory.create_queen()      # d1
board_Array[4] = white_factory.create_king()       # e1
board_Array[5] = white_factory.create_bishop()     # f1
board_Array[6] = white_factory.create_knight()     # g1
board_Array[7] = white_factory.create_rooks()      # h1
for i in range(8, 16):                             # a2 to h2
    board_Array[i] = white_factory.create_pawn()

# Place black pieces
board_Array[56] = black_factory.create_rooks()     # a8
board_Array[57] = black_factory.create_knight()    # b8
board_Array[58] = black_factory.create_bishop()    # c8
board_Array[59] = black_factory.create_queen()     # d8
board_Array[60] = black_factory.create_king()      # e8
board_Array[61] = black_factory.create_bishop()    # f8
board_Array[62] = black_factory.create_knight()    # g8
board_Array[63] = black_factory.create_rooks()     # h8
for i in range(48, 56):                            # a7 to h7
    board_Array[i] = black_factory.create_pawn()
print(board_Array)
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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pieces.handle_mouse_event(event)
    # Fill the screen with a background color 


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
