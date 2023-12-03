import sys


def surrounding_numbers(lines: list[list[str]], r: int, c: int) -> list[(int, int)]:
    '''
    Return positions of all surrounding digits
    '''
    adj = []
    d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    # check all adjacent cells for digits
    # ignores numbers right next to each other, so they arent counted twice later
    for dr, dc in d:
        try:
            if lines[r + dr][c + dc] != '.' and \
            (r + dr, c + dc + 1) not in adj and (r + dr, c + dc - 1) not in adj:
                adj.append((r + dr, c + dc))
        except:
            continue

    return adj


def get_all_digits(lines: list[list[str]], nr: int, nc: int) -> str:
    '''
    Given a coordinate to a digit, returns the full number that digit is part of
    '''
    digits = lines[nr][nc]
    temp_c = nc - 1
    
    # get left adj. digits
    while temp_c >= 0 and lines[nr][temp_c] in '0123456789':
        digits = lines[nr][temp_c] + digits
        temp_c -= 1
    
    # get right adj. digits
    temp_c = nc + 1
    while temp_c < len(lines[0]) and lines[nr][temp_c] in '0123456789':
        digits = digits + lines[nr][temp_c]
        temp_c += 1
    
    return int(digits)


def part1(lines: list[list[str]]) -> None:
    '''
    Part 1 solution
    '''
    total = 0

    # get all characters with special symbols
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] not in '0123456789.':

                # add all surrounding numbers to sum & remove from list
                for nr, nc in surrounding_numbers(lines, r, c):
                    
                    digits = get_all_digits(lines, nr, nc)

                    print(f'| {digits}')
                    total += digits
    print(total, '\n')


def part2(lines: list[list[str]]) -> None:
    '''
    Part 2 solution
    '''
    total = 0
    
    # get all * characters
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == '*':

                # if next to exactly 2 numbers
                surrounding_digits = surrounding_numbers(lines, r, c)
                if len(surrounding_digits) == 2:
                    
                    # add the product of those 2 numbers
                    nums = [get_all_digits(lines, nr, nc) for nr, nc in surrounding_digits]
                    print(f'| {nums[0]} * {nums[1]} == {nums[0] * nums[1]}')
                    total += nums[0] * nums[1]
    print(total)
                    

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in sys.stdin]
    part1(lines)
    part2(lines)

