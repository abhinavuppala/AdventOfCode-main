# save input text in array
with open("input.txt") as f:
    input_lines = [x.strip("\n") for x in f.readlines()]

# returns amt of times x appears in arr
def amount(arr, x):
    sum = 0
    for i in arr:
        if i == x:
            sum += 1
    return sum

# get numbers into 2d array
grid = []
for line in input_lines:
    grid.append([int(x) for x in list(line)])

# all edges will be visible
rows = len(grid)
cols = len(grid[0])
visible = 2 * cols + 2 * rows - 4

# goes through all inner items
for i in range(1, rows-1):
    temp = ""
    for j in range(1, cols-1):
        col = [grid[x][j] for x in range(cols)]
        # check if visible in the row, left side
        if grid[i][j] == max(grid[i][:j+1]) and amount(grid[i][:j+1], grid[i][j]) == 1:
            visible += 1
        # check if visible in the row, right side
        elif grid[i][j] == max(grid[i][j:]) and amount(grid[i][j:], grid[i][j]) == 1:
            visible += 1
        # check if visible in the col, top side
        elif grid[i][j] == max(col[:i+1]) and amount(col[:i+1], grid[i][j]) == 1:
            visible += 1
        # check if visible in the col, bottom side
        elif grid[i][j] == max(col[i:]) and amount(col[i:], grid[i][j]) == 1:
            visible += 1

print("Visible trees: ", visible)