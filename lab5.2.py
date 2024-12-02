point1 = tuple(float(i) for i in input("Enter coordinates of the first point (x1, y1) separated by spaces: ").split())
point2 = tuple(float(i) for i in input("Enter coordinates of the second point (x2, y2) separated by spaces: ").split())
x1, y1 = point1[0], point1[1]
x2, y2 = point2[0], point2[1]
if y1 != y2:
    dope = (x1 - x2) / (y1 - y2)
    equation = f"(x - {x1}) = {dope} * (y - {y1})"
else:
    equation = f"The line is vertical, equation: x = {x1}"
print(equation)
