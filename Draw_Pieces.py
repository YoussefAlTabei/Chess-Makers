import pygame
from PiecesFactory import WhiteFactory, BlackFactory
from Color import Color as c 
class Draw_pieces:
    """
    Class to draw the chess pieces
    """
    white_Pieces = ['white_bishop.png', 'white_king.png', 'white_knight.png', 'white_pawn.png', 'white_queen.png', 'white_rook.png']
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

    def draw_white_pieces(self):
        """
        Draw the white chess pieces
        """
        for piece in self.white_Pieces:
            pawn_image = pygame.image.load("pieces_photos/white_pieces/" + piece)  
            pawn_image = pygame.transform.scale(pawn_image, (self.square_size, self.square_size))

            if piece == 'white_bishop.png':
                self.screen.blit(pawn_image, (2 * self.square_size, 7 * self.square_size))  # (col, row)
                self.screen.blit(pawn_image, (5 * self.square_size, 7 * self.square_size))
            elif piece == 'white_king.png':
                self.screen.blit(pawn_image, (3 * self.square_size, 7 * self.square_size))
            elif piece == 'white_rook.png':
                self.screen.blit(pawn_image, (0 * self.square_size, 7 * self.square_size))
                self.screen.blit(pawn_image, (7 * self.square_size, 7 * self.square_size))
            elif piece == 'white_queen.png':
                self.screen.blit(pawn_image, (4 * self.square_size, 7 * self.square_size))
            elif piece == 'white_knight.png':
                self.screen.blit(pawn_image, (1 * self.square_size, 7 * self.square_size))
                self.screen.blit(pawn_image, (6 * self.square_size, 7 * self.square_size))
            else:  # White pawns
                for i in range(8):
                    self.screen.blit(pawn_image, (i * self.square_size, 6 * self.square_size))
    def draw_black_pieces(self):
        """
        Draw the black chess pieces
        """
        for piece in self.black_Pieces:
            pawn_image = pygame.image.load("pieces_photos/black_pieces/" + piece)  
            pawn_image = pygame.transform.scale(pawn_image, (self.square_size, self.square_size))

            if piece == 'black_bishop.png':
                self.screen.blit(pawn_image, (2 * self.square_size, 0 * self.square_size))  # (col, row)
                self.screen.blit(pawn_image, (5 * self.square_size, 0 * self.square_size))
            elif piece == 'black_king.png':
                self.screen.blit(pawn_image, (3 * self.square_size, 0 * self.square_size))
            elif piece == 'black_rook.png':
                self.screen.blit(pawn_image, (0 * self.square_size, 0 * self.square_size))
                self.screen.blit(pawn_image, (7 * self.square_size, 0 * self.square_size))
            elif piece == 'black_queen.png':
                self.screen.blit(pawn_image, (4 * self.square_size, 0 * self.square_size))

            elif piece == 'black_knight.png':
                self.screen.blit(pawn_image, (1 * self.square_size, 0 * self.square_size))
                self.screen.blit(pawn_image, (6 * self.square_size, 0 * self.square_size))
            else:  # Black pawns
                for i in range(8):
                    self.screen.blit(pawn_image, (i * self.square_size, 1 * self.square_size))
    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a piece is clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // self.square_size
            col = mouse_x // self.square_size
            print(row, col)
            index = row * 8 + col
            print (index)
@staticmethod
def initate_pieces(board_Array):
    white_factory = WhiteFactory()
    black_factory = BlackFactory()

    # Place white pieces
    board_Array[0] = white_factory.create_rooks(index=0, arr=board_Array)      # a1
    board_Array[1] = white_factory.create_knight(index=1, arr=board_Array)     # b1
    board_Array[2] = white_factory.create_bishop(index=2, arr=board_Array)     # c1
    board_Array[3] = white_factory.create_queen(index=3, arr=board_Array)      # d1
    board_Array[4] = white_factory.create_king(index=4, arr=board_Array)       # e1
    board_Array[5] = white_factory.create_bishop(index=5, arr=board_Array)     # f1
    board_Array[6] = white_factory.create_knight(index=6, arr=board_Array)     # g1
    board_Array[7] = white_factory.create_rooks(index=7, arr=board_Array)      # h1
    # for i in range(8, 16):                                                     # a2 to h2
    #     board_Array[i] = white_factory.create_pawn(index=i, arr=board_Array)

    # Place black pieces
    board_Array[56] = black_factory.create_rooks(index=56, arr=board_Array)    # a8
    board_Array[57] = black_factory.create_knight(index=57, arr=board_Array)   # b8
    board_Array[58] = black_factory.create_bishop(index=58, arr=board_Array)   # c8
    board_Array[59] = black_factory.create_queen(index=59, arr=board_Array)    # d8
    board_Array[60] = black_factory.create_king(index=60, arr=board_Array)     # e8
    board_Array[61] = black_factory.create_bishop(index=61, arr=board_Array)   # f8
    board_Array[62] = black_factory.create_knight(index=62, arr=board_Array)   # g8
    board_Array[63] = black_factory.create_rooks(index=63, arr=board_Array)    # h8
    # for i in range(48, 56):                                                    # a7 to h7
    #     board_Array[i] = black_factory.create_pawn(index=i, arr=board_Array)

