from code_for_testing import Human

import pytest

import logging

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel('INFO')


@pytest.fixture()
def human():
    print("\nFixture started")
    yield Human(name="John", age=20, gender="male")
    print("\nFixture finished")


@pytest.fixture()
def human_almost_dead():
    print("\nFixture started")
    yield Human(name="Abe", age=105, gender="male")
    print("\nFixture finished")
