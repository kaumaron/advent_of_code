import argparse
import re

not_symbols = '0123456789.'
numbers = '0123456789'

def symbol_mapper(arr_txt):
    symbol_map = {}
    for r, row in enumerate(s): 
         for c, el in enumerate(row): 
             if el not in not_symbols: 
                 symbol_map[(r,c)] = el
    return list(symbol_map.keys())


def compute_neighbors(r,c, br, bc):
    neighbors = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            neighbors.append((r+x, c+y))
    return list(filter(lambda x: x[0] <= br and x[1] <= bc and x[0] >= 0 and x[1] >= 0, neighbors))


def return_parts(r, c):
    parts = []
    # traverse right
    print(f'traversing: {r[c:]}')
    right = search_numbers(r[c:])
    # traverse left
    print(f'traversing: {r[:c+1][::-1]}')
    left = search_numbers(r[:c+1][::-1])
    if len(right) > 0:
        parts.append(int(right))
    if len(left) > 0:
        parts.append(int(left[::-1]))
    return parts

def search_numbers(r):
    for idx in range(len(r)):
        if r[idx] in numbers:
            continue
        elif r[:idx]:
            return r[:idx]
        else:
            return ''
        
def check_neighbors(r, c, bc):
    numbers = {}
    if r[c] in numbers:
        numbers[c] = r[c]
    else:
        return None
    


if __name__ == '__main__':
    # Input paths
    test_path = 'tests/'
    input_path = 'inputs/'
    file_ext = '.txt'

    # Parser for command line args
    parser = argparse.ArgumentParser(
                        prog='Gondola Lift',
                        description='Engine Part Numbers',
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
        answer_list = []
        test_list = []
        if mode == 1:
            with open(file=file) as f:
                answer_list = f.readline().split(',')
                answer_sum = sum([int(val) for val in answer_list])
                arr_input = []
                for line in f.readlines():
                    arr_input.append(line)
                bounds = (len(arr_input)-1, len(arr_input[0])-1)


                    
        if mode == 2:
            with open(file=file) as f:
                answer_list = f.readline().split(',')
                answer_sum = sum([int(val) for val in answer_list])
                for line in f.readlines():
                    pass


        # for all tests
        test_sum = sum([int(val) for val in test_list])
        if answer_list == test_list:
            print('Part List: Passed!')
        else:
            print(f'Part List: Failed!\n{answer_list} expected,\n{test_list} generated.')
        quit() 

    if mode == 1:
        answer_list = 0
        with open(file=file) as f:
                for line in f.readlines():
                    pass
                    # true_total += game_possible(line[0], r, g, b)
        print(answer_list)
        quit()
    
    if mode == 2:
        answer_list = 0
        with open(file=file) as f:
                for line in f.readlines():
                    pass
                    # true_total += game_power(line[0])
        print(answer_list)
        quit()
