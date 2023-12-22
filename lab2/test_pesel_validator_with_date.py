#Author Hubert Wawszczak

from lab2.pesel_validator_with_date import validate_pesel
import pytest

def test_valid_pesel():
    assert validate_pesel("44051401458")  # Prawidłowy PESEL

def test_invalid_pesel_length():
    with pytest.raises(ValueError):
        validate_pesel("123456789")

def test_invalid_pesel_characters():
    with pytest.raises(ValueError):
        validate_pesel("abcdefghijk")

def test_invalid_pesel_checksum():
    with pytest.raises(ValueError):
        validate_pesel("44051401459")  # Nieprawidłowy PESEL

def test_invalid_pesel_date():
    with pytest.raises(ValueError):
        validate_pesel("99023012345")  # Nieprawidłowa data urodzenia
def test_invalid_pesel_date():
    with pytest.raises(ValueError):
        validate_pesel("99023012345")  # Nieprawidłowa data urodzenia

def test_invalid_pesel_date2():
    with pytest.raises(ValueError):
        validate_pesel("99143012345")

def test_valid_pesel_date3():
    assert validate_pesel("49040501580")  # Prawidłowy PESEL

def test_invalid_pesel_date4():
    with pytest.raises(ValueError):
        validate_pesel("02123212345")