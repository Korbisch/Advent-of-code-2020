# advent of code day 3 part 2

data = []

# read in file line by line
with open('/Users/korbinianschleifer/documents/advent_of_code_2020/inputs/trees.txt') as file:
    data.append(file.readlines())
data = data[0]

max_row_length = 30

step_size = 3
trees_product = 1

print(len(data))

for step in [1, 3, 5, 7]:
    tree_counter = 0
    col_counter = 0
    step_size = step

    # check number of trees for each step size
    for i in range(len(data)):
        # pos 31 -> 0 / 32 -> 1 / 33 -> 2
        if (col_counter > max_row_length):
            col_counter -= (max_row_length + 1)
        if (data[i][col_counter] == '#'):
            tree_counter += 1
        col_counter += step_size

    # create the product of trees
    trees_product *= tree_counter

# special case: rigth: 1 and down: 2
tree_counter = 0
col_counter = 0
# check number of trees for each step size
for i in range(0, len(data), 2):
    # pos 31 -> 0 / 32 -> 1 / 33 -> 2
    if (col_counter > max_row_length):
        col_counter -= (max_row_length + 1)
    if (data[i][col_counter] == '#'):
        tree_counter += 1
    col_counter += 1

trees_product *= tree_counter

print(trees_product)
