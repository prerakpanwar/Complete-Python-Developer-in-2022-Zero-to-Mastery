from functools import reduce

new_list = [1, 2, 3]

print(list(map(lambda item: item * 2, [1, 2, 3])))

print(list(filter(lambda item: item % 2 != 0, [1, 2, 3])))

print(reduce(lambda acc, item: acc + item, [1, 2, 3]))


#square
my_list = [5,4,3]
print(list(map(lambda item : item**2, [5,4,3])))

#sort according to second item of tuple
a = [(0, 2), (4, 3), (10, -1),(9, 9) ]
a.sort(key = lambda item: item[1])
print(a)
