import math

radius = int(input('Enter the radius of the circle (in m)... '))

circumference = 2*radius*math.pi
area = math.pi*(radius**2)

print('Circumference :', circumference,"m")
print('Area :', area, "sq m")