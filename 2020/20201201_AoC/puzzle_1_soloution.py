from puzzle_1_input import input 
numbers_list = input()

for num in numbers_list:
    numbers_list.remove(num)
    for other_num in numbers_list:
        if other_num + num == 2020:
            print(num)
            print(other_num)
            print(other_num * num)
            break
        else:
            next


    