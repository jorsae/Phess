from chess.pieces.piece import Piece

class Queen(Piece):
    @property
    def name(self):
        return "Queen"
    
    @property
    def abbreviation(self):
        return "Q"
    
    @property
    def value(self):
        return 9
    
    @property
    def movement(self):
        return []