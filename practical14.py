import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # Overriding the distance method from Point2D
    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )
    # --- Testing the class ---
p1 = Point3D(1, 2, 3)
p2 = Point3D(4, 6, 8)

print("3D Point 1:", p1)
print("3D Point 2:", p2)
print("Distance between p1 and p2:", round(p1.distance(p2), 2))    