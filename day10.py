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
    numbers.remove(0)

    return one_jolt_dif * three_jolt_dif

print('solution 1:', find_solution(numbers))


### Part 2 ###

def find_solution2(numbers: list) -> int:
    solution = {0:1} # keeps track of numbers and current possibilities
    numbers.sort()
    for number in numbers:
        # initialize dictionary for this number
        solution[number] = 0
        # possibilities are (pos. num - 1) + (pos. num - 2) + (pos. num - 3)
        if number - 1 in solution:
            solution[number] += solution[number-1]
        if number - 2 in solution:
            solution[number] += solution[number-2]
        if number - 3 in solution:
            solution[number] += solution[number-3]

    return solution[numbers[-1]]

print('test should be 8:', find_solution2([1,4,5,6,7,10,11,12,15,16,19]))
test = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
print('test should be 19208:', find_solution2(test))
print('solution 2:', find_solution2(numbers))
