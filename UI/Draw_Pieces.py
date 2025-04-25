import pygame
import os
from Color import Color
from Empty import Empty
from PiecesFactory import WhiteFactory, BlackFactory


class Draw_pieces:
    """
    Class to draw the chess pieces.
    """
    white_Pieces = ['white_king.png', 'white_knight.png', 'white_bishop.png', 'white_pawn.png', 'white_queen.png', 'white_rook.png']
    black_Pieces = ['black_king.png', 'black_knight.png', 'black_bishop.png', 'black_pawn.png', 'black_queen.png', 'black_rook.png']

    def __init__(self, screen, square_size):
        """
        :param screen: Pygame screen surface
        :param square_size: Size of each chess square in pixels
        """
        self.screen = screen
        self.square_size = square_size
        self.selected_piece = None
        self.selected_piece_pos = None
        self.dragging = False

        self.piece_images = {}
        self.circle_image = None
        self.square_image = None

        self.load_images()

    def load_images(self):
        """
        Load and scale all chess piece images and helper UI images.
        """
        for piece in self.white_Pieces + self.black_Pieces:
            piece_name = piece.split('.')[0]  # e.g., "white_king"
            color = "white" if piece_name.startswith("white") else "black"
            image_path = os.path.join("Images", "pieces_photos", f"{color}_pieces", piece)
            try:
                image = pygame.image.load(image_path)
                image = pygame.transform.scale(image, (self.square_size, self.square_size))
                self.piece_images[piece_name] = image
            except pygame.error as e:
                print(f"[ERROR] Couldn't load image '{image_path}': {e}")

        # Load optional circle image for move indicators
        try:
            circle_path = os.path.join("Images", "Black_circle2.png")
            circle_img = pygame.image.load(circle_path)
            size = int(self.square_size * 0.25)
            self.circle_image = pygame.transform.scale(circle_img, (size, size))
        except pygame.error as e:
            print(f"[ERROR] Couldn't load circle image: {e}")

        # Optional highlight square image
        try:
            square_path = os.path.join("Images", "Square1.png")
            square_img = pygame.image.load(square_path)
            self.square_image = pygame.transform.scale(square_img, (self.square_size, self.square_size))
        except pygame.error as e:
            print(f"[WARNING] Couldn't load square image: {e}")

    def draw_sqr(self, index):
        """
        Draw a highlight square at a given board index.
        """
        if self.square_image:
            x = (index % 8) * self.square_size
            y = (index // 8) * self.square_size
            self.screen.blit(self.square_image, (x, y))

    def draw_circle(self, index):
        """
        Draw a circle indicator at a given board index.
        """
        if self.circle_image:
            x = (index % 8) * self.square_size + (self.square_size - self.circle_image.get_width()) // 2
            y = (index // 8) * self.square_size + (self.square_size - self.circle_image.get_height()) // 2
            self.screen.blit(self.circle_image, (x, y))

    def draw_pieces_from_array(self, board_Array):
        """
        Draw chess pieces based on the provided board array.
        :param board_Array: A list representing the board, with piece instances or Empty.
        """
        for index, piece in enumerate(board_Array):
            if piece and not isinstance(piece, Empty) and hasattr(piece, 'color') and hasattr(piece, 'name'):
                color = "white" if piece.color == Color.WHITE else "black"
                piece_key = f"{color}_{piece.name.lower()}"  # e.g., "white_king"
                if piece_key in self.piece_images:
                    piece_image = self.piece_images[piece_key]
                    x = (index % 8) * self.square_size
                    y = (index // 8) * self.square_size
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
