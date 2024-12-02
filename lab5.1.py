import math
point1 = (1, 2, 3)
point2 = (4, 5, 6)
def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
distance = euclidean_distance(point1, point2)
print("The Euclidean distance between", point1, "and", point2, "is:", distance)
