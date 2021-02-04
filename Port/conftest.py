import pytest


@pytest.fixture()
def login_01():
    print('----用例的前置----')
    yield
    print("---用例的后置-----")


@pytest.fixture(scope='class')
def login_class():
    print("---类的前置-------")
    yield
    print("------类的后置----------")
