# Solution to day 10

import os
# path to file
dir = os.path.dirname(__file__)
file = os.path.join(dir, 'inputs/day10.txt')

# list of numbers
numbers = list()

# read file line by line
with open(file, 'r') as file:
    for line in file:
        number = int(line[:-1])
        numbers.append(number)

### Part 1 ###
def find_solution(numbers: list) -> int:
    one_jolt_dif = 0
    three_jolt_dif = 0

    # start from 0 -> not in the input data
    numbers.append(0)
    numbers.sort()

    for j in range(1,len(numbers)):
        i = j - 1
        result = numbers[j] - numbers[i]
        if result == 1:
            one_jolt_dif += 1
        if result == 3:
            three_jolt_dif += 1

    # built in adapter is 3 higher than last element
    three_jolt_dif += 1

    return one_jolt_dif * three_jolt_dif

print('solution 1:', find_solution(numbers))


### Part 2 ###
