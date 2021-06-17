import pytest
import sys
sys.path.append('src')
from chess.utility import Colour
from chess.pieces import Queen

queen = Queen(Colour.BLACK)

def test_queen_name():
    assert(queen.name) == 'Queen'

def test_queen_abbreviation():
    assert(queen.abbreviation) == 'Q'

def test_queen_value():
    assert(queen.value) == 9