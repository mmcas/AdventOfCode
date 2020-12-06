from puzzle_6_input import answers_list

answers = answers_list()

def sum_answers_answered_once():
    return sum(len(set(''.join(answer))) for answer in answers)

def sum_answers_answered_by_all():
    return sum(len(set.intersection(*[set(string) for string in answer])) for answer in answers)

#Soloution 6a
print(sum_answers_answered_once())

#Soloution 6b
print(sum_answers_answered_by_all())