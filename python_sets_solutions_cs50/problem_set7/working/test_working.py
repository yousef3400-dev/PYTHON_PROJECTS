import pytest
from working import convert


def test_valid_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_overnight_and_noon_midnight():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:59 PM to 12:01 AM") == "12:59 to 00:01"


def test_invalid_times():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 5 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("12:60 AM to 5 PM")


def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9 am to 5 pm")
    with pytest.raises(ValueError):
        convert("9:0 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("")
