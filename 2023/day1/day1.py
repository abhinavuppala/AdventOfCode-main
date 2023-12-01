# Advent of code 2023 Day 1

import sys


def part1():

    sum = 0
    
    for line in sys.stdin:
        digits = ''

        # get all digits
        for c in line.rstrip('\n'):
            if c in '0123456789': digits += c

        # concat first & last digit
        sum += int(digits[0] + digits[-1])

    print(sum)


def part2():

    sum = 0
    for line in sys.stdin:

        # different types of digits at respective indexes
        line = line.rstrip()
        letter_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        num_digits = ['0', '1', '2', '3', '4', '5', '6','7', '8', '9']
        digits = letter_digits + num_digits
        
        # trim line until starts with a digit
        while not any(line.startswith(d) for d in digits):
            line = line[1:]
        
        # get numerical digit from string
        for d in letter_digits:
            if line.startswith(d): first_digit = letter_digits.index(d)
        for d in num_digits:
            if line.startswith(d): first_digit = num_digits.index(d)

        # trim line until ends with a digit
        while not any(line.endswith(d) for d in digits):
            line = line[:-1]
        
        # get numerical digit from string
        for d in letter_digits:
            if line.endswith(d): last_digit = letter_digits.index(d)
        for d in num_digits:
            if line.endswith(d): last_digit = num_digits.index(d)
        
        # concat first & last digit
        sum += int(str(first_digit) + str(last_digit))
    
    print(sum)