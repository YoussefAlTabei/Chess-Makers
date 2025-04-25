from enum import Enum

class BoardPalettes(Enum):
    CLASSIC_WOOD = [(139, 69, 19), (245, 222, 179)]
    MODERN_BLUE = [(26, 35, 126), (187, 222, 251)]

    def __getitem__(self, item):
        return self.value[item]