from library.parser import FenParser
from chess.pieces import Pawn, Knight, Bishop, Rook, Queen, King
from chess.utility import Colour

print(Colour.WHITE)

b = Bishop(Colour.WHITE)

print(b)

fp = FenParser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
fp.parse()