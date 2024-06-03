from PIL import Image

img = Image.open('/home/nabiel/PycharmProjects/Scientific-Computing-using-Python/classNotes/apr4/bonsai.jpg')

def blackAndWhite(image):
    blackPixel = (0,0,0)
    whitePixel = (255, 255, 255)
    width, height = image.size  

    for y in range(height):  
        for x in range(width):  
            (r,g,b) = image.getpixel((x,y))  
            average = (r+g+b) // 3

            if average < 128:
                image.putpixel((x,y), blackPixel)  
            else:
                image.putpixel((x,y), whitePixel)
    return image

bwImage = blackAndWhite(img)
bwImage.show()
