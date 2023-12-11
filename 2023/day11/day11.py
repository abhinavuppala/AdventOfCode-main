import sys
from itertools import chain

def solution() -> None:
    '''
    Solution for part 1 and 2, just change the value of SPACE
    '''
    grid = [list(line.rstrip()) for line in sys.stdin]

    # find which cols & rows need to be duplicated
    rows_to_dupe = [False if any(c == '#' for c in row) else True for row in grid]
    cols_to_dupe = [False if any(grid[r][c] == '#' for r in range(len(grid))) else True for c in range(len(grid[0]))]

    # how many each empty row/col is replaced with
    # part 1 - 2, part 2 - 1_000_000
    # change this for part 1 vs part 2
    SPACE = 1_000_000

    # find all points to check
    points = list(chain.from_iterable([[(r, c) for c in range(len(grid[0])) if grid[r][c] == '#'] for r in range(len(grid))]))
    current = points.pop()
    path_total = 0

    while len(points) > 0:
        r, c = current

        # total cells travelled
        for dr, dc in points:
            path_total += abs(r - dr) + abs(c - dc)

            # account for extra space crossed
            spaces = rows_to_dupe[min(r, dr) : max(r, dr)].count(True) + cols_to_dupe[min(c, dc) : max(c, dc)].count(True)
            path_total += spaces * (SPACE - 1)
        
        current = points.pop()

    print(path_total)

if __name__ == '__main__':
    solution()
