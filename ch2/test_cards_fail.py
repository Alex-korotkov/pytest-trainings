import pytest
from cards import Card

def test_equality_fail():
    c1 = Card("sit there", "Brian")
    c2 = Card("do something", "okken")
    assert c1 == c2

def test_with_fail():
    c1 = Card("sit there", "Brian")
    c2 = Card("do something", "okken")
    if c1 != c2:
        pytest.fail("they don't match")

if __name__ == "__main__":
    test_equality_fail()