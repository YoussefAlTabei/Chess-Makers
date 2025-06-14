import config  # Will auto set paths

import pygame
import UI.Board as Board
from BoardPalettes import BoardPalettes as bp
import Draw_Pieces as dp
from Empty import Empty
from Draw_legal_moves import draw_legal
from Game_logic.Movement import Movement as mv
from MouseEvents import event_handler as eh
from Color import Color
from Pin import Pin     
########################### Intialization ##########################################################
def redraw():
    chess_board.draw_board()  # Draw the chessboard
    pieces.draw_pieces_from_array(board_Array)  # Draw the pieces on the board
pygame.init()
# Initialize the board as a 1D list with 64 elements
board_Array = [Empty(_) for _ in range(64)]
# Create factories for white and black pieces
dp.initiate_pieces(board_Array)


#################################### Set up the display ####################################################
pygame.display.set_caption("Chess Game")
WINDOW_SIZE = (800, 800)  # Width and height of the window
SQUARE_SIZE = WINDOW_SIZE[0] // 8
screen = pygame.display.set_mode(WINDOW_SIZE)
chess_board = Board.Board(screen,bp.MODERN_BLUE)
pieces = dp.Draw_pieces(screen,SQUARE_SIZE)
pygame.display.set_caption("Chess Game")

############################### Flags ##########################################################
testing = True
white_turn = True
running = True
clicked = True# Flag to track if a piece is clicked
drawing = False
moved = False
piece_selected = False
piece = None  # The piece that is currently selected
############################## Game Logic ###################################################################3
redraw()

moves = []  # List to store legal moves for the selected piece
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if drawing:
                try:
                    for i in drawn_moves:
                        pieces.redraw_square(i,board_Array,chess_board)  # Redraw the square to erase the circle
                    print("Cleared drawn moves")
                except Exception as e:
                    print(e) # Erase the circle at the index
                drawing = False
            index = eh.left_click(event, board_Array, pieces) 
            if testing:
                print(f"Index: {index}")
            if piece_selected  and index in moves: # and not isinstance(board_Array[index], Empty):
                print("here")
                try:
                    if piece.color == Color.WHITE and not white_turn:
                        continue
                    elif piece.color == Color.BLACK and white_turn:
                        continue
                except Exception as e:
                    print(e)
                temp = piece.index
                mv.move_piece(board_Array,piece.index, index)
                if testing:
                    print("Piece moved")
                pieces.redraw_square(temp,board_Array,chess_board)
                pieces.redraw_square(index,board_Array,chess_board)
                drawing = False
                white_turn = not white_turn
                moved = True
                piece_selected = False
                moves = []
                piece = Empty(index)  # Reset the piece to an empty piece
            if not isinstance(board_Array[index], Empty):
                board_Array[index].pin_status = Pin.pin_check(index,board_Array) 
                if testing:
                    print(f"Pin status for piece at index {index}: {board_Array[index].pin_status}")
                moves = board_Array[index].get_moves()
            piece = board_Array[index]
            if not isinstance(piece, Empty):
                    piece_selected = True
            if testing:
                print(f"{piece} clicked at index: {index}, piece_Selected: {piece_selected}, moves: {moves}")

            if not moved and not isinstance(board_Array[index], Empty):
                drawn_moves = draw_legal(board_Array, index, pieces)
                drawing = True
                if testing:
                    print(f"Legal moves drawn for piece at index {index}: {drawn_moves}")  

            moved = False



# Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
