#using 'with' we dont have to worry about close() the file

#1-READ
with open('prerak.txt') as my_file:
	print(my_file.readlines())

#OR as mode='r' by default

# with open('prerak.txt',mode='r') as my_file:
# 	print(my_file.readlines())

#2-WRITE
# with open('prerak.txt',mode='w') as my_file:
# 	text = my_file.write(':(')
# 	print(text)

#3-READ AND WRITE
# with open('prerak.txt',mode='r+') as my_file:
# 	text = my_file.write(':(')
# 	print(text)

#4-APPEND
# with open('prerak.txt',mode='a') as my_file:
# 	text = my_file.write(':(')
# 	print(text)


#5-using non exesting file name with mode='r','w','a','r+'
# with open('surprised.txt',mode='r+') as my_file:
# 	text = my_file.write(':O')
# 	print(text)

#with 'w' and 'a' it will create a new file but it will show filenot found error with 'r' and 'r+'