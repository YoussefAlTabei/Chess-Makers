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
from Game_logic.Validator import Validator
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
game_status = "CONTINUE"
############################## Game Logic ###################################################################3
redraw()

moves = []  # List to store legal moves for the selected piece
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_status != "CONTINUE":
            continue

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
            
            # 1. Handle Move Execution
            if piece_selected and index in moves:
                try:
                    if piece.color == Color.WHITE and not white_turn:
                        continue
                    elif piece.color == Color.BLACK and white_turn:
                        continue
                except Exception as e:
                    print(e)
                
                temp = piece.index
                mv.move_piece(board_Array, piece.index, index)
                
                if testing:
                    print("Piece moved")
                
                pieces.redraw_square(temp, board_Array, chess_board)
                pieces.redraw_square(index, board_Array, chess_board)
                
                white_turn = not white_turn
                moved = True
                piece_selected = False
                moves = []
                piece = Empty(index)
                
                # Check for Checkmate/Stalemate after move
                game_status = Validator.is_checkmate(board_Array, Color.WHITE if white_turn else Color.BLACK)
                if game_status != "CONTINUE":
                    print(f"Game Over: {game_status}")

            # 2. Handle Piece Selection
            elif not isinstance(board_Array[index], Empty):
                if (board_Array[index].color == Color.WHITE and white_turn) or \
                   (board_Array[index].color == Color.BLACK and not white_turn):
                    
                    # Use Validator for legal moves
                    moves = Validator.get_legal_moves(board_Array, index)
                    piece = board_Array[index]
                    piece_selected = True
                    
                    if testing:
                        print(f"Selected {piece} at {index}. Legal moves: {moves}")

            # 3. Handle Drawing Legal Moves
            if moved:
                drawing = False
            elif piece_selected and not isinstance(board_Array[index], Empty):
                 drawn_moves = draw_legal(board_Array, index, pieces, moves_override=moves) 
                 drawing = True
            
            moved = False



# Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
