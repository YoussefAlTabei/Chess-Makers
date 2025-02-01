from Pieces import Piece
from Empty import Empty
from Rook import Rook
from Bishop import Bishop
from Queen import Queen
from Knight import Knight
from Pawn import Pawn
import Color as c
class King(Piece):
    """
    King class that inherits from Piece
    """
    def __init__(self, color, index):
        super().__init__(color, index)
        self.index = index
        self.in_check = False
        self.has_moved = False
    def check(self,enemy_list):
        """determines wether the king is in check
        Args:
            enemy_list (Piece): list of pieces of opposite color

        Returns:
            bool: True if king is in check, False otherwise
        """
        king_file = self.index % 8
        king_rank = self.index // 8
        for p in enemy_list:
            if isinstance(p, Rook):
                return rook_check(p)
            if isinstance(p, Bishop):
                bishop_check(p)
            if isinstance(p, Queen):
                rook_check(p)
                
            if isinstance(p, Knight):
                if abs(p.index % 8 - king_file) == 2 and abs(p.index // 8 - king_rank) == 1:
                    return True
                if abs(p.index % 8 - king_file) == 1 and abs(p.index // 8 - king_rank) == 2:
                    return True
            if isinstance(p, Pawn):
                if p.color == c.WHITE:
                    if p.index % 8 == king_file + 1 and p.index // 8 == king_rank + 1:
                        return True
                    if p.index % 8 == king_file - 1 and p.index // 8 == king_rank + 1:
                        return True
                if p.color == c.BLACK:
                    if p.index % 8 == king_file + 1 and p.index // 8 == king_rank - 1:
                        return True
                    if p.index % 8 == king_file - 1 and p.index // 8 == king_rank - 1:
                        return True
        def rook_check(self,p):
            """determines if the king is in check by a rook

            Args:
                p (Piece): Object of type Rook

            Returns:
                bool: True if king is in check, False otherwise
            """
            if p.index % 8 == king_file:
                temp = king_file
                dir = king_file - p.index % 8
                if dir < 0: dir = 1
                else: dir = -1
                while temp != p.index % 8:
                    temp += 8 * dir
                    if not isinstance(self.arr[8*king_rank+temp],Empty):
                        return False
                return True
            if p.index // 8 == king_rank:
                temp = king_rank
                dir = king_rank - p.index // 8
                if dir < 0: dir = 1
                else: dir = -1
                while temp != p.index // 8:
                    temp += dir
                    if not isinstance(self.arr[temp * 8 + king_file],Empty):
                        return False
                return True
        def bishop_check(self,p):
            """determines if the king is in check by a Bishop

            Args:
                p (Piece): Object of type Bishop

            Returns:
                bool: True if king is in check, False otherwise
            """
            if abs(p.index % 8 - king_file)/ abs(p.index // 8 - king_rank)==1:
                x_dir = king_file - p.index % 8
                y_dir = king_rank - p.index // 8
                if x_dir < 0: x_dir = 1
                else: x_dir = -1
                if y_dir < 0: y_dir = 1
                else: y_dir = -1
                temp_x = king_file
                temp_y = king_rank
                while temp_x != p.index % 8 and temp_y != p.index // 8:
                    temp_x += x_dir
                    temp_y += y_dir
                    if not isinstance(self.arr[temp_y * 8 + temp_x],Empty):
                        return False
                return True
    def check_legal_moves(self):
        """checks the legal moves of the king

        Returns:
            array (int): indexes of legal moves
        """
        for i in [-9,-8,-7,-1,1,7,8,9]:
            if self.index + i >= 0 and self.index + i < 64:
                if self.arr[self.index + i].color != self.color:
                    if not self.check(self.arr[self.index + i]):
                        self.legal_moves.append(self.index + i)
        return self.legal_moves