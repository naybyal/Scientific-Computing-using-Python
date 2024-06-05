from PIL import Image

def rgb_to_grayscale(r, g, b):
    return int(0.2989 * r + 0.5870 * g + 0.1140 * b)

image = Image.open('./blurred_image.jpg')

width, height = image.size

for i in range(width):
    for j in range(height):
        (r,g,b) = image.getpixel((i, j)) 
        grayscale = rgb_to_grayscale(r, g, b)
        image.putpixel((i, j), (grayscale, grayscale, grayscale))

image.show()
