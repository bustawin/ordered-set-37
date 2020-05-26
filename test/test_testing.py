import pytest

from ordered_set_37 import OrderedSet


def test_add():
    x = OrderedSet([1, 2, -1, "bar"])
    x.add(0)
    assert list(x) == [1, 2, -1, "bar", 0]


def test_discard():
    x = OrderedSet([1, 2, -1])
    x.discard(2)
    assert list(x) == [1, -1]


def test_getitem():
    x = OrderedSet([1, 2, -1])
    assert x[0] == 1
    assert x[1] == 2
    assert x[2] == -1
    with pytest.raises(IndexError):
        x[3]


def test_len():
    x = OrderedSet([1])
    assert len(x) == 1


def test_iter():
    for x in OrderedSet([1]):
        assert x == 1


def test_str():
    x = OrderedSet([1, 2, 3])
    assert str(x) == "{1, 2, 3}"


def test_repr():
    x = OrderedSet([1, 2, 3])
    assert repr(x) == "<OrderedSet {1, 2, 3}>"
