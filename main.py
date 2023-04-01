# 1. Доработать класс FlatIterator в коде ниже.
# Должен получиться итератор, который принимает список списков и возвращает
# их плоское представление, т. е. последовательность, состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.

from itertools import chain

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter = -1
        self.list_of_list = list(chain.from_iterable(list_of_list))

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter + 1 >= len(self.list_of_list):
            raise StopIteration()
        else:
            self.counter += 1
            return self.list_of_list[self.counter]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


# 2. Доработать функцию flat_generator.
# Должен получиться генератор, который принимает
# список списков и возвращает их плоское представление.
# Функция test в коде ниже также должна отработать без ошибок.

import types


def flat_generator(list_of_lists):
    for i in list_of_lists:
        for j in i:
            yield j


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()


# 3.* Необязательное задание.
# Написать итератор, аналогичный итератору из задания 1,
# но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:


from itertools import chain


class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter = -1

        self.new_list = []

        for line in self.list_of_list:
            for i in line:
                if str(type(i)) != "<class 'list'>":
                    self.new_list.append(i)
                else:
                    i = list(chain.from_iterable(i))
                    i = list(chain.from_iterable(i))
                    i = list(chain.from_iterable(i))
                    i = list(chain.from_iterable(i))
                    for j in i:
                        self.new_list.append(j)

            self.list_of_list = self.new_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter + 1 >= len(self.list_of_list):
            raise StopIteration()
        else:
            self.counter += 1
            return self.list_of_list[self.counter]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()


# 4.* Необязательное задание.
# Написать генератор, аналогичный генератору из задания 2,
# но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:

import types
from itertools import chain


def flat_generator(list_of_list):
    new_list = []

    for line in list_of_list:
        for i in line:
            if str(type(i)) != "<class 'list'>":
                new_list.append(i)
            else:
                i = list(chain.from_iterable(i))
                i = list(chain.from_iterable(i))
                i = list(chain.from_iterable(i))
                i = list(chain.from_iterable(i))
                for j in i:
                    new_list.append(j)
    for i in new_list:
        yield i


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
