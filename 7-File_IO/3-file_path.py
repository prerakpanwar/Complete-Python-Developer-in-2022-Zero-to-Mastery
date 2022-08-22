#1-this will throw an error FileNotFoundError: [Errno 2] No such file or directory: 'panwar.txt'

# with open('panwar.txt',mode='r') as my_file:
# 	print(my_file.read())


#2-using relative path

# with open('file_paths\panwar.txt',mode='r') as my_file:
# 	print(my_file.read())


#3-using Absolute Path

# with open(r'D:\PYTHON\Python_sublime_text3\Advanced_Python\7-File_IO\file_paths\panwar.txt',mode='r') as my_file:
# 	print(my_file.read())


#4-from the current folder .\

# with open(r'.\file_paths\panwar.txt',mode='r') as my_file:
# 	print(my_file.read())


#5-from back a folder ..\

with open(r'..\file_paths\panwar.txt',mode='r') as my_file:
	print(my_file.read())
#this will throw an error as it goes to 7-File_IO folder and searches for panwar.txt there


#NOTE:r stands for "raw" and will cause backslashes in the string to be interpreted as actual backslashes rather than special characters. 



