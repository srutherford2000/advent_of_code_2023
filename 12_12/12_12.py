import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse

def manual_read(file_path):
    record_info = []
    
    in_file = open(file_path)
    for line in in_file:
        record,nums = line.strip().split()
        record_info.append((record, [int(i) for i in nums.split(",")]))
    in_file.close()
    return record_info

def solve_both(grouped_data):
    p1_ans = 0
    p2_ans = 0
    for record, nums in grouped_data:
        p1_ans += recursive_try(record, nums, False)
        p2_ans += recursive_try(record +("?" + record)*4, nums * 5, False)
    return p1_ans, p2_ans
    

memo = {}

def recursive_try(line, nums, needs_to_be_dot):
    key = (line, tuple(nums), needs_to_be_dot)

    if key in memo:
        return memo[key]

    if (len(line) == 0) and (len(nums) == 0):
        result = 1
    elif len(line) == 0:
        result = 0
    elif (len(nums) == 0) and ("#" not in line):
        result = 1
    elif len(nums) == 0:
        result = 0
    elif sum(nums) > len(line):
        result = 0
    elif needs_to_be_dot and line[0] == "#":
        result = 0
    elif needs_to_be_dot:
        result = recursive_try(line[1:], nums, False)
    else:
        result = 0

        if (line[0] == ".") or (line[0] == "?"):
            result += recursive_try(line[1:], nums, False)
        if (line[0] == "#") or (line[0] == "?"):
            try:
                for i in range(nums[0]):
                    if line[i] == ".":
                        raise IndexError

                result += recursive_try(line[i+1:], nums[1:], True)
            except:
                pass

    memo[key] = result
    return result


def main():
    file_path = only_filepath_argparse()
    records_and_nums = manual_read(file_path)
    p1_ans, p2_ans = solve_both(records_and_nums)
    print(f"Part 1 Ans {p1_ans}")
    print(f"Part 2 Ans {p2_ans}")


if __name__ == "__main__":
    main()