import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import read_and_split  

def hash(string):
    hash_val = 0
    for chr in string:
        hash_val += ord(chr)
        hash_val *= 17
        hash_val %=256
    return hash_val

def add_to_map(map, new_str):
    label, lens = new_str.split("=")
    hashed_label = hash(label)

    if not (hashed_label in map):
        map[hashed_label] = {}
    
    map[hashed_label][label] = int(lens)

    return map

def remove_from_map(map, new_str):
    label = new_str[:-1]
    hashed_label = hash(label)

    if (hashed_label in map) and (label in map[hashed_label]):
        del map[hashed_label][label]

    return map

def parse_into_hashmap(data):
    map = {}
    for new_str in data:
        if "=" in new_str:
            #we do the add/replace action
            map = add_to_map(map, new_str)
        elif "-" in new_str:
            #we do remove action
            map = remove_from_map(map, new_str)
        else:
            print(f"String '{new_str}' did not have = or - sign in it")
    return map
  

def part_1(data):
    return sum([hash(string) for string in data])

def part_2(data):
    hash_map = parse_into_hashmap(data)

    total = 0
    for key,val in hash_map.items():
        for slot, focal_length in enumerate(val.values()):
            total += (key+1) * (slot+1) * focal_length
    return total


def main():
    file_path = only_filepath_argparse()
    input_data = read_and_split(file_path,",", str)[0]
    print(f"Part 1 Ans {part_1(input_data)}")
    print(f"Part 2 Ans {part_2(input_data)}")




if __name__ == "__main__":
    main()