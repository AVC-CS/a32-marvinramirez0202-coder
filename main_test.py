import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # data1: 30 male, 40 female, 30 others -> Male:30.00% Female:40.00% Others:30.00%
    regex_test([r'30\.00', r'40\.00', r'30\.00'], lines)


@pytest.mark.T2
def test_main_2():
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # data2: 50 male, 25 female, 25 others -> Male:50.00% Female:25.00% Others:25.00%
    regex_test([r'50\.00', r'25\.00', r'25\.00'], lines)


@pytest.mark.T3
def test_main_3():
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # data3: 10 male, 80 female, 10 others -> Male:10.00% Female:80.00% Others:10.00%
    regex_test([r'10\.00', r'80\.00', r'10\.00'], lines)


@pytest.mark.T4
def test_main_4():
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # data4: 60 male, 20 female, 20 others -> Male:60.00% Female:20.00% Others:20.00%
    regex_test([r'60\.00', r'20\.00', r'20\.00'], lines)
