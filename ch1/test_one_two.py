def test_passing():    
    print('ttttttttttttttttttttttt')
    assert (1,2,3) == (1,2,3)

def test_faling():
    assert (1,2,3) == (3,2,1)

def test_train_simple_assert():

    assert 1 in [2,3,4,1]
    assert 5 > 4
    assert 'fizz' in 'fizzbuzzfizz'
