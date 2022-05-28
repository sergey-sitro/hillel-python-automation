import pytest
# pytest -s pytest_tests.py

def setup():
    print("basic setup into module")
 
def teardown():
    print("basic teardown into module")

def setup_module(module):
    print("setup_module")

def teardown_module(module):
    print("teardown_module")

def setup_function(function):
    print ("function setup")
 
def teardown_function(function):
    print ("function teardown")


@pytest.fixture()
def resource_setup(request):
    print("resource_setup")
    def resource_teardown():
        print("resource_teardown")
    request.addfinalizer(resource_teardown)


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


def test_that_needs_resource(resource_setup):
    print("test_that_needs_resource")


class TestClassExample:
    def setup(self):
        print("basic setup into class")
 
    def teardown(self):
        print("basic teardown into class")
 
    def setup_class(cls):
        print("class setup")
 
    def teardown_class(cls):
        print("class teardown")
 
    def setup_method(self, method):
        print("method setup")
 
    def teardown_method(self, method):
        print("method teardown")
 
    def test_numbers(self):
        assert 5*6 == 30 
 
    def test_strings(self):
        assert 'b'*2 == 'bb'