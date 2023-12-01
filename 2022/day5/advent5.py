import re

# save input text
with open("input.txt") as f:
    input_text = f.read()

lines = input_text.split("\n")

# get string input into usable format
stack_text = lines[0:lines.index("")]
steps_text = lines[lines.index("")+1:]

stack_ct = int(stack_text[-1][-2])
stacks_rev = [[] for i in range(stack_ct)] # temp empty

# get letters into stack lists
for i in range(len(stack_text)-1):
    line = stack_text[-1 * (2+i)]

    # stores them in *reverse* order (1st item is bottom of stack, etc.)
    for j in range(stack_ct):
        if line[1 + 4*j] != " ": stacks_rev[j].append(line[1 + 4*j])

# get stacks into correct order (top of stack @ index 0, etc.)
stacks = []
for stack in stacks_rev:
    stacks.append(stack[::-1])

# store values in steps as dicts within list
steps = []
for line in steps_text:
    r = r"[0-9]+"
    nums = [int(x) for x in re.findall(r, line)]
    steps.append({"amt": nums[0], "from": nums[1], "to": nums[2]})

# input has stacks 1-9 so no re needed
# but steps are single and double digits, so re is needed

"""
PART ONE ONLY

# moving boxes around from one stack to another (all steps)
for i in range(len(steps)):
    for j in range(steps[i]["amt"]):
        temp = stacks[steps[i]["from"]-1].pop(0)
        stacks[steps[i]["to"]-1].insert(0, temp)
"""

# moving boxes around from one stack to another (all steps)
for i in range(len(steps)):
    f = steps[i]["from"]-1
    t = steps[i]["to"]-1
    amt = steps[i]["amt"]

    temp = stacks[f][0:amt]
    del stacks[f][0:amt]
    for x in temp[::-1]:
        stacks[t].insert(0, x)

# printing top of each stack
code = ""
for stack in stacks:
    code += stack[0]

print("code: ", code)