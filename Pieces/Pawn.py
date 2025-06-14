from Pieces import Piece
from Game_logic.PinStatus import PinStatus
from Game_logic.Color import Color as c
import Empty
class Pawn(Piece):

    def __init__(self, color,index,arr):
        super().__init__(color, arr,index)
        self.index = index
        self.has_moved = False
        self.pin_state = PinStatus.NOT_PINNED
        self.en_passant = False
        self.arr = arr
        self.name = "pawn"
    def get_moves(self):
        """
        Get the legal moves for the pawn
        
        Returns:
            arr[int]: list of indexes of legal moves for the pawn
        """
        legal_moves = []
        legal_moves += self.check_legal_moves()
        return legal_moves
    def check_legal_moves(self):
        """
        Check the legal moves for the pawn
        
        arr[int]: list of indexes of legal moves for the pawn
        """
        legal_moves = []
        color_direction = -1 if self.color == c.WHITE else 1 # 1 for white, -1 for black
        if self.pin_state != PinStatus.PINNED_DIAG and self.pin_state != PinStatus.PINNED_HORZ:
            if isinstance(self.arr[self.index + 8 * color_direction], Empty.Empty):
                legal_moves.append(self.index + 8* color_direction)
                if isinstance(self.arr[self.index + 16* color_direction], Empty.Empty):
                    if not self.has_moved:
                        legal_moves.append(self.index + 16* color_direction)
        if self.pin_state != PinStatus.PINNED_VERT and self.pin_state != PinStatus.PINNED_HORZ:
            if not isinstance(self.arr[self.index + 7* color_direction], Empty.Empty) and self.index % 8 != 0 and self.arr[self.index + 7* color_direction].color != self.color:
                legal_moves.append(self.index + 7* color_direction)
            if not isinstance(self.arr[self.index + 9* color_direction], Empty.Empty) and self.index % 8 != 7 and self.arr[self.index + 9* color_direction].color != self.color:
                legal_moves.append(self.index + 9* color_direction)  
        if not isinstance(self.arr[self.index -1 * color_direction], Empty.Empty) and self.arr[self.index-1* color_direction].color != self.color and isinstance(self.arr[self.index-1* color_direction], Pawn) and self.arr[self.index-1* color_direction].en_passant:
            legal_moves.append(self.index-7 * color_direction)
        if not isinstance(self.arr[self.index + 1 * color_direction], Empty.Empty) and self.arr[self.index+1* color_direction].color != self.color and isinstance(self.arr[self.index+1* color_direction], Pawn) and self.arr[self.index+1* color_direction].en_passant:
            legal_moves.append(self.index+9 * color_direction )
        return legal_moves