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

# all edges will have total score of 0, not max
rows = len(grid)
cols = len(grid[0])

# look for max viewing score
max = 0
for i in range(1, rows-1):
    for j in range(1, cols-1):
        col = [grid[x][j] for x in range(cols)]
        row = grid[i]

        score = 1

        # amount of trees viewable to left
        temp = 0
        for x in range(len(row[:j])):
            y = len(row[:j]) - 1 - x
            if row[:j][y] >= grid[i][j]:
                temp = x+1
                break
        if temp == 0:
            temp = len(row[:j])
        score *= temp

        # amount of trees viewable to right
        temp = 0
        for x in range(len(row[j+1:])):
            if row[j+1:][x] >= grid[i][j]:
                temp = x+1
                break
        if temp == 0:
            temp = len(row[j+1:])
        score *= temp

        # amount of trees viewable to up
        temp = 0
        for x in range(len(col[:i])):
            y = len(col[:i]) - 1 - x
            if col[:i][y] >= grid[i][j]:
                temp = x+1
                break
        if temp == 0:
            temp = len(col[:i])
        score *= temp

        # amount of trees viewable to down
        temp = 0
        for x in range(len(col[i+1:])):
            if col[i+1:][x] >= grid[i][j]:
                temp = x+1
                break
        if temp == 0:
            temp = len(col[i+1:])
        score *= temp
                
        if score > max: max = score

print("FINAL MAX TREE SCORE: ",max)

# could be more efficient, maybe reusing the code to check the max