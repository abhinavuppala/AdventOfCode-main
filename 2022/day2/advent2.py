import argparse

"""
A X - rock (1)
B Y - paper (2)
C Z - scissors (3)

win - 6
draw - 3
loss - 0
"""

# values for player picks
player_values = {"X": 1, "Y": 2, "Z": 3}

# parse arguments from cmd prompt
def get_args():
    parser = argparse.ArgumentParser(description="Get text file input")
    parser.add_argument("--file", default="input.txt", help="TXT file name (default: input.txt)")
    return parser.parse_args()

args = get_args()

# save input text
with open(args.file) as f:
    input_text = f.read()

lines = input_text.split("\n")

sum = 0
for line in lines:
    # value for player pick
    sum += player_values[line[2]]

    # player win
    if line in ["A Y", "B Z", "C X"]:
        sum += 6
    # draw
    elif line in ["A X", "B Y", "C Z"]:
        sum += 3

print(sum)
