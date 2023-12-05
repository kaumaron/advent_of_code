import argparse

parser = argparse.ArgumentParser(
                    prog='Trebuchet',
                    description='Sums values of calibration data for a trebuchet',
                    epilog='That is it.')
parser.add_argument('-t', '--test',
                    action='store_true')
parser.add_argument('-f', '--filename',
                    action='store')
parser.add_argument('-f', '--filename',
                    action='store')
parser.add_argument('-m', '--mode',
                    action='store', choices=[1,2])
args = parser.parse_args()
test = args.test
file = args.filename
mode = args.mode

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


if __name__ == '__main__':
    if test:
        test_cases = [
            ('66vqnbtonefour2qpd', 62),
            ('spone1ninendxnqxfqvh', 11),
            ('96hfphsnpmbx6rv', 96),
            ('ninesevensixsix5g', 55),
            ('7jttgkv', 77),
            ('3gfsnineqbbfsrgpgtcjone', 33),
        ]
        total = sum([test[1] for test in test_cases])

        print('single tests')
        for test in test_cases:
            print(get_two_digit_num(test[0]) == test[1])
        
        print('sum test')
        running = 0
        for test in test_cases:
            running += get_two_digit_num(test[0])
        print(total == running)
        quit()

    total = 0
    with open(file=file) as f:
        for line in f.readlines():
            total += get_two_digit_num(line)
    print(total)
    quit()        