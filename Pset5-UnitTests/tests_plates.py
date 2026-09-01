from plates import is_valid

def main():
    test_is_valid()

def test_is_valid():
    assert is_valid("6767d") == False
    assert is_valid("DGSTATS") == False
    assert is_valid("abcd") == True
    assert is_valid("xy12") == True
    assert is_valid("dg067") == False
    assert is_valid("67420") == False
    assert is_valid("bob2l") == False
    assert is_valid("ap!.4") == False


if __name__ == "__main__":
    main()
