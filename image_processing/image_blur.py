from PIL import Image

def blur_image(input_image_path, radius=1):
    input_image = Image.open(input_image_path)
    width, height = input_image.size
    blurred_image = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            sum_r, sum_g, sum_b = 0, 0, 0
            pixel_count = 0
            for i in range(-radius, radius + 1):
                for j in range(-radius, radius + 1):
                    nx = x + i
                    ny = y + j 
                    if 0 <= nx < width and 0 <= ny < height:
                        r, g, b = input_image.getpixel((nx, ny))
                        sum_r += r
                        sum_g += g
                        sum_b += b
                        pixel_count += 1
            avg_r = sum_r // pixel_count
            avg_g = sum_g // pixel_count
            avg_b = sum_b // pixel_count
            blurred_image.putpixel((x, y), (avg_r, avg_g, avg_b))
    return blurred_image

blurred_image = blur_image('./img17.jpg')
blurred_image.show()








