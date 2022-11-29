import pytest

from pythonBasics.pytest.accum import Accumulator


@pytest.fixture
def accum():
    return Accumulator()