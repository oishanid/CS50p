from fuel import convert, gauge
import pytest


def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("1/2") == 50
    with pytest.raises(ValueError):
        assert convert("-1/2")
    with pytest.raises(ValueError):
        assert convert("3/2")
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        assert convert("3/0")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(67) == "67%"


if __name__ == "__main__":
    main()
