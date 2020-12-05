from puzzle_5_input import boarding_pass_list

seat_ids = []
boarding_passes = boarding_pass_list()

def get_all_seat_ids(bp_list):
    for bp in bp_list:
        r = get_row(bp)
        c = get_column(bp)
        seat_ids.append(get_seat_id(r,c))
    return seat_ids

#find row
def get_row(string):
    rows = range(0, 128)
    for char in string[0:7]:
        half = len(rows)//2
        if char == 'F':
            rows = rows[:half]
        else:
            rows = rows[half:]
    return rows[0]

#find column
def get_column(string):
    columns = range(0,8)
    for char in string[7:]:
        half = len(columns)//2
        if char == 'L':
            columns = columns[:half]
        else:
            columns = columns[half:]
    return columns[0]

#calculate Seat ID
def get_seat_id(row, column):
    return row * 8 + column

#Soloution 5a
print(max(get_all_seat_ids(boarding_passes)))  

    
