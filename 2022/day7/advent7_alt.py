# save input text in array
with open("input.txt") as f:
    input_lines = [x.strip("\n") for x in f.readlines()]

# returns sum of the dict d, and a list of all sums of nested dicts
def get_sums(d, sums):
    sum = 0
    for x in d.values():
        if type(x) == int:
            sum += x
        elif type(x) == dict:
            sum += get_sums(x, sums)[0]
    sums.append(sum)
    return sum, sums


main = {}
current_dir = main
cd = []

# updates main dict representing the file tree
for i, l in enumerate(input_lines):
    if l[0:4] == "$ cd":
        if l[5] == ".":
            # cd ..
            cd.pop(-1)
            temp = main
            for i in cd:
                temp = temp[i]
            current_dir = temp
        elif l[5] != "/":
            # cd [name]
            current_dir = current_dir[l[5:]]
            cd.append(l[5:])
    elif l[0:4] == "$ ls":
        # get contents of ls command
        for j in range(i+1, len(input_lines)):
            if input_lines[j][0] == "$":
                temp = j
                break
            temp = len(input_lines)
        files = input_lines[i+1:temp]
        for f in files:
            if f[0:3] == "dir":
                # dir
                current_dir[f[4:]] = {}
            else:
                # file
                current_dir[f.split()[1]] = int(f.split()[0])

print(main)
print(get_sums(main, [])[1])

sums = sorted(get_sums(main, [])[1])

sum = 0

for i, k in enumerate(sums):
    if k > 1000000:
        break
    sum += k
    
# 2048963 is too high

print(sum)