from chess.pieces.piece import Piece

class King(Piece):
    @property
    def name(self):
        return "King"
    
    @property
    def abbreviation(self):
        return "K"
    
    @property
    def value(self):
        return 100
    
    @property
    def movement(self):
        return []