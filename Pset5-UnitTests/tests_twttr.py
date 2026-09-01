from twttr import shorten


def main():
    test_shorten()
    test_no_vowels()
    test_soccer()


def test_shorten():
    assert shorten("BOB ROSS") == "BB RSS"
    assert shorten("CS50") == "CS50"


def test_no_vowels():
    assert shorten("xyz") == "xyz"


def test_soccer():
    assert shorten("Messi10") == "Mss10"
    assert shorten("Ronaldo7!") == "Rnld7!"


if __name__ == "__main__":
    main()
