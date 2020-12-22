# advent of code day 6

# list of answers
answers = []

# read in file line by line
with open('/Users/korbinianschleifer/Developer/advent_of_code_2020/inputs/customs-form.txt', 'r') as file:
    answers = file.readlines()

# replace line break with empty string
answers = [x.replace('\n', '') for x in answers]
answers.append('')

# create an empty set
group_answers = set()
# create a counter to count answers
answer_counter = 0

for string in answers:
    # if string is empty add length to counter and reset set 
    if string == '':
        answer_counter += len(group_answers)
        group_answers.clear()
    for char in string:
        group_answers.add(char)


print('sum of questions anyone answered yes:', answer_counter)

# part 2: sum of questions everyone answered yes
# count intersecting elements
intersec_counter = 0
set1 = set()
set2 = set()

test = ['xgwq', 'mohv', 'w', 'ertbzsjk', 'udf', '', 'abc', 'abc', 'abc', '']

for string in answers:
    # if string is empty add length to counter and reset sets
    # next group starts
    if string == '':
        # don't add to counter if set contains dummy value
        if set1 != {'0'}:
            intersec_counter += len(set1)
        # reset all sets
        set1.clear()
        set2.clear()

    # fill set1 with data and use as intersection set
    elif len(set1) == 0:
        for char in string:
            set1.add(char)

    # fill set2 with every new line = form sheet
    elif len(set2) == 0:
        for char in string:
            set2.add(char)

    # if sets are full get the intersection
    if len(set1) != 0 and len(set2) != 0:
        set1 = set.intersection(set1, set2)
        # dummy value if there is no intersection
        # skips all following until next group
        # because there can't be an intersection with 0
        if len(set1) == 0:
            set1.add('0')
        set2.clear()
        

print('sum of questions everyone in the group answered with yes:', intersec_counter)

    