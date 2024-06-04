from PIL import Image, ImageFilter


#   blurring doesn't work on palette images
with Image.open("blurred_image.jpg") as picture: 
    blur = picture.filter(ImageFilter.BLUR)
    blur.show()
    blur.save("img_blurred.jpg")