import sys
import re
from itertools import chain

# Currently doesn't work, Part 1 works but part 2 doesn't work for the 0-width gaps. Still working on that

def part1() -> list[list[str | int]]:
    '''
    Part 1 solution
    '''

    # get starting row & column
    grid = [list(line.rstrip()) for line in sys.stdin]
    start = (r := grid.index(list(filter(lambda row: any(c == 'S' for c in row), grid))[0]),
            grid[r].index('S'))    # (row, col)

    # BFS variables, each state includes distance from start
    queue, q_i = [(*start, 0)], 0
    visited = []
    d = {(1, 0): ['|', 'L', 'J'], (-1, 0): ['|', '7', 'F'],
        (0, 1): ['-', 'J', '7'], (0, -1): ['-', 'F', 'L']}
    farthest = 0

    while q_i < len(queue):
        r, c, dist = queue[q_i]

        # if already visited
        if (r, c) in visited:
            q_i += 1
            continue
        visited.append((r, c))

        for dr, dc in d:

            # if out of bounds
            if r + dr < 0 or r + dr >= len(grid): continue
            if c + dc < 0 or c + dc >= len(grid[0]): continue

            # if pipe is pointing right way, then add to queue
            if grid[r + dr][c + dc] in d[(dr, dc)]:
                queue.append((r + dr, c + dc, dist + 1))
                farthest = max(dist + 1, farthest)
        
        # replace pipe with number
        grid[r][c] = str(dist)
        q_i += 1

    print(farthest)
    return grid


def part2(grid: list[list[str | int]]) -> None:
    '''
    Part 2 solution
    
    346 is too high
    TODO: figure out how to deal with squeezing through pipes
    '''
    print(*grid, sep='\n')

    # for each . check all directions (recursively)
    # if enclosed by integers, it's inside the pipes
    # if it reaches the edges, it's outside the pipes
    cache = {}
    visited = []

    # for gaps <1 width: add spacer characters within grid, fill in gaps of pipe path, then check should work
    # adding temporary characters in between all cells of the grid
    grid_with_gaps = [[grid[r][int(c / 2)] if c % 2 == 0 else '?' for c in range(len(grid[0]) * 2 - 1)] for r in range(len(grid))]
    grid_with_gaps = [grid_with_gaps[int(i / 2)] if i % 2 == 0 else ['?' for _ in range(len(grid_with_gaps[0]))] for i in range(len(grid) * 2 - 1)]

    # closing horizontal gaps of pipe
    for r in range(0, len(grid_with_gaps), 2):
        for c in range(1, len(grid_with_gaps[0]), 2):
            if grid_with_gaps[r][c+1].isnumeric() and grid_with_gaps[r][c-1].isnumeric() and abs((a := int(grid_with_gaps[r][c+1])) - (b := int(grid_with_gaps[r][c-1]))) == 1:
                grid_with_gaps[r][c] = f'{(a + b) / 2}'

    # closing vertical gaps of pipe
    for r in range(1, len(grid_with_gaps), 2):
        for c in range(0, len(grid_with_gaps[0]), 2):
            if grid_with_gaps[r+1][c].isnumeric() and grid_with_gaps[r-1][c].isnumeric() and abs((a := int(grid_with_gaps[r+1][c])) - (b := int(grid_with_gaps[r-1][c]))) == 1:
                grid_with_gaps[r][c] = f'{(a + b) / 2}'


    # print(*grid_with_gaps, sep='\n')

    # since isnumeric() doesn't work with decimals, and I can't use
    # replace since the blank spaces are . in the grid
    def is_float(x):
        try:
            float(x)
            return True
        except:
            return False
        

    def is_outside(r, c):
        
        # assumes that (r, c) isn't part of the pipe path [isn't a num]
        if (r, c) in cache: return cache[(r, c)]
        visited.append((r, c))

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        outside = True

        for dr, dc in d:

            # if next to an outside cell -> it's outside also
            if (r + dr, c + dc) in cache:
                if cache[(r + dr, c + dc)] == True:
                    outside = True
                    break
            
            # avoid going back & forth
            elif (r + dr, c + dc) in visited:
                continue
            
            # it's on the border of the grid -> impossible to be within pipes -> oustide
            elif r + dr in [-1, 0, len(grid_with_gaps) - 1, len(grid_with_gaps)] or c + dc in [-1, 0, len(grid_with_gaps[0]) - 1, len(grid_with_gaps[0])]:
                outside = True
                break

            # if next to a non-pipe loop cell -> see if it's also outside
            elif not is_float(grid_with_gaps[r + dr][c + dc]):
                if is_outside(r + dr, c + dc):
                    outside = True
                    break
                else:
                    oustide = False
                    break

            # otherwise, it's next to a number, which means we need to check other directions
            else:
                pass
        
        # didn't break out -> not oustide
        else:
            outside = False


        cache[(r, c)] = outside
        return outside
                


    # get all values to check within grid with gaps
    to_check = []
    for r in range(len(grid_with_gaps)):
        for c in range(len(grid_with_gaps[0])):
            if not is_float(grid_with_gaps[r][c]): to_check.append((r, c))
    
    # get all tiles that are inside the pipes
    # AKA unable to reach the outside border of the grid
    inside_tiles = []
    for r, c in to_check:
        if not is_outside(r, c):
            inside_tiles.append((r, c))

    for r, c in inside_tiles:
        grid_with_gaps[r][c] = 'I'

    print(len(inside_tiles), inside_tiles)
    print(*[grid_with_gaps[r][c] for (r, c) in inside_tiles])

    # print(*grid_with_gaps, sep='\n')

    new_grid = [grid_with_gaps[r] for r in range(0, len(grid_with_gaps), 2)]
    new_grid = [[row[c] for c in range(0, len(grid_with_gaps[0]), 2)] for row in new_grid]
    print()
    print(*new_grid, sep='\n')



if __name__ == '__main__':
    part2(part1())
