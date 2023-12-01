f = input("Input or Test File? (I/T) ").lower()
if f == "t":
    file = "test.txt"
else:
    file = "input.txt"

# save input text in array
with open(file) as f:
    input_lines = [x.strip("\n") for x in f.readlines()]

l = 0 # input line
i = 0 # CRT position
x = 1 # sprite pos
add = None
strength = 0
cycles = [20, 60, 100, 140, 180, 220]
crt = [["." for i in range(40)] for i in range(6)]

print()
print("========================================")

while l < len(input_lines):
    line = input_lines[l]

    # update CRT line (part 2)
    if i % 40 <= x+1 and i % 40 >= x-1:
        crt[int(i / 40)][i % 40] = "#"
    
    # update strength total (part 1)
    if i+1 in cycles:
        strength += x * (i+1)

    # if line says noop, then move on
    if line[:4] == "noop":
        l += 1
        i += 1
        continue
    # if line says addx, do command over 2 turns
    else:
        # 1st turn: stores value to add, does nothing
        if add == None:
            add = int(line[5:])
            i += 1
            continue
        # 2nd turn: updates x with addx value
        else:
            x += add
            add = None
            l += 1
    i += 1

for line in crt:
    temp = ""
    for x in line:
        temp += x
    print(temp)

print("========================================")
print("Strength: {}\n".format(strength))