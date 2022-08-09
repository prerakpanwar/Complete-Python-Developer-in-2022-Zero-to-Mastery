def multiplyby_2(item):
    return item * 2

print(list(map(multiplyby_2, [1, 2, 3])))       ## list() is added because filter function returns a generator.

#################################################### 

new_list = [1, 2, 3]

def multiplyby_2(item):
    return item * 2

print(list(map(multiplyby_2, new_list)))
print(new_list)
#here its a "pure func" as it does not affect the outside #world i.e. it doesn't modify the new_list


####################################################

#program to print username in capital letters
new_list = ['prerak', 'paNwar', 'hero']


def capital_letter(item):
    return item.upper()

print(list(map(capital_letter, new_list)))



