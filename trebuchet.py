import argparse

parser = argparse.ArgumentParser(
                    prog='Trebuchet',
                    description='Sums values of calibration data for a trebuchet',
                    epilog='That is it.')
parser.add_argument('-t', '--test',
                    action='store_true')
parser.add_argument('-f', '--filename',
                    action='store')
parser.add_argument('-m', '--mode',
                    action='store', choices=['1','2'])
args = parser.parse_args()
test = args.test
file = args.filename
mode = int(args.mode)

nums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    0: 0
}

def get_two_digit_num(input_str: str) -> int:
    digits = ''
    idx_digit = -1
    for i, loc in enumerate(input_str):
        if loc.isnumeric():
            digits += loc
            idx_digit = i
            break
    for i in list(range(idx_digit, len(input_str)))[::-1]:
        if input_str[i].isnumeric():
            digits += input_str[i]
            break
    return int(digits)

def format_numbers(input_str):
    min_idx = len(input_str)
    max_idx = -1
    left = 0
    right = 0
    for k, v in text_nums.items(): 
        if input_str.find(k) > -1: 
            idx = input_str.find(k)
            if idx < min_idx:
                min_idx = idx
                left = v
            if idx > max_idx:
                max_idx = idx
                right = v
    return (left * 10) + right


if __name__ == '__main__':
    if test:
        if mode == 1:
            test_cases = [
                ('66vqnbtonefour2qpd', 62),
                ('spone1ninendxnqxfqvh', 11),
                ('96hfphsnpmbx6rv', 96),
                ('ninesevensixsix5g', 55),
                ('7jttgkv', 77),
                ('3gfsnineqbbfsrgpgtcjone', 33),
            ]

        if mode == 2:
            test_cases = [
                ('66vqnbtonefour2qpd', 62),
                ('spone1ninendxnqxfqvh', 19),
                ('96hfphsnpmbx6rv', 96),
                ('ninesevensixsix5g', 95),
                ('7jttgkv', 77),
                ('3gfsnineqbbfsrgpgtcjone', 31),
            ]

        total = sum([test[1] for test in test_cases])

        print('\nsingle tests')
        for test in test_cases:
            print(get_two_digit_num(test[0]) == test[1])
        
        print('\nsum test')
        running = 0
        for test in test_cases:
            running += get_two_digit_num(test[0])
        print(total == running)
        quit()

    if mode == 1:
        total = 0
        with open(file=file) as f:
            for line in f.readlines():
                total += get_two_digit_num(line)
        print(total)
        quit()
    
    if mode == 2:
        total = 0
        with open(file=file) as f:
            for line in f.readlines():
                total += format_numbers(line)
        print(total)
        quit()