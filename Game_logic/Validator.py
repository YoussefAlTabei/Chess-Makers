from Game_logic.Color import Color
from Pieces.Empty import Empty
from Pieces.King import King

class Validator:
    @staticmethod
    def is_square_attacked(board, target_index, attacker_color):
        """
        Checks if a square is under attack by any piece of a specific color.
        """
        for i, piece in enumerate(board):
            if not isinstance(piece, Empty) and piece.color == attacker_color:
                # Get pseudo-legal moves for the piece
                # Note: Pieces must have get_moves() implemented
                # We use a simple version of get_moves that doesn't recurse into validation
                moves = piece.get_moves()
                if target_index in moves:
                    return True
        return False

    @staticmethod
    def get_legal_moves(board, piece_index):
        """
        Filters pseudo-legal moves to only those that don't leave the king in check.
        """
        piece = board[piece_index]
        if isinstance(piece, Empty):
            return []

        pseudo_moves = piece.get_moves()
        legal_moves = []
        king_color = piece.color
        enemy_color = Color.BLACK if king_color == Color.WHITE else Color.WHITE

        for move_index in pseudo_moves:
            # Simulate the move
            original_from_piece = board[piece_index]
            original_to_piece = board[move_index]
            
            # Temporary Move
            board[move_index] = original_from_piece
            board[piece_index] = Empty(piece_index)
            board[move_index].index = move_index

            # Find King's position
            king_pos = -1
            for i, p in enumerate(board):
                if isinstance(p, King) and p.color == king_color:
                    king_pos = i
                    break
            
            # Check if King is safe
            if king_pos != -1 and not Validator.is_square_attacked(board, king_pos, enemy_color):
                legal_moves.append(move_index)

            # Undo Move
            board[piece_index] = original_from_piece
            board[move_index] = original_to_piece
            board[piece_index].index = piece_index
            if not isinstance(board[move_index], Empty):
                board[move_index].index = move_index

        return legal_moves

    @staticmethod
    def is_checkmate(board, turn_color):
        """
        Checks if the player of the given color is in checkmate.
        """
        enemy_color = Color.BLACK if turn_color == Color.WHITE else Color.WHITE
        
        # 1. Find King
        king_pos = -1
        for i, p in enumerate(board):
            if isinstance(p, King) and p.color == turn_color:
                king_pos = i
                break
        
        # 2. Check if in check
        in_check = Validator.is_square_attacked(board, king_pos, enemy_color)
        
        # 3. Check if any legal moves exist
        has_legal_move = False
        for i, piece in enumerate(board):
            if not isinstance(piece, Empty) and piece.color == turn_color:
                if len(Validator.get_legal_moves(board, i)) > 0:
                    has_legal_move = True
                    break
        
        if in_check and not has_legal_move:
            return "CHECKMATE"
        if not in_check and not has_legal_move:
            return "STALEMATE"
        return "CONTINUE"
