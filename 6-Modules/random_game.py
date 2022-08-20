# import random  # OR from random import randint
#
# answer = (random.randint(1, 10))  # OR answer = randint(1, 10)
#
# while True:
#     try:
#         num = int(input('guess a number between 1 and 10: '))
#         if 0 < num < 11:
#             if num == answer:
#                 print('you are a genius')
#                 break
#         else:
#             print('hey, I said 1~10')
#     except ValueError:
#         print('enter a number between 1 and 10 only')
#         continue

# ###################################################################################################################################

from random import randint
# you will need to run this on your machine and not this website for the sys.argv to work!
import sys
# The sys module in Python provides various functions and variables that are used to manipulate different parts of
# the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and
# functions that interact strongly with the interpreter.

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue
