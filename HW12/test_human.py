from code_for_testing import Human


# import logging
#
# logger = logging.getLogger()
# logger.setLevel('INFO')


def test_human_grow(human):
    human.grow()
    assert human.age == 21, f"\nActual: {human.age}\nExpected: 21"


def test_human_dead(human_almost_dead):
    human_almost_dead.grow()
    assert human_almost_dead.status == "dead"
