from PIL import Image
import numpy as np

def detect_edges(input_image_path):
    input_image = Image.open(input_image_path).convert('L')  # Convert to grayscale
    
    # Sobel kernels
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    width, height = input_image.size
    input_pixels = input_image.load()
    edge_image = Image.new('L', (width, height))
    edge_pixels = edge_image.load()

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            gx = sum(input_pixels[x + i, y + j] * sobel_x[i + 1, j + 1] for i in range(-1, 2) for j in range(-1, 2))
            gy = sum(input_pixels[x + i, y + j] * sobel_y[i + 1, j + 1] for i in range(-1, 2) for j in range(-1, 2))
            edge_magnitude = min(max(int(np.sqrt(gx**2 + gy**2)), 0), 255)
            edge_pixels[x, y] = edge_magnitude

    return edge_image

edge_image = detect_edges('./img17.jpg')
edge_image.show()




