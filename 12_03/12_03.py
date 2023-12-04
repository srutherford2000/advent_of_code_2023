import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import basic_read

def check_surrounding(x_ind, y_ind, grid):
    dead_space_count = 0
    num_count = 0
    other_count = 0

    for new_x in range(max(0,x_ind-1), min(len(grid[0]), x_ind+2)):
        for new_y in range(max(0, y_ind-1), min(len(grid), y_ind+2)):
            if (new_x == x_ind) and (new_y == y_ind):
                pass
            elif grid[new_y][new_x].isdigit():
                num_count+=1
            elif grid[new_y][new_x] == ".":
                dead_space_count += 1
            else:
                other_count += 1
    
    return (dead_space_count, num_count, other_count)

def get_number_index(row):
    all_num_idxs=[]
    this_num_idx = []
    for i,chr in enumerate(row):
        if chr.isdigit():
            this_num_idx.append(i)
        elif len(this_num_idx) != 0:
            all_num_idxs.append(this_num_idx)
            this_num_idx = []
    
    if len(this_num_idx) != 0:
            all_num_idxs.append(this_num_idx)
            this_num_idx = []
    
    return all_num_idxs

def part1(input_data):
    total_sum = 0
    for y_idx, row in enumerate(input_data):
        num_idxs = get_number_index(row)
        for num_idx in num_idxs:
            for x_idx in num_idx:
                (_,_,num_symbols) = check_surrounding(x_idx, y_idx,input_data)
                if num_symbols != 0:
                    total_sum += int(row[num_idx[0]:num_idx[-1]+1])
                    break
                
    return total_sum

def has_two_numbers(y_ind, x_ind, all_num_idxs, grid):
    found_nums = None
    for new_x in range(max(0,x_ind-1), min(len(grid[0]), x_ind+2)):
        for new_y in range(max(0, y_ind-1), min(len(grid), y_ind+2)):
            if (new_x == x_ind) and (new_y == y_ind):
                pass
            else:
                for possible_num_inds in all_num_idxs[new_y]:
                    if new_x in possible_num_inds:
                        number_found = int(grid[new_y][possible_num_inds[0] : possible_num_inds[-1]+1])

                        if found_nums is None:
                            found_nums = {(new_y, possible_num_inds[0], number_found)}
                        else:
                            found_nums.add((new_y, possible_num_inds[0], number_found))
        
    if len(found_nums) == 2:
        (_,_, gear1) = found_nums.pop()
        (_,_, gear2) = found_nums.pop()
        return gear1 * gear2
    return 0


def part2(input_data):
    total_sum = 0

    all_num_idxs = []
    for row in input_data:
        all_num_idxs.append(get_number_index(row))

    for y_ind, row in enumerate(input_data):
        for x_ind, chr in enumerate(row):
            if chr == "*":
                total_sum += has_two_numbers(y_ind, x_ind, all_num_idxs, input_data)

    return total_sum
                    




def main():
    file_path = only_filepath_argparse()
    input_data = basic_read(file_path, str)
    print(f"Part 1 Ans: {part1(input_data)}")
    print(f"Part 2 Ans: {part2(input_data)}")





if __name__ == "__main__":
    main()