import pytest
from max_n import max_n


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (([1, 2, 3, 4, 5], 3), [3, 4, 5]),
        ((list(range(1000)), 5), [995, 996, 997, 998, 999]),
        (([3, 2, 1], 1), [3]),
    ],
)
def test_max_n(test_input, expected):
    assert max_n(*test_input) == expected
