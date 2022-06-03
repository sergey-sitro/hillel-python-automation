from code_for_testing import Human

import pytest

import logging

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel('INFO')


@pytest.fixture()
def human():
    logging.info("Fixture started")
    yield Human(name="John", age=20, gender="male")
    logger.info("Fixture finished")


@pytest.fixture()
def human_almost_dead():
    logging.info("Fixture started")
    yield Human(name="Abe", age=105, gender="male")
    logger.info("Fixture finished")
