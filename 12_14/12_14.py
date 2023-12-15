import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import basic_read  

def tilt_north(data):
    new_table = ["" for _ in range(len(data))]
    for x_ind in range(len(data[0])):
        ind_to_add_to = 0
        for y_ind in range(len(data)):
            chr = data[y_ind][x_ind]
            if chr == "O":
                new_table[ind_to_add_to] += "O"
                ind_to_add_to+=1
            elif chr == "#":
                while ind_to_add_to < y_ind:
                    new_table[ind_to_add_to] += "."
                    ind_to_add_to += 1
                new_table[y_ind] += "#"
                ind_to_add_to = y_ind +1
        while ind_to_add_to < len(data):
            new_table[ind_to_add_to] += "."
            ind_to_add_to += 1
    return new_table

def rotate_clockwise(grid):
    rotated_grid = ["" for _ in range(len(grid[0]))]
    for row in grid:
        for i, chr in enumerate(row):
            rotated_grid[i] = chr + rotated_grid[i]
    return rotated_grid

def spin_cycle(data):
    new_data = data
    for i in range(4):
        new_data = tilt_north(new_data)
        new_data = rotate_clockwise(new_data)
    return new_data

def find_load(table):
    total = 0
    for i, row in enumerate(table):
        total += (len(table) - i) * row.count("O")
    return total

def part_1(data):
    return find_load(tilt_north(data))

def part_2(data):
    #find the cycle
    cycle = None
    seen_grids = {}
    for i in range(1000000000):
        data = spin_cycle(data)

        if tuple(data) in seen_grids:
            cycle = i - seen_grids[tuple(data)]
            break
        
        seen_grids[tuple(data)] = i

    #do the remainder part
    for _ in range((1000000000 -(i+1)) % cycle):
        data = spin_cycle(data)
    
    return find_load(data)



def main():
    file_path = only_filepath_argparse()
    input_data = basic_read(file_path, str)

    print(f"Part 1 Ans: {part_1(input_data)}")
    print(f"Part 2 Ans: {part_2(input_data)}")


if __name__ == "__main__":
    main()