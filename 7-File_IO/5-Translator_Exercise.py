import translate
from translate import Translator
translator= Translator(to_lang="ja")
try:
	with open(r'.\file_paths\dehradun.txt',mode='r') as my_file:
		text= (my_file.read())
		translation = translator.translate(text)
		print(translation)
		# with open('dehradun2.txt',mode='w') as my_file2:
		# 	my_file2.write(translation)
			
except FileNotFoundError as err:
	print('file does not exist, Please check your PATH')
	raise err
