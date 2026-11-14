from response import is_valid


def test_is_valid():
    assert is_valid("malan@harvard.edu") == "Valid"
    assert is_valid("malan@@@harvard.edu") == "Invalid"
    assert is_valid("malan@harvard..edu") == "Invalid"
    assert is_valid("malan@harvard.edu.") == "Invalid"
