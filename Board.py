import pygame

from BoardPalettes import BoardPalettes


class Board:
    """
    Class to represent the chess board
    """

    def __init__(self, screen, palette: BoardPalettes):
        """
        Constructor
        :param screen:
        :param palette:
        """
        self.screen = screen
        self.palette = palette

    def draw_board(self):
        """
        Draw the chess board
        :return:        None
        """
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = self.palette[1]
                    # print(color)
                else:
                    color = self.palette[0]
                    # print(color)
                pygame.draw.rect(self.screen, color, [col * 100, row * 100, 100, 100])
        pygame.display.update()

    def set_palette(self, palette: BoardPalettes):
        """
        Set the palette of the board
        :param palette:
        :return:
        """
        self.palette = palette
        self.draw_board()

    def get_palette(self) -> BoardPalettes:
        """
        Get the palette of the board
        :return:
        """
        return self.palette