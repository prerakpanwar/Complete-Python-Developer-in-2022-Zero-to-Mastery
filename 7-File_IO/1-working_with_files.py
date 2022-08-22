#open(),read(),seek(),readline(),readlines()

# my_file = open('prerak.txt')
# print(my_file)
# print(my_file.read())
# print(my_file.read())



my_file = open('prerak.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
# my_file.seek(6)
# print(my_file.read())


# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())


# print(my_file.readlines())

my_file.close()