import math
from math import sin
from math import degrees

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

angle_A = math.asin(2 * area / (b * c))
angle_B = math.asin(2 * area / (a * c))
angle_C = math.asin(2 * area / (a * b))
    
angle_A = math.degrees(angle_A)
angle_B = math.degrees(angle_B)
angle_C = math.degrees(angle_C)

print(f"The angles of the triangle are: A = {angle_A:.2f}°, B = {angle_B:.2f}°, C = {angle_C:.2f}°")
