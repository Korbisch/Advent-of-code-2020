# Solution to day 9

import os
# path to file
dir = os.path.dirname(__file__)
file = os.path.join(dir, 'inputs/day9.txt')

# list of numbers
numbers = list()

# read file line by line
with open(file, 'r') as file:
    for line in file:
        number = int(line[:-1])
        numbers.append(number)

# Part 1
def find_solution(numbers: list) -> int:
    for i in range(25, len(numbers)):
        current = numbers[i]
        if not sum_is_possible(numbers[i-25:i], current):
            return current
    return -1

def sum_is_possible(numbers: list, target: int) -> bool:
    num_set = set(numbers) # 25 numbers to check
    # run through list and check if val is in set that is not equal to num
    for num in numbers:
        val = target - num
        if val in num_set and val != num:
            return True
    return False

# part 1 solution
print('incorrect value:', find_solution(numbers))