from PIL import Image

def reduce_image_size(input_image_path, new_width, new_height):
    input_image = Image.open(input_image_path)
    input_pixels = input_image.load()
    width, height = input_image.size

    ratio_w = width / new_width
    ratio_h = height / new_height

    reduced_image = Image.new('RGB', (new_width, new_height))
    reduced_pixels = reduced_image.load()

    for x in range(new_width):
        for y in range(new_height):
            source_x = int(x * ratio_w)
            source_y = int(y * ratio_h)
            reduced_pixels[x, y] = input_pixels[source_x, source_y]

    return reduced_image

input_image_path = 'img17.jpg'
new_width = 1366
new_height = 768
resized_image = reduce_image_size(input_image_path, new_width, new_height)
resized_image.show()





