import leapyear
import pytest

def test_is_leapyear():
    assert leapyear.is_leapyear(2020)
def test_is_leapyear2():
    assert leapyear.is_leapyear(1800) == False
