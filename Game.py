import pygame
import UI.Board as Board
from BoardPalettes import BoardPalettes as bp
import Draw_Pieces as dp
from Empty import Empty
try:
    from MouseEvents import event_handler as eh
except ModuleNotFoundError:
    print("Error: 'MouseEvents' module not found. Ensure 'MouseEvents.py' exists in the same directory.")
    eh = None
def redraw():
    chess_board.draw_board()  # Draw the chessboard
    pieces.draw_pieces_from_array(board_Array)  # Draw the pieces on the board
pygame.init()
# Initialize the board as a 1D list with 64 elements
board_Array = [Empty(_) for _ in range(64)]
# Create factories for white and black pieces
dp.initate_pieces(board_Array)

# Set up the display
WINDOW_SIZE = (800, 800)  # Width and height of the window
SQUARE_SIZE = WINDOW_SIZE[0] // 8
screen = pygame.display.set_mode(WINDOW_SIZE)
chess_board = Board.Board(screen,bp.MODERN_BLUE)
pieces = dp.Draw_pieces(screen,SQUARE_SIZE)
pygame.display.set_caption("Chess Game")

#################################################################################################3
redraw()
# pieces.draw_white_pieces()
# pieces.draw_black_pieces()
# Main game loop
running = True
temp = board_Array[35]
board_Array[35] = board_Array[58]
board_Array[58] = temp
board_Array[35].index = 35
print(board_Array[35], board_Array[58])
# for p in board_Array:
#     #print(p,p.index)
#     if not isinstance(p, Empty):
#         print(p, p.index)
#         print(p.get_moves())
redraw()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # mouse_x, mouse_y = event.pos
            # row = mouse_y // SQUARE_SIZE
            # col = mouse_x // SQUARE_SIZE
            # index = row * 8 + col
            # moves = board_Array[index].get_moves()
            # print(moves)
            # print(f"Piece clicked at index: {index} {board_Array[index]}")
            redraw()
            eh.left_click(event, board_Array, pieces)

                    
    # Fill the screen with a background color 


# Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
