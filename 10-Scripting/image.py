from PIL import Image, ImageFilter

img = Image.open(r'.\pokedex\pikachu.jpg')

# print(img)
print(img.format)
# print(img.size)
# print(img.mode)

# print(dir(img))  #functions, methods, attributes, properties this img have using dir command

filtered_image = img.filter(ImageFilter.BLUR)   #SMOOTH,SHARPEN try these too

filtered_image.save('blur.png', 'png')
filtered_image.show()

converted_image = img.convert('L')
converted_image.save('grey.png', 'png')
converted_image.show()


