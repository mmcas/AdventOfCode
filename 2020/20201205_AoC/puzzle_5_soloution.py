from puzzle_5_input import boarding_pass_list

def get_boarded_seat_ids(bp_list):
    seat_ids = []
    for bp in bp_list:
        r = get_row(bp)
        c = get_column(bp)
        seat_ids.append(get_seat_id(r,c))
    return seat_ids

def get_row(string):
    rows = range(0, 128)
    for char in string[0:7]:
        half = len(rows)//2
        if char == 'F':
            rows = rows[:half]
        else:
            rows = rows[half:]
    return rows[0]

def get_column(string):
    columns = range(0,8)
    for char in string[7:]:
        half = len(columns)//2
        if char == 'L':
            columns = columns[:half]
        else:
            columns = columns[half:]
    return columns[0]

def get_seat_id(row, column):
    return row * 8 + column
 
def get_possible_seats():
    possible_seats = []
    for r_num in range(0,128):
        for c_num in range (0,8):
            possible_seats.append(r_num * 8 + c_num)
    return possible_seats

def get_missing_seats(full_list, boarded_list):
    return set(full_list) - set(boarded_list)

def get_your_seat(missing_seats):
    for seat in missing_seats:
        if seat + 1 in missing_seats or seat - 1 in missing_seats:
            continue
        return seat

#Soloution 5a
seats = get_boarded_seat_ids(boarding_pass_list())
print(max(seats)) 

#Soloution 5b
all_seats = get_possible_seats()
missing_seats = get_missing_seats(all_seats, seats)
print(get_your_seat(missing_seats))

    
