import sys

MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14


def get_values(draw: str) -> (int, int, int):
    ''' Get RGB values from one draw of the game '''
    
    # split by comma
    r, g, b = 0, 0, 0
    colors = draw.lstrip().split(', ')

    # get int in front of color name
    for color in colors:
        if color.endswith('green'):  g += int(color.split(' ')[0])
        elif color.endswith('red'):  r += int(color.split(' ')[0])
        elif color.endswith('blue'): b += int(color.split(' ')[0])
    
    return r, g, b


def parse_line_part1(line: str) -> int:
    ''' Part 1: parse 1 line of input & return game ID or 0 '''
    
    # get game ID and draws list for one part
    game, info = line.split(':')
    _, game_id = game.split(' ')
    draws = info.split(';')

    # get RGB values, if they are within max return ID, else 0
    for draw in draws:
        r, g, b = get_values(draw)
    
        if not (r <= MAX_RED and g <= MAX_GREEN and b <= MAX_BLUE):
            return 0
    return int(game_id)


def parse_line_part2(line: str) -> int:
    ''' Part 2: parse 1 line of input & return product of min of each color '''
    
    # get game ID and draws list for one part
    game, info = line.split(':')
    _, game_id = game.split(' ')
    draws = info.split(';')
    red, green, blue = 0, 0, 0

    # get max RGB values for each category for any 1 draw
    for draw in draws:
        r, g, b = get_values(draw)
        red, green, blue = max(red, r), \
                           max(green, g), \
                           max(blue, b)
    
    # return product
    return red * green * blue


if __name__ == '__main__':
    print(sum(parse_line_part2(line.rstrip()) for line in sys.stdin))
