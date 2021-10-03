import string
import requests
import math
import re
from functools import total_ordering


class IncrementError(Exception):
    def __init__(self):
        self.message = 'Maximal value is reached.'
        super().__init__(self.message)


class PaginationError(Exception):
    def __init__(self):
        self.message = 'Exception: Invalid index. Page is missing'
        super().__init__(self.message)


class NotFoundOnPageError(Exception):
    def __init__(self):
        self.message = 'Exception: \'great\' is missing on the pages'
        super().__init__(self.message)


class Counter:
    def __init__(self, start=0, stop=None):
        self.value = start
        self.stop = stop
        print(f'Start value: {self.value}\n'
              f'Stop value: {self.stop}')

    def increment(self):
        if self.stop is None or self.value < self.stop:
            self.value += 1
            return
        elif self.value == self.stop:
            # print('Maximal value is reached.')
            raise IncrementError()

    def get(self):
        print(self.value)


class HistoryDict:
    def __init__(self, init_dict):
        self.init_dict = init_dict
        self.history_list = []

    def set_value(self, key, value):
        self.history_list.insert(0, key)
        if len(self.history_list) > 10:
            self.history_list.pop()
        self.init_dict[key] = value

    def get_history(self):
        print(self.history_list)


class Cipher:
    def __init__(self, key_word):
        self.key_word = key_word
        self.alphabet = string.ascii_lowercase
        self.cipher_alphabet = self.__cipher_generator()

    # noinspection DuplicatedCode
    def encode(self, init_string: str):
        cipher_string = ''
        for i in init_string:
            upper_flag = i.isupper()
            if i == ' ':
                cipher_letter = ' '
            else:
                if upper_flag:
                    cipher_letter = str(self.cipher_alphabet[self.alphabet.find(i.lower())]).upper()
                else:
                    cipher_letter = str(self.cipher_alphabet[self.alphabet.find(i)])

            cipher_string += cipher_letter

        print(f'Encoded string: {cipher_string}')

    # noinspection DuplicatedCode
    def decode(self, decode_string: str):
        decipher_string = ''
        for i in decode_string:
            upper_flag = i.isupper()
            if i == ' ':
                decipher_letter = ' '
            else:
                if upper_flag:
                    decipher_letter = str(self.alphabet[self.cipher_alphabet.find(i.lower())]).upper()
                else:
                    decipher_letter = str(self.alphabet[self.cipher_alphabet.find(i)])

            decipher_string += decipher_letter

        print(f'Decoded string: {decipher_string}')

    def __cipher_generator(self):
        temp_alphabet = list(string.ascii_lowercase)
        temp_key_word = self.key_word.replace(' ', '')
        for i in temp_key_word:
            temp_alphabet.remove(i)

        return self.key_word + ''.join(temp_alphabet)


class Bird:
    def __init__(self, name: str):
        self.name = name

    def fly(self):
        print(f'{self.name} bird can fly')

    def walk(self):
        print(f'{self.name} bird can walk')

    def swim(self):
        print(f'{self.name} bird can swim')

    def __str__(self):
        abilities_string = f'{self.name} in total can fly, swim, walk.'
        print(abilities_string)
        return abilities_string


class FlyingBird(Bird):
    def __init__(self, name, ration='grains'):
        # Bird.__init__(self, name)
        self.ration = ration
        super().__init__(name)

    def eat(self):
        print(f'{self.name} mostly eats {self.ration}')


class NonFlyingBird(Bird):
    def __init__(self, name, ration='fish'):
        # Bird.__init__(self, name)
        self.ration = ration
        super().__init__(name)

    def eat(self):
        print(f'{self.name} mostly eats {self.ration}')

    def fly(self):
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")

    def __str__(self):
        abilities_string = f'{self.name} in total can swim, walk.'
        print(abilities_string)
        return abilities_string


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        # FlyingBird.__init__(name)
        super().__init__(name)

    def fly(self):
        FlyingBird.fly(self)


class Sun:
    __instance = None

    def __init__(self):
        if Sun.__instance is not None:
            print('Sun already exists')
        else:
            Sun.__instance = self

    @staticmethod
    def inst():
        if Sun.__instance is None:
            print('Sun is created')
            Sun()
        else:
            print('Sun already exists')
        return Sun.__instance


@total_ordering
class Money:
    __exchange_rate = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()['rates']
    # __default_currency = ''

    def __init__(self, amount, currency='USD'):
        self.amount = float(format(amount, '.2f'))
        self.currency = currency

    def __add__(self, other):
        if type(other) == type(self):
            if self.currency == other.currency:
                return Money(self.amount + other.amount, self.currency)
            else:
                other_amount = (other.amount * Money.__exchange_rate[self.currency]) / \
                               Money.__exchange_rate[other.currency]
                return Money(self.amount + other_amount, self.currency)

        else:
            return Money(self.amount + other, self.currency)

    def __radd__(self, other):
        return Money(self.amount + other, self.currency)

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            other_amount = (other.amount * Money.__exchange_rate[self.currency]) / Money.__exchange_rate[other.currency]
            return Money(abs(self.amount - other_amount), self.currency)

    def __mul__(self, other):
        return Money(self.amount * other, self.currency)

    def __rmul__(self, other):
        return Money(self.amount * other, self.currency)

    def __truediv__(self, other):
        return Money(self.amount / other, self.currency)

    def __eq__(self, other):
        return Money(self.amount == other.amount, self.currency)

    def __lt__(self, other):
        return Money(self.amount < other.amount, self.currency)

    def __str__(self):
        temp_amount = format(self.amount, ".2f")
        return f'{temp_amount} {self.currency}'


