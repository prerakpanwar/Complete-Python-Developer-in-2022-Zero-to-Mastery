try:
	with open('panwar.txt',mode='r') as my_file:
		print(my_file.read())

except FileNotFoundError as err:
	print('file does not exist, Please check your PATH')
	raise err
