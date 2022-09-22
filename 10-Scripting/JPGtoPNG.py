import sys					#to take input in command line : run using python3 JPGtoPNG.py pokedex\ new\ (for windows)
import os					#to grab path ; we can use pathlib too
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)
    

for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')
