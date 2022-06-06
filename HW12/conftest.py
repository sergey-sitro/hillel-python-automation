from code_for_testing import Human

import pytest

import logging

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel('INFO')


@pytest.fixture()
def human():
    logger.info("\nFixture started")
    yield Human(name="John", age=20, gender="male")
    logger.info("\nFixture finished")


@pytest.fixture()
def human_almost_dead():
    logger.info("\nFixture started")
    yield Human(name="Abe", age=105, gender="male")
    logger.info("\nFixture finished")


@pytest.fixture()
def friend():
    logger.info("\nFixture started")
    yield Human(name="Peter", age=18, gender="male")
    logger.info("\nFixture finished")


@pytest.fixture()
def dead_human():
    logger.info("\nFixture started")
    dead_human = Human(name="Dave", age=106, gender="male")
    dead_human.grow()
    yield dead_human
    logger.info("\nFixture finished")
