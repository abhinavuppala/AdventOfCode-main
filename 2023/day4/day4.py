import sys

def part1() -> dict:
    '''
    Part 1 solution
    '''
    total = 0
    lines = [line.rstrip() for line in sys.stdin]
    cards = dict()

    for i, line in enumerate(lines):

        # parse input line for player & winning cards
        card, winners = line.rstrip().split(' | ')
        _, card = card.split(':')
        card, winners = card.strip().replace('  ', ' ').split(' '), winners.strip().replace('  ', ' ').split(' ')
        
        # get the cards in common
        card, winners = set(map(int, card)), set(map(int, winners))
        cards[i] = len(card.intersection(winners))

        # part 1: add points based on matches
        if len(card.intersection(winners)) > 0:
            total += 2 ** (len(card.intersection(winners)) - 1)

    print(total)
    return cards


def part2(cards: dict) -> None:
    '''
    Part 2 solution
    '''
    counts = [1 for _ in range(len(cards))]

    # gets quantity of each card & adds below cards
    # trash efficiency but worked for this I guess
    for card in cards:
        for _ in range(counts[card]):
            for i in range(card + 1, cards[card] + card + 1):
                counts[i] += 1

    print(sum(counts))


if __name__ == '__main__':
    part2(part1())
