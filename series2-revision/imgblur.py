from PIL import Image

def blur_image(input_image, radius=1):
    input_image = Image.open(input_image)
    width, height = input_image.size
 
    blurred_image = Image.new('RGB', (width, height))
    
    neighborhood_size = radius * 2 + 1
    
    for x in range(width):
        for y in range(height):
            sum_r, sum_g, sum_b = 0, 0, 0
            pixel_count = 0
            for i in range(-radius, radius + 1):
                for j in range(-radius, radius + 1):
                    # Get the pixel position
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

input_image_path = '/home/nabiel/PycharmProjects/Scientific-Computing-using-Python/series2-revision/unnamed.png'
blurred_image_result = blur_image(input_image_path, radius=3)
blurred_image_result.save('blurred_image_result.jpg')

print('Image blurred without using the filter() method and saved successfully.')
