from typing import List
import string
import collections
import pandas as pd


LOREM_IPSUM_TEXT = '../data/lorem_ipsum.txt'
CSV_FILE = '../data/students.csv'


def integer_validation() -> int:
    """
    Asks user to enter an integer, and checks if input is right.
    """
    while True:
        number = input('Enter a number: ')
        try:
            number = int(number)
            break
        except ValueError:
            print('Number must be an integer. Try again.')

    return number


def task_4_1():
    """
    Task 4.1
    Open file data/unsorted_names.txt in data folder. Sort the
    names and write them to a new file called sorted_names.txt.
    Each name should start with a new line.
    """
    print('Task 4.1')

    names = []
    with open('../data/unsorted_names.txt', 'r') as file:
        for name in file:
            names.append(name)

    names.sort()
    with open('../data/sorted_names.txt', 'w') as file:
        for name in names:
            file.write(name)

    print('Names were sorted and written to "/data/sorted_names.txt"')


def most_common_words(filepath: str, number_of_words: int) -> List[str]:
    """
    Returns a list of most common words in a given file. Amount of returned words is limited by
    number of words.
    """
    sep_symbols = string.whitespace + string.punctuation
    most_common_words_dict = collections.Counter()
    with open(filepath, 'r') as file:
        for line in file:
            line = line.lower()
            for symbol in sep_symbols:
                if symbol in line:
                    line = line.replace(symbol, ' ')

            line_words = line.strip().split(' ')
            line_words = list(filter(lambda x: x != '', line_words))
            for word in line_words:
                most_common_words_dict[word] += 1

    most_common_words_list = sorted(most_common_words_dict.items(),
                                    key=lambda x: x[1], reverse=True)
    most_common_words_list = list(word[0] for word in most_common_words_list[:number_of_words])
    return most_common_words_list


def task_4_2():
    """
    Task 4.2
    Implement a function which search for most common words
    in the file. Use data/lorem_ipsum.txt file as a example.
    """
    print('Task 4.2')

    print('Amount of most common words you want to see.')
    number = integer_validation()
    most_common_words_list = most_common_words(LOREM_IPSUM_TEXT, number)
    print(most_common_words_list)


def get_top_performers(file_path: str, number_of_top_students: int) -> List[str]:
    """
    Return top students based on their average mark. Amount of students is limited by given integer.
    """
    students_data = pd.read_csv(file_path)
    top_students = students_data.sort_values(by='average mark', ascending=False).head(number_of_top_students)
    return top_students['student name'].to_list()


def ordered_by_age(init_file_path: str, to_file_path: str) -> None:
    """
    Rewrites given .csv of students performance to another .csv file, but this time ordered
    by their age.
    """
    students_data = pd.read_csv(init_file_path)
    students_data = students_data.sort_values(by='age', ascending=False)
    try:
        with open(to_file_path, 'w') as file:
            file.write(students_data.to_csv(index=False))
        print(f'Writing data of students performance ordered by their age to {to_file_path} '
              f'is finished.')
    except Exception as err:
        print(f'Something went wrong while writing to {to_file_path}. {err} happened.')


def task_4_3():
    """
    Calls functions, that return top performers and write data of students performance
    ordered by their age to another .csv.
    """
    print('Task 4.3')

    print('Amount of top students you want to see.')
    number = integer_validation()
    top_performers = get_top_performers(CSV_FILE, number)
    print(f'Top students: {top_performers}')
    ordered_by_age(CSV_FILE, '../data/students_ordered_age.csv')


def task_4_4():
    """
    Look through file modules/legb.py.
    1) Find a way to call inner_function without moving it from inside of enclosed_function.
    2.1) Modify ONE LINE in inner_function to make it print variable 'a' from global scope.
    2.2) Modify ONE LINE in inner_function to make it print variable 'a' form enclosing function.

    """
    print('Task 4.4')

    print('1. Inner function can be called from enclosed_function. For that we have to '
          'add "inner_function()" right after its declaration and initialization.')
    print('2.1. If modifying allows to change blank line, than line 8 can be modified. "global a" '
          'will make assignment done on line 9 relate to variable a declared on global scope'
          'on line 1.')
    print('2.2 Printing variable from enclosed scope will be possible after commenting line 9,'
          'where variable becomes local.')


def remember_result(function):
    """
    Saves result of last call of given function.
    """
    memo = {'cache': None}

    def wrapper(*args):
        print(f'Last value: {memo["cache"]}')
        result = function(*args)
        memo['cache'] = result

        return result

    return wrapper


@remember_result
def sum_list(*args):
    """
    Just a generic function for decorator testing.
    """
    result = ''
    try:
        int(args[0])
        result = 0
    except ValueError:
        pass
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


def task_4_5():
    """
    Implement a decorator remember_result which remembers last result of function it decorates
    and prints it before next call.
    """
    print('Task 4.5')

    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)


def call_once(func):
    """
    Saves result of the first call of given function.
    """
    memo = {'cache': None}

    def wrapper(*args):
        result = func(*args)
        if memo['cache']:
            pass
        else:
            memo['cache'] = result

        return memo['cache']

    return wrapper


@call_once
def sum_of_numbers(a, b):
    """
    Just a generic function for decorator testing.
    """

    return a + b


def task_4_6():
    """
    Implement a decorator call_once which runs a function or method once and caches the result.
    All consecutive calls to this function should return cached result no matter the arguments.
    """
    print('Task 4.6')

    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))


def task_4_7():
    """
    Run the module modules/mod_a.py. Check its result. Explain why does this happen.
    Try to change x to a list [1,2,3]. Explain the result. Try to change import to from x
    import * where x - module names. Explain the result.

    """
    print('Task 4.7')

    print('When we run unchanged mod_a.py for the first time "print(mod_c.x)" prints "5" cause'
          'code starts with going through all imported modules, and in mod_b.py "x" value from '
          'mod_c.py is changed directly. '
          'Such output won\'t be changed by changing "x" value to a list in mod_c.py, cause of '
          'behavior same to a previous case. Even if import will be changed to "from x import *" '
          'behavior will still be the same, mod_b.py will change "x" value and only after that '
          '"print" in mod_a.py will have access to it.')


def checker():
    """
    Function to choose task. Asks for a task number and in return calls corresponding function.
    """
    task_dict = {'4.1': task_4_1, '4.2': task_4_2, '4.3': task_4_3, '4.4': task_4_4, '4.5': task_4_5,
                 '4.6': task_4_6, '4.7': task_4_7}
    while True:
        task_number = input('\nEnter number of task you want to see [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7] or press ENTER '
                            'to exit: ') or '4.5'

        if task_number == '':
            confirmation = input('Do you really want to exit y|n: ').lower()
            if confirmation == 'y':
                exit()
        elif task_number not in task_dict.keys():
            print('Try again')
        else:
            task_dict[task_number]()


if __name__ == '__main__':
    checker()
