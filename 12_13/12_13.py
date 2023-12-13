import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import read_separated_multiline_input  

def count_wrong(list1, list2):
    ind = 0
    wrong = 0
    while (ind < len(list1)) and (ind<len(list2)):
        for chr1,chr2 in zip(list1[ind], list2[ind]):
            if chr1 != chr2:
                wrong += 1
        ind += 1
    return wrong

def transpose_input(data):
    transposed = ["" for _ in data[0]]
    for row in data:
        for i, chr in enumerate(row):
            transposed[i] += chr
    return transposed

def search_for_symetry(set_of_data, smudges_allowed):
    for i in range(1,len(set_of_data)):
        first_half = set_of_data[:i]
        second_half = set_of_data[i:]

        if count_wrong(first_half[::-1], second_half) == smudges_allowed:
            return i
    
    return None


def solve_both(data):
    p1_ans = 0
    p2_ans = 0
    for grid in data:
        try: 
            p1_ans += 100 * search_for_symetry(grid, 0)
        except:
            p1_ans += search_for_symetry(transpose_input(grid), 0)
        
        try:
            p2_ans += 100 * search_for_symetry(grid, 1)
        except:
            p2_ans += search_for_symetry(transpose_input(grid), 1)
    
    return p1_ans, p2_ans

def main():
    file_path = only_filepath_argparse()
    input_data = read_separated_multiline_input(file_path, None, str)
    p1_ans, p2_ans = solve_both(input_data)
    print(f"Part 1 Ans: {p1_ans}")
    print(f"Part 2 Ans: {p2_ans}")


if __name__ == "__main__":
    main()