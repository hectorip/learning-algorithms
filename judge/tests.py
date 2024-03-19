import pytest
from main import findJudge


@pytest.mark.parametrize(
    "input, expected",
    (
        ([3, [[1, 3], [2, 3]]], 3),
        ([1, []], 1),
        ([1001, []], -1),
        ([2, []], -1),
    ),
)
def test_find_judge(input, expected):
    assert findJudge(input[0], input[1]) == expected

