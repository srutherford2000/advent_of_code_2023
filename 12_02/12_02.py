import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse

max_dict = {"red":12,"green": 13, "blue":14}

def parse_file_into_dict(file_path):
    info = {}
    input_file = open(file_path)
    for line in input_file:
        line = line.strip()
        [game_part, marble_part] = line.split(": ")
        [_,game_num] = game_part.split(" " )
        each_round = marble_part.split("; ")
        this_games_info = []
        for round in each_round:
            this_rounds_dict = {}
            marbles_shown = round.split(", ")
            for marble in marbles_shown:
                [num_color, color] = marble.split(" ")
                this_rounds_dict[color] = int(num_color)
            this_games_info.append(this_rounds_dict)
        info[int(game_num)] = this_games_info
    input_file.close()

def part1_is_valid_game(game_info):
    for round in game_info:
        for color in max_dict.keys():
            if (color in round) and (round[color] > max_dict[color]):
                return False
    return True

def part1_count_valid_games(input_info):
    part1_sum = 0
    for game_id, game_data in input_info.items():
        if part1_is_valid_game(game_data):
            part1_sum += game_id
    return part1_sum

def part2_marbles_power(game_info):
    min_dict = {}
    for round in game_info:
        for color, count in round.items():
            if (color not in min_dict) or (count > min_dict[color]):
                min_dict[color] = count

    marble_power = 1
    for value in min_dict.values():
        marble_power *= value

    return marble_power

def part2_sum_marble_power(input_info):
    part2_sum = 0
    for game_data in input_info.values():
        part2_sum += part2_marbles_power(game_data)
    return part2_sum


def main():
    file_path = only_filepath_argparse()
    input_data = parse_file_into_dict(file_path)
    print(f"Part1 Ans: {part1_count_valid_games(input_data)}")
    print(f"Part2 Ans: {part2_sum_marble_power(input_data)}")




if __name__ == "__main__":
    main()