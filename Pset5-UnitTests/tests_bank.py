from bank import value


def main():
    test_value()


def test_value():
    assert value("Hello world") == 0
    assert value("horSes are dead") == 20
    assert value("dead horse.") == 100


if __name__ == "__main__":
    main()
