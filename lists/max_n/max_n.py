"""
https://www.tryexponent.com/courses/data-structures/largest-numbers

Let's say we have a long list of unsorted numbers (potentially millions), and we want to find the M largest numbers contained in it. 
Implement a function find_largest(input, m) that will find and return the largest m values given an input array or file.
"""
from os import stat
import time
from heapq import heappop, heappush


def max_n(numbers, n):
    # Insertion sort on a list of n elements
    # solution assumes len(numbers) > n > 0

    result = numbers[:n]
    result.sort()
    total_res = 1
    for num in numbers[n:]:
        if num > result[0]:
            result[0] = num
            # Insertion sort => Fastest with nearly sorted
            for i in range(n - 1):
                if result[i] > result[i + 1]:
                    result[i], result[i + 1] = result[i + 1], result[i]

    return result


def max_n_optimal(numbers, n):
    result = [float("-inf")]
    total = 1
    for num in numbers:
        if num > result[0]:
            if total >= n:
                heappop(result)
            total += 1
            heappush(result, num)

    return result


def find_largest(file, n):
    nums = [int(x) for x in file]
    start_time = time.time()
    print("Starting", start_time)
    print(max_n_optimal(nums, n))
    end_time = time.time()
    print("End", end_time)
    print("Diff: ", end_time - start_time)


# Find the largest numbers in the file

if __name__ == "__main__":
    with open("numbers.txt") as file:
        find_largest(file, 100)  # => [998, 999]
