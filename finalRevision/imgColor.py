from PIL import Image, ImageEnhance

with Image.open("blurred_image.jpg") as picture:
    color = ImageEnhance.Color(picture).enhance(2.5)
    color.show()
    color.save("color.jpg")