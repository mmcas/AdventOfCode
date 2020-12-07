import re
from puzzle_7_input import bags_list, test_bags_list
permitted_color = "shiny gold"
bags = bags_list()
all_colors = set()

while True:
    matched_colors = []
    reg = rf'(?P<color>[\w\s]+) bags contain .*(?:{permitted_color}).*'
    for bag in bags:
        match = re.search(reg, bag, re.IGNORECASE)
        if match:
            if match.group('color'):
                matched_colors.append(match.group('color'))
    if len(matched_colors) == 0:
        break
    all_colors = all_colors | set(matched_colors)
    permitted_color = '|'.join(matched_colors)

print(len(all_colors))



    
