import random
import string
import numpy as np
import pandas


# Python Practice - Session 1

TASK_STRING = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation)
                      for i in range(random.randrange(1, 20)))


def task1_1():
    # Task 1.1
    print('Task 1.1')

    counter = 0
    for _ in TASK_STRING:
        counter += 1
    print(f'\'{TASK_STRING}\' length is {counter}')
    print('\n')


def task1_2():
    # Task 1.2
    print('Task 1.2')

    count_string = input('Enter a string or press ENTER to use auto-generated string: ') or TASK_STRING
    print(f"Your string is '{count_string}'")
    count_string = count_string.lower()

    count_dict = {}
    for i in count_string:
        if i in count_dict.keys():
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    print(count_dict)
    return count_dict


def task1_3():
    # Task 1.3
    print('Task 1.3')

    example_list = ['red', 'white', 'black', 'red', 'green', 'black']
    task_list = input('Enter comma separated sequence of word or press ENTER to use \'example_list\': ') or example_list
    if task_list is not example_list:
        task_list = list(task_list.split(', '))
    task_list = list(set(task_list))
    task_list.sort()
    print(f'List of unique words in a sorted sequence: {task_list}')
    print('\n')


def task1_3_2():
    # Task 1.3 (2)
    print('Task 1.3.2')

    input_number = int(input('Enter an integer to get all divisors for it: '))

    divisors = set()
    for i in range(1, input_number+1):
        if input_number % i == 0:
            divisors.add(i)

    print(sorted(divisors))
    print('\n')


def task1_4():
    # Task 1.4
    print('Task 1.4')
    # Dictionary from Task 1.2 was used here
    print('Using function for Task 1.2 to get unordered dictionary')
    count_dict = task1_2()
    print(f'Initial dictionary: {count_dict}')
    print('Dictionary sorted by key: ', end='')
    for i in sorted(count_dict.keys()):
        print(f'\'{i}\': {count_dict[i]}', end=', ')
    print('\n')


def task1_5():
    # Task 1.5
    print('Task 1.5')

    unique_items = set()
    # Input was considered as a hardcoded list of dictionaries, not a dynamic input
    example_input = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
                     {"V": "S009"}, {"VIII": "S007"}]
    print(f'Input: {example_input}')
    for i in example_input:
        unique_items.add(*list(i.values()))
    print(f'All unique values in a given list of dictionaries : {unique_items}')
    print('\n')


def task1_6():
    # Task 1.6
    print('Task 1.6')

    example_input = (1, 2, 3, 4)
    integer_tuple = input('Enter integers for tuple of press ENTER to use \'example_input\': ') or example_input
    if integer_tuple is not example_input:
        integer_tuple = tuple(integer_tuple.strip().split(' '))
    converted_tuple = int(''.join(map(str, integer_tuple)))
    print(f'{converted_tuple} {type(converted_tuple)}')
    print('\n')


def task1_6_2():
    # Task 1.6 (2)
    print('Task 1.6.2')

    mtb_numbers = set()
    while True:
        number = input('Enter number that is in multiplication table or press ENTER to finish: ')
        if number == '':
            break
        number = int(number)
        if number in range(1, 10):
            mtb_numbers.add(number)
        else:
            print('Your number is smaller than 1 or bigger than 9. Try again')

    if mtb_numbers:
        mtb_numbers = list(mtb_numbers)
        mtb_numbers.sort()
        mtb_numbers = np.array(mtb_numbers)
        table = mtb_numbers * mtb_numbers[:, None]
        print('-----Multiplication table-----')
        print(pandas.DataFrame(table, mtb_numbers, mtb_numbers))
    print('\n')


def checker():
    while True:
        task_number = input('Enter number of task you want to see [1.1, 1.2, 1.3, 1.3.2, 1.4, 1.5, 1.6, 1.6.2] or '
                            'ENTER to exit: ')
        if not task_number:
            break
        task_dict = {'1.1': task1_1, '1.2': task1_2, '1.3': task1_3, '1.3.2': task1_3_2, '1.4': task1_4, '1.5': task1_5,
                     '1.6': task1_6, '1.6.2': task1_6_2}

        task_dict[task_number]()


if __name__ == '__main__':
    checker()
