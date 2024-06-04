from PIL import Image, ImageEnhance

with Image.open("blurred_image.jpg") as picture:
    contrast = ImageEnhance.Contrast(picture)
    contrast = contrast.enhance(1.5)    # +50% contrast
    contrast.show()
    contrast.save("img_contrast.jpg")

    