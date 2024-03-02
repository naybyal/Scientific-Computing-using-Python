# distance b/w two points (x1, y1) and (x2, y2)
# d^2 = (x2- x1)^2 + (y2-y1)^2
import math

print("Unit : m\n")

x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))

x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("\nThe distance is ", distance,"m")