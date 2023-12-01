from sys import stdin

# class definition of Node
class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}

def find_item_arr_2D(target, grid):
    # finds rows that have "S" in them, returns the row and column no. they are in
    return list(filter(lambda x: x != False, [(i, row.index(target)) if target in row else False for i, row in enumerate(grid)]))[0]

grid = [list(line) for line in stdin]

# get start and end coords in tuple (row, col)
start = find_item_arr_2D("S", grid)
end = find_item_arr_2D("E", grid)

# TO DO: implement BFS, find viable locations by using adjacent squares (see phone picture)