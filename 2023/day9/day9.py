# def predict_next(values: list[int]):
    
#     # if all values are not 0, calls itself with differences list
#     # otherwise, returns 0 predicted & recursion backtracks
#     if not all(value == 0 for value in values):
#         return values[-1] + predict_next([values[i+1] - values[i] for i in range(len(values) - 1)])
#     else:
#         return 0

# print(sum([predict_next([int(x) for x in line.rstrip().split()]) for line in __import__('sys').stdin]))           # Part 1
# print(sum([predict_next([int(x) for x in line.rstrip().split()[::-1]]) for line in __import__('sys').stdin]))     # Part 2

# ^^ Original solution

# 1 liner solution because why not
print(sum([(f := lambda values: (values[-1] + f([values[i+1] - values[i] for i in range(len(values) - 1)])) if not all(value == 0 for value in values) else 0)([int(x) for x in line.rstrip().split()[::-1]]) for line in __import__('sys').stdin]))
