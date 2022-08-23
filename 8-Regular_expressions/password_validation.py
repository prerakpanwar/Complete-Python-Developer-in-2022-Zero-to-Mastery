#at least 8 char long
#contain any sort of letters,numbers, and $%#@ only
#end with a number
import re

pattern = re.compile(r"[a-zA-Z0-9$%#@]{7,}\d")

password= input('enter your password: ')

a= pattern.search(password)

if (a):
	print(f'correct password, {a}')
else:
	print(f'incorrect password, {a} ,enter a new one')