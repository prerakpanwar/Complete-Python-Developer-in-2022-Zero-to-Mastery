#pure function as it dont interact                           #with outside world
#as everything is contained within the function multiplyby_2


def multiplyby_2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiplyby_2([1, 2, 3]))

#not pure as the fuction interacts with new_list which is #outside the scope of the function
new_list = []


def multiplyby_2(li):
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiplyby_2([1, 2, 3]))