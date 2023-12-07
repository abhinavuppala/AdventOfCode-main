import sys

PART2 = True

# highest to lowest (13 total)
if PART2:
    STRENGTH = 'AKQT98765432J'
else:
    STRENGTH = 'AKQJT98765432'


# first, assign integer values:
# 5 of a kind = 0
# 4 of a kind = 1
# ...
# one pair = 5
# high card = 6

# then, add decimal values for tiebreakers
# first character:  +0.00 if A, +0.01 if K, ...
# second character: +0.0000 if A, +0.0001 if K, ...
# using hundredths because 13 possible characters
# no duplicate cards


def is_full_house(line: str) -> bool:
    '''
    True if cards are a full house
    '''
    for c in set(line):
        if line.count(c) not in [2, 3]:
            return False
    return True


def is_2_pair(line: str) -> bool:
    '''
    True if cards are a 2 pair
    '''
    for c in set(line):
        if line.count(c) not in [2, 1]:
            return False
    return True


def find_best_card(hand: str) -> int:
    '''
    Find best card by replacing jokers, and return the int value
    '''
    hand_no_j = hand.replace('J', '')
    
    # 1 pair, if all other 4 are unique
    if len(set(hand_no_j)) == 4:
        return 5
    
    # 3 unique cards -> either 1 pair given or 2 jokers
    # either way, best option here is to get a 3 of a kind
    elif len(set(hand_no_j)) == 3:
        return 3
    
    # 2 unique cards -> either 1, 2, 3 jokers
    # 3 jokers: no pairs given -> 4 of a kind
    # 2 jokers: 1 pair given -> 4 of a kind
    # 1 joker:  2 pairs given -> full house
    #           if 3 of a kind + 1 -> 4 of a kind
    elif len(set(hand_no_j)) == 2:
        if len(hand_no_j) == 4 and is_2_pair(hand_no_j): 
            return 2
        else: return 1

    # 1 unique card -> either 1, 2, 3, 4 jokers
    # either way, all jokers can match the 1 unique card -> 5 of a kind
    elif len(set(hand_no_j)) == 1:
        return 0
    
    # all jokers -> 5 of a kind
    else:
        return 0
    
    

def solution() -> None:
    '''
    Part 1 and 2 Solution
    Change part by changing bool at top of the script
    '''
    cards_bids = [line.rstrip().split() for line in sys.stdin]
    cards_bids = [(x, int(y)) for (x, y) in cards_bids]
    card_values = []

    for cards, bid in cards_bids:
        s = set(cards)
        card_val = 0

        # has a joker in the hand
        if PART2 and ('J' in s):
            card_val = find_best_card(cards)

        # 5 of a kind
        elif len(s) == 1:
            card_val = 0

        # 4 of a kind or full house
        elif len(s) == 2:
            if not is_full_house(cards):
                card_val = 1
            else:
                card_val = 2

        # 3 of a kind or 2 pair
        elif len(s) == 3:
            if not is_2_pair(cards):
                card_val = 3
            else:
                card_val = 4

        # 1 pair
        elif len(s) == 4:
            card_val = 5
            
        # high card
        elif len(s) == 5:
            card_val = 6
        
        else:
            print('ERROR')
            break
        
        # tiebreakers
        for i in range(len(cards)):
            card_val += STRENGTH.find(cards[i]) * float(f'0.0{"0"*(i*2)}1')
        card_values.append(card_val)


    # get cards with ranks like so: (rank, (card_str, bid))
    cards_with_ranks = list(zip(card_values, cards_bids))
    cards_with_ranks.sort(key = lambda x: x[0])
    cards_with_ranks = [(len(cards_with_ranks) - i, cards_with_ranks[i][1]) for i in range(len(cards_with_ranks))]

    # sum all weighted winnings
    bid_sums = list((x[0] * x[1][1]) for x in cards_with_ranks)
    print(sum(bid_sums))


if __name__ == '__main__':
    solution()
