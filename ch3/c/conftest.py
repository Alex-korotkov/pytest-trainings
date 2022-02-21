import pytest


@pytest.fixture(scope="session")
def total_balls():
    yield [1,2,3] 

@pytest.fixture(scope="function")
def eight_ball_list(total_balls):

    '''
    test docstring

    ''' 
    return total_balls+[4]

@pytest.fixture()
def mentos():

    '''
    mentos docstring

    '''

    yield {1:"something", 2:"someting", 3:"something"}