class Pagination:
    def __init__(self, init_text: str, symbols_amount: int):
        self.init_text = init_text
        self.symbols_amount = symbols_amount
        self.items = len(self.init_text)
        self.pages_amount = int(math.ceil(round(len(self.init_text) / self.symbols_amount)))
        self.pages_content = self.__pages_generator()

    def page_count(self):
        print(self.pages_amount)

    def item_count(self):
        print(self.items)

    def count_items_on_page(self, page):
        try:
            print(len(self.pages_content[page]))
        except IndexError:
            raise PaginationError

    def find_page(self, symbols: str):
        pos = [m.start() for m in re.finditer(symbols, self.init_text)]
        if pos:
            pages = []
            if len(symbols) == 1:
                for i in pos:
                    pages.append(i // self.symbols_amount)
            elif len(symbols) > 1:
                for i in pos:
                    start_pos = (i // self.symbols_amount)
                    end_pos = ((i + len(symbols)) // self.symbols_amount)
                    pages.extend([i for i in range(start_pos, end_pos+1)])

            print(pages)
        else:
            raise NotFoundOnPageError

    def display_page(self, page: int):
        try:
            print(f"'{self.pages_content[page]}'")
        except IndexError:
            raise PaginationError

    def __pages_generator(self):
        temp_pages_list = []
        temp_text = self.init_text
        while temp_text:
            temp_pages_list.append(temp_text[:self.symbols_amount])
            temp_text = temp_text[self.symbols_amount:]

        return temp_pages_list


def task_4_1():
    c = Counter(start=42)
    try:
        c.increment()
    except IncrementError as e:
        print(e)
    c.get()

    c = Counter()
    try:
        c.increment()
    except IncrementError as e:
        print(e)
    c.get()

    try:
        c.increment()
    except IncrementError as e:
        print(e)
    c.get()

    c = Counter(start=42, stop=43)
    try:
        c.increment()
    except IncrementError as e:
        print(e)
    c.get()

    try:
        c.increment()
    except IncrementError as e:
        print(e)
    c.get()


def task_4_2():
    d = HistoryDict({'foo': 42})
    d.set_value('bar', 43)
    d.get_history()

    d.set_value('car', 43)
    d.get_history()

    d.set_value('far', 43)
    d.get_history()

    d.set_value('har', 43)
    d.get_history()

    d.set_value('uar', 43)
    d.get_history()

    d.set_value('oar', 43)
    d.get_history()

    d.set_value('par', 43)
    d.get_history()

    d.set_value('qar', 43)
    d.get_history()

    d.set_value('rar', 43)
    d.get_history()

    d.set_value('har', 43)
    d.get_history()

    d.set_value('yar', 43)
    d.get_history()

    d.set_value('ear', 43)
    d.get_history()


def task_4_3():
    cipher = Cipher('crypto')
    cipher.encode('Hello world')
    cipher.decode('Fjedhc dn atidsn')


def task_4_4():
    b = Bird("Any")
    b.walk()

    p = NonFlyingBird("Penguin", "fish")
    try:
        p.fly()
    except AttributeError as e:
        print(f'AttributeError: {e}')
    p.eat()
    str(p)
    p.swim()

    c = FlyingBird("Canary")
    str(c)
    c.eat()
    c.swim()
    c.walk()

    s = SuperBird("Gull")
    str(s)
    s.fly()
    s.swim()
    s.walk()
    s.eat()

    print(SuperBird.__mro__)


def task_4_5():
    print('Task 4.5 was not in a task')


def task_4_6():
    p = Sun.inst()
    f = Sun.inst()
    z = Sun.inst()
    print(p is f)
    print(p is z)


def task_4_7():
    print('USD - default currency')
    x = Money(10.2398423, "BYN")
    print(x)
    y = Money(11)  # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")
    print(x + z)
    print(z + 3.11 * x + y * 0.8)

    print(x * 2.4)
    print(2.4 * x)
    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)  # result in “BYN”


def task_4_8():
    pages = Pagination('Your beautiful text', 5)

    pages.page_count()
    pages.item_count()

    pages.count_items_on_page(0)
    pages.count_items_on_page(3)
    try:
        pages.count_items_on_page(4)
    except PaginationError as e:
        print(e)

    pages.find_page('Your')
    pages.find_page('e')
    pages.find_page('beautiful')
    try:
        pages.find_page('great')
    except NotFoundOnPageError as e:
        print(e)
    pages.display_page(0)


def checker():
    """
    Function to choose task. Asks for a task number and in return calls corresponding function.
    """
    task_dict = {'4.1': task_4_1, '4.2': task_4_2, '4.3': task_4_3, '4.4': task_4_4, '4.5': task_4_5,
                 '4.6': task_4_6, '4.7': task_4_7, '4.8': task_4_8}
    while True:
        task_number = input('\nEnter number of task you want to see [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8] '
                            'or press ENTER to exit: ')

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
