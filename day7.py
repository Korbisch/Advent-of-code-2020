# advent of code 2020 day 7 part 1 & 2

# list of answers
bags = []

# read in file line by line
with open('/Users/korbinianschleifer/Developer/advent_of_code_2020/inputs/bags.txt', 'r') as file:
    bags = file.readlines()


# bags to look for and resulting colors
colors = {'shiny gold'}

# function to find colors
def find_colors(colors):
    search_bags = list(colors)
    for bag in bags:
        for color in search_bags:
            if bag.find(color) > -1:
                # add beginning color to set (first two words)
                colors.add(bag.split()[0] + ' ' + bag.split()[1])
    return colors

# search as long as new colors are found
while len(colors) < len(find_colors(colors)):
    find_colors(colors)
    

# don't count the shiny gold bag
colors.remove('shiny gold')


# number of colors that can contain at least one shiny gold bag
print('number of colors:', len(colors))


# part 2: number of bags in a shiny gold bag

total = -1
bags_dict = { "shiny gold" : 1 }
while len(bags_dict) > 0:
    key = list(bags_dict.keys())[0]
    total += bags_dict[key]
    if key in bags:
        for newbag in bags[key]:
            if newbag[1] not in bags_dict:
                bags_dict[newbag[1]] = 0
            bags_dict[newbag[1]] += (list(bags_dict.values())[0] * newbag[0])
    del bags_dict[key]

print('part 2 solution:', total)