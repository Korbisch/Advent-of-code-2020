# advent of code day 3

data = []

# read in file line by line
with open('/Users/korbinianschleifer/documents/advent_of_code_2020/inputs/trees.txt') as file:
    data.append(file.readlines())
data = data[0]

col_counter = 0
tree_counter = 0
max_row_length = 30

# search for trees
for i in range(len(data)):
    # pos 31 -> 0 / 32 -> 1 / 33 -> 2
    if (col_counter > max_row_length):
        col_counter -= (max_row_length + 1)
    if (data[i][col_counter] == '#'):
        tree_counter += 1
    col_counter += 3

print(tree_counter)



