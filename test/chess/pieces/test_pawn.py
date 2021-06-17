import pytest
import sys
sys.path.append('src')
from chess.utility import Colour
from chess.pieces import Pawn

pawn = Pawn(Colour.BLACK)

def test_pawn_name():
    assert(pawn.name) == 'Pawn'

def test_pawn_abbreviation():
    assert(pawn.abbreviation) == ''

def test_pawn_value():
    assert(pawn.value) == 1