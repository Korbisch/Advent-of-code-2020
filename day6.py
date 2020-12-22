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

answers = [groups for groups in answers if groups == '']
print('max possible count:', len(answers) * 26)

print('sum of answer counts:', answer_counter)