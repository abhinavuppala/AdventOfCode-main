f = input("Input or Test File? (I/T) ").lower()
if f == "t":
    file = "test.txt"
else:
    file = "input.txt"

# save input text in array
with open(file) as f:
    input_lines = [x.strip("\n") for x in f.readlines()]

directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
h = {"x": 0, "y": 0}
k = [{"x": 0, "y": 0} for i in range(9)] # this time, there are 9 different knots
visited = []

# returns if they are touching, or where to move it
# moves p2 to p1 (use p1 as H, p2 as T)
def in_range(p1, p2):
    x_range = [p1["x"]-1, p1["x"]+1]
    y_range = [p1["y"]-1, p1["y"]+1]
    # if p2 is in the x-range and y-range of p1 (they are touching)
    if p2["x"] in list(range(x_range[0], x_range[1]+1)) and p2["y"] in list(range(y_range[0], y_range[1]+1)):
        return True
    else:
        # possible points that p2 can move to (hardcoded because only 8 points)
        points = [  [p2["x"]+1, p2["y"]+1], [p2["x"]+1, p2["y"]], [p2["x"]+1, p2["y"]-1],
                    [p2["x"], p2["y"]+1],                          [p2["x"], p2["y"]-1],
                    [p2["x"]-1, p2["y"]+1], [p2["x"]-1, p2["y"]], [p2["x"]-1, p2["y"]-1]]
        temp = {"x": 0.1, "y": 0.1}
        # finds the optimal spot for p2 to move to - directly adj. preferred
        for point in points:
            if point[0] in list(range(x_range[0], x_range[1]+1)) and point[1] in list(range(y_range[0], y_range[1]+1)):
                temp["x"], temp["y"] = point[0], point[1]
                if point[0] == p1["x"] or point[1] == p1["y"]:
                    return temp
        if temp != {"x": 0.1, "y": 0.1}: return temp

# move head and tail for each input line
for line in input_lines:
    direction = line[0]
    distance  = int(line[2:])
    for i in range(distance):
        if k[-1] not in visited:
            visited.append(k[-1])

        # update H position
        h["x"] += directions[direction][0]
        h["y"] += directions[direction][1]

        # if not touching, moves T
        temp = in_range(h, k[0])
        if temp != True: k[0] = temp

        for i in range(0, len(k)-1):
            temp = in_range(k[i], k[i+1])
            if temp != True: k[i+1] = temp
        

    if k[-1] not in visited:
            visited.append(k[-1])

print(visited)
print("Spaces T has visited:",len(visited))

# 6263-6265 are too high