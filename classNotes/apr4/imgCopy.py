#   Copying an image

from PIL import Image

img = Image.open('/home/nabiel/PycharmProjects/Scientific-Computing-using-Python/classNotes/apr4/bonsai.jpg')


imgCopy = img.copy()

imgCopy.show()