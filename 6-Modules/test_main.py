# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# print(__name__)
# from utility import multiply, divide
# import shopping.more_shopping.shopping_cart
#
# # OR from shopping.more_shopping.shopping_cart import buy
# # print(buy('apple')
# if __name__ == '__main__':
#     print(shopping.more_shopping.shopping_cart.buy('apple'))
#     print(divide(5, 2))
#     print(multiply(5, 2))
# else:
#     print('run this')
#
# ###########################################################################################################
# # built-in module random
# import random
#
# # help(random)                                  #to know more about random
# print(random)
# print(dir(random))  # dir is used to get all the methods we can use with random
# print(random.random())  # gives a random number between 0 and 1
# print(random.randint(1, 10))  # gives a random number between 1 and 10
# print(random.choice([1, 2, 3, 4, 5]))  # chooses any number from the given list
# my_list = [1, 2, 3, 4, 5]
# (random.shuffle(my_list))  # shuffles a sequence like a list
# print(my_list)
#
# ###########################################################################################################
# # built-in module sys
# import sys
#
# sys.argv


###########################################################################################################
import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)
