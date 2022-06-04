import pytest


@pytest.mark.positive
@pytest.mark.grow_func
def test_human_grow(human):
    """
    Decription: check that human is growing for 1 year
    while using grow() function

    Precondition: human is created

    Steps:
    1. call grow() function for human
    2. observe human.age

    Expected result: human.age is increased by one year
    """

    human.grow()
    assert human.age == 21, f"\nActual: {human.age}\nExpected: 21"


@pytest.mark.positive
@pytest.mark.grow_func
def test_human_dead(human_almost_dead):
    """
    Description: check that humam is dead if it's age is over age_limit

    Precondition: human.age = human.age_limit

    Steps:
    1. call grow() function for human
    2. observe human.status

    Expected result: human.status is "dead"
    """
    human_almost_dead.grow()
    assert human_almost_dead.status == "dead"


@pytest.mark.positive
@pytest.mark.change_name_func
def test_change_name(human):
    """
    Description: check that human can change a name

    Precondition: human is created

    Steps:
    1. call change_name() function and pass new name to it
    2. observe human new name

    Expected result: human has new name
    """

    human.change_name("Serhii Matkobozhyk")
    assert human.name == "Serhii Matkobozhyk", f"Name is {human.name}, expected: Serhii Matkobozhyk"


@pytest.mark.negative
@pytest.mark.change_name_func
def test_change_name_negative(human):
    with pytest.raises(SyntaxError):
        human.change_name("serhii")
