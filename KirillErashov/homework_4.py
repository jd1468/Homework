import string
from typing import List, Tuple, Set, Dict


def quotation_mark_changer(init_list: List[str]) -> List[str]:
    """
    Changes ' to " and vice versa in a given string.
    """
    for i in range(len(init_list)):
        if init_list[i] == '"':
            init_list[i] = '\''
        elif init_list[i] == '\'':
            init_list[i] = '"'

    return init_list


def task_4_1():
    """
    Task 4.1
    Implement a function which receives a string and replaces all " symbols with ' and vise versa.
    """
    print('Task 4.1')

    init_string = list(input('Enter a string where you want to replace quotation marks: '))
    init_string = quotation_mark_changer(init_string)

    print(''.join(init_string))


def palindrome_checker(init_list: List[str]) -> List[str]:
    """
    Checks if given string is palindrome.
    Separates string in its middle and compares substring by poping last symbol.
    If first half is empty in the end, than string is a palindrome.
    """
    string_middle = len(init_list) // 2
    first_half = init_list[:string_middle]
    for i in init_list[string_middle:]:
        if first_half[-1] == i:
            first_half.pop()

    return first_half


def task_4_2():
    """
    Task 4.2
    Write a function that check whether a string is a palindrome or not.
    Usage of any reversing functions is prohibited.
    """
    print('Task 4.2')

    init_string = list(input('Enter a string: ').lower())

    palindrome_checker_result = palindrome_checker(init_string)
    if palindrome_checker_result:
        print(f'{"".join(init_string)} is not a palindrome')
    else:
        print(f'{"".join(init_string)} is a palindrome')


def string_split(init_string: str, sep_symbol: str, sep_limit: int) -> List[str]:
    """
    Takes string, symbols by which that string must be separated and limit of separations.
    Splits given string by sep symbols. Stops if number of separations reaches sep limit.
    Returns list of sub string.
    """
    split_list = []
    start_index = 0
    sep_iteration = 1
    for i in range(len(init_string)):
        if init_string[i] in sep_symbol:
            if (i - start_index) <= 1:
                split_list.append('')
            else:
                split_list.append(init_string[start_index+1: i])

            start_index = i

            if sep_iteration == sep_limit:
                break
            else:
                sep_iteration += 1

    split_list.append(init_string[start_index+1: len(init_string)+1])
    return split_list


def task_4_3():
    """
    Task 4.3
    Implement a function which works the same as str.split method
    (without using str.split itself, of course).
    """
    print('Task 4.3')

    init_string = input('Enter sequence you want to split: ')
    sep_symbol = input('Enter symbol(-s) you want to use as a separator or press ENTER to use \' \' '
                       'and finish input: ') or ' '
    while True:
        sep_limit = input('Enter limit to separations or press ENTER to go through whole sequence: ')
        if not sep_limit:
            sep_limit = 0
            break

        try:
            sep_limit = int(sep_limit)
            break
        except ValueError:
            print('Separations limit must be an integer. Try again')

    sep_list = string_split(init_string, sep_symbol, sep_limit)
    print(sep_list)


def string_index_separation(init_string: str, index_list: List[int]) -> List[str]:
    """
    Take string and list of indexes.
    Separates string by given indexes. Index will be ignored if is out of given string's range.
    Returns separated string as list of substrings.
    """
    start_index = 0
    split_list = []
    for i in index_list:
        split_list.append(init_string[start_index: i])
        start_index = i
        if start_index >= len(init_string):
            break
        elif i == index_list[-1]:
            split_list.append((init_string[start_index:]))

    return split_list


def task_4_4():
    """
    Task 4.4
    Implement a function split_by_index(s: str, indexes: List[int]) -> List[str]
    which splits the s string by indexes specified in indexes.
    Wrong indexes must be ignored.
    """
    print('Task 4.4')

    init_string = input('Enter string you want to separate by indexes: ')
    index_list = []

    while True:
        index = input('Enter index you want to separate by or press ENTER to finish: ') or ''
        if not index:
            break

        try:
            index = int(index)
            index_list.append(index)
        except ValueError:
            print('Index must be integer. Try again')

    index_list.sort()

    split_list = string_index_separation(init_string, index_list)

    print(split_list)


def get_digits(num: int) -> Tuple[int]:
    """
    Takes int as a parameter and returns tuple of all digits that int consists of.
    """
    num = list(map(int, str(num)))
    return tuple(num)


def task_4_5():
    """
    Task 4.5
    Implement a function get_digits(num: int) -> Tuple[int]
    which returns a tuple of a given integer's digits.
    """
    print('Task 4.5')

    number = None
    while True:
        try:
            number = int(input('Enter an integer: '))
            break
        except ValueError:
            print('Number must be an integer. Try again.')
            continue

    number_list = get_digits(number)

    print(number_list)


def get_longest_word(s: str) -> str:
    """
    Finds longest word in a given string.
    If there are multiple words with same length, the first one will be returned.
    """
    for i in string.whitespace:
        s = s.replace(i, ' ')

    input_list = list(s.split(' '))
    longest_word = ''
    for i in input_list:
        if len(i) > len(longest_word):
            longest_word = i

    return longest_word


def task_4_6():
    """
    Task 4.6
    Implement a function get_shortest_word(s: str) -> str
    which returns the longest word in the given string.
    The word can contain any symbols except whitespaces
    (, \n, \t and so on). If there are multiple longest
    words in the string with a same length return the word
    that occures first.
    """
    print('Task 4.6')

    input_string = input('Enter string, where you want to find longest word: ')
    longest_word = get_longest_word(input_string)

    print(longest_word)


