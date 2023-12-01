import time
import math

f = input("Input or Test File? (I/T) ").lower()
if f == "t":
    file = "test.txt"
else:
    file = "input.txt"
print()

# break input into paragraphs
with open(file) as f:
    input_paras = f.read().split("\n\n")

# each monkey is represented by a dict w/in this list
# monkey 0 is 1st item, monkey 1 is 2nd item, etc.
monkeys = []

# parse input text and convert to usable info
# monkey = {items: [int], operation: str, test: int, throw: {"true": int, "false": int}}
for i, k in enumerate(input_paras):
    lines = k.split("\n")
    monkey = {}
    monkey["items"] = [int(x) for x in lines[1][lines[1].index(":")+2:].split(", ")]
    monkey["operation"] = lines[2][lines[2].index(":")+8:].replace("old","k")
    monkey["test"] = int(lines[3][lines[3].index("y")+2:])
    monkey["throw"] = {"true": int(lines[4][-1]), "false": int(lines[5][-1])}
    monkeys.append(monkey)

"""
Steps for 1 monkey
===================
Worry level multiplied by monkey's operation
Worry level divided by 3, truncated
Check monkey's condition (divisible by x)
Move to other monkey accordingly
Repeat for all items of that monkey
"""

# thanks to vinny
lcm = math.lcm(*[monkeys[i]["test"] for i in range(len(monkeys))])

turns = 10000
inspect_counts = [0 for i in range(len(monkeys))]

start = time.time()

# move items around for 20 turns
for i in range(turns):
    # perform 1 round of moving items around

    if i % 1000 == 0 or i == 20:
        print("Turn",i)
        print(inspect_counts)
        print(time.time() - start)
        print("===================")

    for x, m in enumerate(monkeys):
        temp = len(m["items"])

        for i in range(temp):
            inspect_counts[x] += 1
            k = m["items"][0]
            worry = eval(m["operation"])

            if worry % m["test"] == 0:
                monkeys[m["throw"]["true"]]["items"].append(worry % lcm)
                m["items"].pop(0)
            else:
                monkeys[m["throw"]["false"]]["items"].append(worry % lcm)
                m["items"].pop(0)

print("Turn",turns)
print(inspect_counts)
print("Monkey Business: ",sorted(inspect_counts)[-2] * sorted(inspect_counts)[-1])
print("Total time:", time.time() - start)