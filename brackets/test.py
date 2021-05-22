import pytest
from main import check


@pytest.mark.parametrize(
    "input, expected",
    (
        ("()", True),
        ("(]", False),
    ),
)
def test_bracket_checker(input, expected):
    assert check(input) == expected