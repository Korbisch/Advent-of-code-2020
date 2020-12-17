# password tester day 2

data = []
# read in file line by line
with open('/Users/korbinianschleifer/documents/advent_of_code_2020/inputs/passwords.txt') as file:
    data = file.readlines()

# create set
pw_counter = 0
new_pw_counter = 0

# search for correct passwords
for password in data:
    split = password.split()

    # get the min and max value of allowed characters
    numbers = split[0]
    number_split = numbers.split('-')
    min = int(number_split[0])
    max = int(number_split[1])

    # positions to be checked
    pos_1 = min - 1
    pos_2 = max - 1

    # get the character to search for
    char = split[1][0]

    # get the string to be searched
    string = split[2]
    string.strip()

    # search the string
    count = string.count(char)

    if count >= min and count <= max:
        #print(True, count)
        pw_counter += 1
    else:
        # delete entry from
        print(False)

    # new rule with positions
    if (string[pos_1] == char and string[pos_2] != char) or (string[pos_1] != char and string[pos_2] == char):
        # password is correct
        new_pw_counter += 1


print('number of correct passwords from old shop:', pw_counter)
print('correct passwords from new shop:', new_pw_counter)