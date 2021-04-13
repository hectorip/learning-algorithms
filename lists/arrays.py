# You are given an n x n 2D matrix that represents an image.
# Rotate the image by 90 degrees (clockwise).


def rotate(matrix):
    """rotates the matrix 90 degrees clockwise"""


def rotated_index(i, j, n):
    new_i = j
    new_j = n - 1 - i
    return new_i, new_j


# i = 0, j = 0 => i' = n - 1 - i, j'= 0 + j
# 0, 0, 1 -> 0, n-1 - 0
# 0, 2, 3
# 2 , 2, 9
# 2, 0, 7

00, 01, 02, 12,
a = [
    [7, 2, 1],
    [4, 5, 6],
    [9, 8, 3],
]

a_rotated = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]

[
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]

[
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4],
]
