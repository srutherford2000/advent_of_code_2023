import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import read_from_regex

p1_card_value = "AKQJT98765432"
p2_card_value = "AKQT98765432J"

def custom_sort(s, card_value):
    return [card_value.index(c) for c in s]

def get_counts(hand):
    counts = {}
    for card in hand:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    
    return counts

def rank_hand(counts):
    if len(counts) == 1: 
        #5 of a kind
        hand_rank = 6
    elif (len(counts) == 2) and (4 in list(counts.values())):
        #4 of a kind
        hand_rank = 5
    elif (len(counts) == 2) and (3 in list(counts.values())):
        #full house
        hand_rank = 4
    elif (len(counts) == 3) and (3 in list(counts.values())):
        #3 of a kind
        hand_rank = 3
    elif (len(counts) == 3) and (list(counts.values()).count(2) == 2):
        #2 pairs
        hand_rank = 2
    elif (len(counts) == 4):
        #1 pair
        hand_rank = 1
    elif (len(counts) == 5):
        #literally nothing
        hand_rank = 0

    return hand_rank

def give_card_value(hand):
    counts = get_counts(hand)
    rank_p1 = rank_hand(counts)

    if ("J" in counts) and (counts["J"] != 5):
        counts[max((k for k, v in counts.items() if k != "J"), key=lambda k: counts[k])] += counts["J"]
        del counts["J"]
    rank_p2 = rank_hand(counts)

    return rank_p1, rank_p2

def get_points_from_ranks(sorted_ranks, way_to_sort, hand_to_score):
    hand_multiplier = 1
    total_points = 0
    
    for i in range(7): #this 7 represents the 7 different cateories we could have 
        if i in sorted_ranks:
            hands_in_this_rank = sorted_ranks[i]
            hands_in_this_rank = sorted(hands_in_this_rank, key=lambda x: custom_sort(x, way_to_sort))[::-1]
            for hand in hands_in_this_rank:
                total_points += hand_to_score[hand]*hand_multiplier
                hand_multiplier+=1
    return total_points
    
    

def solve_both_parts(input_dict):
    p1_cards_sorted_by_rank = {}
    p2_cards_sorted_by_rank = {}
    for hand in input_dict.keys():
        p1_rank,p2_rank = give_card_value(hand)
        if p1_rank not in p1_cards_sorted_by_rank:
            p1_cards_sorted_by_rank[p1_rank] = []
        if p2_rank not in p2_cards_sorted_by_rank:
            p2_cards_sorted_by_rank[p2_rank] = []
        p1_cards_sorted_by_rank[p1_rank].append(hand)
        p2_cards_sorted_by_rank[p2_rank].append(hand)

    return get_points_from_ranks(p1_cards_sorted_by_rank, p1_card_value, input_dict), get_points_from_ranks(p2_cards_sorted_by_rank, p2_card_value, input_dict)


def main():
    file_path = only_filepath_argparse()
    input_dict = {hand:score  for [hand,score] in read_from_regex(file_path, r'(\w+) (\d+)',[str,int])}
    p1_ans, p2_ans = solve_both_parts(input_dict)
    print(f"Part 1 Ans: {p1_ans}")
    print(f"Part 2 Ans: {p2_ans}")



if __name__ == "__main__":
    main()