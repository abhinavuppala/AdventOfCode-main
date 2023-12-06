import math

def part2():
    '''
    Part 2 Solution
    '''
    time, record = 61677571, 430103613071150

    # equation: x * (time - x) - record > 0
    # from derivative, it's increasing then decreasing
    # which means that numbers between x1 and x2 are valid solutions
    # since it's increasing from x2, to max, then decreasing to x1
    x1 = (time + math.sqrt(time ** 2 - 4 * record)) / 2
    x2 = (time - math.sqrt(time ** 2 - 4 * record)) / 2

    print(x1, x2)

    print(math.ceil(x1) - math.ceil(x2))


def part1():
    '''
    Part 1 solution
    '''
    times = [61, 67, 75, 71]
    records = [430, 1036, 1307, 1150]
    # times, records = [7, 15, 30], [9, 40, 200]

    total = 1

    # calculate all possible wins for each amount of button holding
    # then find how many of those win
    for i in range(len(times)):
        distances = [x * (times[i] - x) for x in range(times[i])]
        wins = list(filter(lambda x: records[i] < x, distances))
        total *= len(wins)

    print(total)

if __name__ == '__main__':
    part1()
    print()
    part2()

# didn't parse input since it was literally just a few numbers
