from puzzle_4_input import passport_input
import re

passports_list = passport_input()
valid_fields_set = {"byr", "iyr", "eyr","hgt", "hcl", "ecl", "pid", "cid"}
passports_with_fields = []
valid_passports = []

def get_passports_with_valid_fields(passports):
    for passport in passports:
        fields_set = set(passport.keys())
        difference = valid_fields_set - fields_set
        if len(difference) == 0 or difference == {'cid'}:
            passports_with_fields.append(passport)
    return passports_with_fields

def get_valid_passports(passports):
    print(len(passports))
    for passport in passports:
        if is_valid(passport) is True:
            valid_passports.append(passport)
    return valid_passports

def is_valid(item):
    return all([
        valid_byr(item['byr']), 
        valid_iyr(item['iyr']), 
        valid_eyr(item['eyr']),
        valid_hgt(item['hgt']),
        valid_hcl(item['hcl']),
        valid_ecl(item['ecl']),
        valid_pid(item['pid'])
    ])


def valid_num(num, min, max):
    return int(num) in range(min, max)

def valid_byr(byr_year):
    return valid_num(byr_year, 1920, 2003)
    
def valid_iyr(iyr_year):
    return valid_num(iyr_year, 2010, 2021)

def valid_eyr(eyr_year):
    return valid_num(eyr_year, 2020, 2031)

def valid_hgt(value):
    m = re.match(r'(?P<hgt>\d+)(?P<unit>cm|in)', value)
    if m:
        if m.group('unit') == 'cm':
            return valid_num(m.group('hgt'), 150, 194)
        if m.group('unit') == 'in':
            return valid_num(m.group('hgt'), 59, 77)
    return False

def valid_hcl(string):
    return True if re.match(r'^#[0-9a-f]{6}$', string) else False

def valid_ecl(string):
    return string in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_pid(id):
    return True if re.match(r'^\d{9}$', id) else False

#soloution 4 a 
passsports_with_fields = get_passports_with_valid_fields(passports_list)
print(len(passsports_with_fields))
#soloution 4 b 
print(len(get_valid_passports(passsports_with_fields)))