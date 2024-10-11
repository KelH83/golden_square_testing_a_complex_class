from lib.most_often import MostOften

new_list = ['dog', 'cat', 'snake', 'monkey', 'cat' ]
most_often = MostOften(new_list)

def test_creates_instance():
    assert isinstance(most_often, MostOften)
    assert most_often.starting_list == new_list

def test_add_new_updates_starting_list():
    most_often.add_new('cat')
    assert most_often.starting_list == ['dog', 'cat', 'snake', 'monkey', 'cat', 'cat' ]

def test_get_most_often_returns_the_most_common_item():
    assert most_often.get_most_often() == 'cat'

def test_get_most_often_returns_no_clear_winner():
    new_list = ['dog', 'cat', 'snake', 'monkey']
    most_often = MostOften(new_list)
    assert most_often.get_most_often() == 'no clear winner'