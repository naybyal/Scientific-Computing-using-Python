from PIL import Image

img = Image.open('/home/nabiel/PycharmProjects/Scientific-Computing-using-Python/classNotes/apr4/bonsai.jpg')

def grayScale(image):
    (width, height) = image.size  

    for y in range(height):  
        for x in range(width):  
            (r, g, b) = image.getpixel((x, y))  
            grayscale = int(0.299 * r + 0.587 * g + 0.114 * b)
            image.putpixel((x, y), (grayscale, grayscale, grayscale))
    return image

grayImage = grayScale(img)
grayImage.show()
