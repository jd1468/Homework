from contextlib import contextmanager
import time


# 7.1
class FileContextManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Error occured. {exc_val}')

        self.file.close()
        return True


class CustomBaseException(Exception):
    pass


class NonIntegerInput(CustomBaseException):
    def __init__(self):
        self.message = 'Input must be an integer'
        super().__init__(self.message)


class NotInRangeInput(CustomBaseException):
    def __init__(self):
        self.message = 'Input must be greater than 2'
        super().__init__(self.message)


class NotEvenNumber(CustomBaseException):
    def __init__(self):
        self.message = 'Number must be even'
        super().__init__(self.message)


class GoldbachsConjecture:
    def __init__(self):
        print('-----Goldbach\'s conjecture-----')
        print('-----According to Goldbach, every number greater than 2 '
              'can be decomposed into sum of 2 prime numbers')

        self.game_loop()

    def game_loop(self):
        flag = True
        while flag:
            while True:
                try:
                    number = self.input_checker()
                    break
                except NotInRangeInput as err:
                    print(err)
                except NonIntegerInput as err:
                    print(err)
                except NotEvenNumber as err:
                    print(err)
            prime_pair = self.goldbachs_conjecture_checker(number)
            if prime_pair is not None:
                print(f'Pairs of prime numbers for {number} is: {", ".join(str(i) for i in prime_pair)}')
            flag = self.quit_checker()

    @staticmethod
    def input_checker():
        while True:
            number = input('Enter an integer number that is greater than 2: ')
            try:
                number = int(number)
            except ValueError:
                raise NonIntegerInput

            if number <= 2:
                raise NotInRangeInput

            return number

    def goldbachs_conjecture_checker(self, number):
        prime_pairs = []
        for i in range(number // 2 + 1):
            if self.prime_checker(i):
                k = number - i
                if self.prime_checker(k):
                    prime_pairs.append((i, k))
        return prime_pairs

    @staticmethod
    def prime_checker(number):
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False

        return True

    @staticmethod
    def quit_checker():
        while True:
            answer = input('Press q if you want to exit or ENTER to continue playing: ')
            if answer == 'q':
                return False
            elif answer == '':
                return True
            else:
                continue

    def __del__(self):
        print('-----Thank you for playing-----')


# 7.7
class MyNumberCollection:
    def __init__(self, *args):
        if isinstance(args[0], int):
            self.start = self.number_checker(args[0])
            self.end = self.number_checker(args[1])
            self.step = self.number_checker(args[2])
            self.collection = self.collection_generator(self.start, self.end, self.step)
        else:
            self.collection = list(self.collection_checker(args[0]))

        self.iterator_position = 0

    def append(self, number):
        self.collection.append(self.number_checker(number))

    @staticmethod
    def collection_generator(start, end, step):
        collection = []
        for i in range(start, end, step):
            collection.append(i)
        if end not in collection:
            collection.append(end)
        return collection

    @staticmethod
    def number_checker(number):
        if isinstance(number, int):
            return number
        else:
            raise TypeError('Collection can contain only integers')

    @staticmethod
    def collection_checker(collection):
        flag = True
        for i in collection:
            if not isinstance(i, int):
                flag = False
                break

        if flag:
            return collection
        else:
            raise TypeError('Collection can contain only integers')

    def __str__(self):
        return str(self.collection)

    def __add__(self, other):
        return MyNumberCollection(self.collection + other.collection)

    def __getitem__(self, item):
        return pow(self.collection[self.number_checker(item)], 2)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.collection[self.iterator_position]
        except IndexError:
            raise StopIteration

        self.iterator_position += 1

        return item


# 7.8
class MySquareIterator:
    def __init__(self, collection):
        self.collection = self.__iterable_checker(collection)
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            square_number = pow(self.collection[self.start], 2)
        except TypeError:
            print(f'{self.collection[self.start]} is not a number. Collection must consist '
                  f'of numbers')
            raise StopIteration
        except IndexError:
            raise StopIteration
        except ValueError:
            print(f'{self.collection} is not an iterable object')
            raise StopIteration
        self.start += 1
        return square_number

    @staticmethod
    def __iterable_checker(input_object):
        if hasattr(input_object, '__iter__'):
            return input_object
        else:
            raise ValueError('Iterable object must be passed')


# 7.9
class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_value = self.__correction()
        self.increment = self.__increment_definition()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value >= self.end:
            self.end_reached = True
            return 'Out of numbers!'

        x = self.current_value
        self.current_value += 2
        return x

    def __increment_definition(self):
        if self.start < self.end:
            increment = 1
        else:
            increment = -1

        return increment

    @staticmethod
    def __is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    def __correction(self):
        if not self.__is_even(self.start):
            return self.start + 1
        else:
            return self.start


def exec_time_logger(write_path):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            finish = time.time()
            exec_time = finish - start
            with open(write_path, 'a') as f:
                f.write(str(exec_time) + '\n')
        return inner_wrapper
    return wrapper


# 7.2
@exec_time_logger('func_exec_time.log')
def test_function():
    for i in range(23929):
        pow(i, 2334)
    # a = [pow(i,  2398472987423) for i in range(1233435345)]


# 7.2
@contextmanager
def file_context_manager(file_name, mode):
    file = open(file_name, mode)
    try:
        yield file
    except Exception as err:
        print(err)
    finally:
        file.close()


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            with open('none_error_logging.txt', 'a') as file:
                file.write('No exception was generated')
        except Exception as err:
            print(f'Exception: {err}. {func.__name__} function')

        return 1

    return wrapper


@exception_handler
def exception_generator():
    print(10/0)


@exception_handler
def no_exception_generator():
    print(2*10)


# 7.5
def input_checker():
    while True:
        number = input('Enter an integer number that is greater than 2 and is even: ')
        try:
            number = int(number)
        except ValueError:
            raise NonIntegerInput

        if number <= 2:
            raise NotInRangeInput

        if number % 2 == 0:
            print('Number is even')
            return number
        else:
            raise NotEvenNumber


# 7.10
def endless_generator():
    value = 1
    while True:
        yield value
        value += 2


# 7.11
def endless_fib_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def quit_loop():
    flow_control = input('press \'q\' to exit loop or ENTER to continue')
    if flow_control == 'q':
        return False
    else:
        return True


def task_7_1():
    with FileContextManager('test_file.txt', 'r') as file:
        content = file.read()
        print(content)

    with FileContextManager('test_file_2.txt', 'r') as file:
        content = file.read()
        print(content)

    try:
        content_checker = file.read()
        print(content_checker)
    except ValueError as err:
        print(f'ValueError: {err}')


def task_7_2():
    with file_context_manager('test_file.txt', 'r') as file:
        content = file.read()
        print(content)

    try:
        content_check = file.read()
        print(content_check)
    except ValueError as err:
        print(f'ValueError: {err}')


def task_7_3():
    test_function()


def task_7_4():
    exception_generator()
    no_exception_generator()


def task_7_5():
    while True:
        try:
            input_checker()
        except NonIntegerInput as err:
            print(err)
        except NotInRangeInput as err:
            print(err)
        except NotEvenNumber as err:
            print(err)

        if not quit_loop():
            break


def task_7_6():
    """
    Проблема Гольдбаха — утверждение о том, что любое чётное число, начиная с 4,
    можно представить в виде суммы двух простых чисел.
    """
    GoldbachsConjecture()


def task_7_7():
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
    try:
        col3 = MyNumberCollection((1, 2, 3, "4", 5))
        print(col3)
    except TypeError as err:
        print(f'TypeError: {err}')
    col1.append(7)
    print(col1)
    try:
        col2.append("string")
    except TypeError as err:
        print(f'TypeError: {err}')
    print(col1 + col2)
    print(col1)
    print(col2)
    print(col2[4])
    for item in col1:
        print(item, end=' ')
    print('\n')
    for item in col1 + col2:
        print(item, end=' ')


def task_7_8():
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)

    lst = ['1', 2, '3', 4, '5']
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)

    try:
        lst = 46
        itr = MySquareIterator(lst)
        for item in itr:
            print(item)
    except ValueError as err:
        print(err)


