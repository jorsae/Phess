from chess.pieces.piece import Piece

class Pawn(Piece):
    @property
    def name(self):
        return "Pawn"
    
    @property
    def abbreviation(self):
        return ""
    
    @property
    def value(self):
        return 1
    
    @property
    def movement(self):
        return []