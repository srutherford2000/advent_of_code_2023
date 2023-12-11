import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import basic_read
from itertools import combinations

def get_ind_before(list_of_values, val):
    ind = 0
    while (ind<len(list_of_values)) and (val > list_of_values[ind]):
        ind += 1
    return ind

def get_expanded_rows_and_cols(grid):
    bad_rows = []
    for y_ind,row in enumerate(grid):
        if "#" not in row:
            bad_rows.append(y_ind)
    
    bad_cols = []
    for x_ind in range(len(grid[0])):
        if "#" not in [grid[y_ind][x_ind] for y_ind in range(len(grid))]:
            bad_cols.append(x_ind)
    
    return bad_rows, bad_cols

def get_adjusted_galaxy_inds(grid, expanded_rows, expanded_cols, expansion_amount):
    id_inds = []

    for y_ind in range(len(grid)):
        for x_ind in range(len(grid[0])):
            if grid[y_ind][x_ind] == "#":
                num_expanded_cols = get_ind_before(expanded_cols, x_ind)
                adjusted_x = x_ind + (num_expanded_cols*(expansion_amount-1))
                num_expanded_rows = get_ind_before(expanded_rows, y_ind)
                adjusted_y = y_ind + (num_expanded_rows*(expansion_amount-1))
                id_inds.append((adjusted_x, adjusted_y))

    return id_inds

def solve_galaxy(input_data, expansion_amount):
    bad_rows, bad_cols = get_expanded_rows_and_cols(input_data)
    galaxy_inds = get_adjusted_galaxy_inds(input_data, bad_rows, bad_cols, expansion_amount)

    all_combos = combinations(galaxy_inds,2)
    distances = 0

    for ((x1,y1),(x2,y2)) in all_combos:
        distances += abs(x1-x2) + abs(y1-y2)
    
    return distances

def main():
    file_path = only_filepath_argparse()
    input_data = basic_read(file_path, str)
    print(f"Part 1 Ans: {solve_galaxy(input_data, 2)}")
    print(f"Part 2 Ans: {solve_galaxy(input_data, 1000000)}")

if __name__ == "__main__":
    main()