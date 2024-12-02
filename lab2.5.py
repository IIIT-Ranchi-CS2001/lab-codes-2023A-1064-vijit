# Roots of Quadratic Equation

import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))


# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Determine the nature of the roots
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The equation has two distinct real roots: R1 = ",root1, "and R2 = ",root2)
elif discriminant == 0:
    # One real repeated root
    root = -b / (2 * a)
    print("The equation has one real repeated root: R1 = R2 = ",root)
else:
    # Two complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    print("The equation has two complex roots: R1 = ",real_part, " + ",imaginary_part, "i and R2 = ",real_part, " - ", imaginary_part,"i")
