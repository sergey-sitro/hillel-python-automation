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

    human.change_name("Serhii")
    assert human.name == "Serhii", f"Name is {human.name}, expected: Serhii"


@pytest.mark.negative
@pytest.mark.change_name_func
@pytest.mark.parametrize("name", ["serhii", "sErhii", " ", "4", "matkobozhy", "matkobozhyk", "Serhii Matkobozhyk"])
def test_change_name_negative(human, name):
    """
    Description: check that changed human name should start with uppercase letter
                 and be less than 10 symbols length

    Precondition: human is created

    Step 1: call change_name() function and pass 'serhii' to it
    Expected result: SyntaxError exception is raised with 'Name should starts with capital letter' message

    Step 2: call change_name() function and pass 'sErhii' to it
    Expected result: SyntaxError exception is raised with 'Name should starts with capital letter' message

    Step 3: call change_name() function and pass ' ' to it
    Expected result: SyntaxError exception is raised with 'Name should starts with capital letter' message

    Step 4: call change_name() function and pass '4' to it
    Expected result: SyntaxError exception is raised with 'Name should starts with capital letter' message

    Step 5: call change_name() function and pass 'matkobozhy' to it
    Expected result: SyntaxError exception is raised with 'Name should starts with capital letter' message

    Step 6: call change_name() function and pass 'matkobozhyk' to it
    Expected result: SyntaxError exception is raised with 'Name should starts with capital letter' message

    Step 7: call change_name() function and pass 'Serhii Matkobozhyk' to it
    Expected result: SyntaxError exception is raised with 'Name should starts with capital letter' message
    """

    with pytest.raises(SyntaxError) as e:
        human.change_name(name)
    assert str(e.value) == 'Name should starts with capital letter'


@pytest.mark.positive
@pytest.mark.gender_func
@pytest.mark.parametrize("new_gender", ["female", "male"])
def test_gender_func(human, new_gender):
    """
    Description: check that human can change gender

    Preconditions:
    1. human is created
    2. human gender is 'male'

    Step 1: change human gender to 'female'
    Expected result: human gender is changed to 'female'

    Step 2: change human gender back to 'male'
    Expected result: human gender is 'male' again
    """

    human.gender = new_gender
    assert human.gender == new_gender


@pytest.mark.negative
@pytest.mark.gender_func
def test_gender_not_expected(human):
    """
    Description: check that exception is raised while trying to set unexpected gender

    Precondition: human is created

    Steps:
    1. set human gender value which is not in ['female', 'male']

    Expected result: Exception is raised with 'Gender is not as expected' message
    """
    with pytest.raises(Exception) as e:
        human.gender = "ape"
    assert str(e.value) == 'Gender is not as expected'



