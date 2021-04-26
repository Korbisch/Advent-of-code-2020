# advent of code 2020 day 8 part 1 & 2

# list of operations
operations = []

# read in file line by line
with open('/Users/korbinianschleifer/Developer/advent_of_code_2020/inputs/day8.txt', 'r') as file:
    operations = file.readlines()

acc = 0
index = 0
already_visited = set()

while index < len(operations):
    if index in already_visited:
        print('result:', acc)
        break
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
