#how can we acquire power the list() already has in our class

class SuperList(list):
    def __init__(self, my_list):
        self.my_list = my_list

    def __len__(self):
        return 1000


super_list1 = SuperList([1, 2, 3, 4, 5, 6, 7, 8, 9, 9])

print(len(super_list1))
print(super_list1.append(5))
print(super_list1[0])
print(issubclass(SuperList, list))



#answer : by making list as a parent class of SuperList