def foo(init_list: List[int]) -> List[int]:
    """
    Takes a list of integers and returns new list with same length,
    where each element is product of all other element
    """
    product_list = []
    for i in range(len(init_list)):
        product = 1
        for k in range(len(init_list)):
            if k == i:
                continue
            else:
                product *= init_list[k]
        product_list.append(product)

    return product_list


def task_4_7():
    """
    Task 4.7
    Implement a function foo(List[int]) -> List[int] which, given a list
    of integers, return a new list such that each element at index i of
    the new list is the product of all the numbers in the original array
    except the one at i.
    """
    print('Task 4.7')

    init_list = []
    while True:
        number = input('Enter an integer or press ENTER to finish input: ')
        if not number:
            break
        try:
            number = int(number)
        except ValueError:
            print('Number must be an integer. Try again.')
            continue
        init_list.append(number)

    product_list = foo(init_list)

    print(product_list)


def get_pairs(init_list: List[int]) -> List[tuple] or None:
    """
    Creates and returns a list of tuples of all of elements of a given list,
    combined step by step in pairs of two.
    """
    pairs_list = []
    if len(init_list) == 1:
        return None

    for i in range(len(init_list)-1):
        pairs_list.append((init_list[i], init_list[i+1]))

    return pairs_list


def task_4_8():
    """
    Task 4.8
    Implement a function get_pairs(lst: List) -> List[Tuple]
    which returns a list of tuples containing pairs of elements.
    Pairs should be formed as in the example. If there is only
    one element in the list return None instead.
    """
    print('Task 4.8')

    init_list = []
    while True:
        value = input('Enter a value or press ENTER to finish input: ')
        if not value:
            break
        try:
            value = int(value)
            init_list.append(value)
        except ValueError:
            init_list.append(value)

    print(get_pairs(init_list))


def test_1_1(string_list: List[str]) -> Set[str]:
    """
    Returns set of characters that appear in all strings.
    """
    all_strings_characters = set(string.ascii_lowercase)
    for i in string_list:
        all_strings_characters = all_strings_characters.intersection(set(i))

    return all_strings_characters


def test_1_2(string_list: List[str]) -> Set[str]:
    """
    Returns set of characters that appear at least in one string.
    """
    one_string_characters = set()
    for i in string_list:
        one_string_characters.update(set(i))

    return one_string_characters


def test_1_3(string_list: List[str]) -> Set[str]:
    """
    Returns set of characters that appear at least in two strings.
    """
    appear_in_two_characters = set()

    for i in string_list:
        for k in string_list:
            if k == i:
                continue
            appear_in_two_characters.update(set(i).intersection(set(k)))

    return appear_in_two_characters


def tes_1_4(string_list: List[str]) -> Set[str]:
    """
    Returns set of characters of alphabet that were not used in any string.
    """
    alphabet_characters = set(string.ascii_lowercase)
    for i in string_list:
        alphabet_characters.difference_update(set(i))

    return alphabet_characters


def task_4_9():
    """
    Task 4.9
    Implement a bunch of functions which receive a changeable number
    of strings and return next parameters: characters that appear in
    all strings characters that appear in at least one string characters
    that appear at least in two strings characters of alphabet, that
    were not used in any string Note: use string.ascii_lowercase for
    list of alphabet letters
    """
    print('Task 4.9')

    # test_strings = ["hello", "world", "python", '2341234o']  # initial test strings
    test_strings = []
    while True:
        init_string = input('Enter a string you want to use in test or press ENTER to finish input: ')
        if init_string == '':
            break
        else:
            test_strings.append(init_string)

    print(test_1_1(test_strings))
    print(test_1_2(test_strings))
    print(test_1_3(test_strings))
    print(tes_1_4(test_strings))


def generate_squares(num: int) -> Dict[int, int]:
    """
    Takes an integer and returns dict, where keys 'r all integers from 1 to given number included, and corresponding
    values are their squares.
    """
    squares_dict = {}
    for i in range(1, num+1):
        squares_dict[i] = i**2

    return squares_dict


def task_4_10():
    """
    Task 4.10
    Implement a function that takes a number as an argument and returns
    a dictionary, where the key is a number and the value is the square
    of that number.
    """
    while True:
        number = input('Enter number, which will be limit for squares generation: ')
        try:
            number = int(number)
            break
        except ValueError:
            print('Number must be an integer. Try again.')

    squares_dict = generate_squares(number)

    print(squares_dict)


def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    """
    Summarizes all values in all dictionaries with same keys.
    """
    combined_dict = {}
    for i in args:
        print(f'Initial dictionary: {i}')
        for k in i.keys():
            if k in combined_dict.keys():
                combined_dict[k] += i[k]
            else:
                combined_dict[k] = i[k]

    return combined_dict


def task_4_11():
    """
    Task 4.11
    Implement a function, that receives changeable number of
    dictionaries (keys - letters, values - numbers) and combines them
    into one dictionary. Dict values ​​should be summarized in case of
    identical keys
    """

    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    print(f'Summarised dictionary: {combine_dicts(dict_1, dict_2)}')
    print(f'Summarised dictionary: {combine_dicts(dict_1, dict_2, dict_3)}')


def checker():
    """
    Function to choose task. Asks for a task number and in return calls corresponding function.
    """
    task_dict = {'4.1': task_4_1, '4.2': task_4_2, '4.3': task_4_3, '4.4': task_4_4, '4.5': task_4_5,
                 '4.6': task_4_6, '4.7': task_4_7, '4.8': task_4_8, '4.9': task_4_9, '4.10': task_4_10,
                 '4.11': task_4_11}
    while True:
        task_number = input('\nEnter number of task you want to see [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10,'
                            ' 4.11] or press ENTER to exit: ')

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
