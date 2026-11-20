import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# --- Testing the class ---
p1 = Point2D(2, 3)
p2 = Point2D(5, 7)

print("Point 1:", p1)
print("Point 2:", p2)
print("Distance between p1 and p2:", p1.distance(p2))