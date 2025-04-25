from enum import Enum
class PinStatus(Enum):
    NOT_PINNED = 0
    PINNED_VERT = 1
    PINNED_HORZ = 2
    PINNED_DIAG = 3