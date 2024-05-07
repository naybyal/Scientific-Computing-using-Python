from PIL import Image, ImageFilter


input_image = Image.open('unnamed.png')

blurred_image = input_image.filter(ImageFilter.BLUR)
blurred_image.save('blurred_image.jpg')

print('Image blurred and saved successfully.')



