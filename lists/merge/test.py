import pytest
from merge import ListNode, merge_list


@pytest.mark.parametrize(
    "input,expected",
    (
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (([], []), []),
        (([1, 1001], [2, 1000]), [1, 2, 1000, 1001]),
    ),
)
def test_merge(input, expected):

    assert merge_list(input[0], input[1]) == expected
