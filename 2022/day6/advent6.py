# save input text
with open("input.txt") as f:
    input_text = f.read()

index = 0

# find the first substring with 14 in a row unique letters
for i in range(len(input_text)-13):
    if len(set(input_text[i:i+14])) == len(input_text[i:i+14]):
        index = i + 14
        break

print(index)