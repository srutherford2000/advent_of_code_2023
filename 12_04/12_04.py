import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import read_from_regex

def cards_to_dict(input_data):
    card_dict = {}
    for row in input_data:
        lottery_nums = set(int(i) for i in row[1].split())
        found_numbers = set(int(i) for i in row[2].split())

        num_overlap = len(lottery_nums.intersection(found_numbers))
        card_dict[row[0]] = [i for i in range(row[0]+1, row[0]+1+num_overlap)]

    return card_dict

def part1(card_dict):
    total_sum = 0
    for i in card_dict.values():
        if len(i) != 0:
            total_sum += 2**(len(i)-1)
    return total_sum

def recurse_on_card(card_dict, recurse_val, memo={}):
    if len(card_dict[recurse_val]) == 0:
        return 1
    
    if recurse_val in memo:
        return memo[recurse_val]

    total_sum = 1
    for num in card_dict[recurse_val]:
        total_sum += recurse_on_card(card_dict, num, memo)

    memo[recurse_val] = total_sum
    return total_sum

def part2(card_dict):
    total_sum = 0
    for card in list(card_dict.keys()):
        total_sum += recurse_on_card(card_dict, card)
    return total_sum


def main():
    file_path = only_filepath_argparse()
    input_data = read_from_regex(file_path, r'Card [ ]*(\d+): (.*)\|(.*)',[int,str,str])
    card_dict = cards_to_dict(input_data)
    print(f"Part 1 Ans: {part1(card_dict)}")
    print(f"Part 2 Ans: {part2(card_dict)}")

if __name__ == "__main__":
    main()