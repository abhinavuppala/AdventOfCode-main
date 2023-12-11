import sys
from math import lcm as cheese

def create_tree(lines: list[str]) -> (str, dict):
    '''
    Create & return tree structure & directions from input lines
    '''
    path, _, *nodes = lines

    # create tree structure
    tree_nodes = dict()
    for node in nodes:
        head, values = node.split(' = ')
        l, r = values.strip('()').split(', ')
        tree_nodes[head] = {'L': l, 'R': r}
    
    return path, tree_nodes


def part2(lines: list[str]) -> None:
    '''
    Part 2 solution
    '''
    path, tree_nodes = create_tree(lines)

    # find how often each state cycles from start -> Z-state
    steps = 0
    current = list(filter(lambda x: x[-1] == 'A', tree_nodes.keys()))
    looping_nums = [0 for _ in range(len(current))]
    finished = False
    while not all(looping_nums):
        for step in path:
            current = [tree_nodes[head][step] for head in current]
            steps += 1
            for i in range(len(current)):
                if current[i].endswith('Z'):
                    looping_nums[i] = steps
    
    # if the 1st one loops to 2, 2nd one to 3, and other nums
    # the time they all line up should be the least common multiple
    print(cheese(*looping_nums))
    

def part1() -> None:
    '''
    Part 1 solution
    '''
    lines = [line.rstrip() for line in sys.stdin]
    path, tree_nodes = create_tree(lines)

    # keep following pattern until ZZZ reached
    steps = 0
    start, end = 'AAA', 'ZZZ'
    current = start
    while current != end:
        for step in path:
            current = tree_nodes[current][step]
            steps += 1
            if current == end: break
    print(steps)

    return lines

if __name__ == '__main__':
    part2(part1())
