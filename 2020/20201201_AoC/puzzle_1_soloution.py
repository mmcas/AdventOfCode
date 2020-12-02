from puzzle_1_input import input 
numbers_list = input()

def find_two_nums(num_list):
    for num in num_list:
        num_list.remove(num)
        for other_num in num_list:
            if other_num + num == 2020:
                return(other_num * num)
            else:
                next


def find_three_nums(num_list):
    for num in num_list:
        num_list.remove(num)
        for other_num in num_list:
            for third_num in num_list:
                if third_num + other_num + num == 2020:
                    return(third_num * other_num * num)
                else:
                    next


print(find_two_nums(numbers_list))
print(find_three_nums(numbers_list))