import pytest


# для проверки сложения нужно рассмотреть три случая: когда аргумент < 0, > 0 или == 0
@pytest.mark.parametrize(
    "i",
    [
        pytest.param(
            1, id="+"
        ),
        pytest.param(
            -1, id="-"
        ),
        pytest.param(
            0, id="null"
        )
    ],
)
def test_int1(i):
    assert i + i == 2*i


def test_int2():
    try:
        assert 2 + 2 == 5
    except AssertionError:
        pass


def test_int3():
    assert 5 * 5 == 5 ** 2


def test_set1():
    assert len({1, 2, 3}) == 3


def test_set2():
    set1 = {1, 2, 3}
    set1.add(1)
    assert set1 == {1, 2, 3}


def test_set3():
    set1 = {1, 2}
    set2 = {2, 3}
    assert set1.union(set2) == {1, 2, 3}

