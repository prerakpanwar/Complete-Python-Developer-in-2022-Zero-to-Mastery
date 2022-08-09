#Python's reduce() is a function that implements a mathematical technique called folding or reduction.
#reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.

from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))  #we dont use list() as we are producing a single value
#OR
# print(reduce(accumulator, my_list))
#by default it takes 0 as start

print(my_list)