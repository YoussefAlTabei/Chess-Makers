import config  # Will auto set paths

import pygame
import UI.Board as Board
from BoardPalettes import BoardPalettes as bp
import Draw_Pieces as dp
from Empty import Empty
from Draw_legal_moves import draw_legal
from Game_logic.Movement import move_piece
from MouseEvents import event_handler as eh

    
########################### Intialization ##########################################################
def redraw():
    chess_board.draw_board()  # Draw the chessboard
    pieces.draw_pieces_from_array(board_Array)  # Draw the pieces on the board
pygame.init()
# Initialize the board as a 1D list with 64 elements
board_Array = [Empty(_) for _ in range(64)]
# Create factories for white and black pieces
dp.initate_pieces(board_Array)


#################################### Set up the display ####################################################
pygame.display.set_caption("Chess Game")
WINDOW_SIZE = (800, 800)  # Width and height of the window
SQUARE_SIZE = WINDOW_SIZE[0] // 8
screen = pygame.display.set_mode(WINDOW_SIZE)
chess_board = Board.Board(screen,bp.MODERN_BLUE)
pieces = dp.Draw_pieces(screen,SQUARE_SIZE)
pygame.display.set_caption("Chess Game")

############################### Flags ##########################################################
testing = False
white_turn = True
running = True
clicked = False  # Flag to track if a piece is clicked
############################## Game Logic ###################################################################3
redraw()

if testing:
    for p in board_Array:
        if not isinstance(p, Empty):
            print(p, p.index)
            print(p.get_moves())

redraw()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if testing:
                mouse_x, mouse_y = event.pos
                row = mouse_y // SQUARE_SIZE
                col = mouse_x // SQUARE_SIZE
                index = row * 8 + col
                moves = board_Array[index].get_moves()
                print(moves)
                print(f"Piece clicked at index: {index} {board_Array[index]}")
            redraw()
            index = eh.left_click(event, board_Array, pieces)
            
            if clicked  and index is not None and index in moves:
                if testing:
                    print(f"Moving piece from index {index} to {moves[0]}")
                pieces.move_piece(board_Array, index, moves[0])
                redraw()
                #clicked = True
            if clicked == False and  index is not None and not isinstance(board_Array[index], Empty):
                if not isinstance(board_Array[index], Empty):
                    moves = (board_Array[index].get_moves())
                if testing:
                    print(f"Piece clicked at index: {index} {board_Array[index]}")
                draw_legal(board_Array, index, pieces)
            if clicked == True:
                moves = []
            clicked != clicked       
    # Fill the screen with a background color 


# Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
