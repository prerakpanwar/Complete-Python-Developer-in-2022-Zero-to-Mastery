# The sys module in Python provides various functions and variables that are used to manipulate different parts of
# the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and
# functions that interact strongly with the interpreter.
# To learn more about sys (https://www.knowledgehut.com/blog/programming/sys-argv-python-examples)
import sys

first = sys.argv[1]
last = sys.argv[2]
print(f'hiiiii {first} {last}')
