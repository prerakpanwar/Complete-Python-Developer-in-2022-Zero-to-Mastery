from PIL import Image, ImageFilter

img = Image.open(r'.\pokedex\pikachu.jpg')
filtered_image = img.convert('L')

# crooked = filtered_image.rotate(90)
# resize = filtered_image.resize((300,300))   #accepts values as tuple
box = (100,100,400,400)
croped = filtered_image.crop(box)

croped.save('blur2.png', 'png')
croped.show()