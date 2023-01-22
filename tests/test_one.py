import pytest


@pytest.fixture(scope="function")
def new_fixture():
    print("FFFFIXTURE")


@pytest.fixture(scope="session")
def new_fixture1(request):
    print("Building")

    def final():
        print("DE-Building")

    request.addfinalizer(final)


def test_one(new_fixture, new_fixture1):
    assert (3, 2) == (3, 2)


def test_one1(new_fixture, new_fixture1):
    assert (3, 2) == (3, 2)
