from code_for_testing import Human

import pytest

import logging

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel('INFO')


@pytest.fixture()
def human():
    logger.info("\nFixtire started")
    yield Human(name="John", age=20, gender="male")
    logger.info("\nFixtire finished")


@pytest.fixture()
def human_almost_dead():
    logger.info("\nFixtire started")
    yield Human(name="Abe", age=105, gender="male")
    logger.info("\nFixtire finished")


@pytest.fixture()
def friend():
    logger.info("\nFixtire started")
    yield Human(name="Peter", age=18, gender="male")
    logger.info("\nFixtire finished")
