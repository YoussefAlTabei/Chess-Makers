import pygame
import os
from Color import Color
from Empty import Empty
from PiecesFactory import WhiteFactory, BlackFactory

class Draw_pieces:
    """
    Class to draw the chess pieces
    """
    white_Pieces = ['white_king.png', 'white_knight.png', 'white_bishop.png', 'white_pawn.png', 'white_queen.png', 'white_rook.png']
    black_Pieces = ['black_bishop.png', 'black_king.png', 'black_knight.png', 'black_pawn.png', 'black_queen.png', 'black_rook.png']

    def __init__(self, screen, square_size):
        """
        Constructor
        :param screen: Pygame screen surface
        :param square_size: Size of each chess square in pixels
        """
        self.screen = screen
        self.square_size = square_size
        self.selected_piece = None  # Track the selected piece
        self.selected_piece_pos = None  # Track the position of the selected piece
        self.dragging = False  # Track if a piece is being dragged

    # def draw_white_pieces(self):
    #     """
    #     Draw the white chess pieces
    #     """
    #     for piece in self.white_Pieces:
    #         pawn_image = pygame.image.load(os.path.join("Images", "pieces_photos", "white_pieces", piece))
    #         pawn_image = pygame.transform.scale(pawn_image, (self.square_size, self.square_size))

    #         if piece == 'white_bishop.png':
    #             self.screen.blit(pawn_image, (2 * self.square_size, 7 * self.square_size))  # (col, row)
    #             self.screen.blit(pawn_image, (5 * self.square_size, 7 * self.square_size))
    #         elif piece == 'white_king.png':
    #             self.screen.blit(pawn_image, (3 * self.square_size, 7 * self.square_size))
    #         elif piece == 'white_rook.png':
    #             self.screen.blit(pawn_image, (0 * self.square_size, 7 * self.square_size))
    #             self.screen.blit(pawn_image, (7 * self.square_size, 7 * self.square_size))
    #         elif piece == 'white_queen.png':
    #             self.screen.blit(pawn_image, (4 * self.square_size, 7 * self.square_size))
    #         elif piece == 'white_knight.png':
    #             self.screen.blit(pawn_image, (1 * self.square_size, 7 * self.square_size))
    #             self.screen.blit(pawn_image, (6 * self.square_size, 7 * self.square_size))
    #         else:  # White pawns
    #             for i in range(8):
    #                 self.screen.blit(pawn_image, (i * self.square_size, 6 * self.square_size))

    # def draw_black_pieces(self):
    #     """
    #     Draw the black chess pieces
    #     """
    #     for piece in self.black_Pieces:
    #         pawn_image = pygame.image.load(os.path.join("Images", "pieces_photos", "black_pieces", piece))
    #         pawn_image = pygame.transform.scale(pawn_image, (self.square_size, self.square_size))

    #         if piece == 'black_bishop.png':
    #             self.screen.blit(pawn_image, (2 * self.square_size, 0 * self.square_size))  # (col, row)
    #             self.screen.blit(pawn_image, (5 * self.square_size, 0 * self.square_size))
    #         elif piece == 'black_king.png':
    #             self.screen.blit(pawn_image, (3 * self.square_size, 0 * self.square_size))
    #         elif piece == 'black_rook.png':
    #             self.screen.blit(pawn_image, (0 * self.square_size, 0 * self.square_size))
    #             self.screen.blit(pawn_image, (7 * self.square_size, 0 * self.square_size))
    #         elif piece == 'black_queen.png':
    #             self.screen.blit(pawn_image, (4 * self.square_size, 0 * self.square_size))
    #         elif piece == 'black_knight.png':
    #             self.screen.blit(pawn_image, (1 * self.square_size, 0 * self.square_size))
    #             self.screen.blit(pawn_image, (6 * self.square_size, 0 * self.square_size))
    #         else:  # Black pawns
    #             for i in range(8):
    #                 self.screen.blit(pawn_image, (i * self.square_size, 1 * self.square_size))

    def draw_circle(self, arr):
        posible_move = pygame.image.load(os.path.join("Images", "Grey_circle.png"))
        posible_move = pygame.transform.scale(posible_move, (self.square_size, self.square_size))
        for i in arr:
            self.screen.blit(posible_move, (i % 8 * self.square_size, i // 8 * self.square_size))
    def draw_pieces_from_array(self, board_Array):
        """
        Draw the pieces on the board based on the board array
        :param board_Array: Array representing the board state
        """
        for index, piece in enumerate(board_Array):
            if piece and not isinstance(piece, Empty) and hasattr(piece, 'color') and hasattr(piece, 'name'):
                color = "white" if piece.color == Color.WHITE else "black"
                piece_image = pygame.image.load(os.path.join("Images", "pieces_photos", f"{color}_pieces", f"{color}_{piece.name}.png"))
                piece_image = pygame.transform.scale(piece_image, (self.square_size, self.square_size))
                # Flip the board vertically to make white at the bottom and black at the top
                x = (index % 8) * self.square_size
                y = (index // 8) * self.square_size
                # Debugging: Ensure piece attributes are correct
                # if not piece.name or not piece.color:
                #     print(f"Error: Piece at index {index} is missing attributes.")
                # else:
                #     print(index, piece.name, piece.color, x, y)
                self.screen.blit(piece_image, (x, y))
@staticmethod
def initate_pieces(board_Array):
    white_factory = WhiteFactory()
    black_factory = BlackFactory()

    # Place black pieces
    board_Array[0] = black_factory.create_rooks(index=0, arr=board_Array)      # a1
    board_Array[1] = black_factory.create_knight(index=1, arr=board_Array)     # b1
    board_Array[2] = black_factory.create_bishop(index=2, arr=board_Array)     # c1
    board_Array[3] = black_factory.create_queen(index=3, arr=board_Array)      # d1
    board_Array[4] = black_factory.create_king(index=4, arr=board_Array)       # e1
    board_Array[5] = black_factory.create_bishop(index=5, arr=board_Array)     # f1
    board_Array[6] = black_factory.create_knight(index=6, arr=board_Array)     # g1
    board_Array[7] = black_factory.create_rooks(index=7, arr=board_Array)      # h1
    for i in range(8, 16):                                    # a2 to h2
        board_Array[i] = black_factory.create_pawn(index=i, arr=board_Array)

    # Place white pieces
    board_Array[56] = white_factory.create_rooks(index=56, arr=board_Array)    # a8
    board_Array[57] = white_factory.create_knight(index=57, arr=board_Array)   # b8
    board_Array[58] = white_factory.create_bishop(index=58, arr=board_Array)   # c8
    board_Array[59] = white_factory.create_queen(index=59, arr=board_Array)    # d8
    board_Array[60] = white_factory.create_king(index=60, arr=board_Array)     # e8
    board_Array[61] = white_factory.create_bishop(index=61, arr=board_Array)   # f8
    board_Array[62] = white_factory.create_knight(index=62, arr=board_Array)   # g8
    board_Array[63] = white_factory.create_rooks(index=63, arr=board_Array)    # h8
    for i in range(48, 56):                                   # a7 to h7
        board_Array[i] = white_factory.create_pawn(index=i, arr=board_Array)
