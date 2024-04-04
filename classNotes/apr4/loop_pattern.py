#   loop pattern for traversing a grid

width = 3
height = 3

for y in range(height):
    for x in range(width):
        print("(",x,",",y,")", end=" ")
    print()

