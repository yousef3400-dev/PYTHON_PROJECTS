from datetime import date

from seasons import minutes_in_words, parse_date


def test_parse_valid():
    assert parse_date("2000-01-01") == date(2000, 1, 1)
    assert parse_date("  2000-01-01 ") == date(2000, 1, 1)


def test_parse_wrong_format():
    for s in ["", "abc", "January 1, 2000", "2000/01/01",
              "01-01-2000", "2000-1-1", "2000-01-011", "2000-01-01abc"]:
        assert parse_date(s) is None


def test_parse_impossible_date():
    assert parse_date("2000-13-01") is None
    assert parse_date("2023-02-30") is None
    assert parse_date("2023-02-29") is None   # مش سنة كبيسة
    assert parse_date("2024-02-29") == date(2024, 2, 29)


def test_one_year():
    assert minutes_in_words(date(1999, 1, 1), date(2000, 1, 1)) == \
        "Five hundred twenty-five thousand, six hundred minutes"


def test_two_years():
    assert minutes_in_words(date(1998, 1, 1), date(2000, 1, 1)) == \
        "One million, fifty-one thousand, two hundred minutes"


def test_leap_year():
    assert minutes_in_words(date(2000, 1, 1), date(2001, 1, 1)) == \
        "Five hundred twenty-seven thousand forty minutes"


def test_zero():
    assert minutes_in_words(date(2000, 1, 1), date(2000, 1, 1)) == "Zero minutes"
