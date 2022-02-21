from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards


@pytest.fixture(scope="session")
def db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()

@pytest.fixture(scope="function")
def cards_db(db):
    """CardsDB object that's empty"""
    db.delete_all()
    return db

@pytest.fixture(params=["done", "in prog",  "todo"])
def start_state(request):
    return request.param

def pytest_generate_tests(metafunc):
    if "start_state_gen" in metafunc.fixturenames:
        metafunc.parametrize("start_state_gen",["done", "in prog",  "todo"])