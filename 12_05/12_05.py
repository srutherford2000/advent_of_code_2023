import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse

def manual_read(filepath):
    input_file = open(filepath)

    input_data = []
    this_translation = []
    for line in input_file:
        if line.strip() == "":
            input_data.append(this_translation)
            this_translation = []
        else:
            this_translation.append(line.strip())
    input_data.append(this_translation)

    input_file.close()
    return input_data

def find_seed_location(seed, input_maps):
    cur_seed_val = seed
    for map in input_maps:
        for trans in map[1:]:
            [dst, src, trans_range] = [int(i) for i in trans.split()] 
            if (cur_seed_val >= src) and (cur_seed_val < src+trans_range):
                cur_seed_val -= (src - dst)
                break

    return cur_seed_val

def part_1(input_data):
    seeds_to_check = [int(i) for i in input_data[0][0].split()[1:]]

    min_seed_loc = None
    for seed in seeds_to_check:
        field_loc = find_seed_location(seed, input_data[1:])
        if (min_seed_loc is None) or (field_loc < min_seed_loc):
            min_seed_loc = field_loc
    return min_seed_loc

def part_2(input_data):
    seeds_to_check = [int(i) for i in input_data[0][0].split()[1:]]

    min_seed_loc = None
    for i in range(0,len(seeds_to_check),2):
        for seed in range(seeds_to_check[i+1]):
            seed += seeds_to_check[i]
            field_loc = find_seed_location(seed, input_data[1:])
            if (min_seed_loc is None) or (field_loc < min_seed_loc):
                min_seed_loc = field_loc
    return min_seed_loc

def main():
    file_path = only_filepath_argparse()
    input_data = manual_read(file_path)
    print(f"Part 1 Ans: {part_1(input_data)}")
    print(f"Part 2 Ans: {part_2(input_data)}")

if __name__ == "__main__":
    main()