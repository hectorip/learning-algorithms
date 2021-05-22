import pytest
from roman_numerals import transform


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("M", 1000),
        ("MCMLXXXVIII", 1988),
        ("CDXLIV", 444),
        ("CCC", 300),
        ("LXIV", 64),
    ],
)
def test_numeral_transform(test_input, expected):
    assert transform(test_input) == expected
