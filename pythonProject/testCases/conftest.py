import pytest


@pytest.fixture(scope="function", autouse=False)
def test_pre():
    print("start")
    yield
    print("end")