#to create profile picture for any social media site & to keep the aspect ratio we use thumbnail()
from PIL import Image, ImageFilter

img = Image.open(r'.\pokedex\astro.jpg')
print(img.size)
img.thumbnail((400,400))   
img.save('thumbnail.jpg')
print(img.size)
img.show()