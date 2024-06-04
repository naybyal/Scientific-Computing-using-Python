from PIL import Image

with Image.open("retroimg.png") as picture:
    mirror = picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.show()
    mirror.save("retroimg_mirror.png")