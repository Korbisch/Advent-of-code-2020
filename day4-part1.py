# advent of code day 4

data = []

# read in file line by line
with open('/Users/korbinianschleifer/documents/advent_of_code_2020/inputs/passports.txt', 'r') as file:
    data = file.readlines()
# prevent mistake
data.append('')

# delete the line break('\n') from the data
data = [x.replace('\n', '') for x in data]

# dictionary to safe one passport
passport = {}
passports = []
# construct passport as single dictionary from file and add to passports list
for line in data:
    # only add to dict if line is not empty
    if line != '':
        mydict = dict((k.strip(), v.strip()) for k,v in (item.split(':') for item in line.split(' ')))
        passport.update(mydict)
    # if line is empty, the next passport begins
    elif line == '':
        passports.append(passport)
        passport = {}

total_passports = len(passports)
print(total_passports)

# set of strings to check
pp_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
invalid_passports = 0

# check for correct passports
for passport in passports:
    for str in pp_fields:
        if str not in passport:
            invalid_passports += 1
            break

print('number of valid passports:', total_passports - invalid_passports)