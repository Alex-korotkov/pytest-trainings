from cards import Card
import pytest


def test_start_from_in_prog(cards_db):
    index = cards_db.add_card(Card("something in progress", state="in prog"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"
    
def test_start_from_done(cards_db):
    index = cards_db.add_card(Card("something is done", state="done"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

def test_start_from_in_todo(cards_db):
    index = cards_db.add_card(Card("something in todo", state="todo"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"


@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ("some write", "done"),
        ("some write", "in prog"),
        ("some write", "todo"),
    ],
)
def test_start(cards_db, start_summary, start_state):
    index = cards_db.add_card(Card(start_summary, state=start_state))
    cards_db.start(index)

    card = cards_db.get_card(index)
    assert card.state == "in prog"

def test_start_fixture(cards_db, start_state):
    index = cards_db.add_card(Card(start_state,state=start_state))
    cards_db.start(index)

    card = cards_db.get_card(index)
    assert card.state == "in prog"

def test_start_gen(cards_db, start_state_gen):
    index = cards_db.add_card(Card(start_state_gen,state=start_state_gen))
    cards_db.start(index)

    card = cards_db.get_card(index)
    assert card.state == "in prog"