def task_7_9():
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))

    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)
        if not quit_loop():
            break


def task_7_10():
    gen = endless_generator()
    while True:
        print(next(gen))
        if not quit_loop():
            break


def task_7_11():
    gen = endless_fib_generator()
    while True:
        print(next(gen))
        if not quit_loop():
            break


def checker():
    """
    Function to choose task. Asks for a task number and in return calls corresponding function.
    """
    task_dict = {'7.1': task_7_1, '7.2': task_7_2, '7.3': task_7_3, '7.4': task_7_4, '7.5': task_7_5,
                 '7.6': task_7_6, '7.7': task_7_7, '7.8': task_7_8, '7.9': task_7_9, '7.10': task_7_10,
                 '7.11': task_7_11}
    while True:
        task_number = input('\nEnter number of task you want to see [7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, '
                            '7.8, 7.9, 7.10, 7.11] or press ENTER to exit: ')

        if task_number == '':
            confirmation = input('Do you really want to exit y|n: ').lower()
            if confirmation == 'y':
                exit()
        elif task_number not in task_dict.keys():
            print('Try again')
        else:
            task_dict[task_number]()


"""
Checked: 
7.1 - True
7.2 - True
7.3 - True
7.4 - True
7.5 - True
7.6 - True
7.7 - True
7.8 - True
7.9 - True
7.10 - True
7.11 - True
"""

if __name__ == '__main__':
    checker()
