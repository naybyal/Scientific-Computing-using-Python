# from PIL import Image
# myImage = Image.open("/home/nabiel/PycharmProjects/Scientific-Computing-using-Python/classNotes/mar25/bonsai.jpg")
# myImage.show()

# import Image

# img = Image.open('/home/nabiel/PycharmProjects/Scientific-Computing-using-Python/classNotes/mar25/bonsai.jpg')

# img.draw()

# img = Image(150,150)
# img.draw()
# blue = (0,0,255)

# y = img.getHeight()//2
# print(150//2)
# for x in range(img.getWidth()):
#     img.setPixel(x,y,blue)

# img.draw()

from PIL import Image
im = Image.open("/home/nabiel/PycharmProjects/Scientific-Computing-using-Python/classNotes/mar25/bonsai.jpg")
im.rotate(45).show()