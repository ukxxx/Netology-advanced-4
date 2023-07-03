class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = []

    def __iter__(self):
        for item in self.list_of_list:
            if isinstance(item, list):
                self.flat_list.extend(FlatIterator(item))
            else:
                self.flat_list.append(item)
        return self
    
    def __next__(self):
        if not self.flat_list:
            raise StopIteration
        else:
            return self.flat_list.pop(0)


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