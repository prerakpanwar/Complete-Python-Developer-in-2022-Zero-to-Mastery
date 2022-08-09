my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

#using list comprehension

my_list = [char for char in 'hello']
print(my_list)

#printing 100 numbers in a list
my_list2 = [num for num in range(1, 101)]
print(my_list2)

#printing power of 2 for my_list2
my_list3 = [num**2 for num in range(1, 101)]
print(my_list3)

#printing even numbers for my_list3
my_list4 = [num**2 for num in range(1, 101) if num % 2 == 0]
print(my_list4)

#SET is same as LIST only difference is [] into {}
#also SET prints only unique numbers
my_list5 = {num**2 for num in range(1, 101) if num % 2 == 0}
print(my_list5)


#DICT
#mydict = {key:value for key,value in iterable}

sDict = {x.upper(): x*3 for x in 'coding'}
print (sDict)


my_simple_dict = {'a': 1, 'b': 2}
sDict1 = {k: v for k, v in my_simple_dict.items() if v % 2 == 0}

print(sDict1)


my_dict = {num:num**2 for num in [1,2,3,4]}       #when we take key and value same
print(my_dict)