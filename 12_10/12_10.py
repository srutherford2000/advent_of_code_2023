#credit to: https://www.reddit.com/r/adventofcode/comments/18eza5g/2023_day_10_animated_visualization/
#had a really good visualization which helped make a much more efficent part 2

import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import basic_read

moves = {"|":[None, (0,1), None, (0,-1)], 
         "-":[(1,0),None, (-1,0), None], 
         "L":[None, (1,0), (0,-1), None], 
         "J":[(0,-1), (-1,0), None, None], 
         "7":[(0,1), None, None, (-1,0)], 
         "F":[None, None, (0,1), (1,0)]}


def find_s_ind(input_data):
    for y_ind, row in enumerate(input_data):
        if "S" in row:
            return (row.index("S"), y_ind)
        

def find_next_ind(cur_ind, last_ind, grid):
    ret_val = None

    cur_x, cur_y = cur_ind
    last_x, last_y = last_ind
    if (cur_x > last_x) and (cur_y == last_y):
        move_ind = 0
    elif (cur_x == last_x) and (cur_y > last_y):
        move_ind = 1
    elif (cur_x < last_x) and (cur_y == last_y):
        move_ind = 2
    elif (cur_x == last_x) and (cur_y < last_y):
        move_ind = 3
    
    try:
        x_adjust, y_adjust = moves[grid[cur_y][cur_x]][move_ind]
        ret_val = (cur_x+x_adjust, cur_y+y_adjust)
    except:
        pass

    return ret_val

def run_path(first_ind, second_ind, grid):
    ind_to_step = {}
    ind_to_step[first_ind] = 0

    step = 1

    last_ind = first_ind
    cur_ind = second_ind
    next_ind = find_next_ind(cur_ind, last_ind, grid)
    ind_to_step[cur_ind] = step
    step += 1

    while (next_ind is not None) and (next_ind != first_ind):
        
        last_ind = cur_ind
        cur_ind = next_ind
        next_ind = find_next_ind(cur_ind, last_ind, grid)
        ind_to_step[cur_ind] = step
        step += 1
    
    loop_found = next_ind == first_ind
    return (loop_found, ind_to_step)


def get_ind_to_step(input_data):
    s_x,s_y = find_s_ind(input_data)

    possible_paths = [(s_x-1, s_y), (s_x+1, s_y), (s_x, s_y-1), (s_x, s_y+1)]

    for path in possible_paths:
        found_loop, ind_to_step = run_path((s_x, s_y), path, input_data)
        if found_loop:
            return (ind_to_step)
        
def solve_both(input_data):
    ind_to_steps = get_ind_to_step(input_data)
    return ((len(ind_to_steps) + 1) // 2, part_2(input_data, ind_to_steps))

def part_2(input_data, ind_to_steps):
    area = 0
    non_zero_counter = 0

    for y_ind in range(len(input_data)-1):
        for x_ind in range(len(input_data[0])):
            point = (x_ind, y_ind)
            point_below = (x_ind, y_ind+1)

            if (point in ind_to_steps) and (point_below in ind_to_steps):
                points_step = ind_to_steps[point]
                point_below_step = ind_to_steps[point_below]
                if ((point_below_step + 1) % len(ind_to_steps)) == points_step:
                    non_zero_counter += 1
                elif ((point_below_step - 1) % len(ind_to_steps)) == points_step:
                    non_zero_counter -= 1
            
            elif (point not in ind_to_steps) and (non_zero_counter!=0):
                area += 1
    return area

    
def main():
    file_path = only_filepath_argparse()
    input_data = basic_read(file_path, str)
    p1_ans, p2_ans = solve_both(input_data)
    print(f"Part 1 Ans: {p1_ans}")
    print(f"Part 2 Ans: {p2_ans}")

if __name__ == "__main__":
    main()