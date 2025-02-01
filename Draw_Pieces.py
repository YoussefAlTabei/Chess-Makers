import pygame

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
                self.screen.blit(pawn_image, (4 * self.square_size, 7 * self.square_size))
            elif piece == 'white_rook.png':
                self.screen.blit(pawn_image, (0 * self.square_size, 7 * self.square_size))
                self.screen.blit(pawn_image, (7 * self.square_size, 7 * self.square_size))
            elif piece == 'white_queen.png':
                self.screen.blit(pawn_image, (3 * self.square_size, 7 * self.square_size))
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
                self.screen.blit(pawn_image, (4 * self.square_size, 0 * self.square_size))
            elif piece == 'black_rook.png':
                self.screen.blit(pawn_image, (0 * self.square_size, 0 * self.square_size))
                self.screen.blit(pawn_image, (7 * self.square_size, 0 * self.square_size))
            elif piece == 'black_queen.png':
                self.screen.blit(pawn_image, (3 * self.square_size, 0 * self.square_size))
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