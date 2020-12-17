# advent of code day 1

data = []
# read in file line by line
with open('/Users/korbinianschleifer/documents/advent_of_code_2020/inputs/twentytwenty.txt', 'r+') as file:
    data = file.readlines()

# parse it to an int
data = [int(x) for x in data]


# faster way with set
seen = set()
for el in data:
    if 2020 - el in seen:
        print("solution found", el, 2020 - el)
        break
    seen.add(el)
