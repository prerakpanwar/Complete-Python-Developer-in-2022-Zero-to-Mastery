import re

pattern = re.compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
string = input('enter your email address: ')

a= pattern.search(string)


if (a):
	print(f'correct email, {a}')
else:
	print(f'incorrect email, {a} ,enter a new one')


