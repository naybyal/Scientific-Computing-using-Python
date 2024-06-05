from PIL import Image

def rgb_to_bw(r, g, b, threshold=128):
    luminance = int(0.2989*r + 0.5870*g + 0.1140*b)
    return 255 if luminance > threshold else 0

image = Image.open('./blurred_image.jpg')

width, height = image.size

for i in range(width):
    for j in range(height):
        (r,g,b) = image.getpixel((i, j)) 
        bw = rgb_to_bw(r, g, b)
        image.putpixel((i, j), (bw, bw, bw))

image.show()
