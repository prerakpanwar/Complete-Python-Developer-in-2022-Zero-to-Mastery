new_list = [1, 2, 3]

def multiplyby_2(item):
    return item * 2

def only_odd(item):
    return item % 2 !=0

print(list(filter(only_odd, [1, 2, 3])))
print(new_list)


#################################################

new_list = ['prerak', 'PaNwar', 'hero', 'Prateek']


def a_fun(item):
    if item[0]=='p' or item[0]=='P' and item[-1]=='k':
        return True

print(list(filter(a_fun, new_list)))
print(new_list)