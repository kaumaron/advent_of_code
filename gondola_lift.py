import argparse
import re



if __name__ == '__main__':
    # Input paths
    test_path = 'tests/'
    input_path = 'inputs/'
    file_ext = '.txt'

    # Parser for command line args
    parser = argparse.ArgumentParser(
                        prog='Trebuchet',
                        description='Sums values of calibration data for a trebuchet',
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
                    pass

                    # true_value = 
                    # test_value = 

                    # true_total += true_value
                    # test_total += test_value

                    # if test_value != true_value:
                    #     print(f'{line[0]} failed! {test_value} returned')
        if mode == 2:
            with open(file=file) as f:
                r,g,b = max_colors(f.readline())
                for line in f.readlines():
                    pass

                    # true_value = 
                    # test_value = 

                    # true_total += true_value
                    # test_total += test_value

                    # if test_value != true_value:
                    #     print(f'{line[0]} failed! {test_value} returned')

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
                    pass
                    # true_total += game_possible(line[0], r, g, b)
        print(true_total)
        quit()
    
    if mode == 2:
        true_total = 0
        with open(file=file) as f:
                r,g,b = max_colors(f.readline())
                for line in f.readlines():
                    pass
                    # true_total += game_power(line[0])
        print(true_total)
        quit()
