from puzzle_2_input import passwords

passwords_list = passwords()

def valid_policy_one():
    return len(list(filter(lambda row: row['min'] <= row['password'].count(row['letter']) <= row['max'], passwords_list)))

print(valid_policy_one())

def valid_policy_two():
    return len(list(filter(lambda row: (row['password'][row['min']-1] == row['letter'] and row['password'][row['max']-1] != row['letter']) or (row['password'][row['min']-1] != row['letter'] and row['password'][row['max']-1] == row['letter']), passwords_list)))

print(valid_policy_two())