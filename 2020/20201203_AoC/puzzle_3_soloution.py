from puzzle_3_input import tree_map, test_tree_map

roads = tree_map()
slope = 0
count_trees = 0
l = len(roads)
for i, road in enumerate(roads):
    if i < l:
        possible_tree = roads[i][slope]
        count_trees += possible_tree.count('#')
        slope = (slope + 3) % 31

    
print(count_trees)