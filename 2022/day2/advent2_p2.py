import argparse

"""
A/B/C - rock/paper/scissors
X/Y/Z - loss/draw/win (6/3/0)
"""

# values for game results
result_values = {"X": 0, "Y": 3, "Z": 6}

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
    # value for game result
    sum += result_values[line[2]]
    
    # player picks rock
    if line in ["A Y", "C Z", "B X"]:
        sum += 1
    # picks paper
    elif line in ["B Y", "C X", "A Z"]:
        sum += 2
    else:
        sum += 3

print(sum)
