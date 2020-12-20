# advent of code day 4
import re


data = []

# read in file line by line
with open('/Users/korbinianschleifer/documents/advent_of_code_2020/inputs/passports.txt', 'r') as file:
    data = file.readlines()
# prevent mistake of dictionary creation
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

# function to check if heigth is correct
def check_height(str):
    if (str[-2:] == 'cm' and str[:3].isdigit() and 150 <= int(str[:3]) <= 193):
        return True
    elif (str[-2:] == 'in' and str[:2].isdigit() and 59 <= int(str[:2]) <= 76):
        return True
    else:
        return False

valid_passports = 0

# check for correct passports
for passport in passports:

    # set values to check
    byr, iyr, eyr, hgt, hcl, ecl, pid = passport.get('byr'), passport.get('iyr'), passport.get('eyr'), passport.get('hgt'), passport.get('hcl'), passport.get('ecl'), passport.get('pid')
    
    # check for missing values
    if ((None not in [byr, iyr, eyr, hgt, hcl, ecl, pid]) and
        # check for correct values
        (len(byr) == 4 and 1920 <= int(byr) <= 2002) and # birth year
        (len(iyr) == 4 and 2010 <= int(iyr) <= 2020) and # issue year
        (len(eyr) == 4 and 2020 <= int(eyr) <= 2030) and # expiration year
        (check_height(hgt)) and # height
        (hcl[0] == '#' and len(hcl[1:]) == 6 and bool(re.match('^[#a-f0-9]*$', hcl))) and # hair color
        (ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and # eye color
        (len(pid) == 9 and pid.isdigit())): # passport id

            # add to valid passports
            valid_passports += 1


print('number of valid passports:', valid_passports)