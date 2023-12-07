import argparse
import re

game_id = re.compile(r'(?<=Game\s)(\d+)')
reds = re.compile(r'(\d+)\s(?=red)')
blues = re.compile(r'(\d+)\s(?=blue)')
greens = re.compile(r'(\d+)\s(?=green)')

def game_possible(line, max_red = 10, max_green = 10, max_blue = 10):
    line = line.split(':')
    game_num = int(game_id.search(line[0]).group())

    for game in line[1].split(';'):
        red, blue, green = parse_colors(game)
        if red > max_red or green > max_green or blue > max_blue:
            return 0
    return game_num

def game_power(line):
    max_red = 0
    max_green = 0
    max_blue = 0
    for game in line.split(':')[1].split(';'):
        red, blue, green = parse_colors(game)
        if red > max_red:
            max_red = red
        if blue > max_blue:
            max_blue = blue
        if green > max_green:
            max_green = green
    return max_blue * max_red * max_green

def max_colors(line):
    red = int(reds.search(line).group())
    green = int(greens.search(line).group())
    blue = int(blues.search(line).group())
    return red, green, blue

def parse_colors(game):
    try:
        red = int(reds.search(game).group())
    except:
        red = 0
    try:
        green = int(greens.search(game).group())
    except:
        green = 0
    try:
        blue = int(blues.search(game).group())
    except:
        blue = 0
    return red, blue, green

if __name__ == '__main__':
    # Input paths
    test_path = 'tests/'
    input_path = 'inputs/'
    file_ext = '.txt'

    # Parser for command line args
    parser = argparse.ArgumentParser(
                        prog='Snow Island',
                        description='Maths some cubes',
                        epilog='That is it.')
    parser.add_argument('-t', '--test',
                        action='store_true')
    parser.add_argument('-d', '--day',
                        action='store')
    parser.add_argument('-m', '--mode',
                        action='store', choices=['1','2'])
    args = parser.parse_args()

    # Assign command line args
    test = args.test
    mode = int(args.mode)
    filebase = f'day_{args.day}'
    if test:
        file = test_path + filebase + f'_{int(mode)}' + file_ext
    else:
        file = input_path + filebase + file_ext

    if test:
        true_total = 0
        test_total = 0
        
        if mode == 1:
            with open(file=file) as f:
                r,g,b = max_colors(f.readline())
                for line in f.readlines():
                    line = line.split('|')

                    true_value = int(line[1])
                    test_value = game_possible(line[0], r, g, b)

                    true_total += true_value
                    test_total += test_value

                    if test_value != true_value:
                        print(f'{line[0]} failed! {test_value} returned')
        if mode == 2:
            with open(file=file) as f:
                r,g,b = max_colors(f.readline())
                for line in f.readlines():
                    line = line.split('|')

                    true_value = int(line[1])
                    test_value = game_power(line[0])

                    true_total += true_value
                    test_total += test_value

                    if test_value != true_value:
                        print(f'{line[0]} failed! {test_value} returned')

        # for all tests
        if true_total == test_total:
            print('Total Value: Passed!')
        else:
            print(f'Total Value: Failed! {true_total} expected, {test_total} generated.')
        quit() 

    if mode == 1:
        true_total = 0
        with open(file=file) as f:
                r,g,b = max_colors(f.readline())
                for line in f.readlines():
                    line = line.split('|')
                    true_total += game_possible(line[0], r, g, b)
        print(true_total)
        quit()
    
    if mode == 2:
        true_total = 0
        with open(file=file) as f:
                r,g,b = max_colors(f.readline())
                for line in f.readlines():
                    line = line.split('|')
                    true_total += game_power(line[0])
        print(true_total)
        quit()
