from puzzle_3_input import tree_map, test_tree_map
from math import prod as prod


roads = tree_map()

def count_num_trees(num, down_two=False, roads=roads):
    slope = 0
    count_trees = 0
    l = len(roads)
    for i, road in enumerate(roads):
        if down_two and i % 2 != 0:
            continue
        if i < l:
            possible_tree = roads[i][slope]
            count_trees += possible_tree.count('#')
            slope = (slope + num) % 31
    return count_trees

#Solution 3a
three = count_num_trees(3)
print(three)

#Solution 3b
one = count_num_trees(1)
five = count_num_trees(5)
seven = count_num_trees(7)
one_two_down = count_num_trees(1, True)

factor = one * three * five * seven * one_two_down
print(factor)