# advent of code 2020 day 8 part 1 & 2

import os
# path to file
dir = os.path.dirname(__file__)
file = os.path.join(dir, 'inputs/day8.txt')

# list of lines in the program
program = list()

# read file line by line
with open(file, 'r') as file:
    for i,line in enumerate(file):
        program.insert(i, dict())
        program[i]['operation'] = line[:3]
        program[i]['operator'] = line[4:5]
        program[i]['value'] = int(line[5:-1])

# part 1
def calc_acc_sum_on_fail(program: list) -> int:
    acc_sum = 0
    index = 0
    already_visited = set()

    while index not in already_visited:
        already_visited.add(index)

        operation = program[index]['operation'] # acc, jmp or nop
        operator = program[index]['operator'] # + or -
        value = program[index]['value'] # value eg. 50

        # change index
        index += add_new_index(operation, operator, value)
        
        # add to accumulator
        acc_sum += add_to_acc(operation, operator, value)
    
    return acc_sum

# calculates the value that should be added to the index
def add_new_index(operation, operator, value) -> int:
    if operation in ['nop', 'acc']:
        return 1
    elif operation == 'jmp':
        return value if operator == '+' else -value
    return 0

# calculates the value that should be added to the accumulator
def add_to_acc(operation, operator, value) -> int:
    if operation == 'acc':
        return value if operator == '+' else -value
    return 0

print('accumulator sum on failure:', calc_acc_sum_on_fail(program))

# part 2

# calculate the sum on correct execution
def calc_acc_sum_on_exec(program: list) -> int:
    acc = 0
    index = 0
    already_visited = set()
    changed_operations = set()
    op_count = 0

    while index < len(program):

        operation = program[index]['operation'] # acc, jmp or nop
        operator = program[index]['operator'] # + or -
        value = program[index]['value'] # value eg. 50

        # try the change
        if op_count == 0 and index not in changed_operations and (operation in ['jmp','nop']):
            # change the operation
            operation = switch_operations(operation)
            # add the index you have tried to change
            changed_operations.add(index)
            op_count = 1

        if index in already_visited:
            # loop -> reset and restart
            index = 0
            acc = 0
            operation = ''
            already_visited.clear()
            op_count = 0
            continue

        already_visited.add(index)

        # change index
        index += add_new_index(operation, operator, value)

        # add to accumulator
        acc += add_to_acc(operation, operator, value)

    return acc

# changes the operation from jmp to nop and from nop to jmp
def switch_operations(operation: str) -> str:
    if operation == 'jmp':
        return 'nop'
    elif operation == 'nop':
        return 'jmp'
    return operation

print('accumulator correct execution:', calc_acc_sum_on_exec(program))
