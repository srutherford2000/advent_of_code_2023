import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from functools import reduce
from itertools import repeat
from math import sqrt, floor, ceil

def find_x_given_y(y, a,b,c):
    new_c = c - y
    determinant = sqrt(b**2 - 4*a*new_c)
    return ceil(((-b + determinant)/(2*a))), floor(((-b - determinant)/(2*a)))

def find_boats_quadratic(args):
    racetime, max_distance = args
    low_bound, up_bound = find_x_given_y(max_distance, -1, racetime, 0)

    if (-(low_bound**2) + racetime*low_bound) == max_distance:
        low_bound += 1
    if (-(up_bound**2) + racetime*up_bound) == max_distance:
        up_bound -= 1

    return up_bound - low_bound + 1

def main():
    file_path = only_filepath_argparse()
    input_file = open(file_path)
    times = input_file.readline().strip().split()[1:]
    distances = input_file.readline().strip().split()[1:]
    input_file.close()

    print(f"Part 1 Ans: {reduce(lambda prod, args: prod* find_boats_quadratic(args), zip([int(i) for i in times], [int(i) for i in distances]),1)}")
    print(f"Part 2 Ans: {find_boats_quadratic((int(''.join(times)), int(''.join(distances))))}")


if __name__ == "__main__":
    main()