import pytest


@pytest.fixture()
def setup():
    print("Launching bowser")
    yield
    print("closing browser")

