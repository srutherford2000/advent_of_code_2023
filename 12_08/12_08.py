import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import basic_read
import re
from math import lcm

def steps_to_dict(input_data):
    pattern = re.compile(r'(\w+) = \((\w+), (\w+)\)')
    room_to_lr = {}
    for line in input_data:
        groups = pattern.match(line)
        room_to_lr[groups[1]] = (groups[2], groups[3])
    return room_to_lr

def p1_criteria(room):
    return room == "ZZZ"
def p2_criteria(room):
    return room[-1] == "Z"

def find_steps(parsed_rooms, directions, start_room, end_criteria):
    steps = 0
    room_name = start_room

    while end_criteria(room_name) == False:
        if directions[steps % len(directions)] == "L":
            room_name = parsed_rooms[room_name][0]
        elif directions[steps % len(directions)] == "R":
            room_name = parsed_rooms[room_name][1]
        steps += 1
    
    return steps

def part_2(parsed_rooms, directions):
    loop_intervals = []

    for room in [room for room in parsed_rooms.keys() if room[-1] == "A"]:
        loop_intervals.append(find_steps(parsed_rooms, directions, room, p2_criteria))
    
    return lcm(*loop_intervals)


def main():
    file_path = only_filepath_argparse()
    dirs,_, *steps = basic_read(file_path, str)
    rooms_parsed = steps_to_dict(steps)
    print(f"Part 1 Ans: {find_steps(rooms_parsed, dirs, 'AAA', p1_criteria)}")
    print(f"Part 2 Ans: {part_2(rooms_parsed, dirs)}")


if __name__ == "__main__":
    main()