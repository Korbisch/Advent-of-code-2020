# advent of code 2020 day 7

# list of answers
bags = []

# read in file line by line
with open('/Users/korbinianschleifer/Developer/advent_of_code_2020/inputs/bags.txt', 'r') as file:
    bags = file.readlines()


# bags to look for and resulting colors
colors = {'shiny gold'}

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