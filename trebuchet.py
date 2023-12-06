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
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0
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
    for k, v in nums.items(): 
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
        total = 0
        test_total = 0
        
        if mode == 1:
            with open(file=file) as f:
                for line in f.readlines():
                    line = line.split(' ')
                    test_case, value = line[0], int(line[1])
                    test_result = get_two_digit_num(test_case)
                    total += test_result
                    test_total += value
                    if test_result != value:
                        print(f'{test_case} failed.')
        if mode == 2:
            with open(file=file) as f:
                for line in f.readlines():
                    line = line.split(' ')
                    test_case, value = line[0], int(line[1])
                    test_result = format_numbers(test_case)
                    total += test_result
                    test_total += value
                    if test_result != value:
                        print(f'{test_case} failed.')

        if total == test_total:
            print('Total Value: Passed!')
        else:
            print(f'Total Value: Failed! {total} expected, {test_total} generated.')
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