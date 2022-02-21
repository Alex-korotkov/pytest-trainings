import pytest


def test_balls(eight_ball_list):
    assert [1,2,3,4] == eight_ball_list

def test_fresh(mentos):
    assert {1:"something", 2:"someting", 3:"something"} == mentos

def test_both(mentos):
    assert mentos == {1:"something", 2:"someting", 3:"something"}
