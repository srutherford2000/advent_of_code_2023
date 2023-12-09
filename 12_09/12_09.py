import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import read_and_split

def find_both_next(nums):
    rounds = [nums]
    current_round = 0
    
    while all([i == 0 for i in rounds[current_round]]) is False:
        new_round = []
        for i in range(1, len(rounds[current_round])):
            new_round.append(rounds[current_round][i] - rounds[current_round][i-1])
        rounds.append(new_round)
        current_round += 1
    
    rounds[current_round].append(0)
    rounds[current_round].append(0)
    current_round -= 1

    while current_round >= 0:
        rounds[current_round].append(rounds[current_round][-1] + rounds[current_round+1][-1])
        rounds[current_round] = [rounds[current_round][0] - rounds[current_round+1][0]] + rounds[current_round]
        current_round -= 1

    return (rounds[0][-1], rounds[0][0])

def solve_both_parts(input_data):
    p1_sum = 0
    p2_sum = 0
    for set_of_nums in input_data:
        p1_add, p2_add = find_both_next(set_of_nums)
        p1_sum += p1_add
        p2_sum += p2_add
    return p1_sum, p2_sum

def main():
    file_path = only_filepath_argparse()
    input_data = read_and_split(file_path, None,int)
    p1_ans, p2_ans = solve_both_parts(input_data)
    print(f"Part 1 Ans: {p1_ans}")
    print(f"Part 2 Ans: {p2_ans}")

if __name__ == "__main__":
    main()