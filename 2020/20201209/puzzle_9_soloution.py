from puzzle_9_input import encrypted_list
encodings = encrypted_list()

check_encodings = encodings[25:]
start = 0 
end = 25

for check in check_encodings:
    preamble = encodings[start:end]
    combinations = []
    [[combinations.append(other_num + num) for other_num in preamble if other_num is not num]for num in preamble]
    if check not in combinations:
        print(check)
        break
    start += 1
    end += 1
    


