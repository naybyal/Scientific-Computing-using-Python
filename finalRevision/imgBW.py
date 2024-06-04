from PIL import Image

with Image.open("retroimg.png") as picture:
    bw_picture = picture.convert("L")
    bw_picture.show()
    bw_picture.save("retroimg_bw.png")