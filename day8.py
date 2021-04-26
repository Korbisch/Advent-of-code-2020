# advent of code 2020 day 8 part 1 & 2

# list of operations
operations = []

# read in file line by line
with open('/Users/korbinianschleifer/Developer/advent_of_code_2020/inputs/day8.txt', 'r') as file:
    operations = file.readlines()

acc = 0
index = 0
already_visited = set()

while index not in already_visited:
    already_visited.add(index)

    operation = operations[index][:3] # acc, jmp or nop
    operator = operations[index][4:5] # + or -
    value = int(operations[index][5:-1]) # value eg. 50

    if operation == 'nop':
        index += 1
    if operation == 'acc':
        if operator == '+':
            acc += value
        else:
            acc -= value
        index += 1
    if operation == 'jmp':
        if operator == '+':
            index += value
        else:
            index -= value

print('accumulator:', acc)

# part 2

# keeps track of the previous index -> is the operation that should be changed
acc = 0
index = 0
already_visited = set()
changed_operations = set()
op_count = 0

while index < len(operations):

    operation = operations[index][:3] # acc, jmp or nop
    operator = operations[index][4:5] # + or -
    value = int(operations[index][5:-1]) # value eg. 50

    # try the change
    if op_count == 0 and index not in changed_operations and (operation in ['jmp','nop']):
        # change operation
        if operation == 'jmp':
            operation = 'nop'
        elif operation == 'nop':
            operation = 'jmp'
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

    # don't add on reset
    if operation != '':
        already_visited.add(index)

    if operation == 'nop':
        index += 1
    if operation == 'acc':
        if operator == '+':
            acc += value
        else:
            acc -= value
        index += 1
    if operation == 'jmp':
        if operator == '+':
            index += value
        else:
            index -= value

print('accumulator correct execution:', acc)