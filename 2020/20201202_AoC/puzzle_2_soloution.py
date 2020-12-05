from puzzle_2_input import passwords

passwords_list = passwords()

def policy_one_condition(r):
    return r['min'] <= r['password'].count(r['letter']) <= r['max']

def valid_policy_one():
    return len(list(filter(lambda row: policy_one_condition(row), passwords_list)))

def policy_two_first_condition(r):
    return r['password'][r['min']-1] == r['letter'] and r['password'][r['max']-1] != r['letter']

def policy_two_second_condition(r):
    return r['password'][r['min']-1] != r['letter'] and r['password'][r['max']-1] == r['letter']

def valid_policy_two():
    return len(list(filter(lambda row: policy_two_first_condition(row) or policy_two_second_condition(row), passwords_list)))

#soloution 2a
print(valid_policy_one())

#soloution 2b
print(valid_policy_two())