# advent of code day 5 part 1 & 2

# list of seats
seats = []

# read in file line by line
with open('/Users/korbinianschleifer/documents/advent_of_code_2020/inputs/seats.txt', 'r') as file:
    seats = file.readlines()


# recursive function to get the row or column in range
def get_row_or_column(str, range):
    lower, upper = range
    # if string is zero then return the row
    if str == '':
        return lower
    # if string is F then return lower part
    if str[0] == 'F' or str[0] == 'L':
        upper -= int((upper-lower) / 2) + 1
        return get_row_or_column(str[1:], (lower, upper))
    # if string is B then return upper part
    elif str[0] == 'B' or str[0] == 'R':
        lower += int((upper - lower) / 2) + 1
        return get_row_or_column(str[1:], (lower, upper))

# part 1: specify highest id
max_id = 0
# part 2: find my seat
seat_ids = []

for seat in seats:
    # first get the row number from 128 rows
    row_number = get_row_or_column(seat[:7], (0,127))
    # then get the column number from 8 seats per row
    col_number = get_row_or_column(seat[7:-1], (0,7))

    # calculate the id number
    id_number = row_number * 8 + col_number

    # add to list to find my missing seat
    seat_ids.append(id_number)

    # if id_number is bigger, then save as max id
    if (id_number > max_id):
        max_id = id_number


# print the highest id for all boarding passes
print('Highest ID number is:', max_id)

# sort seat ids
seat_ids.sort()

# function to find missing id
def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]

# print my seat id
print('My seat has the ID:', find_missing(seat_ids))