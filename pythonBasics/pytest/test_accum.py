import pytest

from pythonBasics.pytest.accum import Accumulator


@pytest.mark.accum
def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0


@pytest.mark.accum
def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1


@pytest.mark.accum
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


@pytest.mark.accum
def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


@pytest.mark.accum
def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError) as error:
        accum.count = 10

# def test_accumulator_add_error():
#     accum = Accumulator()
#     accum.add()
#     accum.add()
#     assert accum.count == 4
