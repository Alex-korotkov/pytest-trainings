def func(x):
    return x+1

def test_answer():
    assert func(3) == 5

def test_assertion_introspection():
    # assert func(2) % 2 == 0, "value was odd, should be even"
    assert func(2) % 2 == 0