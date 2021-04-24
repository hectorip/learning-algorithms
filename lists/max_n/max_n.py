"""
https://www.tryexponent.com/courses/data-structures/largest-numbers

Let's say we have a long list of unsorted numbers (potentially millions), and we want to find the M largest numbers contained in it. 
Implement a function find_largest(input, m) that will find and return the largest m values given an input array or file.
"""

def max_n(numbers, n):
    # Insertion sort on a list of n elements
    result = [numbers[0]]
    for num in numbers[1:]:
        if num > result[0]:
            pass

# Create a new file with line-separated numbers
# with open('numbers.txt', 'w') as file:
#   for n in range(0, 1000):
#     print(str(n), file=file)

# # Find the largest numbers in the file
# with open('numbers.txt') as file:
#   find_largest(file, 2)  # => [998, 999]